"""Realize the parameter configuration function of dataset, model, training and verification code."""
import torch
from torch.backends import cudnn

# ==============================================================================
# General configuration
# ==============================================================================
torch.manual_seed(0)
device = torch.device("cuda", 0)
cudnn.benchmark = True
upscale_factor = 2
mode = "train"
exp_name = "MSRU_x2"

# ==============================================================================
# Training configuration
# ==============================================================================
if mode == "train":
    # Dataset
    train_image_dir = f"data\shuffled2D_train_HR"
    valid_image_dir = f"data\shuffled2D_valid_HR"

    image_size = 33
    batch_size = 32
    num_workers = 4

    # Incremental training and migration training
    resume = False
    strict = True
    start_epoch = 0
    resume_weight = ""

    # Total number of epochs. SGD: 580000. Adam: 10000
    epochs = 300

    # SGD optimizer parameter (less training and better PSNR)
    model_optimizer_name = "sgd"
    model_lr = 1e-4
    model_momentum = 0.9
    model_weight_decay = 1e-4
    model_nesterov = False

    # Adam optimizer parameter (faster training and low PSNR)
    # model_optimizer_name = "adam"
    # model_lr = 1e-4
    # model_betas = (0.9, 0.999)

    print_frequency = 100

# ==============================================================================
# Verify configuration
# ==============================================================================
if mode == "valid":
    # Test data address
    sr_dir = f"results/test/{exp_name}"
    hr_dir = f"data\shuffled2D_test_HR"

    model_path = f"results/{exp_name}/best24.41.pth"
