from PIL import Image
from tra import var
#import kivy
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
class imk:
    def img(fil_path,scr_la,des_la):
        im = Image.open(fil_path)

        text = pytesseract.image_to_string(im, lang = scr_la, config=tessdata_dir_config)

        print(text)
        vr1= var.trann(text,des_la)
        return  vr1


#with open('maic.txt', mode='w') as file:
#   file.write(vr1)

dj="how are you"
