import numpy as np
import matplotlib.pyplot as plt
import cv2
from tkinter import *
from tkinter import filedialog, messagebox
import os
from pytesseract import Output
import pytesseract
import cv2

root=Tk()
root.title("Text OCR ")
root.geometry("500x250") 
root.resizable(0,0)
root.configure(bg='black')

def open_img():
	global my_image

	root.filename=filedialog.askopenfilename(initialdir='/media/abrar/DATA/projects',title = "Select a File", filetypes = (("all files", "*.*"),("Text files", "*.txt*")))
	my_label=Label(root,text=root.filename).pack()
	my_image=cv2.imread(root.filename)
	
	rgb = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
	results = pytesseract.image_to_data(rgb, output_type=Output.DICT)

	# loop over each of the individual text localizations
	for i in range(0, len(results["text"])):
		# extract the bounding box coordinates of the text region from
		# the current result
		x = results["left"][i]
		y = results["top"][i]
		w = results["width"][i]
		h = results["height"][i]

		# extract the OCR text itself along with the confidence of the
		# text localization
		text = results["text"][i]
		conf = int(results["conf"][i])

		# filter out weak confidence text localizations
		if conf > 0:
			# strip out non-ASCII text so we can draw the text on the image
			# using OpenCV, then draw a bounding box around the text along
			# with the text itself
			text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
			cv2.rectangle(my_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
			cv2.putText(my_image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
				1.2, (0, 0, 0), 3)
			final=my_image
			path='/media/abrar/DATA/projects/OCR/Output'
			cv2.imwrite(os.path.join(path,'final.jpg'),final)
	messagebox.showinfo(title='OCR',message='Check Output folder')
			

my_btn=Button(root,text='Browse:',command=open_img,height=5,width=15,font=('Comic Sans MS',25,'bold'),bg='DarkOrchid3',fg='Yellow').pack()
root.mainloop()			