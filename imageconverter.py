# *******************************
# * IMAGE CONVERTER PYTHON TEST *
# *******************************

# ***********
# * IMPORTS *
# ***********
from PIL import Image
from imgpy import Img
import svgutils.compose as svgc

# ************************
# * ADDITIONAL VARIABLES *
# ************************
# This tuplet can be changed to any size the user wants, (width, height) of the resized image
size = (150, 150)
# Method used to resample the image, LANCZOS = the best performance for rescaling, but the slowest
resample_method = Image.LANCZOS

# ********************************************************************
# * image1.jpg must be compatible with Safari, Chrome, Edge, Firefox *
# ********************************************************************
#---------------------------------------------------------------------------------------------------------------
# I chose JPEG because it's a loss compression method, but its good for small sized images
# It's recommended to use JPEG only for final copyphotos, if the user is sure that the final product will not be changed again
#---------------------------------------------------------------------------------------------------------------
# Load the JPG image
image1 = Image.open("./input_images/image1.jpg")
# Determine the extension of the file
image1_extension = "jpeg"
image1_extension_format = image1_extension.upper()
# Resize image 1 to 150px width, 150px height using the resample_method saved above
image1_resized = image1.resize(size, resample_method)
# Save image 1 as a JPEG file
image1_resized.save('./output_images/image1_output.%s' % (image1_extension), image1_extension_format)

# ********************************************************
# * image2.svg can be compatible only with Google Chrome *
# ********************************************************
#---------------------------------------------------------------------------------------------------------------
# Since svgutils is not such a strong library for python and and I could not retrieve the width and height from
# the original picture, I had to hard code it, I know, bad coding, but still better than not solving the issue
#---------------------------------------------------------------------------------------------------------------
# Load SVG image
image2_svg_original = svgc.SVG('./input_images/image2.svg')
# SVG image 2 will be translated 40px on horizontal, 40px on vertical and scaled to 0.09 of its original size
image2_svg_original.moveto(40,40, 0.09)
# create a SVG figure with width 150, height 150 based on the SVG image received as input
figure = svgc.Figure( 150, 150, image2_svg_original)
# svgutils can only save a SVG as a SVG
figure.save("./output_images/image2_output.svg")

# ********************************************************
# * image3.gif can be compatible only with Google Chrome *
# ********************************************************
#---------------------------------------------------------------------------------------------------------------
# A GIF file can not be treated as a simple image, it has a sequence of frames and it need another library.
#---------------------------------------------------------------------------------------------------------------
# Deal with GIF files using impgpy library
with Img(fp='./input_images/image3.gif') as gif:
    gif.resize(size, resample=resample_method)
    gif.save(fp='./output_images/image3_output.gif')

# ********************************************************************
# * image4.png must be compatible with Safari, Chrome, Edge, Firefox *
# ********************************************************************
# Load the PNG file
image4 = Image.open("./input_images/image4.png")
# Determine the extension of the file
image4_extension = "png"
image4_extension_format = image4_extension.upper()
# Resize image 4 to 150px width, 150px height using the resample_method saved above
image4_resized = image4.resize(size, resample_method)
# Save image 4 as a PNG file
image4_resized.save('./output_images/image4_output.%s' % (image4_extension), image4_extension_format)

# ********************************************************************
# * image5.png must be compatible with Safari, Chrome, Edge, Firefox *
# ********************************************************************
#---------------------------------------------------------------------------------------------------------------
# A PNG file can not be converted using this methods into a JPEG file, because of the RGBA format
# So we will just resize the image and save it as PNG again
#---------------------------------------------------------------------------------------------------------------
# Load PNG file
image5 = Image.open("./input_images/image5.png")
# Determine the extension of the file
image5_extension = "png"
image5_extension_format = image5_extension.upper()
# Resize image 5 to 150px width, 150px height using the resample_method saved above
image5_resized = image5.resize(size, resample_method)
# Save image 5 as a PNG file
image5_resized.save('./output_images/image5_output.%s' % (image5_extension), image5_extension_format)
