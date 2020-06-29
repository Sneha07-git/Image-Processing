import sys
import os
from PIL import Image

# command line input
image_folder = sys.argv[1]
new_folder = sys.argv[2]

print(image_folder,new_folder)

if not os.path.exists(new_folder):  #to create a folder
    os.mkdir(new_folder)

for file_name in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file_name}')
    clean_name = os.path.splitext(file_name)[0] #to remove .jpg extention
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print('all done!')
