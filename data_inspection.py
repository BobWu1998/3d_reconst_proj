from scipy.io import loadmat

# Replace 'filename.mat' with the path to your .mat file
mat_data = loadmat('/home/bobwu/Documents/shared/rgbd-scenes/desk/desk_1.mat')

# the mat file contains dict_keys(['__header__', '__version__', '__globals__', 'bboxes'])
# where the bboxes are the bounding boxes for each image

import cv2
depth_dir = '/home/bobwu/Documents/shared/rgbd-scenes/desk/desk_1/desk_1_1_depth.png'
img = cv2.imread(depth_dir, cv2.IMREAD_GRAYSCALE)
breakpoint()