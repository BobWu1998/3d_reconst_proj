#!/bin/bash

# Define an array of objects
objs=( desk kitchen_small meeting_small table table_small)
scene_nums=( 3 1 1 1 2)

# objs=(table_small)
# scene_nums=(2)

save_path=/home/bobwu/Documents/shared/recon_results_v1/

method=rris

# Iterate through the arrays
for i in "${!objs[@]}"; do
    obj=${objs[$i]}
    scene_num=${scene_nums[$i]}
    for num in $(seq 1 $scene_num); do
        echo "Running $method $mesh_method on $obj $num"
        python main.py \
            --name "$method"_"$obj"_"$num" \
            --obj "$obj" \
            --num "$num" \
            --method "$method" \
            --mesh_method "$mesh_method" \
            --enable_viz \
            --save_path "$save_path"
    done
done
# python main.py --name rris_as_table_1 --obj table --num 1 --mesh_method as --enable_viz