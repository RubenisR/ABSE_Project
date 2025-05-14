import torch

# Load GPU checkpoint onto CPU
state = torch.load(
    "apps/radiology/model/pretrained_deepedit_dynunet.pt",
    map_location=torch.device("cpu"),
)
# Save back as a CPU checkpoint
torch.save(state, "apps/radiology/model/pretrained_deepedit_cpu.pt")
