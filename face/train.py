import os
import cv2
import numpy as np
from PIL import Image 
import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create() 
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

baseDir = os.path.dirname(os.path.abspath(__file__))
imageDir = os.path.join(baseDir, "imagenes")



courrentId = 0
labelIds = {}
xTrain = []
yLabels = []

for root, dirs, files in os.walk(imageDir):
	for file in files:
		if file.endswith("jpg") or file.endswith("jpeg"):
			path = os.path.join(root, file)
			label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
			print(label, path)

			if not label in labelIds:
				labelIds[label] = courrentId
				courrentId += 1
			id_ = labelIds[label]

			print(labelIds)

			#xTrain.append(path)
			#yLabels.append(label)

			pilImage = Image.open(path).convert("L")
			size = (550,550)
			finalImg = pilImage.resize(size, Image.ANTIALIAS)

			imageArray = np.array(finalImg, "uint8")
			#print(imageArray)
			faces = faceCascade.detectMultiScale(imageArray, scaleFactor=1.5, minNeighbors=5)

			for (x,y,w,h) in faces:
				roi = imageArray[y:y+h, x:x+w]
				xTrain.append(roi)
				yLabels.append(id_)

with open("labels.pickle", 'wb') as f:
	pickle.dump(labelIds, f)

recognizer.train(xTrain, np.array(yLabels))
recognizer.save("trainner.yml")

 