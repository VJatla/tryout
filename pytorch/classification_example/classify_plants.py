import torchvision
from torchvision import transforms

# Train, validate and test paths
trn_data_path = "data/trn"
val_data_path = "data/val"
tst_data_path = "data/tst"

# Processing and creating a torch.tensor from the data
transforms = transforms.Compose([transforms.Resize(64),
                                 transforms.ToTensor(),
                                 transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                      std=[0.229, 0.224, 0.225] )])
# 
trn_data = torchvision.datasets.ImageFolder(root=trn_data_path,
                                            transform=transforms)
val_data = torchvision.datasets.ImageFolder(root=val_data_path,
                                            transform=transforms)
tst_data = torchvision.datasets.ImageFolder(root=tst_data_path,
                                             transform=transforms)
# Data loader
batch_size = 2
trn_data_loader = data.DataLoader(trn_data, batch_size=batch_size)
val_data_loader  = data.DataLoader(val_data, batch_size=batch_size)
tst_data_loader  = data.DataLoader(tst_data, batch_size=batch_size)
