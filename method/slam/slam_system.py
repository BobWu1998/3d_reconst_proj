import open3d as o3d
import os, sys

pyexample_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pyexample_path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import slam_update

def pipeline(config):
    slam_update.run(config)