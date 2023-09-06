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

To use the yolo5 code locally (not containerized), clone the yolo5 repo and copy the python code I uploaded to the directory of the yolo5 repo.

link to yolo5:
https://github.com/ultralytics/yolov5.git

Telegram bot is running on app.py, and requires bot.py for functionality.



