import open3d as o3d

# # Load the mesh from the file
# mesh_name = '/home/bobwu/Documents/shared/recon_results/rris_table_1_all_dataset/scene_table_1/integrated.ply'
# mesh = o3d.io.read_triangle_mesh(mesh_name)
# mesh.compute_vertex_normals()
# # Visualize the mesh
# o3d.visualization.draw_geometries_with_editing([mesh])

pcd_name = '/home/bobwu/Documents/shared/recon_results/rris_table_1_test_dataset/scene_table_1/pc.ply'
pc0 = '/home/bobwu/Documents/shared/recon_results/rris_table_1_all_dataset/fragments_table_1/fragment_000.ply'
pc1 = '/home/bobwu/Documents/shared/recon_results/rris_table_1_all_dataset/fragments_table_1/fragment_001.ply'
pc2 = '/home/bobwu/Documents/shared/recon_results/rris_table_1_all_dataset/fragments_table_1/fragment_002.ply'


pcd_name = '/home/bobwu/Documents/shared/recon_results/rris_pc_table_1_v1_dataset/scene_table_1/pc.ply'
pcd = o3d.io.read_point_cloud(pcd_name)
# Visualize the point cloud
# o3d.visualization.draw_geometries([o3d.io.read_point_cloud(pc0),o3d.io.read_point_cloud(pc1),o3d.io.read_point_cloud(pc2)])
o3d.visualization.draw_geometries([pcd])