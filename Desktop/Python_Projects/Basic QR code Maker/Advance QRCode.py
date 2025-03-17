import qrcode as qr
from PIL import Image
import random
qr1=qr.QRCode(version=1,border=4,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10)
print("ENTER URL: ")
img_qr=input()
name=str(random.randint(1000,99999)) +".png"
qr1.add_data(img_qr)
qr1.make(fit=True)
img = qr1.make_image(fill_color="blue", back_color="white")
img.save(name)
