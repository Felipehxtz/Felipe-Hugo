import cv2
import datetime
# define a video capture object
cap = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Width: ' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
    datet = str(datetime.datetime.now())
    frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()




"""

img = cv2.imread('lena.jpg', 1)
cv2.line(img, (100, 100), (200, 100), (10, 100, 255), 5)
cv2.arrowedLine(img, (0, 0), (255, 255), (10, 100, 255), 5)
img = cv2.rectangle(img, (220, 240), (346, 368), (10, 100, 255), -1)
print(img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()



# define a video capture object
cap = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Width: ' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
    frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

"""
