from PIL import Image
from PIL.ImageChops import invert
import os


if __name__ == "__main__":
	channels = []
	texcount = 0
	try:
		for file in os.listdir():
		    if file.endswith("_normal.tga") or file.endswith("_nmap.tga") or file.endswith("_n.tga") or file.endswith("_nm.tga") or file.endswith("_norm.tga") or file.endswith("_normals.tga") or file.endswith("_nrm.tga") or file.endswith("_normal.vtf.tga") or file.endswith("_nmap.vtf.tga") or file.endswith("_n.vtf.tga") or file.endswith("_nm.vtf.tga") or file.endswith("_norm.vtf.tga") or file.endswith("_normals.vtf.tga") or file.endswith("_nrm.vtf.tga"):
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

