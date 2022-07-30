from turtle import fillcolor
import qrcode 


data = "Apple bottom jeans, boots with the furrrrrrrrrrr" 

qr = qrcode.QRCode(version = 1, box_size = 10, border = 4)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = "black", back_color = "red" )

img.save("D:/Codes/misc/JESSICADIDUSLEEPWITHURGODDAMNTEACHER.png")