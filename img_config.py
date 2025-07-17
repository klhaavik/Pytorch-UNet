import os
import cv2
import numpy as np
from PIL import Image

dir = "C:/Users/bachc/GitHub/Synthset-Generation/Blender/Cbus/Images/Sem_seg"

# for imgfile in os.listdir(dir):
#     filename = os.path.join(dir, imgfile)
#     if(filename.endswith(".keep")): continue
#     print(filename)
#     image = cv2.imread(filename)
#     # arr = np.asarray(bytearray(img.read()), dtype=np.uint8)
#     # image = cv2.imdecode(img,-1) # 'load it as it is'
#     s = image.shape
#     #check if third tuple of s is 4
#     #if it is 4 then remove the 4th channel and return the image.
#     if len(image.shape) > 2 and image.shape[2] == 4:
#     #convert the image from RGBA2RGB
#         image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR) 
#     cv2.imwrite(filename, image)



def convert_to_binary(input_path, output_path, threshold=128):
    """
    Converts a PNG image to true black and white (binary).

    Args:
        input_path (str): Path to the input PNG image.
        output_path (str): Path to save the output binary PNG image.
        threshold (int): Pixel value threshold (0-255). 
                            Pixels above this value become white (255), 
                            and pixels below become black (0).
    """
    try:
        img = Image.open(input_path).convert('L')  # Open and convert to grayscale ('L' mode)

        # Apply threshold to binarize the image
        # 'point' method applies a function to each pixel
        # 'mode=1' specifies a 1-bit pixel format (black and white)
        binary_img = img.point(lambda x: 255 if x > threshold else 0, mode='1')

        binary_img.save(output_path)
        print(f"Image successfully converted and saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Create a dummy image for testing if you don't have one
# from PIL import ImageDraw
# img_test = Image.new('RGB', (100, 100), color = 'red')
# draw = ImageDraw.Draw(img_test)
# draw.text((10,10), "Hello", fill=(0,0,0))
# img_test.save("input_image.png")

desired_threshold = 25 # Adjust this value based on your image content



for imgfile in os.listdir(dir):
    if not os.path.isfile(os.path.join(dir, imgfile)): continue
    filename = os.path.join(dir, imgfile)
    if filename.endswith(".keep"): continue
    input_image_path = filename
    output_image_path = filename
    convert_to_binary(input_image_path, output_image_path, desired_threshold)
