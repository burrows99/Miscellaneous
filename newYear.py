import PIL.image
CHARACTERS=['@','#','S','%','?','*','+',';',':',',','.']

def resizeImage(image,newWidth=100):
  width,height=image.size
  ratio=height/width
  newHeight=int(newWidth*ratio)
  resizedImage=image.resize((newWidth,newHeight))
  return(resizedImage)

def grayify(image):
  grayscaleImage=image.convert("L")
  return(grayscaleImage)

def pixelsToAscii(image):
  pixels=image.getdata()
  characters="".join([CHARACTERS[pixel//25] for pixel in pixels])
  return(characters)

def main(newWidth=100):
  path='Users/raburrows/Desktop/download.jpeg'
  try:
    image=PIL.image.open(path)
  except:
    print(path,"is not a valid path.")
  newImageData=pixelsToAscii(grayify(resizeImage(image)))
  pixelCount=len(newImageData)
  asciiImage="\n".join(newImageData[i:(i+newWidth)] for i in range(pixelCount,newWidth))
  print(asciiImage)
