#USER INPUT
#COMPUTER INPUT
#IF USER INPUT = COMPUTER INPUT then "PRINT "GAME IS TIE"
#    IF USER INPUT = PAPER,COMPUTER INPUT = ROCK THEN PRINT "YOU WIN!!COMPUTER LOSE,PAPER COVERS ROCK".
#ELSEIF USER INPUT = PAPER,COMPUTER INPUT = import random
#%%
import cv2
import time
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5', compile = 'False')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1,224,224,3), dtype=np.float32)
import random
possible_input = ['rock','paper','scissor']
computer_input = random.choice(possible_input)

while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize( frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np=np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
    elif prediction[0][0] > 0.7:
        user_input = 'rock'
        print('User: ',user_input) 
        print('Computer: ', computer_input) 
        if user_input == computer_input:
            print("Game is Tie")  
        elif user_input == 'rock' and computer_input == 'scissor':
            print("YOU WINS!!COMPUTER LOSE, ROCK SMASHES SCISSOR")
        elif user_input == 'rock' and computer_input == 'paper':
            print("COMPUTER WINS!!YOU LOSE, PAPER COVERS ROCK")   
        break                       
    elif prediction[0][1] > 0.7:
        user_input = 'paper'
        print('User: ',user_input) 
        print('Computer: ', computer_input)  
        if user_input == computer_input:
           print("Game is Tie")  
        elif user_input == 'paper' and computer_input == 'rock':
           print("YOU WIN!!COMPUTER LOSE,PAPER COVERS ROCK")
        elif user_input == 'paper' and computer_input == 'sciccor':
           print("COMPUTER WINS!!YOU LOSE, SCISSOR CUTS THE PAPER") 
        break                            
    elif prediction[0][2] > 0.7:
        user_input = 'scissor'
        print('User: ',user_input) 
        print('Computer: ', computer_input)
        if user_input == computer_input:
           print("Game is Tie")   
        elif user_input == 'scissor'and computer_input == 'paper':
            print("YOU WINS!!COMPUTER LOSE, SCISSOR CUTS THE PAPER")
        else:
            print("COMPUTER WINS!!YOU LOSE, ROCK SMASHES SCISSOR")   
        break        
    
time.sleep(10)    
cap.release()
cv2.destroyAllWindows()


        
#if user_input THEN PRINT "COMPUTER WINS!!YOU LOSE, SCISSOR CUTS THE PAPER"
#ELSEIF USER INPUT = ROCK, COMPUTER INPUT = SCISSOR THEN PRINT "YOU WINS!!COMPUTER LOSE, ROCK SMASHES SCISSOR"
#ELSEIF USER INPUT = ROCK, COMPUTER INPUT = PAPER THEN PRINT "COMPUTER WINS!!YOU LOSE, PAPER COVERS ROCK"
#ELSEIF USER INPUT = sCISSOR, COMPUTER INPUT = PAPER THEN PRINT "YOU WINS!!COMPUTER LOSE, SCISSOR CUTS THE PAPER"
#ELSEIF USER INPUT = sCISSOR, COMPUTER INPUT = ROCK THEN PRINT "COMPUTER WINS!!YOU LOSE, ROCK SMASHES SCISSOR"



# %%
