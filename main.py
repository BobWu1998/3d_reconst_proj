import open3d as o3d
from options import Options
import os
from scipy.io import loadmat
import pc_recon.rris.rris_pipeline as rris

if __name__ == "__main__":
    option = Options()
    args = option.parser.parse_args()

    # use the options
    name = args.name

    if args.pc_method == 'rris':
        rris.pipeline(args)