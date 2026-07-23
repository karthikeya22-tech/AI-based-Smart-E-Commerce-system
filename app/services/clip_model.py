# CLIP model wrapper
import torch
import clip
from PIL import Image

class CLIPModel:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Loading CLIP on {self.device}...")
        self.model, self.preprocess = clip.load("VitB/32", device=self.device)
        self.model.eval()
        print("CLIP model loaded successfully.")
        
        
    def preprocess_image(self, image_path: str):
        image = Image.open(image_path).convert("RGB")
        
        return self.preprocess(image).unsqueeze(0).to(self.device)
    
    @torch.no_grad()
    def encode_image(self, image_path: str):
        image = self.preprocess_image(image_path)
        embedding = self.model.encode_image(image)
        embedding /= embedding.norm(dim=-1, keepdim=True)
        return embedding.cpu().numpy()[0]
    
    @torch.no_grad()
    def encode_text(self, text: str):
        tokens = clip.tokenize([text]).to(self.device)
        embedding = self.model.encode_text(tokens)
        embedding /= embedding.norm(dim=-1, keepdim=True)

        return embedding.cpu().numpy()[0]
    clip_model=CLIPModel()