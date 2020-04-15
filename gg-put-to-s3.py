import boto3
import cv2
import os
import uuid
import numpy as np

from threading import Timer

s3 = boto3.resource('s3')
capture = cv2.VideoCapture(0)

def gg_put_to_s3():
    try:
        ret, frame = capture.read()
        file_name = str(uuid.uuid4()) + ".png"
        cv2.imwrite(file_name, frame)
        s3_key = "/png/" + file_name
        s3.meta.client.upload_file(file_name, "gg-png-119463424712", s3_key)
    except Exception as e:
        print(e)
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)
    Timer(30, gg_put_to_s3).start()

gg_put_to_s3()

def function_handler(event, context):
    return