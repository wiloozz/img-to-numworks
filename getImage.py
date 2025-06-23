from PIL import Image
import parameters

if parameters.showResult:
    from kandinsky import set_pixel

img = Image.open(parameters.SRCimage).convert("RGB")

def getImgPixel(x,y):
    try:
        r,g,b = img.getpixel((x,y))
        return (r,g,b)
    except: return (0,0,0) # // executed if the image is smaller than the window

text = ""

for x in range(320):

    for y in range(240):

        r,g,b = getImgPixel(x,y)
        
        colSum = r+g+b
        
        if colSum > parameters.colorSensibility:
            text += "1"
        else:
            text += "0"
            set_pixel(x,y,(0,0,0))

with open(parameters.outputFile,"w") as file:
    file.write(text)