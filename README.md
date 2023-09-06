App deployment used by 3 microservices, Users send images through an interactive Telegram bot 
(the bot you've implemented in the Python project), the service detects objects in the image and sends the results to the user

The service consists of 3 microservices:

polybot: Telegram Bot container.
yolo5: Image prediction container based on the Yolo5 pre-train deep learning model.
mongoDB: MongoDB cluster to store data.



To deploy MongoDB replica set with docker:
https://www.mongodb.com/compatibility/deploying-a-mongodb-cluster-with-docker

To use yolo5 code locally (not containerized), clone the yolo5 repo and copy the python code i uploaded to the directory of yolo5 repo.

link to yolo5:
https://github.com/ultralytics/yolov5.git

polybot is running on app.py, and requires bot.py for functionality.


