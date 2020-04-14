import boto3
import cv2
import os
import uuid
import numpy as np

def gg_put_to_s3():
    capture = cv2.VideoCapture(0)
    frame_count = 0
    while True:
        try:
            ret, frame = capture.read()
            if not n < 900:
                break
            else:
                frame_count = 0
                file_name = str(uuid.uuid4())
                file_path = "/tmp/{}.png".format(file_name)
                cv2.imwrite(file_path)
            frame_count += 1
        except Exception as e:
            raise e
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

gg_put_to_s3()

def function_handler(event, context):
    return