import importlib
import os
import sys
from typing import Optional, Any

import torch
import torch.nn as nn
from ultralytics import YOLO

from app.utils.ml_models.ml_models_path_structure import ml_models_dict_path_structure


def load_ml_yolo_model(
        ml_model_name: str,
        task: str,
) -> Optional[YOLO]:
    """
    Loads a machine learning YOLO model for a given task and target class.

    Args:
        ml_model_name: The name of the target class.
        task: The task that the model is used for.

    Returns:
        A YOLO model, or None if the model could not be loaded.
    """
    ml_model_data: dict = ml_models_dict_path_structure[task][ml_model_name]
    full_ml_model_path: str = f"{ml_model_data['path']}/{ml_model_data['weights_file_name']}"

    if not os.path.exists(full_ml_model_path):
        return None

    ml_classification_model: YOLO = YOLO(full_ml_model_path)

    return ml_classification_model


def load_ml_torch_model(
        ml_model_name: str,
        task: str,
) -> Optional[nn.Module]:
    """
    Load a PyTorch machine learning model from a specified model directory.

    Args:
        ml_model_name (str): The name of the machine learning model to load.
        task (str): The task or purpose of the model.

    Returns:
        Optional[nn.Module]: The loaded PyTorch model as an instance of nn.Module,
        or None if the model or weights file does not exist.
    """
    ml_model_data: dict = ml_models_dict_path_structure[task][ml_model_name]
    model_directory_path: str = ml_model_data["path"]
    full_ml_weights_path: str = f"{model_directory_path}/{ml_model_data['weights_file_name']}"
    full_ml_net_path: str = f"{model_directory_path}/{ml_model_data['file_net_name']}"
    net_class_name: str = ml_model_data['net_class_name']
    net_input_size: int = ml_model_data['net_input_size']
    file_net_name: str = ml_model_data["file_net_name"]
    module_net_name: str = file_net_name.split(sep=".")[0]

    if not os.path.exists(full_ml_weights_path):
        return None

    if not os.path.exists(full_ml_net_path):
        return None

    sys.path.append(model_directory_path)

    net_module: Any = importlib.import_module(
        name=module_net_name
    )

    net_class: nn.Module = getattr(net_module, net_class_name)

    current_net: nn.Module = net_class(net_input_size)
    current_net.load_state_dict(torch.load(full_ml_weights_path))

    return current_net.eval()
