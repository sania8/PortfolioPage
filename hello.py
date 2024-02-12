import cv2

def resize_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Check if the image is successfully loaded
    if image is None:
        print("Error: Unable to load the image.")
        return None
    
    # Resize the image to 300x300 pixels
    resized_image = cv2.resize(image, (300, 300))
    
    return resized_image

# Example usage
resized_image = resize_image("assets/img/new1.png")  # Replace "input_image.jpg" with your image file path

