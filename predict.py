import torch
from torchvision import transforms
from PIL import Image

# Load the trained model
model = torch.load('ABD.pt')
model.eval()

# Function to predict
def predict(image_path):
    image = Image.open(image_path)
    transform = transforms.Compose([transforms.Resize((224, 224)),
                                    transforms.ToTensor()])
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)
    return output

# Example usage
output = predict('path_to_image.png')
print(output)
