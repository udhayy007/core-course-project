"""
import os
from PIL import Image, ImageChops, ImageEnhance

# Function to convert input image to ELA applied image
def convert_to_ela_image(path, quality):
    original_image = Image.open(path).convert("RGB")

    # Save the image at the given quality
    resaved_file_name = "resaved_image.jpg"  # Predefined filename for the resaved image
    original_image.save(resaved_file_name, "JPEG", quality=quality)
    resaved_image = Image.open(resaved_file_name)

    # Get the difference between the original image and the resaved image
    ela_image = ImageChops.difference(original_image, resaved_image)

    # Get extrema to find the scaling factor
    extrema = ela_image.getextrema()
    max_difference = max([pix[1] for pix in extrema])
    if max_difference == 0:
        max_difference = 1
    scale = 350.0 / max_difference

    # Enhance the ELA image to brighten the differences
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)

    ela_image_path = "ela_image.png"
    ela_image.save(ela_image_path)  # Save the ELA image

    return ela_image_path  # Return the path to the ELA image


if __name__ == "__main__":
    # If this script is executed directly, it will run the conversion
    import sys
    file_path = sys.argv[1]
    quality = int(sys.argv[2])
    convert_to_ela_image(file_path, quality).show()

"""
import os
from PIL import Image, ImageChops, ImageEnhance

# Converts input image to ELA applied image
def convert_to_ela_image(path, quality):
    original_image = Image.open(path).convert("RGB")

    # Resaving input image at the desired quality
    resaved_file_name = "resaved_image.jpg"  # Predefined filename for resaved image
    original_image.save(resaved_file_name, "JPEG", quality=quality)
    resaved_image = Image.open(resaved_file_name)

    # Pixel difference between original and resaved image
    ela_image = ImageChops.difference(original_image, resaved_image)

    # Scaling factors are calculated from pixel extremas
    extrema = ela_image.getextrema()
    max_difference = max([pix[1] for pix in extrema])
    if max_difference == 0:
        max_difference = 1
    scale = 350.0 / max_difference

    # Enhancing ELA image to brighten the pixels
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)

    ela_image.save("ela_image.png")  # Save the ELA image as a PNG
    return ela_image


