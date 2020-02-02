from PIL import Image
import time

if __name__ == "__main__":
	img = Image.open('heath.jpg')
	img.show()
	time.sleep(3)
	r, g, b = img.split()
	con_img = Image.merge("RGB", (g, b, r))
	con_img.show()
	time.sleep(1.5)
	con_img = img.convert("L")
	con_img.show()
	
