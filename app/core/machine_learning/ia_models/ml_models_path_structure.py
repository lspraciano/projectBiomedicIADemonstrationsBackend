from typing import Dict

from configuration.configs import settings

app_root_path: str = settings.ROOT_PATH_FOR_DYNACONF + "/app"
ml_models_path: str = f"{app_root_path}/core/machine_learning/ia_models"
detection_path: str = f"{app_root_path}/core/machine_learning/ia_models/detection"

ml_models_dict_path_structure: Dict = {
    "classification": {
    },
    "detection": {
        "scanned_wbc_model": {
            "weights_file_name": "scanned_wbc_model.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "microscope_wbc_model": {
            "weights_file_name": "white_blood_cells_v7_y10.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "blood_serum_model": {
            "weights_file_name": "blood_serum_model.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "ki67_model": {
            "weights_file_name": "ki67_model.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "melanoma_model": {
            "weights_file_name": "melanoma_model.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "sperm_model": {
            "weights_file_name": "sperm_model.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "chromosomes_model": {
            "weights_file_name": "cromo_v7_yolo10s_1152.pt",
            "path": f"{detection_path}",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
    },
    "pose": {
    }
}
