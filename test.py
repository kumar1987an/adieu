import qrcode

img = qrcode.make("https://replit.com/@jarvis0530/adieu#main.py")
img.save("myqrcode.png")
img.show()
