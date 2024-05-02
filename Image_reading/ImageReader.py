from PIL import Image
import matplotlib.pyplot as plt

image_path = "./image.png"

try:
    with open(image_path, 'rb') as f:
        img = Image.open(f)
        
        width, height = img.size
        
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                
                print(f"Pixel at ({x}, {y}): Red={r}, Green={g}, Blue={b}")
    
    plt.imshow(img)
    plt.show()

except IOError as e:
    print(f"An error occurred while processing the image: {e}")
