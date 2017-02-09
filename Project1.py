from PIL import Image, ImageFilter

#defining variables/constructor
def med(mylist):
    listlength = len(mylist)
    sortedValues = sorted(mylist)
    middleIndex = (listlength + 1)//2 - 1
    return sortedValues[middleIndex]

#Openening up pictures
pictures = [] #pictures is a variable for storing how many pictures there are
pictures.append(Image.open("Images/1.png")) #Note to self. For opening up the img, just have the fold that the pictures are in
pictures.append(Image.open("Images/2.png"))
pictures.append(Image.open("Images/3.png"))
pictures.append(Image.open("Images/4.png"))
pictures.append(Image.open("Images/5.png"))
pictures.append(Image.open("Images/6.png"))
pictures.append(Image.open("Images/7.png"))
pictures.append(Image.open("Images/8.png"))
pictures.append(Image.open("Images/9.png"))

#Defining variables    
Width, Height = pictures[0].size #Will set the width and height of the final image
redPixel = [] #Red pixel count from the images
greenPixel = [] #Green pixel count from the images
bluePixel = [] #Blue pixel count from the images
    
Red, Green, Blue = pictures[6].getpixel((2,3)) 
    
print(Red, Green, Blue) 

#prints out the final image    
finalimg = Image.new("RGB", (Width, Height), "white") #finalimg is a vairable to get the final img

for x in range(Width): #Defines what the finalimg width is. Also a loop to print out the final imagae
        for y in range(Height): #Defines what the finalimg height is
            for myImage in pictures:
                Red, Green, Blue = myImage.getpixel((x,y))
                redPixel.append(Red)
                greenPixel.append(Green)
                bluePixel.append(Blue)
            
            medianRed = med(redPixel) 
            medianGreen = med(greenPixel)
            medianBlue = med(bluePixel)
            
            finalimg.putpixel((x, y), (medianRed, medianGreen, medianBlue))
            
            redPixel = [] #Final red pixel count
            greenPixel = [] #Final green pixel count
            bluePixel = [] #Final blue pixel count
    
finalimg.save("finalimage.png") #Saves the image under Project1 folder
    