import cv2
import pytesseract
import numpy as np
from Database import Database
import re
#__init__'s
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
cascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
license_plate_pattern = re.compile(r'^[A-Z]-\d{3}-[A-Z]{2}$')
visited = set()
db = Database()

Tolls = {"Car":45,
         "Jeep":45,
         "Van":45,
         "LCV":75,
         "Bike":0,
         "Bus":150,
         "Truck":150}

states={"AN":"Andaman and Nicobar","AP":"Andhra Pradesh","AR":"Arunachal Pradesh","AS":"Assam","BR":"Bihar",
        "CG":"Chattisgarh","CH":"Chandigarh","DD":"Dadra and Nagar Haveli and Daman and Diu","DL":"Delhi",
        "GA":"Goa","GJ":"Gujarat","HP":"Himachal Pradesh","HR":"Haryana","JH":"Jharkhand",
         "JK":"Jammu and Kashmir","KA":"Karnataka","KL":"Kerala","KS":"Kyasamballi","LA":"Ladakh",
         "LD":"Lakshadweep","MH":"Maharashtra","ML":"Meghalaya","MN":"Manipur","MP":"Madhya Pradesh",
        "MZ":"Mizoram","NL":"Nagaland","OD":"Odisha","PB":"Punjab","PY":"Puducherry","RJ":"Rajasthan",
        "SK":"Sikkim","TN":"Tamil Nadu","TR":"Tripura","TS":"Telangana","UK":"Uttarakhand",
        "UP":"Uttar Pradesh","WB":"West Bengal","R":"Romania", "N":"Norway", "L":"Luxembourg", "H": "Hungary", "K": "Kenya"}

def extract_num(frame):
        global read
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        nplate = cascade.detectMultiScale(gray,1.1,4)
        for(x,y,w,h) in nplate:
                a,b=(int(0.02*frame.shape[0]),int(0.025*frame.shape[1]))
                plate=frame[y+a:y+h-a,x+b:x+w-b, :]
                #image processing
                kernel=np.ones((1,1),np.int8)
                plate=cv2.dilate(plate,kernel,iterations=1)
                plate = cv2.erode(plate, kernel, iterations=1)
                plate_gray=cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
                (thresh,plate)=cv2.threshold(plate_gray,127,255,cv2.THRESH_BINARY)
                read=pytesseract.image_to_string(plate)
                read=''.join(e for e in read if e.isalnum)
                stat=read[0:2]
                if license_plate_pattern.match(read):
                        if read not in visited:
                                if "-" in stat:
                                        stat = stat.replace("-","")
                                try:
                                        ret = db.display_vehicle_details(read[0:-1])
                                        if ret:
                                                print('Vehicle belongs to',states[stat])
                                                print("plate_number: ",read)
                                                vehicle_type = Tolls[db.get_type(read[0:-1])]
                                                print(f"Toll calculated: {vehicle_type}")
                                        visited.add(read)      
                                except:
                                        print('State not recognized!')
                
                cv2.rectangle(frame,(x,y),(x+w,y+h),(51,51,255),2)
                cv2.rectangle(frame,(x,y-40),(x+w,y),(51,51,255),-1)
              
                plate_resized = cv2.resize(plate, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
                cv2.imshow("Plate", plate_resized)
                #cv2.imshow("Plate",plate)
                # Save the detected plate for the first frame only
                cv2.imwrite('detected_plate.jpg', plate_resized)
                break  # Break after processing the first frame
        cv2.imshow("Result", frame)       
       
cap=cv2.VideoCapture('./demo.mp4')
ret = True
while ret:
        ret,frame=cap.read()
        if not ret:
                break
        extract_num(frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
                break
cap.release()
cv2.destroyAllWindows()


# frame = cv2.imread("./test2.jpeg")
# extract_num(frame)