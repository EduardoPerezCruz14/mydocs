import cv2 as cv

video = cv.VideoCapture(0)

while True:
    ret, frame = video.read()

    # ret = video.set(cv.CAP_PROP_FRAME_HEIGHT, height)
    # ret = video.set(cv.CAP_PROP_FRAME_WIDTH, width)
    
    if not ret:
        break    
    
    frame = cv.resize(frame,[640,480])

    cv.imshow('Frame', frame)
    
    if not cv.waitKey(1) == -1: # The value we send is the "delay".
                                # That means each 1ms check if any key of the keyboard is pressed. 
                                # If not then return -1  
        break
    
video.release()
cv.destroyAllWindows()