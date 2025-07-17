import torch
import monai
from monai.networks.layers import Norm

configuration = {
    "checkpoint": './oct-datavol-1/checkpoints/oct_flexunet_2d_fold_4_best.pth',
    "model_type": "FlexibleUNet",
    "model_params": dict(
        spatial_dims=2,
        in_channels=1,
        out_channels=16,
        norm='BATCH',
        dropout=0.1,
        backbone='efficientnet-b5',
        pretrained=True,
    )
}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load full model
model_cls = getattr(monai.networks.nets, configuration['model_type'])
model = model_cls(
    backbone=configuration['model_params']['backbone'],
    spatial_dims=configuration['model_params']['spatial_dims'],
    in_channels=configuration['model_params']['in_channels'],
    out_channels=configuration['model_params']['out_channels'],
    norm=getattr(Norm, configuration['model_params']['norm']),
    dropout=configuration['model_params']['dropout'],
    pretrained=configuration['model_params']['pretrained'],
).to(device)

if configuration['checkpoint'] is not None:
    print(f"Checkpoint loaded from: {configuration['checkpoint']}")
    model.load_state_dict(torch.load(configuration['checkpoint'], map_location=device))

# Or use only the encoder part
encoder = model.encoder
encoder.eval()

# Example
dummy_input = torch.randn(1, 1, 256, 256).to(device)
with torch.no_grad():
    features = encoder(dummy_input)

print(f"Encoder returned {len(features)} feature maps:")
for i, f in enumerate(features):
    print(f" - Feature {i}: shape = {f.shape}")

final_embedding = features[-1]
print(f"\nFinal embedding map shape: {final_embedding.shape}")

pooled = torch.nn.functional.adaptive_avg_pool2d(final_embedding, 1)
embedding_vector = pooled.view(pooled.size(0), -1)
print(f"Flattened embedding vector shape: {embedding_vector.shape}")