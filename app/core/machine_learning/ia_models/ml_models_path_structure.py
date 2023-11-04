from typing import Dict

from configuration.configs import settings

app_root_path: str = settings.ROOT_PATH_FOR_DYNACONF + "/app"
ml_models_path: str = f"{app_root_path}/utils/ml_models"
classification_path: str = f"{app_root_path}/utils/ml_models/classification"
detection_path: str = f"{app_root_path}/utils/ml_models/detection"
pose_path: str = f"{app_root_path}/utils/ml_models/pose"

ml_models_dict_path_structure: Dict = {
    "classification": {
        "ski_mask": {
            "weights_file_name": "ski_mask.pt",
            "path": f"{classification_path}/protection_equipments",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "cover_sleeve": {
            "weights_file_name": "cover_sleeve.pt",
            "path": f"{classification_path}/protection_equipments",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "carabiner": {
            "weights_file_name": "carabiner.pt",
            "path": f"{classification_path}/protection_equipments",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "shirt": {
            "weights_file_name": "shirt.pt",
            "path": f"{classification_path}/protection_equipments",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "protection_equipments_person": {
            "weights_file_name": "person_pose.pth",
            "path": f"{classification_path}/protection_equipments",
            "file_net_name": "person_pose_net.py",
            "net_input_size": 34,
            "net_class_name": "PersonPoseNeuralNetwork"
        },
    },
    "detection": {
        "verification": {
            "weights_file_name": "verification.pt",
            "path": f"{detection_path}/verification",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "signaling": {
            "weights_file_name": "signaling.pt",
            "path": f"{detection_path}/signaling",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "locks": {
            "weights_file_name": "locks.pt",
            "path": f"{detection_path}/locks",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        },
        "protection_equipments": {
            "weights_file_name": "protection_equipments.pt",
            "path": f"{detection_path}/protection_equipments",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        }
    },
    "pose": {
        "person": {
            "weights_file_name": "person_pose.pt",
            "path": f"{pose_path}/person",
            "file_net_name": "",
            "net_input_size": 0,
            "net_class_name": ""
        }

    }
}
