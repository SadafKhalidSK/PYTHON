from PIL import Image, ImageDraw
import qrcode

data = "https://www.youtube.com/results?search_query=simmi+lil+world"

img = qrcode.make(data)
img.save("Learntoqrcode_QR.png")
print("✅ QR code saved as Learntoqrcode_QR.png")
