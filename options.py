import argparse

class Options(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        
        req = self.parser.add_argument_group('Required')
        req.add_argument('--name', type=str, required=True, help='Name of the experiment')
        req.add_argument('--obj', type=str, required=True, help='Name of the object')
        req.add_argument('--num', type=int, required=True, help='Number of the object')

        gen = self.parser.add_argument_group('General')
        gen.add_argument('--data_root', type=str, default='/home/bobwu/Documents/shared/rgbd-scenes/', help='Path to the data directory')
        gen.add_argument('--save_path', type=str, default='/home/bobwu/Documents/shared/recon_results/', help='Path to save the output')
        gen.add_argument('--root', type=str, default='/home/bobwu/Documents/3d_reconst_proj/', help='Path to the root directory')
        gen.add_argument('--debug_mode', action='store_true', help='Debug mode')
        gen.add_argument('--enable_viz', action='store_true', help='Visualization')
        gen.add_argument('--multi_thread', action='store_true', help='Debug mode')
        gen.add_argument('--depth_scale', type=float, default=1000, help='Depth scale')
        gen.add_argument('--depth_max', type=float, default=3.0, help='Maximum depth')
        gen.add_argument('--depth_min', type=float, default=0.1, help='Minimum depth')
        
        
        gen.add_argument('--device', type=str, default='CPU:0', help='Device')
        
        mt = self.parser.add_argument_group('Method')
        mt.add_argument('--method', type=str, choices=['rgst_frag', 'rris', 'slam'],
                        default='rris', help='Use entire rris pipeline')
        # for running slam
        mt.add_argument('--slam_diff_max', type=float, default=0.07, help='Maximum depth difference')
        mt.add_argument('--slam_voxel_size', type=float, default=0.01, help='Voxel size')
        mt.add_argument('--slam_block_count', type=int, default=10000, help='Block count')
        # for running RRIS
        mt.add_argument('--write_global_pc', action='store_true', default=True, help='Write global point cloud')
        
        mesh = self.parser.add_argument_group('Mesh')
        mesh.add_argument('--mesh_method', type=str, choices=['volumetric', 'poisson', 'as'],
                        default='volumetric', help='Use entire rris pipeline')
        mesh.add_argument('--poisson_voxel_size', type=float, default=0.01, help='Voxel size for poisson reconstruction')
        mesh.add_argument('--as_voxel_size', type=float, default=0.01, help='Voxel size for poisson reconstruction')
        mesh.add_argument('--alpha', type=float, default=0.02, help='Voxel size for poisson reconstruction')
        
        
        frag = self.parser.add_argument_group('Fragment')
        frag.add_argument('--n_frames_per_fragment', type=int, default=50, help='Number of frames per fragment')