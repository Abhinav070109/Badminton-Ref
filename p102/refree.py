import cv2
import time
import dropbox
import random

def main():
    cap = cv2.VideoCapture(0)
    i = 0
  
    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == False:
            break
    
        cv2.imwrite('Frame'+str(i)+'.jpg', frame)
        i += 1
  
    cap.release()
    cv2.destroyAllWindows()
    uploadFile()
    
def uploadFile(imageName):
    access_token = 'ZMpx_jM0QUYAAAAAAAAAASyE_G8xydNC6wPybowp2eafbODITNGJcCEta79jO3ys'
    file = imageName
    file_from = file
    file_to = '/Badminton_Refree/' + (imageName)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to, mode = dropbox.files.WriteMode.overwrite)
        print('File Uploaded')