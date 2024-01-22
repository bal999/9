import cv2

# Path to the downloaded image
image_path = r"CaptchaServlet (1).jfif"

# Load the image using OpenCV
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours in the binary image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours and extract text regions
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    # Filter out small contours
    if w > 10 and h > 10:
        # Draw rectangle around the text region (optional)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract the text region from the original image
        text_region = gray_image[y:y + h, x:x + w]

        # Check if the text region is not empty
        if text_region.size > 0:
            # Perform OCR on the text region (you can use your preferred OCR library)
            # For simplicity, this example just prints the text region in ASCII
            extracted_text = " ".join([str(int(pixel)) for row in text_region for pixel in row])

            # Print the extracted text
            print("Extracted Text:")
            print(extracted_text)

# Show the image with bounding boxes (optional)
cv2.imshow("Text Extraction", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
