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
        gen.add_argument('--save_path', type=str, default='/home/bobwu/Documents/shared/recon/', help='Path to save the output')

        pc = self.parser.add_argument_group('Point Cloud')

        mesh = self.parser.add_argument_group('Mesh')