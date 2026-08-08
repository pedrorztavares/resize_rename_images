from PIL import Image
from pathlib import Path
import os
from os import listdir, rename

BASE_DIR = Path("images")
NEW_DIR = Path("images_save")

def rename ():
    start_sufix = int(input("what number should we start on?"))
    for images_name in os.listdir(BASE_DIR):
        old_path = BASE_DIR / images_name
        
        new_name = f"img_{start_sufix:03d}.png"
        new_path = BASE_DIR / new_name

        os.rename(old_path, new_path)
        
        start_sufix = start_sufix + 1 
        
def resize () :
    for images_name in os.listdir(BASE_DIR):
        old_path = BASE_DIR / images_name
        new_path = NEW_DIR /images_name
        image = Image.open(old_path)
        size = (512,512)
        resize_image = image.resize(size)
        print(new_path)
        resize_image.save(new_path)
        print("Done")



    
if __name__ == "__main__":
    print('hello world')
    rename()
    resize()