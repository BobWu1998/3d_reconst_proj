import argparse

class Options(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        
        req = self.parser.add_argument_group('Required')
        req.add_argument('--name', type=str, required=True, help='Name of the experiment')
        req.add_argument('--obj', type=str, required=True, help='Name of the object')
        req.add_argument('--num', type=int, required=True, help='Number of the object')

        gen = self.parser.add_argument_group('General')
        gen.add_argument('--data_root', type=str, default='/Users/bob/Documents/3D_reconst/shared/rgbd-scenes/', help='Path to the data directory')
        gen.add_argument('--save_path', type=str, default='/home/bobwu/Documents/shared/recon/', help='Path to save the output')
        gen.add_argument('--root', type=str, default='/Users/bob/Documents/3D_reconst/3d_reconst_proj/', help='Path to the root directory')
        gen.add_argument('--debug_mode', action='store_true', help='Debug mode')
        gen.add_argument('--multi_thread', action='store_true', help='Debug mode')
        
        pc = self.parser.add_argument_group('Point Cloud')
        pc.add_argument('--pc_method', type=str, default='rris', help='Method to generate point cloud')

        mesh = self.parser.add_argument_group('Mesh')
        
        frag = self.parser.add_argument_group('Fragment')
        frag.add_argument('--n_frames_per_fragment', type=int, default=50, help='Number of frames per fragment')