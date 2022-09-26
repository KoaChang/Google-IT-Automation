# If I really wanted to I can change all these paths to absolute paths by joining each of
# of them to the home path /Users/malamapono/PyCharmProjects/GoogleITProjects

from PIL import Image
import os
import shutil

if os.path.exists('new_images'):
    # os.rmdir('new_images') doesn't work since directory is not empty
    shutil.rmtree('new_images')
    # removes directory even if it is not empty
    os.mkdir('new_images')
else:
    os.mkdir('new_images')

for filename in os.listdir('images'):
    if filename == '.DS_Store':
        continue
    img = Image.open(os.path.join('images',filename))
    new_img = img.rotate(270).resize((128,128)).convert('RGB')
    path, new_filename = os.path.split(filename)
    new_filename = os.path.splitext(filename)[0]
    # get filename without extension that is throwing errors
    new_img.save(os.path.join('new_images',new_filename +'.jpeg'))

print("Done, successfully transfered")