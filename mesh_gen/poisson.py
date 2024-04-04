import open3d as o3d
from os.path import join
import numpy as np
import matplotlib.pyplot as plt

def poisson_surface_recon(path_dataset, config):
    pcd = o3d.io.read_point_cloud(join(path_dataset, config['template_global_pc']))
    pcd = pcd.voxel_down_sample(voxel_size=config['poisson_voxel_size'])
    
    # estimate the normals of the point cloud
    pcd.normals = o3d.utility.Vector3dVector(np.zeros((1, 3)))
    pcd.estimate_normals()
    pcd.orient_normals_consistent_tangent_plane(30) # flip the direction of normal for bottem surface of thin table
    
    # mesh reconstruction
    with o3d.utility.VerbosityContextManager(
            o3d.utility.VerbosityLevel.Debug) as cm:
        mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
            pcd, depth=9)
    
    # filter out low density vertices
    densities = np.asarray(densities)
    density_colors = plt.get_cmap('plasma')(
        (densities - densities.min()) / (densities.max() - densities.min()))
    density_colors = density_colors[:, :3]
    density_mesh = o3d.geometry.TriangleMesh()
    density_mesh.vertices = mesh.vertices
    density_mesh.triangles = mesh.triangles
    density_mesh.triangle_normals = mesh.triangle_normals
    density_mesh.vertex_colors = o3d.utility.Vector3dVector(density_colors)
    
    vertices_to_remove = densities < np.quantile(densities, 0.01)
    mesh.remove_vertices_by_mask(vertices_to_remove)

    mesh_name = join(path_dataset, config["template_global_mesh"])
    o3d.io.write_triangle_mesh(mesh_name, mesh, False, True)
    
    if config['enable_viz']:
        o3d.visualization.draw_geometries([mesh])
    
        
def run(config):
    poisson_surface_recon(config["path_dataset"], config)
    


