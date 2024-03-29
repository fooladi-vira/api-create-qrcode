import qrcode
import matplotlib.pyplot as plt
import cv2

data='instagram.com/bano_land.onlineshop'
qr=qrcode.QRCode(version=1, box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(
    fill_color="yellow",
    back_color="white")
img.save('qrcode2.jpg')
im=cv2.imread('qrcode2.jpg')
plt.imshow(im)
plt.axis('off')
plt.title('ITVIRACo')
plt.show()