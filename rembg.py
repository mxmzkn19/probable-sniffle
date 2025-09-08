from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    """
    Removes the background from an image and saves the result.
    
    Args:
        input_path (str): The path to the input image file.
        output_path (str): The path to save the output image file.
    """
    try:
        # Open the input image
        input_image = Image.open(input_path)
        
        # Remove the background
        output_image = remove(input_image)
        
        # Save the output image
        output_image.save(output_path)
        print(f"Background successfully removed and saved to {output_path}")
        
    except FileNotFoundError:
        print(f"Error: The file at {input_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Specify the path to your input image and the desired output path.
# Replace 'input_image.png' with the name of your image file.
input_file = 'input_image.png'
output_file = 'output_image_no_bg.png'

remove_background(input_file, output_file)