from os.path import join
def set_default_value(config, key, value):
    if key not in config:
        config[key] = value
        
def get_config(args):
    # load everything in the args into the config
    config = vars(args)
    config['path_intrinsic'] = ""
    config['voxel_size'] = 0.025 #0.025
    config['depth_diff_max'] = 0.03
    config['preference_loop_closure_odometry'] = 0.1
    config['preference_loop_closure_registration'] = 5.0
    config['icp_method'] = "color"
    config['global_registration'] = "ransac"
    config['python_multi_threading'] = args.multi_thread
    config['folder_fragment'] = f"fragments_{args.obj}_{args.num}/"
    config['path_dataset'] = join(args.save_path, f"{args.name}_dataset") # f"{args.save_path}/{args.name}_dataset/"
    config['n_frames_per_fragment'] = args.n_frames_per_fragment
    # config['depth_scale'] = 1000
    config['n_keyframes_per_n_frame'] = 10 # 5
    
    # path related parameters.
    set_default_value(config, "subfolder_slac",
                      "slac/%0.3f/" % config["voxel_size"])
    set_default_value(config, "template_fragment_posegraph",
                      f"fragments_{args.obj}_{args.num}/fragment_%03d.json")
    set_default_value(config, "template_fragment_posegraph_optimized",
                      f"fragments_{args.obj}_{args.num}/fragment_optimized_%03d.json")
    set_default_value(config, "template_fragment_pointcloud",
                      f"fragments_{args.obj}_{args.num}/fragment_%03d.ply")
    set_default_value(config, "folder_scene", 
                      f"scene_{args.obj}_{args.num}/")
    set_default_value(config, "template_global_posegraph",
                      f"scene_{args.obj}_{args.num}/global_registration.json")
    set_default_value(config, "template_global_posegraph_optimized",
                      f"scene_{args.obj}_{args.num}/global_registration_optimized.json")
    set_default_value(config, "template_refined_posegraph",
                      f"scene_{args.obj}_{args.num}/refined_registration.json")
    set_default_value(config, "template_refined_posegraph_optimized",
                      f"scene_{args.obj}_{args.num}/refined_registration_optimized.json")
    set_default_value(config, "template_global_mesh", f"scene_{args.obj}_{args.num}/integrated.ply")
    set_default_value(config, "template_global_mesh_poisson", f"scene_{args.obj}_{args.num}/poisson.ply")
    set_default_value(config, "template_global_mesh_as", f"scene_{args.obj}_{args.num}/as.ply")
    set_default_value(config, "template_global_traj", f"scene_{args.obj}_{args.num}/trajectory.log")
    set_default_value(config, "template_global_pc", f"scene_{args.obj}_{args.num}/pc.ply")

    set_default_value(config, "debug_mode", args.debug_mode)
    set_default_value(config, "write_global_pc", args.write_global_pc)

    
    
    return config