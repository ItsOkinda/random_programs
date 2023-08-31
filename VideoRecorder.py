import cv2

live = cv2 .VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
file=cv2.VideoWriter('output.avi',fourcc,20.0,(1280,720))

while live.isOpened:
    ret,frame= live.read()
    if not ret:
        break
    cv2.imshow("Boy you just got fvked",frame)
    file.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the output file
live.release()
file.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

