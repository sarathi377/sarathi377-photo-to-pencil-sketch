
import cv2

# Read the input image
img = cv2.imread("photo.jpg")

if img is None:
    print("Error: photo.jpg not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert grayscale image
inverted = 255 - gray

# Apply Gaussian blur
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

# Create pencil sketch
sketch = cv2.divide(gray, 255 - blurred, scale=256)

# Save the output image
cv2.imwrite("sketch.jpg", sketch)

print("Pencil sketch saved as sketch.jpg")
