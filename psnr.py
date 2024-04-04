# import open3d as o3d

# # Load the mesh from the file
# # mesh_name = '/home/bobwu/Documents/3d_reconst_proj/rris_desk_3_dataset/scene_desk_3/integrated.ply'
# # mesh_name = '/home/bobwu/Documents/3d_reconst_proj/rris_table_1_dataset/scene_table_1/integrated.ply'
# # mesh_name = '/home/bobwu/Documents/3d_reconst_proj/rris_no_icp_dataset/scene_table_1/integrated.ply'
# mesh_name = '/home/bobwu/Documents/3d_reconst_proj/rris_table_1_high_res_v2_dataset/scene_table_1/integrated.ply'
# # mesh_name = '/home/bobwu/Documents/3d_reconst_proj/dataset/scene_table_1/integrated.ply'
# mesh = o3d.io.read_triangle_mesh(mesh_name)
# mesh.compute_vertex_normals()
# # Visualize the mesh
# o3d.visualization.draw_geometries([mesh])


import open3d as o3d
import numpy as np
from options import Options
import os
from scipy.io import loadmat
from utils import *
import cv2
from config_init import get_config

class CameraPose:

    def __init__(self, meta, mat):
        self.metadata = meta
        self.pose = mat

    def __str__(self):
        return 'Metadata : ' + ' '.join(map(str, self.metadata)) + '\n' + \
            "Pose : " + "\n" + np.array_str(self.pose)

def read_trajectory(filename):
    traj = []
    with open(filename, 'r') as f:
        metastr = f.readline()
        while metastr:
            metadata = list(map(int, metastr.split()))
            mat = np.zeros(shape=(4, 4))
            for i in range(4):
                matstr = f.readline()
                mat[i, :] = np.fromstring(matstr, dtype=float, sep=' \t')
            traj.append(CameraPose(metadata, mat))
            metastr = f.readline()
    return traj

def render_rgbd_image(mesh, pose, intrinsic):
    """
    Renders an RGB-D image from a given mesh and camera pose.
    
    Args:
    - mesh (o3d.geometry.TriangleMesh): The 3D mesh to render.
    - pose (np.ndarray): The 4x4 camera pose matrix.
    - intrinsic (o3d.camera.PinholeCameraIntrinsic): Camera intrinsic parameters.
    
    Returns:
    - o3d.geometry.RGBDImage: The rendered RGB-D image.
    """

    # Create a rendering scene
    vis = o3d.visualization.Visualizer()
    vis.create_window(width=intrinsic.width, height=intrinsic.height,visible=False)  # Use `visible=True` to see the window, if desired
    vis.add_geometry(mesh)
    
    # Set up the camera
    ctr = vis.get_view_control()
    # ctr.convert_from_pinhole_camera_parameters(intrinsic, extrinsic=pose)
    parameters = o3d.camera.PinholeCameraParameters()
    parameters.intrinsic = intrinsic
    parameters.extrinsic = pose
    ctr.convert_from_pinhole_camera_parameters(parameters)
        
    # Render the scene
    vis.update_geometry(mesh)
    vis.poll_events()
    vis.update_renderer()
    
    # Capture the images
    depth = vis.capture_depth_float_buffer(True)
    color = vis.capture_screen_float_buffer(True)
    
    vis.destroy_window()
    
    # Combine the captured images into an RGB-D image
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        o3d.geometry.Image((np.asarray(color) * 255).astype(np.uint8)),
        o3d.geometry.Image((np.asarray(depth) * 1000).astype(np.uint16)),  # Adjust depth scale if necessary
        depth_scale=1000.0,  # Depends on the scale of your depth values
        depth_trunc=3.0,  # Adjust based on the maximum depth value you care about
        convert_rgb_to_intensity=False
    )
    
    return rgbd_image


if __name__ == "__main__":
    option = Options()
    args = option.parser.parse_args()

    config = get_config(args)
        
    rgb_files, depth_files = load_rgbd(config)
    # Example usage
    mesh_name = '/home/bobwu/Documents/shared/recon_results/slam_table_1_v1_dataset/scene_table_1/integrated.ply'
    mesh = o3d.io.read_triangle_mesh(mesh_name)
    mesh.compute_vertex_normals()
    pose = np.eye(4)  # Replace with your actual pose matrix

    flip_transform = np.array([
        [1, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, 1]
    ])
    mesh = mesh.transform(flip_transform)
    
    # intrinsic = o3d.camera.PinholeCameraIntrinsic(
    #     o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
    # intrinsic.set_intrinsics(640, 480, 525, 525, 320, 240)
    intrinsic = o3d.camera.PinholeCameraIntrinsic()
    intrinsic.set_intrinsics(640, 480, 525, 525, 319.5, 239.5)
    
    # Render the RGB-D image
    rgbd_image = render_rgbd_image(mesh, pose, intrinsic)
    o3d.visualization.draw_geometries([rgbd_image])
    
    # import open3d
    # import open3d.visualization.rendering as rendering

    # # Create a renderer with a set image width and height
    # render = rendering.OffscreenRenderer(600, 400)
    # # add mesh to the scene
    # render.scene.add_geometry(mesh)

    # # render the scene with respect to the camera
    # render.scene.camera.set_projection(intrinsic, 0.1, 1.0, 640, 480)
    # img_o3d = render.render_to_image()

    # # we can now save the rendered image right at this point 
    # open3d.io.write_image("output.png", img_o3d, 9)



    
#     # To visualize the RGB-D image
#     # o3d.visualization.draw_geometries([rgbd_image])
#     o3d.visualization.draw_geometries(
#         [rgbd_image],
#         # Camera position is calculated as `lookat + (zoom * front)`
#         front=[0, 1, 1],  # vector FROM origin TO camera (will be normalized)
#         zoom=1,  # multiplies normalized `front` vector to determine position of camera
#         lookat=[-2, 0, -2],  # look at position, determines true forward vector of camera
#         up=[0, 1, 0],  # starting up vector, determines true right vector of camera
#         point_show_normal=True
# )
    