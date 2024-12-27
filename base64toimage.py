import os
import sys
import base64

def base64_to_image(base64_file_path, output_format='jpg'):
    try:
        # Read the base64 file
        with open(base64_file_path, 'r') as base64_file:
            base64_data = base64_file.read()

        # Decode base64 data to binary
        image_data = base64.b64decode(base64_data)

        # Create a new image file
        base_dir = os.path.dirname(base64_file_path) or '.'
        base_name = os.path.basename(base64_file_path)
        new_file_name = os.path.splitext(base_name)[0] + f'_decoded.{output_format}'
        new_file_path = os.path.join(base_dir, new_file_name)

        with open(new_file_path, 'wb') as image_file:
            image_file.write(image_data)

        # Print success message
        print(f"Success! Image file created: {new_file_path}")
    except FileNotFoundError:
        print(f"Error: The file '{base64_file_path}' was not found.")
    except base64.binascii.Error:
        print("Error: The file does not contain valid base64 data.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script_name.py <base64_txt_file> [output_format]")
    else:
        base64_file = sys.argv[1]

        # Handle relative paths without './' or '.\\'
        if not os.path.isabs(base64_file):
            base64_file = os.path.abspath(base64_file)

        output_format = sys.argv[2] if len(sys.argv) == 3 else 'jpg'
        base64_to_image(base64_file, output_format)