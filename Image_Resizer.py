import cv2

upload_Image = 'welcome.jpg'  # Image uploaded
ResultImage = 'Result.jpeg'    # Generated image filename

percent = int(input("Enter the size percent for the image: "))

img = cv2.imread(upload_Image)  # Reading the image with OpenCV

if img is not None:  # Check if the image was properly loaded
    # Getting image dimensions
    height, width = img.shape[:2]

    # Changing its dimensions
    new_width = int(width * percent / 100)
    new_height = int(height * percent / 100)

    # Resizing the image
    out = cv2.resize(img, (new_width, new_height))

    # Generating new image
    cv2.imwrite(ResultImage, out)
    print("Image resized and saved successfully as", ResultImage)
else:
    print("Error: Unable to read the image file.")
