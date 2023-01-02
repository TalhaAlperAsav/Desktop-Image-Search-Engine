 
import argparse
import cv2
from colordescriptor import ColorDescriptor
from searcher import Searcher

def returnvalue():
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--index", required = True,
		help = "Path to where the computed index will be stored")
	ap.add_argument("-q", "--query", required = True,
		help = "Path to the query image")
	ap.add_argument("-r", "--result-path", required = True,
		help = "Path to the result path")


	args = vars(ap.parse_args())

	# initialize the image descriptor
	cd = ColorDescriptor((8, 12, 3))

	# load the query image and describe it
	query = cv2.imread(args["query"])
	features = cd.describe(query)
	# perform the search
	searcher = Searcher(args["index"])
	results = searcher.search(features)
	print(results)

	

	


returnvalue()

















	
	
	
	

	
	

	

