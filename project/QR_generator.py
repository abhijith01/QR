import qrcode
url=input("Enter an url")
img= qrcode.make(url)
img.save("myqr.png")
img.show()
