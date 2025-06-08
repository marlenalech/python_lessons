import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()
qr = qrcode.QRCode(version=None,box_size=10,border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color=(204,125,219), back_color='white')
img.save(filename)
print(f'QR code save as {filename}')
