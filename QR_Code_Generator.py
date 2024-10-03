# QR Code Generator 02/10/2024

import qrcode

# Get URL input from the user
url = input("Enter the URL to generate the QR code for: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # control error correction level
    box_size=10,  # size of the box where QR code is displayed
    border=4,  # thickness of the border
)

qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("qrcode.png")

print("QR code generated, saved as 'qrcode.png'")