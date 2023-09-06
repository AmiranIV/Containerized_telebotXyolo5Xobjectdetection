import uuid
import pymongo
import torch
import json
from PIL import Image
from flask import Flask, request, jsonify
from loguru import logger
import boto3
from bson import json_util
import os

app = Flask(__name__)

# Load the YOLOv5 model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")
model.eval()


@app.route('/predict', methods=['POST'])
def predict():
    # Receives a URL parameter representing the image to predict
    img_name = request.args.get('imgName')
    prediction_id = str(uuid.uuid4())
    logger.info(f'prediction: {prediction_id}. start processing')
    #initilize instance s3 downloading the image
    BUCKET_NAME = <'YOUR-BUCKET-NAME'>
    s3 = boto3.client('s3')
    images_bucket = BUCKET_NAME
    original_img_path = f'/app/{img_name}'
    s3.download_file(images_bucket, img_name, original_img_path)

    # Load the image
    img = Image.open(original_img_path)
    # Run inference
    results = model(img)
    predicted_img_path = f'/app/{prediction_id}.jpeg'
    r_img = results.render()  # returns a list with the images as np.array
    img_with_boxes = r_img[0]  # image with boxes as np.array
    img_with_boxes_pil = Image.fromarray(img_with_boxes)
    img_with_boxes_pil.save(predicted_img_path)
    s3.upload_file(predicted_img_path, images_bucket, f'{prediction_id}.jpeg')

    labels = []

    for label in results.pred[0]:
        class_index = int(label[5])
        class_name = model.names[class_index]
        cx, cy, width, height = label[0:4]
        labels.append({
            "class": class_name,
            "cx": cx.item(),
            "cy": cy.item(),
            "width": width.item(),
            "height": height.item()
        })

    output_json = {
        "prediction_id": str(prediction_id),
        "original_img_path": original_img_path,
        "predicted_img_path": predicted_img_path,
        "labels": labels,
    }
    # Serialize the output_json using json_util
    output_json_serialized = json.loads(json_util.dumps(output_json))


    # Save the JSON to a file
    output_json_path = f'/app/output_{prediction_id}.json'
    with open(output_json_path, 'w') as json_file:
        json.dump(output_json, json_file, indent=4)

    mongodb_uri = 'mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=myReplicaSet'
    database_name = "mydb"
    collection_name = "predictions"
    client = pymongo.MongoClient(mongodb_uri)
    db = client[database_name]
    collection = db[collection_name]
    collection.insert_one(output_json_serialized)


    return jsonify(output_json)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
