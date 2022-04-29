path_to_configs = "./paper/tested_configs/%s.py"

# from custom train dataset
sim_train_mean=[100.618, 99.171, 96.664, 37.286] 
sim_train_std=[67.012, 66.945, 68.539, 47.192]

# from custom val dataset
sim_val_mean=[99.857, 96.167, 97.676, 55.093] 
sim_val_std=[66.85, 66.183, 67.875, 55.906]

# from coco
test_train_mean=[123.675, 116.28, 103.53, 35.3792] 
test_train_std=[58.395, 57.12, 57.375, 45.978]

def add_packages_paths():
    import os, sys
    path = os.path.abspath("./modified_packges")
    sys.path.insert(0,path)

def get_norm_params(input_channels, mode):
    if mode == "train":
        mean = sim_train_std
        std = sim_train_std
    if mode == "test":
        mean = test_train_mean
        std = test_train_std

    options = {
        1: dict(mean=[mean[3]], std=[std[3]], to_rgb=False),
        3: dict(mean=mean[0:3], std=std[0:3], to_rgb=True),
        4: dict(mean=mean, std=std, to_rgb=False),
    }
    return options[input_channels]

