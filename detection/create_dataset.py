import cv2
import os

def framecapture(path, folder):
    cap = cv2.VideoCapture(path)
    property_id = int(cv2.CAP_PROP_FRAME_COUNT)
    length = int(cv2.VideoCapture.get(cap, property_id))
    count = 0
    success = 1
    cut = length - 99
    print(length)

    _dir = "F:\\AccidentDetection\\Accident-Detection-Using-Deep-Learning\\video" + folder
    # _dir = os.path.join('F:',os.sep,'AccidentDetection',os.sep)
    os.mkdir(_dir)

    while success:
        success, image = cap.read()
        if count >= cut:
            n = count - cut
            cv2.imwrite(_dir+'\\frame%d.jpg' % n, image)
        count += 1


temp_dir = "F:\\AccidentDetection\\Accident-Detection-Using-Deep-Learning\\videos"
print(os.listdir(temp_dir))
for video_file in os.listdir(temp_dir):
    print(video_file)
    path = temp_dir + "\\" + video_file
    print(path)
    framecapture(path, video_file)
