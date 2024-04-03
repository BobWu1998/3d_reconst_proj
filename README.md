# 3d_reconst_proj
Works on reconstructing [UWashington dataset](https://rgbd-dataset.cs.washington.edu/dataset/rgbd-scenes/)

## Environment
Using Python 3.10 and conda for this project
To create the env in conda, run 
```
conda create -n recon python==3.10 numpy
pip install open3d
pip install opencv-python
```
To activate the environment, run ```conda activate recon```

To run the point cloud reconstruction with make_fragment and register_fragment only:
```
python main.py --name rris_no_icp --obj table --num 1 --debug_mode --pc_method rgst_frag
```

To run the Robust Reconstruction of Indoor Scenes(RRIS)
```
python main.py --name rris_all --obj table --num 1 --debug_mode
```
