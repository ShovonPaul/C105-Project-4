import os
import cv2

# Set the path for the Images folder
path = "Images/Images"


# Create a list of images
images = []

# Loop through files in the folder
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file

        print(file_name)

        images.append(file_name)

print(len(images))
count = (len(images))

# Get image information
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print(size)

# Create VideoWriter
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Add images to VideoWriter
for i in range(0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("Done!")

