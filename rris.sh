#!/bin/bash

# Define an array of objects
objs=(desk kitchen_small meeting_small table table_small background)
scene_nums=(3 1 1 1 2 11)

# objs=(table_small)
# scene_nums=(2)
data_root=$PATH_TO_RGBD_SCENES
save_path=$PATH_TO_RESULTS

method=rris
mesh_method=volumetric

# Iterate through the arrays
for i in "${!objs[@]}"; do
    obj=${objs[$i]}
    scene_num=${scene_nums[$i]}
    for num in $(seq 1 $scene_num); do
        echo "Running $method $mesh_method on $obj $num"
        python main.py \
            --name "$method" \
            --obj "$obj" \
            --num "$num" \
            --method "$method" \
            --mesh_method "$mesh_method" \
            --data_root "$data_root" \
            --save_path "$save_path"
    done
done
