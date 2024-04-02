import open3d as o3d
from options import Options
import os
from scipy.io import loadmat
# load the data




if __name__ == "__main__":
    option = Options()
    args = option.parser.parse_args()

    # use the options
    data_root = args.data_root
    save_path = args.save_path
    name = args.name

    data_dir = os.path.join(data_root, args.obj, f'{args.obj}_{args.num}')
    mat_data = loadmat(data_dir+'.mat')

    num_images = mat_data['bboxes'].shape[1]

    # load the data
    rgbd_images = []
    # load camera intrinsic, the dataset does not contain camera intrinsic, so we use the default one
    pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)
    
    for img_idx in range(1, num_images):
        # read the images
        depth_dir = os.path.join(data_dir, f'{args.obj}_{args.num}_{img_idx}_depth.png')
        rgb_dir = os.path.join(data_dir, f'{args.obj}_{args.num}_{img_idx}.png')
        depth = o3d.io.read_image(depth_dir)
        rgb = o3d.io.read_image(rgb_dir)
        rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
            rgb,
            depth,
            convert_rgb_to_intensity=False) #This is to preserve 8-bit color channels instead of using single channel float type image.
        
        pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
            rgbd_image, pinhole_camera_intrinsic)

        rgbd_images.append(rgbd_image)
