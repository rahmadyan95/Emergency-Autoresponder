import qrcode

img = qrcode.make("https://maps.app.goo.gl/DMdSaov7ECPFxtku6")\
img.save("qr.png")