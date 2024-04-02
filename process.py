"""Image processing functions."""

from pathlib import Path

from PIL import Image

IMAGES_PATH = Path("drunkImages")
DESTINATION_PATH = Path("processedImages")

def get_image_info(path: Path) ->  None:
    """Extract information from the image."""
    for image_path in path.iterdir():

        image_name = image_path.name
        print(f"Image name: {image_name}")

        with Image.open(image_path) as full_image:


            width, height = full_image.size
            quarter_width = width // 2
            quarter_height = height // 2

            quarters = [
                (0, 0, quarter_width, quarter_height), # Top left quarter
                (quarter_width, 0, width, quarter_height), # Top right quarter
                (0, quarter_height, quarter_width, height), # Bottom left quarter
                (quarter_width, quarter_height, width, height), # Bottom right quarter
            ]
            for i, quarter in enumerate(quarters):
                quarter_image = full_image.crop(quarter)
                quarter_image.save(f"{DESTINATION_PATH}/{i}_{image_name}.webp")


def main() -> None:
    get_image_info(IMAGES_PATH)


if __name__ == "__main__":
    main()
