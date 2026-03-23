from PIL import Image
from PIL.ImageChops import invert
import os


if __name__ == "__main__":
	channels = []
	texcount = 0
	try:
		for file in os.listdir():
		    if file.endswith("_normal.tga") \
		    or file.endswith("_nmap.tga") \
		    or file.endswith("_n.tga") \
		    or file.endswith("_nm.tga") \
		    or file.endswith("_norm.tga") \
		    or file.endswith("_normals.tga") \
		    or file.endswith("_nrm.tga") \
		    or file.endswith("_normal.vtf.tga") \
		    or file.endswith("_nmap.vtf.tga") \
		    or file.endswith("_n.vtf.tga") \
		    or file.endswith("_nm.vtf.tga") \
		    or file.endswith("_norm.vtf.tga") \
		    or file.endswith("_normals.vtf.tga") \
		    or file.endswith("_nrm.vtf.tga") \
		    or file.endswith("_bump.tga") \
		    or file.endswith("_b.tga") \
		    or file.endswith("_bump.vtf.tga") \
		    or file.endswith("_b.vtf.tga") \
		    or file.endswith("_normal.png") \
		    or file.endswith("_nmap.png") \
		    or file.endswith("_n.png") \
		    or file.endswith("_nm.png") \
		    or file.endswith("_norm.png") \
		    or file.endswith("_normals.png") \
		    or file.endswith("_nrm.png") \
		    or file.endswith("_normal.vtf.png") \
		    or file.endswith("_nmap.vtf.png") \
		    or file.endswith("_n.vtf.png") \
		    or file.endswith("_nm.vtf.png") \
		    or file.endswith("_norm.vtf.png") \
		    or file.endswith("_normals.vtf.png") \
		    or file.endswith("_nrm.vtf.png") \
		    or file.endswith("_bump.png") \
		    or file.endswith("_b.png") \
		    or file.endswith("_bump.vtf.png") \
		    or file.endswith("_b.vtf.png"):	
		        image = Image.open(file, "r")
		        channels = image.split()
		        if len(channels) == 4:
		        	red, green, blue, alpha = channels
		        	print("Seperating gloss of " + str(file) + "...")
		        	alphaChannelImage = image.getchannel('A')
		        	alphaChannelImage.save(str(file) + "_gloss.tga")
		        else:
		        	red, green, blue = channels
		        print("Flipping green channel of " + str(file) + "...")
		        image_with_inverted_green = Image.merge('RGB', (red, invert(green), blue))
		        image_with_inverted_green.save(str(file))
		        texcount += 1
		print(f"{texcount} textures converted, press Enter to close")
		input()	
	except Exception as e:
		print(e)
		print("Press Enter to close")
		input()

