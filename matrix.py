from PIL import Image

def image_to_matrix(image_path):
    img = Image.open(image_path)
    img = img.convert("L")  # Convert to grayscale
    matrix = list(img.getdata())
    width, height = img.size
    matrix = [matrix[i * width:(i + 1) * width] for i in range(height)]
    return matrix

# Example usage:
image_path = "trial.jpeg"  # Replace with the path to your image
matrix = image_to_matrix(image_path)
for row in matrix:
    print(row)
