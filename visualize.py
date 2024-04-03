import open3d as o3d

# Load the mesh from the file
# mesh_name = '/home/bobwu/Documents/3d_reconst_proj/rris_desk_3_dataset/scene_desk_3/integrated.ply'
# mesh_name = '/home/bobwu/Documents/3d_reconst_proj/rris_table_1_dataset/scene_table_1/integrated.ply'
# mesh_name = '/home/bobwu/Documents/3d_reconst_proj/rris_no_icp_dataset/scene_table_1/integrated.ply'
mesh_name = '/home/bobwu/Documents/3d_reconst_proj/rris_table_1_high_res_v2_dataset/scene_table_1/integrated.ply'
# mesh_name = '/home/bobwu/Documents/3d_reconst_proj/dataset/scene_table_1/integrated.ply'
mesh = o3d.io.read_triangle_mesh(mesh_name)
mesh.compute_vertex_normals()
# Visualize the mesh
o3d.visualization.draw_geometries([mesh])