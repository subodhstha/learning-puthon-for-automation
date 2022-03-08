import img2pdf
import os

alllist = os.listdir(".")
photolist=[]
for x in alllist:
    if x.endswith(".png") or x.endswith(".jpg"):
        photolist.append(x)

pdf = img2pdf.convert(photolist)

file = open("assignment.pdf","wb")

file.write(pdf)
file.close()
