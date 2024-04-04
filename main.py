from options import Options

from config_init import get_config
from method.slam import slam_system
from method.rris import rris_system, integrate_scene



import integrate_scene
import mesh_gen.poisson as poisson
import mesh_gen.alpha_shapes as alpha_shapes

if __name__ == "__main__":
    option = Options()
    args = option.parser.parse_args()
    config = get_config(args)

    # run point cloud reconstruction pipeline
    if config['method'] == 'slam':
        slam_system.pipeline(config)
    elif config['method'] in ['rris', 'rgst_frag']:
        rris_system.pipeline(config)
        # run mesh reconstruction pipeline
        if config['mesh_method'] == 'volumetric':
            integrate_scene.run(config)
        elif config['mesh_method'] == 'poisson':
            poisson.run(config)
        elif config['mesh_method'] == 'as':
            alpha_shapes.run(config)


