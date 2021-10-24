from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('/home/kali/Desktop/Barcode.png')

result = decode(img)

print(result)