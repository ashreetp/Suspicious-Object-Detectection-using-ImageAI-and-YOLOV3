from imageai.Detection import VideoObjectDetection
import os
from matplotlib import pyplot as plt
import cv2
from playsound import playsound
from twilio.rest import Client

client = Client("AC795e7285f1342ed6905f454144ad1e12", "bcc545f911c7cf6593e37301c726cf11")

execution_path = os.getcwd()

ip=input("Enter The suspecious object name : ")

txt="You have an alert, "
txt+=ip
txt+=" Has been detected.Please check your environment"

def forFrame(frame_number, output_array, output_count, returned_frame): 
    plt.clf()
    plt.imshow(returned_frame, interpolation="none")
    plt.pause(0.001)
    try:
        if output_count[ip]>0:
            client.messages.create(to="+918328099394",from_="+19802012701", body=txt)
            playsound("mus.wav")
    except:
        return


cam=cv2.VideoCapture(0)
video_detector = VideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
video_detector.loadModel()


plt.show()

video_detector.detectObjectsFromVideo(camera_input=cam, output_file_path=os.path.join(execution_path, "video_frame_analysis") ,  frames_per_second=45, per_frame_function=forFrame,  minimum_percentage_probability=85, return_detected_frame=True)
cam.release()
