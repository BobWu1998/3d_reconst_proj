import open3d as o3d
from utils import *

import sys
from os.path import exists, isfile, join, splitext, dirname, basename
from os import listdir, makedirs
import shutil
import time
from slam_utils import extract_trianglemesh, write_poses_to_log
import numpy as np

pyexample_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pyexample_path)

def make_clean_folder(path_folder):
    if not exists(path_folder):
        makedirs(path_folder)
    else:
        shutil.rmtree(path_folder)
        makedirs(path_folder)

def model_update(rgb_files, depth_files, intrinsic, n_files, config):
    device = o3d.core.Device(config['device'])
    T_frame_to_model = o3d.core.Tensor(np.identity(4))
    
    model = o3d.t.pipelines.slam.Model(config['slam_voxel_size'], 16,
                                        config['slam_block_count'], T_frame_to_model,
                                        device)
    depth_ref = o3d.t.io.read_image(depth_files[0])
    input_frame = o3d.t.pipelines.slam.Frame(depth_ref.rows, depth_ref.columns,
                                                intrinsic, device)
    raycast_frame = o3d.t.pipelines.slam.Frame(depth_ref.rows,
                                                depth_ref.columns, intrinsic,
                                                device)
    
    poses = []
    
    for i in range(n_files):
        start = time.time()

        depth = o3d.t.io.read_image(depth_files[i]).to(device)
        color = o3d.t.io.read_image(rgb_files[i]).to(device)

        input_frame.set_data_from_image('depth', depth)
        input_frame.set_data_from_image('color', color)
        if i > 0:
            try:
                result = model.track_frame_to_model(input_frame, raycast_frame,
                                                    config['depth_scale'],
                                                    config['depth_max'],
                                                    config['slam_diff_max']) # config.odometry_distance_thr
                T_frame_to_model = T_frame_to_model @ result.transformation
            except RuntimeError as e:
                # print(f"Tracking failed for this frame due to error: {e}")
                print(f"Tracking failed for this frame, skipping")
                err_pose = -1*np.identity(4)
                poses.append(err_pose)
                continue

        poses.append(T_frame_to_model.cpu().numpy())
        model.update_frame_pose(i, T_frame_to_model)
        model.integrate(input_frame, config['depth_scale'], config['depth_max'])
        model.synthesize_model_frame(raycast_frame, config['depth_scale'],
                                     config['depth_min'], config['depth_max'], False)
        stop = time.time()
        if config['verbose']:
            print('{:04d}/{:04d} slam takes {:.4}s'.format(i, n_files,
                                                        stop - start))
    return model.voxel_grid, poses

def run(config):
    make_clean_folder(join(config["path_dataset"], config["folder_scene"]))
    rgb_files, depth_files = load_rgbd(config)
    n_files = len(rgb_files)
    intrinsic = o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
    intrinsic = o3d.core.Tensor(intrinsic.intrinsic_matrix,
                               o3d.core.Dtype.Float64)

    volume, poses = model_update(rgb_files, depth_files, intrinsic, n_files, config)
    
    
    path_dataset = config['path_dataset']
    mesh_name = join(path_dataset, config["template_global_mesh"])
    
    # post processing the volume, save the mesh
    mesh = volume.extract_triangle_mesh()
    mesh = mesh.to_legacy()
    mesh.compute_vertex_normals()
    mesh.compute_triangle_normals()
    o3d.io.write_triangle_mesh(mesh_name, mesh, False, True)
    
    # save the pose log
    traj_name = join(path_dataset, config["template_global_traj"])
    write_poses_to_log(traj_name, poses)

    # if viz enabled 
    if config['enable_viz']:
        flip_transform = [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]
        mesh = mesh.transform(flip_transform)
        o3d.visualization.draw([mesh])
