from PIL import Image, ImageDraw, ImageFont

ASCII = ["@", "#", "$", "%", "?", "+", "*", ";", ":", ",", "."]


def preprocessImage(image, newWidth=150, charWidth=6, charHeight=11):
    width, height = image.size
    ratio = height / width
    newHeight = int(newWidth * ratio * (charWidth / charHeight))
    rImage = image.resize((newWidth, newHeight))
    return rImage.convert("L")


def asciiImage(image, charWidth=6, charHeight=11):
    pixelData = image.getdata()
    asciiCharacter = "".join([ASCII[pixel // 25] for pixel in pixelData])
    width, height = image.size
    finalImage = "\n".join(
        [asciiCharacter[i : i + width] for i in range(0, len(asciiCharacter), width)]
    )
    return finalImage  # For text output, incase of image comment this line and uncomment bottom code

    # IMAGE

    # font = ImageFont.load_default()
    # finalW, finalH = font.getsize(finalImage)
    # counter = finalImage.count("\n")
    # width = (finalW - (counter * charWidth)) // (counter + 1)
    # height = charHeight * (counter + 1) + (counter + 1) * 4
    # # outputImage = Image.new("RGB", (width * charWidth, height * charHeight))
    # outputImage = Image.new("RGB", (width, height))
    # draw = ImageDraw.Draw(outputImage)
    # draw.text((0, 0), finalImage)
    # return outputImage


def main():
    inputPath = input("Path for Image: ")
    try:
        inputImage = Image.open(inputPath)
    except:
        print("Image does not exist!")
        return
    font = ImageFont.load_default()
    width, height = font.getsize("$")
    outputImage = asciiImage(
        preprocessImage(inputImage, 150, widht, height), width, height
    )

    # TEXT
    with open("output.txt", "w") as f:
        f.write(outputImage)

    # IMAGE
    # outputImage.save("outputGrey.jpeg")


main()