# Automatic-Toll-System-with-AI
The provided repository contains information about the implementation of an AI-empowered automatic toll collection system developed for hassle-free toll collection on roads. This system enables tolls to be levied without necessitating a stop in traffic, unlike traditional toll gates.

## Introduction
Modern transportation systems face a myriad of challenges, and one significant bottleneck lies in
the conventional toll collection process. The interruption caused by toll booths not only contributes
to traffic congestion but also hinders the overall efficiency of the transportation network. This
project embarks on an innovative endeavor to address this issue by introducing an automated toll
collection system. This project focuses on leveraging cutting-edge technologies, specifically Artificial Intelligence
(AI), computer vision, and machine learning, to revolutionize toll calculation and collection. The
primary objective is to seamlessly identify license plate numbers in real-time, eliminating the need
for vehicles to come to a complete stop at toll gates. This not only streamlines the toll collection
process but also enhances the flow of traffic. The project’s core innovation lies in the integration of
an AI-driven system capable of not only recognizing license plates but also dynamically calculating
toll charges based on various parameters. By incorporating vehicle characteristics retrieved from a
central database, the system ensures accurate and efficient toll calculations.

## Use Case Diagram
<img width="410" alt="image" src="https://github.com/AryanKulathinal/Automatic-Toll-System-with-AI/assets/116480303/b98cfc5d-edb6-448d-b0ad-383526e9d253">

## Technology Stack
#### Programming Language - Python
#### OCR - Tesseract
#### Computer Vision - OpenCV, Haar-Caascade Algorithm
#### Graphical User Interface - Tkinter
#### Database - SQLite

## Implementation
This system implements automatic number plate recognition for efficient toll calculation using
AI, specifically Machine Learning and Computer Vision techniques. It utilizes the Haar cascade
algorithm to extract number plate regions, which are the regions of interest (ROI) from the input
video. The system then applies OCR (Optical Character Recognition) via the Tesseract framework
to extract the license plate number. Subsequently, the obtained license plate number is used to
access vehicle details from a dummy database to calculate the appropriate toll.
Steps for the model

### Steps For The Model
The idea behind the system is to capture live video from a high-quality camera and process it
through the model. For ease of implementation, a saved video is used as input for proof-of-concept
purposes. The system gives maximum performance when number plate recognition is performed using YOLO v8, but in this demonstration,
we utilize Haar cascade to minimize computational resource requirements and achieve faster
speeds. The extracted license plate number is then used to access vehicle details from a centralized
database, akin to one maintained by a government entity. In this simulation, we employ a dummy
database created using SQLite. The program displays vehicle details and the calculated toll in
the terminal, and it continues running until the user presses the ’q’ key. The entire coding
is implemented in the Python programming language using the required in-built and custom
packages.
### Initialize the necessary libraries and models
It includes the import statements for various Python libraries and the initialization of Tesseract
OCR and a Haar cascade classifier.
#### Importing Libraries

- cv2 (OpenCV): OpenCV is a powerful library for computer vision tasks. In this code, it is used
for image processing, video capture, and drawing rectangles around detected license plates.
pytesseract: This library provides an interface for Tesseract OCR, which is used for text
recognition on the license plates.
- numpy: NumPy is used for numerical operations. It’s often used in image processing tasks for
manipulating pixel values and arrays.
- Database : This module is used to handle interactions with a database using SQLite. It is used for
querying vehicle details from a custom database implemented using SQLite.
re (Regular Expression): The re module is used for regular expression matching. It is employed to
define a pattern for validating license plates.
#### Tesseract and Haar Cascade Initialization

- pytesseract.tesseract_cmd: This line sets the path to the Tesseract OCR executable. Tesseract is
an OCR engine, and this line ensures that Python can find and use the Tesseract executable for text
recognition.
- cascade: The CascadeClassifier is part of the OpenCV library and is used for object detection
using Haar-like features. In this case, it’s used to detect Russian license plates.

### Regular Expressions And Data Structures
It includes the regular expressions used to process licence plates and data structures used to contain
vehicle and other related information.
#### Regular Expressions
It creates a regular expression pattern using the re module in Python. The pattern is designed to
match a specific format for license plates. Figure 4.3 shows the regular expression used. The
components of the regular expression are :
- import r e
- p a t t e r n = r e . compile ( r ’ ^ [A−Z] −\ d {3} −[A−Z]{2} $ ’ )
 <img width="376" alt="image" src="https://github.com/AryanKulathinal/Automatic-Toll-System-with-AI/assets/116480303/ece21d47-d193-4bf3-a6f9-08ded207e81d">

 Figure : Regular Expression Used

- ^ : Anchors the pattern to the start of the string,
ensuring that the entire string is matched
from the beginning.
- [A-Z] : Matches a single uppercase letter.
- \- : Matches a hyphen.
- \d{3} : Matches exactly three digits (0-9).
- \- : Matches another hyphen.
- [A-Z]{2} : Matches exactly two uppercase letters.
- $ : Anchors the pattern to the end of the string,
ensuring that the entire string is matched
until the end.
- The regular expression is designed to match strings like "A-123-AB", where the first part is a single
uppercase letter, followed by three digits, a hyphen, and then two uppercase letters.
#### Data Definitions
- The dictionaries (Tolls and states) map certain keys to corresponding values.
- Tolls: Associates vehicle types (keys) with toll amounts (values). For example, a "Car" has
a toll of 45, a "Bus" has a toll of 150, and so on.
15
-  States: Associates state codes (keys) with the full names of the states (values). For example,
"AN" maps to "Andaman and Nicobar," "AP" maps to "Andhra Pradesh," and so forth.
These data structures are used in the code to retrieve toll amounts based on the type of vehicle
and to display the full name of a state based on its code. In summary, these data structures
help in organizing and retrieving information related to toll amounts and state names, providing a
convenient way to look up data based on specific keys.
### Number Plate Extraction
A function ’extract_num’ is implemented in order to extract number plates from the input video
containing vehicles by giving it frames captured from the input video as input.
#### extract_num()
This function takes a frame (image) as input, detects
license plates, processes the plate image, extracts the text using Tesseract OCR, and performs
various checks and database interactions.Its various components are:
##### Grayscale Conversion
Converts the input frame to grayscale. Grayscale images are often easier to process for OCR tasks.
License Plate Detection
Uses the Haar cascade classifier (’cascade’) to detect potential license plate regions in the grayscale
frame.
##### Plate Extraction and Preprocessing
The number plate region is extracted from the frame using the coordinates obtained from the Haar
cascade detection. Image processing steps include dilation, erosion, thresholding, and resizing,
aimed at enhancing the visibility of characters in the license plate.
##### OCR (Optical Character Recognition) using Tesseract
The python package ’pytesseract’ is used to perform OCR using Tesseract framework on the
preprocessed license plate (plate). The result is stored in read, and non-alphanumeric characters
are removed. stat is a substring of the OCR result, representing the first two characters.
16

##### License Plate Validation and Database Query
Checks if the OCR result matches the specified license plate pattern.If the pattern is matched, it
attempts to query the database for details related to the license plate.
##### Displaying Results and Visualization
Draws rectangles around the detected license plate region and adds a colored bar for displaying
text information. Resizes and displays the extracted license plate ("plate") in a separate window
("Plate").Displays the annotated frame ("frame") with the detected license plate.
Breaking After Processing First Frame
The loop breaks after processing the first detected license plate. This assumes that there’s only one
license plate of interest in each frame.
##### Displaying the Final Result
The final step is to display the final annotated frame with detected license plate information.

- Hence this function essentially performs license plate extraction, OCR, validation, and
visualization for each frame in a video stream. It also interacts with a database for additional
details related to the recognized license plates.
### Main Video Processing Loop
It captures frames from a video file, processes
each frame using the ’extract_num’ function, and breaks the loop when the video ends or the user
presses ’q’. Its various components are:

##### Video Capture
cv2.VideoCapture() creates a video capture object (’cap’) to read frames from the specified video
file.
##### Processing Loop
The processing loop runs as long as frames can be read from the video (’ret’ is True).
Frame Retrieval
cap.read() retrieves the next frame from the video. If ’ret’ is False, it means no more frames are
available, and the loop breaks.

##### License Plate Extraction Function
Calls the ’extract_num’ function to process the current frame for license plate extraction and OCR.
Break Condition (Key Press ’q’)
Checks for the ’q’ key press. If ’q’ is pressed, the loop breaks, allowing the user to exit the video
processing.
##### Release Video Capture Object and Close Windows
Releases the video capture object (cap) and closes all OpenCV windows.
In summary, the main loop processes each frame of the video, extracts license plate information
using the ’extract_num’ function, and displays the annotated frame.The loop continues until
all frames are processed or until the user presses the ’q’ key to exit the application.The
’cv2.VideoCapture’ object is released, and OpenCV windows are closed after the loop completes.
### Dummy Database
A Python script that defines a ‘Database‘ class that serves as an interface for managing vehicle
details stored in an SQLite database is implemented. The class includes methods for initializing
the database, adding new vehicle details, displaying information based on vehicle numbers, and
retrieving the vehicle type. The ‘__init__‘ method establishes a connection to the SQLite database
file, creates a cursor for executing SQL queries, and defines a table structure to store vehicle details
such as vehicle number, name, phone number, state, type, and address. The ‘add_vehicle‘ method
adds new vehicle details to the database, ensuring data integrity by using parameterized queries.
The ‘display _vehicle_details‘ method retrieves and prints information about a vehicle based on its
unique number, while the ‘get_type‘ method fetches and returns the type of a vehicle. The script
also includes a demonstration in the ‘__main__‘ section, showcasing the usage of the ‘Database‘
class to interact with the database. Overall, this script provides a modular and reusable solution for
managing vehicle-related data using SQLite in a Python environment

### Result

The system accurately identifies and tracks vehicles approaching the toll gate. This achievement
forms the foundation for a seamless toll collection process. Following swift vehicle detection, the
system employs Optical Character Recognition (OCR) to read and recognize the number plates of
identified vehicles. This crucial step serves as the bedrock for obtaining detailed information from
our extensive database. The below figure shows the final output including number plate detection, details
of the vehicle and toll calculation.
<img width="388" alt="image" src="https://github.com/AryanKulathinal/Automatic-Toll-System-with-AI/assets/116480303/6cad25be-be38-4ff2-9d4d-780ad383c310">

With the captured number plate information, the system efficiently queries the comprehensive
database, retrieving vital details about registered vehicles such as the owner’s name, vehicle type,
and registration status. This integration ensures precise and up-to-date information retrieval,
crucial for the subsequent toll calculation.
Leveraging the retrieved vehicle details, including type and any applicable toll exemptions or
discounts, the system dynamically calculates toll amounts. This intelligent toll calculation takes
into consideration varying rates for different vehicle types and specific regulations governing toll
charges. Subsequently, the system generates detailed toll bills, offering a transparent breakdown
of charges and relevant information.
The AI automated toll collection system significantly reduces processing time and minimizes
the possibility of errors associated with manual toll collection. Leveraging AI technologies ensures
a high level of accuracy in vehicle detection, number plate recognition, and toll calculation,
resulting in a streamlined and efficient toll gate operation that enhances overall accuracy, efficiency,
and user satisfaction
