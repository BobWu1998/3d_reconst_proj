import math
import multiprocessing
import os, sys
import numpy as np
import open3d as o3d
from os.path import join

pyexample_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pyexample_path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import make_fragments
import register_fragments
import refine_registration
from open3d_example import *

def set_default_value(config, key, value):
    if key not in config:
        config[key] = value
import integrate_scene

def pipeline(args):

    config = {}
    config['path_intrinsic'] = ""
    # config['depth_max'] = 10
    config['voxel_size'] = 0.025
    config['depth_diff_max'] = 0.03
    config['preference_loop_closure_odometry'] = 0.1
    config['preference_loop_closure_registration'] = 5.0
    config['tsdf_cubic_size'] = 0.75
    config['icp_method'] = "color"
    config['global_registration'] = "ransac"
    config['python_multi_threading'] = args.multi_thread
    config['folder_fragment'] = "fragments/"
    config['path_dataset'] = "dataset/"
    config['n_frames_per_fragment'] = args.n_frames_per_fragment
    config['depth_scale'] = 1
    config['n_keyframes_per_n_frame'] = 5
    config['template_fragment_posegraph'] = "fragments/fragment_%03d.json"
    
    # path related parameters.
    set_default_value(config, "folder_fragment", "fragments/")
    set_default_value(config, "subfolder_slac",
                      "slac/%0.3f/" % config["voxel_size"])
    set_default_value(config, "template_fragment_posegraph",
                      "fragments/fragment_%03d.json")
    set_default_value(config, "template_fragment_posegraph_optimized",
                      "fragments/fragment_optimized_%03d.json")
    set_default_value(config, "template_fragment_pointcloud",
                      "fragments/fragment_%03d.ply")
    set_default_value(config, "folder_scene", "scene/")
    set_default_value(config, "template_global_posegraph",
                      "scene/global_registration.json")
    set_default_value(config, "template_global_posegraph_optimized",
                      "scene/global_registration_optimized.json")
    set_default_value(config, "template_refined_posegraph",
                      "scene/refined_registration.json")
    set_default_value(config, "template_refined_posegraph_optimized",
                      "scene/refined_registration_optimized.json")
    set_default_value(config, "template_global_mesh", "scene/integrated.ply")
    set_default_value(config, "template_global_traj", "scene/trajectory.log")

    set_default_value(config, "debug_mode", args.debug_mode)
    # config['n_fragments'] = "n_fragments"
    
    
    # make_fragments.run(config, args)
    register_fragments.run(config, args)
    # refine_registration.run(config)
    # integrate_scene.run(config, args)
    