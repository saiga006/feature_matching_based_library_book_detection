
#from __future__ import print_function
from pyimagesearch import DetectAndDescribe
from pyimagesearch.descriptors import RootSIFT
#import pyqrcode as pie
#import urllib
#url='http://192.168.1.4:8080/shot.jpg'
#socket server prog
import socket
import encodings
#import glob
import serial
import csv
import cv2
import numpy as np
import argparse
import imutils
from imutils.video import WebcamVideoStream
from imutils.video import FPS
#import speech_recognition as sr
#import codecs
#import operator
#from matplotlib import pyplot as plt
#from pyimagesearch.panorama import Stitcher
#import time
def match(kpsA, featuresA, kpsB, featuresB, ratio=0.7, minMatches=22):
		global Qryimage,Testimage
		# compute the raw matches and initialize the list of actual
		# matches
		matcher = cv2.DescriptorMatcher_create("BruteForce")
		rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
		matches = []

		# loop over the raw matches
		for m in rawMatches:
			# ensure the distance is within a certain ratio of each
			# other
			if len(m) == 2 and m[0].distance < m[1].distance * ratio:
				matches.append((m[0].trainIdx, m[0].queryIdx))

		# check to see if there are enough matches to process
		if len(matches) > minMatches:
			# construct the two sets of points

			#cv2.imshow("mapped",Testimage2)
			#cv2.waitkey()
			# show some diagnostic information

			# initialize the output visualization image
			"""(hB, wB) = Testimage.shape[:2]
			(hA, wA) = Qryimage.shape[:2]
			vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
			vis[0:hA, 0:wA] =Qryimage
			vis[0:hB, wA:] = Testimage
			vis2=vis.copy()
			#vis = imutils.resize(vis, width=720)
			# loop over the matches
			mylistA=[]
			mylistB=[]
			for (trainIdx, queryIdx) in matches:
			# generate a random color and draw the match
				color = np.random.randint(0, high=255, size=(3,))
				ptsA = (int(kpsA[queryIdx].pt[0]), int(kpsA[queryIdx].pt[1]))
				mylistA.append(ptsA)
				ptsB = (int(kpsB[trainIdx].pt[0] + wA), int(kpsB[trainIdx].pt[1]))
				mylistB.append(ptsB)
				#print ptsA,ptsB
				#cv2.line(vis, ptsA, ptsB, color, 2)"""
#			print ########################################################
#			print mylistA
#			print ########################################################	
		#	cv2.imshow("Matched", vis)
		#	cv2.waitKey(0)
#			print("# of keypoints from first image: {}".format(len(kpsA)))
#			print("# of keypoints from second image: {}".format(len(kpsB)))
			print("# of matched keypoints: {}".format(len(matches)))

			keyptsA=[kpA.pt for kpA in kpsA]
			keyptsB=[kpB.pt for kpB in kpsB]
			
			pointsB = np.float32([keyptsB[i] for (i, _) in matches])
			pointsA = np.float32([keyptsA[j] for (_, j) in matches])
			mat, status = cv2.findHomography(pointsA, pointsB, cv2.RANSAC, 4.0)
#			print "score:"
			score= float(status.sum()) / status.size
                        print score
			#matchesMask = status.ravel().tolist()
#			print matchesMask
                        if (score*100)>50:
                            for i in xrange(50):
                                ser.write(b'D')
                            print "Written to Stop"
                            
                        if (score*100)>60:
                            
                        
                            (h,w,_) = Qryimage.shape
                            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
                            dst = cv2.perspectiveTransform(pts,mat)
#			print dst
                            fin=np.int32(dst)
                            vv=fin.ravel().tolist()
#			print vv
                            mylistC=[]
                            for i in xrange(0,7,2):
                                xc=vv[i]
                                yc=vv[i+1]
                                mylistC.append((xc,yc))
#			print mylistC
                            color=(0,0,255)
                            for (i,c) in enumerate(mylistC):
				
                            	if i==3:
                            		cv2.line(Testimage, mylistC[i], mylistC[0], color, 2)	
				else:
					cv2.line(Testimage, mylistC[i], mylistC[i+1], color, 2)	
                            cv2.imshow("Bounded", Testimage)
		#	special=Testimage.copy()
			
		#	ping=1
		#	cv2.waitKey(0)
			#img2 = cv2.polylines(Testimage,[fin],True,255,3,8)
			#print img2
		else:
		#	if ping ==1 and len(matches)<8:
		#		(hA, wA) = special.shape[:2]
		#		(hB, wB) = Testimage.shape[:2]
		#		visV = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
		#		visV[0:hA, 0:wA] =special
		#		visV[0:hB, wA:] = Testimage
#				cv2.imwrite("result.jpg",visV)
		#		ping=0
			
			print "BOOK is not present in the frame - %d/%d" % (len(matches),minMatches)
			#matchesMask = None
			
		# no matches were found



#bookname="CIRCUITS AND NETWORKS"
ser=serial.Serial('/dev/ttyACM0')

#authorname="SHYAMMOHAN"

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#setting up server to handle socket connections (type- ip family)
host='192.168.43.111'
port=1025
serversocket.bind((host,port))
serversocket.listen(5)
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--db", required=True,
	help = "path to the book database")
args = vars(ap.parse_args())
vs = WebcamVideoStream(src=0).start()
#constructing a dictionary
db={}
while True:
	clientsock,addr=serversocket.accept()
#	print("client is at following address %s" %str(addr))
#	print "the message is"
        ser.write(b'G')
	message=str(clientsock.recv(1024).decode())
	query=message[2:]
#	print query
	lis=query.split('#')
	bookname=lis[0]
	authorname=lis[1]
	bookname=bookname.upper().strip()
	authorname=authorname.upper().strip()
	#print "bookname:%s \n authorname :%s" %(bookname,authorname)


	#print "no more messages to recv from client"
	#print "closing client socket connection"
	clientsock.close()
	#print bookname,authorname
        #csvReader = csv.reader(codecs.open((args["db"]), 'rU', 'utf-16-le'))
        # loop over the database
        
        imag=""
        for ind in csv.reader(open(args["db"])):
                # update the database using the book name as the key
                if ind[0].strip()==bookname and ind[1].strip()==authorname:
                    print "imag"
                    imag=ind[2]
                #######################################
        #db=sorted(db.items(), key=operator.itemgetter(0))
        #print db
        #creating a temporary dictionary for same book name
       
        #cap = cv2.VideoCapture(0)
        #initialising our imagepath as NONE
        #imagepath="NONE"
        #finding our query book image path from the database
        imagepath="pictures/"+imag
        imagepath=imagepath.lower()

        print imagepath
        
        #imagepath=sum(list(imagepath)+[])
        Qryimage=cv2.imread(imagepath)
        #r = 720 / Qryimage.shape[0]
        #dim = (int(Qryimage.shape[1] * r),720)

# perform the actual resizing of the image
        #resized = cv2.resize(Qryimage, dim, interpolation=cv2.INTER_LINEAR)
        Qryimage = imutils.resize(Qryimage, height=720)
        #cv2.imshow("query",Qryimage)
        extractor=RootSIFT()
        Qobj = DetectAndDescribe(cv2.xfeatures2d.SIFT_create(),
                extractor)
        Qgray = cv2.cvtColor(Qryimage, cv2.COLOR_BGR2GRAY)
        (QueryKps, QueryDescs) = Qobj.describe(Qgray)
        
        #cv2.waitKey(0)
        ##################################################
        while True:



                img=vs.read()

                Testimage=img
        #	cv2.imshow("TEST",Testimage)
                #cv2.waitKey(0)
        # load the query image, convert it to grayscale, and extract
        # keypoints and descriptors
                Tgray = cv2.cvtColor(Testimage, cv2.COLOR_BGR2GRAY)
                (TestKps, TestDescs) = Qobj.describe(Tgray)
                match(QueryKps, QueryDescs,TestKps, TestDescs)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    vs.stop()
                    cv2.destroyAllWindows()
                    break
                
serversocket.close()
	
