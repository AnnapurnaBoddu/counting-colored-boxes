<h1>Counting the Number of Colored Boxes in an Image or PDF</h1>


<b>Project Overview</b>
The objective of this project is to develop a solution that processes an image or a PDF file, detects colored boxes (specifically blue, red, and yellow), and counts them. The solution includes a front-end interface where users can upload a file, and the system will analyze the image and return the number of colored boxes. The project is built using Python, utilizing OpenCV for image processing and Streamlit for the front-end.


 <b>Approach</b>
 
 <b>Image Processing Techniques</b>
 Used OpenCV to perform image processing and detect colored boxes in the uploaded files. 
 
 •	<b>Convert to HSV Color Space:</b> Since the HSV color space separates chromatic content (color information) from intensity, it is easier to define the ranges for different colors. The uploaded image is converted from the BGR format to the HSV format.
 
 •	<b>Define Color Ranges:</b> Manually defined HSV ranges for three colors: blue, red, and yellow. The detection works by creating masks that filter out parts of the image that do not fall within the specified color ranges. 

 •	<b>Contour Detection:</b> After filtering colors, used cv2.findContours to detect contours (shapes) in the masked images. Each contour represents a box, and the number of contours gives us the count of boxes for that color.
 
 •	<b>Handling Color and Size Variations:</b> To ensure robustness, the color ranges were set with some tolerance, allowing the system to handle slight variations in color and intensity. For small contours or irregular shapes, we set a minimum contour area to avoid noise being counted as boxes.


 <b>File Types (PDF and Image)</b>
 
•	<b>Image File Handling:</b> Images (JPEG, PNG) were directly processed using OpenCV.

•	<b>PDF File Handling:</b> For PDFs, used the PyMuPDF library (fitz) to convert each page of the PDF into an image. 

<b>Frontend Development (Streamlit)</b>
The project includes a web-based front-end using Streamlit that allows users to interact with the system

•	File Upload: Streamlit's file_uploader function was used to allow users to upload an image or a PDF. Depending on the file type, the system processes the content accordingly.

•	Image Display: If an image is uploaded, it is displayed on the page. If a PDF is uploaded, each page is converted to an image and displayed along with the detected counts.

•	Display Results: After processing the uploaded file, the detected number of colored boxes (blue, red, yellow) is displayed in the right-hand column.



<b>Deployment Process (Render.com)</b>

Render.com is a cloud platform that offers free hosting for web applications, including Python apps like Streamlit. It is easy to set up and deploy apps directly from GitHub.

<b>Steps to Deploy on Render.com</b>
1.	Create a Render Account: Sign up at Render.com.
2.	Link to GitHub Repository:
   
    o	Push your project to a GitHub repository.
  	
    o	In Render, create a new web service and select your GitHub repository.
  	
3.	Configure the Web Service:

  	o	Environment: Choose Python.

    o	Build Command: Set the build command as:
  	
          pip install -r requirements.txt
  	
    o	Start Command: Set the start command as:
   
          streamlit run app.py
         
5.	Deploy: Once the setup is complete, Render will automatically deploy your app. It will provide a public URL where users can access the app.


<b>Challenges Faced</b>

•	<b>PDF to Image Conversion:</b> Converting PDFs to images while retaining quality was crucial for accurate box detection. We solved this by using the PyMuPDF library, which provides high-quality image rendering from PDF pages.

•	<b>Handling Varying Color and Box Sizes:</b> Adjusting color detection ranges and filtering small contours helped in addressing the variations in the input files.

•	<b>File Size for Hosting:</b>Coudn´t deploy the apllication on tiiny.host due to size constraint and azzure due to monitory reasons, found alternative site render.com





