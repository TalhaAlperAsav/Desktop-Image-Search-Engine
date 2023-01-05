# import the necessary packages
from tkinter import Button,Label
import tkinter
from PIL import ImageTk, Image
import cv2
import os
from tkinter import filedialog as fd
import cv2

from pathlib import Path
import re


def removesuffix(string, suffix):
	if string.endswith(suffix):
		return string[:-len(suffix)]
	return string

def Select_folder():
	home = str(Path.home())
	userlink = home.replace("/","\\")
	global panelA, panelB
	path = fd.askopenfilename(title='Select your folder',filetypes=[('Jpg Files','*.jpg'),('Png Files','*.png')])
	run2 = "python index.py --dataset " + removesuffix(path,os.path.basename(path)) + " --index index.csv"
	cmd = run2.replace("/","\\")
	if os.path.exists(userlink+"\\Desktop\\Code\\VisualStudio\\SoftwareEngineeringProject\\index.csv"):
		os.remove(userlink+"\\Desktop\\Code\\VisualStudio\\SoftwareEngineeringProject\\index.csv")
	os.system(cmd)
	
	run = "python gui.py --index index.csv --query " + path + " --result-path " + os.path.dirname(path) + "\\"
	cmd2 = run.replace("/","\\")
	string = os.popen(cmd2).read()
	my_result = tuple(map(str, string.split(', ')))
	results = []
	cr = 0
	for i in my_result:
		if cr%2 == 1:
			results.append(i)
		cr += 1
	final_results = []
	
	for i in results:
		x = i.replace("'","").replace(")","").replace("\\","/").replace("]","").replace("\n","")
		y = x.replace("//","/")
		final_results.append(y)
	
	root.counter = 1
	ResultID = final_results[root.counter]

	if len(path) > 0:
			# load the image from disk, convert it to grayscale, and detect
			# edges in it
			image = cv2.imread(path)
			#resimage = cv2.imread()
			imageres = cv2.imread(ResultID)
			# OpenCV represents images in BGR order; however PIL represents
			# images in RGB order, so we need to swap the channels
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			imageres = cv2.cvtColor(imageres, cv2.COLOR_BGR2RGB)
			# convert the images to PIL format...
			image = Image.fromarray(image)
			imageres = Image.fromarray(imageres)
			# ...and then to ImageTk format
			image = ImageTk.PhotoImage(image)
			imageres = ImageTk.PhotoImage(imageres)
	if panelA is None or panelB is None:
			# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
			# while the second panel will store the edge map
			panelB = Label(image=imageres)
			panelB.image = imageres
			panelB.pack(side="right", padx=10, pady=10)
		# otherwise, update the image panels
	else:
		# update the pannels
		panelA.configure(image=image)
		panelB.configure(image=imageres)
		panelA.image = image
		panelB.image = imageres	
		
	def clicked():
		if(root.counter < 9):
			root.counter += 1
			ResultID = final_results[root.counter]
			image = cv2.imread(path)
			#resimage = cv2.imread()
			imageres = cv2.imread(ResultID)
			# OpenCV represents images in BGR order; however PIL represents
			# images in RGB order, so we need to swap the channels
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			imageres = cv2.cvtColor(imageres, cv2.COLOR_BGR2RGB)
			# convert the images to PIL format...
			image = Image.fromarray(image)
			imageres = Image.fromarray(imageres)
			# ...and then to ImageTk format
			image = ImageTk.PhotoImage(image)
			imageres = ImageTk.PhotoImage(imageres)
			# the first panel will store our original image
		# update the pannels
			panelA.configure(image=image)
			panelB.configure(image=imageres)
			panelA.image = image
			panelB.image = imageres
		else:
			tkinter.messagebox.showinfo(title=None, message="We are out of suggestions please try different image")
	mybutton = Button(root, text ='Next image',command=clicked)
	mybutton.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
	


if __name__ == "__main__":
	root = tkinter.Tk()
	panelA = None
	panelB = None
	# create a button, then when pressed, will trigger a file chooser
	# dialog and allow the user to select an input image; then add the
	# button the GUI
	btn = Button(root, text="Select an image", command=Select_folder)
	btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
	global mybutton

	root.mainloop()

	
