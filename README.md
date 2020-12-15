# Machine_Learning_Project

Instructions
In this project you must create a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to
produce a model that accurately predicts wind turbine power output from wind speed
values, as in the data set. You must then develop a web service that will respond with
predicted power values based on speed values sent as HTTP requests. Your submission
must be in the form of a git repository containing, at a minimum, the following items:
1. Jupyter notebook that trains a model using the data set. In the notebook you
should explain your model and give an analysis of its accuracy.
2. Python script that runs a web service based on the model, as above.
3. Dockerfile to build and run the web service in a container.
4. Standard items in a git repository such as a README.
To enhance your submission, you might consider developing and comparing more than
one model. Rest assured, all the above concepts will be explored in lecture videos and
other materials in the coming semester.



This assignment contains

Jupyter Notebook - powerproduction.ipynb
https://github.com/g00387822/Machine_Learning_Project/blob/main/powerproduction.ipynb

In the Jupyter Notebook I write about the algorithm I developed for predicting wind speed to power production.
I mainly developed my solution from segmenting the data and doing Simple Linear Regresson on segmented data e.g. data containing Windspeeds 0-5,5-10,10-15,15-20,20-25 and using if else statements to handle anomalies. I touch brief on comparing Simple Linear Regression Forecasts with Polynomial Regression Forecasts.

This assignment had many similiarities to Fundamentals Of Data Analysis Assignment, where I carry out Spearman Rank Tests, Kendall's Correlation Tests as well other Polynomial Corellation checks compared to Simple Linear Regression, this work kind of preludes this assignment, the Jupyter notebook can be viewed here: https://github.com/g00387822/Fundamentals_Data_Analysis_Project/blob/main/Project%202020%20Fundamentals%20of%20Data%20Analysis.ipynb


I also describe the steps that I took to create Flask Project and Associated Docker Files.
I found the Docker aspect of this assignment challenging as I was unable to install docker, I had sought online tutorial help from Stackoverflow as well as from Freelancer, this was done before Ian McLoughlin had released his video on creating Docker files.
The Jupyter Notebook work and the development of the Flask Project is all my own work, I just had some help with Docker, I have copied my Flask Project to two folders.

So I have provided 

flask_web_project_Freelancer_Docker_Example
flask_web_project_Ian_McLoughlin_Docker_Example


To run the flask project you should be able to do so from navigating to the folder in the command prompt and run the following commands

python -m venv venv
.\venv\scripts\activate.bat
pip install -r requirements.txt
set FLASK_APP=app.py
flask run

Open web browser and go to url http://127.0.0.1:5000/ Type in a number in the text box and click 'Submit' button to get the predicted energy from the wind speed


Useful links
https://youtu.be/QjtW-wnXlUY
https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
https://stackoverflow.com/questions/58675081/running-flask-on-windows-doesnt-execute-flask-run-command
https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
https://youtu.be/gQ6lh3ir2Jw
https://stackoverflow.com/questions/51006831/adding-two-numbers-in-flask