import open3d as o3d
from os.path import join
import numpy as np

# https://www.open3d.org/html/tutorial/Advanced/surface_reconstruction.html#Alpha-shapes
def run_alpha_shapes(path_dataset, config):
    pcd = o3d.io.read_point_cloud(join(path_dataset, config['template_global_pc']))
    pcd = pcd.voxel_down_sample(voxel_size=config['as_voxel_size'])
    
    # estimate the normals of the point cloud
    pcd.normals = o3d.utility.Vector3dVector(np.zeros((1, 3)))
    pcd.estimate_normals()
    pcd.orient_normals_consistent_tangent_plane(30) # flip the direction of normal for bottem surface of thin table
    
    # mesh reconstruction
    alpha = config['alpha']
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)
    
    mesh_name = join(path_dataset, config["template_global_mesh"])
    o3d.io.write_triangle_mesh(mesh_name, mesh, False, True)
    if config['enable_viz']:
        o3d.visualization.draw_geometries([mesh])
    
def run(config):
    run_alpha_shapes(config["path_dataset"], config)