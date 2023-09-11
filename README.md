# **OBJECT DETECTION & IMAGE PROCESSING TELEGRAM BOT** 

<img width="731" alt="Screenshot 2023-09-11 at 12 49 39" src="https://github.com/AmiranIV/Containerized_telebotXyolo5Xobjectdetection/assets/109898333/5d7f3a6c-8150-4299-9ebd-2d5728af27d2">

Building an app used by 3 microservice.
User send images through an interactive Telegram bot 
(the bot you've implemented in the Python project), The service detects objects in the image and sends the results to the user.

The request of the user to detect a photo objects orchastrated like this:

1.User uploads image in Chat

2.Image Uploads to S3 bucket

3.yolo5 code adresses S3 bucket 

4.yolo5 analyse the image returns a json with object detected and a processed image.

5.uploads the json to the mongoDB cluster

6.saves the image to S3 bucket

7.bot gets the response, in the bot code the response is parsed and sends back to the user

the object detected.

The service consists of 3 microservices:

polybot: Telegram Bot container.

yolo5: Image prediction container based on the Yolo5 pre-train deep learning model.

mongoDB: MongoDB cluster to store data.

Make sure you have an AWS account with s3 bucket prepared, if you run it locally make sure to preform aws configure 

We first build a mongoDB cluster 


To deploy MongoDB replica set with docker:

https://www.mongodb.com/compatibility/deploying-a-mongodb-cluster-with-docker


To use the yolo5 code locally (not containerized), clone the yolo5 repo and copy the python code I uploaded to the
 
directory of the yolo5 repo.

link to yolo5:

https://github.com/ultralytics/yolov5.git

Telegram bot is running on app.py, and requires bot.py for functionality.

REQUIRED! AWS CLI 

after installed aws cli ,you can preform aws configure but there's no need, because you can grant premission using AWS role to the EC2 instance you deploy the app on.

REQUIRED! DOCKER 
#Once you finish update yolo5 code with your bucket name ,and polybot with your codes , and mongoDB replica set params to adjust to you, preform docker build to both services:
yolo5, and polybot.

Final Step:

once you have the Docker images build of the two micro services plus the mongoDB who is already deployed using docker, you have two options:

1. deploy 3 micro services MANUALLY using docker run for each container using the SAME NETWORK for each microservice.

2. push the polybot and yolo5 apps as docker images to DockerHub, and use one command, docker compose using the composed file I attached, less complicated and more efficient.

#Source to push images to DockerHub- https://www.youtube.com/watch?v=tJsrv_kPh30

#To not post my telegram token , I used secrets.env file.

To use secrets: https://docs.docker.com/compose/compose-file/05-services/#secrets

