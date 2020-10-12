# OCR & Navigation algorithm
The OCR system is used to convert images and videos of text  into letters , words, and sentence. It is widely used in various fields to convert/ extract the information from the image or video  . It is also used  in signature recognition , automated data evaluation , and security  systems. It is commercially used to  validate data  records , passport doc, place signs, business cards ,printouts of static data, and so on . OCR is a field of research in pattern recognition, deep learning ,artificial intelligence and computer vision.  
# •	Project goals:

We will use the existing "OCR" system on images so we will improve it to a system that will work on existing videos and also extract text from real-time video so that we use navigation algorithms and find real-time location, we will need to use existing libraries in python such as OpenCV "so most of the work will be from it," Tesseract , OCR .
Project scope – The project will include existing directories (OpenCV, Tesseract, OCR), movies, images stored in google drive.
A project will integrate with deep learning so we use
On the Nero network we will have 2 layers so that is :
the first Is to enable our SIGMOID output which gives us a probability of the area containing the text or not.
A second layer represents the geometry of the images we can use this geometry to derive the coordinates .

* Understanding OpenCV OCR and Tesseract text recognition:

![image](https://user-images.githubusercontent.com/33619392/73290514-3a631e00-4207-11ea-9b04-8918a0597f78.png)
* work process:
We will perform both (1) text detection and (2) text recognition using OpenCV, Python, and Tesseract.
Using this model we were able to detect and localize the bounding box coordinates of text contained in an image.
The next step is to take each of these areas containing text and actually recognize and OCR the text using OpenCV and Tesseract.
1. Performs text detection using OpenCV’s    EAST text detector, a highly accurate deep        learning text detector used to detect text in natural scene images.
2.Once we have detected the text regions with OpenCV, we’ll then extract each of the text ROIs and pass them into Tesseract, enabling us to build an entire OpenCV OCR pipeline!
The underlying OCR engine itself utilizes a Long Short-Term Memory (LSTM) network, a kind of Recurrent Neural Network (RNN).
As a first step we are almost ready so we will need to use navigation algorithms through which we will know the location so that we consider vectors on all sides and also compare the image size with the real image content through the pixels we will know the user distance.
* Example
This is a project that is a small part of a big project so we have to assemble the system on a robot and test the system so that it is active on a vehicle will work in real time and help the vehicle identify text on the road or any text.   

![image](https://user-images.githubusercontent.com/33619392/73290617-70080700-4207-11ea-91be-4bb33424a46e.png)
**************************************************************************************************************

![image](https://user-images.githubusercontent.com/33619392/73290681-8615c780-4207-11ea-845d-471c7656b623.png)

**************************************************************************************************************
**OCR & Navigation Game

![image](https://user-images.githubusercontent.com/40535130/95772521-8b4b7180-0cc5-11eb-931c-70c6ec2d16ed.png)
