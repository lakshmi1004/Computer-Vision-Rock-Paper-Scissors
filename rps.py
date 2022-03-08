import cv2                          #importing from OpenCV library to solve computer vision problems.
from keras.models import load_model #importing the models from keras API.
import numpy as np                  #code tells Python to bring the NumPy library into your current environment.
model = load_model('p1/keras_model.h5', compile = 'False')
cap = cv2.VideoCapture(0)           #Capturing the image from sysytem camera or tells which camera to use
data = np.ndarray(shape=(1,224,224,3), dtype=np.float32) #shape - array of an image.

while True:
    ret, frame = cap.read() #boolean variable that returns true if the frame is available.
    resized_frame = cv2.resize( frame, (224, 224), interpolation = cv2.INTER_AREA) #Capture the image and resize it in the given area(shrinking)
    image_np = np.array(resized_frame) #Stored as an array.
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame) #cv2.imshow() method is used to display an image in a window(frame).
    # Press q to close the window
    if prediction[0][0] > 0.7:
                user_input = 'Rock'
                print(user_input)                            
    elif prediction[0][1] > 0.7:
                print("paper")                                
    elif prediction[0][2] > 0.7:
                print("scissors")                
    else:
                print("nothing")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        print(cv2.waitKey(1))
cap.release()
cv2.destroyAllWindows()