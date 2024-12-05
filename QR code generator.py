import requests
import pyjokes
import qrcode


joke = pyjokes.get_joke()
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=3,
)
qr.add_data(joke)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")

img.show()
print(f"QR code saved to {img_path}")
