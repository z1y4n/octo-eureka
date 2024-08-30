import torch

# check if CUDA is available
print(torch.cuda.is_available())

# check what is the current device
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
print(torch.version.cuda)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
