# 3d_reconst_proj
This project contains work of reconstructing [UWashington dataset](https://rgbd-dataset.cs.washington.edu/dataset/rgbd-scenes/). It realizes two pipeline for 3D reconstruction. 

The first approach utilizes RGBD Odometry for SLAM in the dataset, a volume is constructed during the reconstruction and directly used for mesh generation.

The second approach uses the approach described in [Robust Reconstruction of Indoor Scenes](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Choi_Robust_Reconstruction_of_2015_CVPR_paper.pdf). It seperates the rgbd video into multiple fragments, calculates the pose graph and optimize it over ICP. By default, it uses volumetric integration for mesh calculation. I also implemented the Poisson surface reconstruction method and Alpha Surface method.

## Installation
Using Python 3.10 and conda for this project
To create the env in conda, run 
```
conda create -n recon python==3.10 numpy
conda activate recon
pip install open3d
pip install opencv-python
```
Set the directories as environment variables. For example in my case I run:
```
export PATH_TO_REPO=/home/bobwu/Documents/3d_reconst_proj/
export PATH_TO_RGBD_SCENES=/home/bobwu/Documents/shared/rgbd-scenes/
export PATH_TO_RESULTS=/home/bobwu/Documents/shared/bw_results/
```

To activate the environment, run 
```
conda activate recon
cd $PATH_TO_REPO
```

Below are the commands to run reconstruction with different methods, note for simplicity, I only provide the command for one scene, e.g. For table_1 in the dataset, we set ```--obj table --num 1```. At the end of this page, I provide the bash file to automate the experiments for all objects in the dataset.

## SLAM using RGBD Odometry

To run the SLAM Pipeline:
```
python main.py --name slam --obj table --num 1 --method slam --data_root $PATH_TO_RGBD_SCENES --save_path $PATH_TO_RESULTS --enable_viz
```
## Robust Reconstruction of Indoor Scenes (RRIS)


To run the RRIS:
```
python main.py --name rris --obj table --num 1 --method rris --mesh_method volumetric --data_root $PATH_TO_RGBD_SCENES --save_path $PATH_TO_RESULTS --enable_viz
```
This could take a while, if you interrupt the reconstruction while it's running, make sure to add ```--overwrite``` when rerun the program.

## Meshing Reconstruction
Running RRIS also saves the global point cloud, which you can use for other meshing methods.

To run the Poisson method, run
```
python main.py --name rris --obj table --num 1 --method rris --mesh_method poisson --data_root $PATH_TO_RGBD_SCENES --save_path $PATH_TO_RESULTS --enable_viz
```
To run the Alpha Shape method, run
```
python main.py --name rris --obj table --num 1 --method rris --mesh_method as --data_root $PATH_TO_RGBD_SCENES --save_path $PATH_TO_RESULTS --enable_viz
```

## Point Cloud & Mesh Visualization
To visualize the point cloud saved while running RRIS
```
python visualize.py --name rris --obj table --num 1 --viz_mode pcd --data_root $PATH_TO_RGBD_SCENES --save_path $PATH_TO_RESULTS 
```

If you ran the experiments without enabling the visualization, you can always visualize the saved meshes by running 
```
# running on meshes generated with rris
python visualize.py --name rris --obj table --num 1 --viz_mode mesh --method rris --mesh_method volumetric --data_root $PATH_TO_RGBD_SCENES --save_path $PATH_TO_RESULTS 

# running on meshes generated with slam
python visualize.py --name rris --obj table --num 1 --viz_mode mesh --method rris --mesh_method volumetric --data_root $PATH_TO_RGBD_SCENES --save_path $PATH_TO_RESULTS 
```
Available mesh_method: volumetric, poisson, as

## Running the experiments automatically
I also automated the program to run all scenes at once for both SLAM and RRIS approaches.
```
bash slam.sh
bash rris.sh
```
Running ```rris.sh``` will take about an hour to finish.


