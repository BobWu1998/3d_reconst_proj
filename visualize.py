import open3d as o3d

from options import Options
from config_init import get_config
from os.path import join

if __name__ == "__main__":
    option = Options()
    args = option.parser.parse_args()
    config = get_config(args)
    
    # breakpoint()
    if config['viz_mode'] == 'mesh':
        if config['viz_mesh_type'] == 'volumetric':
            mesh_name = join(config['path_dataset'], config["template_global_mesh"])
        elif config['viz_mesh_type'] == 'poisson':
            mesh_name = join(config['path_dataset'], config["template_global_mesh_poisson"])
        elif config['viz_mesh_type'] == 'as':
            mesh_name = join(config['path_dataset'], config["template_global_mesh_as"])
            
        mesh = o3d.io.read_triangle_mesh(mesh_name)
        mesh.compute_vertex_normals()
        o3d.visualization.draw_geometries([mesh])
        
    elif config['viz_mode'] == 'pcd':
        pcd_name = join(config["path_dataset"], config["template_global_pc"])
        pcd = o3d.io.read_point_cloud(pcd_name)
        o3d.visualization.draw_geometries([pcd])
    # breakpoint()
        
        
        