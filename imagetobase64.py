import os
import sys
import base64

def image_to_base64(image_path):
    try:
        # Read the image file in binary mode
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Convert image data to base64
        base64_data = base64.b64encode(image_data).decode('utf-8')

        # Create a new file to save the base64 string
        base_dir = os.path.dirname(image_path) or '.'
        base_name = os.path.basename(image_path)
        new_file_name = os.path.splitext(base_name)[0] + '_base64.txt'
        new_file_path = os.path.join(base_dir, new_file_name)

        with open(new_file_path, 'w') as output_file:
            output_file.write(base64_data)

        # Print success message
        print(f"Success! Base64 file created: {new_file_path}")
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <image_file>")
    else:
        image_file = sys.argv[1]

        # Handle relative paths without './' or '.\\'
        if not os.path.isabs(image_file):
            image_file = os.path.abspath(image_file)

        image_to_base64(image_file)
