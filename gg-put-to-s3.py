import boto3
import cv2
import os
import uuid
import numpy as np

s3 = boto3.resource('s3')
capture = cv2.VideoCapture(0)

def gg_put_to_s3():
    frame_count = 0
    while True:
        try:
            ret, frame = capture.read()
            if not frame_count < 900:
                break
            else:
                frame_count = 0
                file_name = str(uuid.uuid4()) + ".png"
                cv2.imwrite(file_name, frame)
            frame_count += 1
        except Exception as e:
            raise e
        finally:
            if os.path.exists(file_name):
                s3_key = "/png/" + file_name
                s3.meta.client.upload_file(file_name, "gg-png-119463424712", s3_key)
                os.remove(file_name)

gg_put_to_s3()

def function_handler(event, context):
    return