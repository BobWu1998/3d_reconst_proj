import os
from scipy.io import loadmat

def load_rgbd(config):
    # load the rgb and depth files
    data_dir = os.path.join(config['data_root'], config['obj'], f"{config['obj']}_{config['num']}")
    
    mat_data = loadmat(data_dir+'.mat')
    num_images = mat_data['bboxes'].shape[1]
    rgb_files = []
    depth_files = []
    
    for img_idx in range(1, num_images):
        # read the images
        depth_dir = os.path.join(data_dir, f"{config['obj']}_{config['num']}_{img_idx}_depth.png")
        rgb_dir = os.path.join(data_dir, f"{config['obj']}_{config['num']}_{img_idx}.png")
        rgb_files.append(rgb_dir)
        depth_files.append(depth_dir)
    
    return rgb_files, depth_files