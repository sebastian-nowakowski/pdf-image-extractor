import sys
import fitz
import io
from PIL import Image

def extract(path: str, output_path: str):
    """[summary]
    Extracts images from pdf file at [path] to [output_path]/
    """
    file = fitz.open(path)
    if file:
        for page_index in range(len(file)):
            # get the page itself
            page = file[page_index]
            image_list = page.get_images()
            # printing number of images found in this page
            if image_list:
                print(f'[+] Found a total of {len(image_list)} images in page {page_index}')
            else:
                print("[!] No images found on page", page_index)
            for image_index, img in enumerate(page.get_images(), start=1):
                pix = fitz.Pixmap(file, img[0])
                pix0 = fitz.Pixmap(fitz.csRGB, pix)
                pix0.save(f'{output_path}/img{img[0]}.jpg')

# gets arguments from command line
extract(sys.argv[1], sys.argv[2])