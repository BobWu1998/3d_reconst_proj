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

def pipeline(config):
    if config['method'] == 'rgst_frag':
        make_fragments.run(config)
        register_fragments.run(config)
    else:
        make_fragments.run(config)
        register_fragments.run(config)
        refine_registration.run(config)

        
        