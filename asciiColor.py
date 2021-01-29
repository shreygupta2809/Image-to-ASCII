from PIL import Image, ImageDraw, ImageFont
from statistics import mean


ASCII = ["@", "#", "$", "%", "?", "+", "*", ";", ":", ",", "."]


def preprocessImage(image, scale=0.7, charWidth=6, charHeight=11):
    ratio = charWidth / charHeight
    width, height = image.size
    newWidth = int(width * scale)
    newHeight = int(newWidth * scale * ratio)
    rImage = image.resize((newWidth, newHeight))
    return rImage


def asciiImage(image, charWidth=6, charHeight=11):
    pixels1 = list(image.getdata())
    width, height = image.size
    outputImage = Image.new("RGB", (charWidth * width, charHeight * height))
    draw = ImageDraw.Draw(outputImage)
    asciiCharacter = "".join([ASCII[int(mean(pixel)) // 25] for pixel in pixels1])
    for i, pixel in enumerate(pixels1):
        coords = (
            (i % width) * charWidth,
            (i // width) * charHeight,
        )
        draw.text(coords, ASCII[int(mean(pixel)) // 25], fill=pixel)
    return outputImage


def main():
    inputPath = input("Path for Image: ")
    try:
        inputImage = Image.open(inputPath)
    except:
        print("Image does not exist!")
        return

    font = ImageFont.load_default()
    width, height = font.getsize("#")
    outputImage = asciiImage(
        preprocessImage(inputImage, 0.7, width, height), width, height
    )
    outputImage.save("output.jpeg")


main()