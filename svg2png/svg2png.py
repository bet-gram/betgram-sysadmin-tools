svg_code = """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="5cm" height="4cm" version="1.1"
     xmlns="http://www.w3.org/2000/svg">
  <desc>Four separate rectangles
  </desc>
    <rect x="0.5cm" y="0.5cm" width="2cm" height="1cm"/>
    <rect x="0.5cm" y="2cm" width="1cm" height="1.5cm"/>
    <rect x="3cm" y="0.5cm" width="1.5cm" height="2cm"/>
    <rect x="3.5cm" y="3cm" width="1cm" height="0.5cm"/>

  <!-- Show outline of canvas using 'rect' element -->
  <rect x=".01cm" y=".01cm" width="4.98cm" height="3.98cm"
        fill="none" stroke="blue" stroke-width=".02cm" />

</svg>
"""

from wand.api import library
import wand.color
import wand.image
from PIL import Image

name = 'chelsea'

file_object = open(name + '.svg', 'r')

with wand.image.Image() as image:
    with wand.color.Color('transparent') as background_color:
        library.MagickSetBackgroundColor(image.wand, 
                                         background_color.resource) 
    image.read(blob=file_object.read())
    png_image = image.make_blob("png32")

with open(name + '.png', "wb") as out:
    out.write(png_image)

img = Image.open(name + '.png').convert('LA')
img.save('greyscale.png')

im = Image.open(name + '.png')
foreground = Image.open('greyscale.png')

bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im, (0, 0), im)
bg.save("test.png")