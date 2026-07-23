# Image upload and processing service
from pathlib import Path
from PIL import Image
import os


class ImageService:

    def __init__(self):

        self.base_dir = Path(__file__).resolve().parents[2]
        self.image_dir = self.base_dir / "data" / "images"

    def get_image_path(self, product_id: int):

        image_path = self.image_dir / f"{product_id}.jpg"

        if image_path.exists():
            return str(image_path)

        return None

    def image_exists(self, product_id: int):

        image_path = self.image_dir / f"{product_id}.jpg"

        return image_path.exists()

    def load_image(self, product_id: int):

        image_path = self.get_image_path(product_id)

        if image_path is None:
            raise FileNotFoundError(
                f"Image not found for Product ID: {product_id}"
            )

        return Image.open(image_path).convert("RGB")

    def save_uploaded_image(
        self,
        image,
        filename: str
    ):

        save_path = self.image_dir / filename

        image.save(save_path)

        return str(save_path)

    def resize_image(
        self,
        image: Image.Image,
        size=(224, 224)
    ):

        return image.resize(size)

    def delete_image(self, filename: str):

        file_path = self.image_dir / filename

        if file_path.exists():
            os.remove(file_path)
            return True

        return False


image_service = ImageService()