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

    data_dir = os.path.join(args.data_root, args.obj, f'{args.obj}_{args.num}')
    mat_data = loadmat(data_dir+'.mat')

    num_images = mat_data['bboxes'].shape[1]

    # load the data
    rgbd_images = []
    rgb_files = []
    depth_files = []
    # load camera intrinsic, the dataset does not contain camera intrinsic, so we use the default one
    pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
    
    # create rgb, depth, and rgbd images
    for img_idx in range(1, num_images):
        # read the images
        depth_dir = os.path.join(data_dir, f'{args.obj}_{args.num}_{img_idx}_depth.png')
        rgb_dir = os.path.join(data_dir, f'{args.obj}_{args.num}_{img_idx}.png')
        rgb_files.append(rgb_dir)
        depth_files.append(depth_dir)

    if args.pc_method == 'rris':
        depth = o3d.io.read_image(depth_dir)
        rgb = o3d.io.read_image(rgb_dir)
        rris.pipeline(args)