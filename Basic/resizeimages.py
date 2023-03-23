import cv2 as cv



def rescaleFrame(frame, scale=0.75):
    width = int(frame. shape [1] * scale)
    height = int(frame. shape [0]* scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video_Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('x'):
        break
capture.release()
cv.destroyAllWindows()

