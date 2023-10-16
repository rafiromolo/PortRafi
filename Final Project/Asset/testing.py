from tkinter import *
from tkinter import messagebox	
from tkinter.ttk import *
import numpy as np
import serial
import time
import pandas as pd
import joblib
import cv2

root = Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title("Microalgae Prediction")

com = 'COM4'
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
meanR = []
meanG = []
meanB = []

redC_int = IntVar()
greenC_int = IntVar()
blueC_int = IntVar()
redI_int = IntVar()
greenI_int = IntVar()
blueI_int = IntVar()
pred_int = IntVar()

redC_val = IntVar()
greenC_val = IntVar()
blueC_val = IntVar()
redI_val = IntVar()
greenI_val = IntVar()
blueI_val = IntVar()

def redC_test():
    ser = serial.Serial(com, 9600, timeout=1)
    global r1
    global redC_int
    global redC_val
    var = '1'

    for i in range(12):
        ser.write(bytes(var, 'utf-8'))
        line = ser.readline()
        if line:
            string = line.decode()
            num = int(string)
            print(num)
            r1.append(num)
            # print(np.mean(r1))
            redC_int.set(np.mean(r1))
    
    redC_val = np.mean(r1)
    ser.close()

def greenC_test():
    ser = serial.Serial(com, 9600, timeout=1)
    global r2
    global greenC_int
    global greenC_val
    var = '2'
    
    for i in range(12):
        ser.write(bytes(var, 'utf-8'))
        line = ser.readline()
        if line:
            string = line.decode()
            num = int(string)
            print(num)
            r2.append(num)
            # print(np.mean(r2))
            greenC_int.set(np.mean(r2))
    
    greenC_val = np.mean(r2)
    ser.close()

def blueC_test():
    ser = serial.Serial(com, 9600, timeout=1)
    global r3
    global blueC_int
    global blueC_val
    var = '3'
    
    for i in range(12):
        ser.write(bytes(var, 'utf-8'))
        line = ser.readline()
        if line:
            string = line.decode()
            num = int(string)
            print(num)
            r3.append(num)
            # print(np.mean(r3))
            blueC_int.set(np.mean(r3))
    
    blueC_val = np.mean(r3)
    ser.close()

def redI_test():
    global r4
    global r5
    global r6
    global redI_int
    global redI_val
    global greenI_int
    global greenI_val
    global blueI_int
    global blueI_val
    ser = serial.Serial(com, 9600, timeout=1)
    time.sleep(2)
    var = '4';
    ser.write(bytes(var, 'utf-8'))

    vid = cv2.VideoCapture(0)
    width, height = 50, 75
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    print("Opening camera...")

    while(vid.isOpened()):
        ret, frame = vid.read()

        if ret == True:
            cv2.imshow('Frame', frame)

            b = frame[:, :, :1]
            g = frame[:, :, 1:2]
            r = frame[:, :, 2:]
  
            # computing the mean
            meanB = np.mean(b)
            meanG = np.mean(g)
            meanR = np.mean(r)

            r4.append(meanR)
            r5.append(meanG)
            r6.append(meanB)
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            elif len(r4) == 10:
                break
            elif cv2.waitKey(25) & 0xFF == ord('s'):
                cv2.imwrite(f'{i+1}.jpg', frame)
                print(f"saving file{i+1}")
                i += 1
        else:
            break
    
    redI_int.set(np.mean(r4))
    greenI_int.set(np.mean(r5))
    blueI_int.set(np.mean(r6))
    redI_val = np.mean(r4)
    greenI_val = np.mean(r5)
    blueI_val = np.mean(r6)

    vid.release()
    cv2.destroyAllWindows()
    ser.close()

def pred():
    global pred_int
    global r1, r2, r3, r4, r5, r6
    df_test = {'r': r1, 'g': r2, 'b': r3, 'mean-cam-r': r4, 'mean-cam-g': r5, 'mean-cam-b': r6}
    # print(df_test)
    df_pred = pd.DataFrame(data=df_test)
    print(df_pred)
    test = joblib.load('model1.pkl')
    test_val = test.predict(df_pred)
    print(test_val)
    pred_int.set(np.median(test_val))



def cok():
    print('test', redC_val)

test_btn = Label(root, text = 'TEST')
cal_btn = Button(root, text = 'CALCULATE', command = cok, width = 20)

redC_label = Button(root, text = 'Red-Color Value', command = redC_test, width = 20)
greenC_label = Button(root, text = 'Green-Color Value', command = greenC_test, width = 20)
blueC_label = Button(root, text = 'Blue-Color Value', command = blueC_test, width = 20)
redI_label = Button(root, text = 'Red Intensity Value', command = redI_test, width = 20)
pre_label = Button(root, text = 'Predict', command = pred, width = 20)
greenI_label = Label(root, text = 'Green Intensity Value')
blueI_label = Label(root, text = 'Blue Intensity Value')
pred_label = Label(root, text = 'Predicted Value')
act_label = Label(root, text = 'Actual Value')
mae_label = Label(root, text = 'Mean Absolute Error')
mse_label = Label(root, text = 'Mean Squared Error')
rmse_label = Label(root, text = 'Root Mean Squared Error')
kfold_label = Label(root, text = 'Repeated k-Fold Cross-Validation')

redC_entry = Entry(root, textvariable=redC_int, width = 10)
greenC_entry = Entry(root, textvariable=greenC_int, width = 10)
blueC_entry = Entry(root, textvariable=blueC_int, width = 10)
redI_entry = Entry(root, textvariable=redI_int, width = 10)
greenI_entry = Entry(root, textvariable=greenI_int, width = 10)
blueI_entry = Entry(root, textvariable=blueI_int, width = 10)
pred_entry = Entry(root, textvariable=pred_int, width = 10)
act_entry = Entry(root, width = 10)
mae_entry = Entry(root, width = 10)
mse_entry = Entry(root, width = 10)
rmse_entry = Entry(root, width = 10)
kfold_entry = Entry(root, width = 10)

test_btn.grid(row = 0, column = 0, padx = 10, pady=5)
redC_label.grid(row = 1, column = 0, padx = 10, pady = 5)
redC_entry.grid(row = 1, column = 1, padx = 10, pady = 5)
greenC_label.grid(row = 2, column = 0, padx = 10, pady = 5)
greenC_entry.grid(row = 2, column = 1, padx = 10, pady = 5)
blueC_label.grid(row = 3, column = 0, padx = 10, pady = 5)
blueC_entry.grid(row = 3, column = 1, padx = 10, pady = 5)
redI_label.grid(row = 1, column = 2, padx = 10, pady = 5)
redI_entry.grid(row = 1, column = 3, padx = 10, pady = 5)
greenI_label.grid(row = 2, column = 2, padx = 10, pady = 5)
greenI_entry.grid(row = 2, column = 3, padx = 10, pady = 5)
blueI_label.grid(row = 3, column = 2, padx = 10, pady = 5)
blueI_entry.grid(row = 3, column = 3, padx = 10, pady = 5)
pre_label.grid(row = 6, column = 0, padx = 10, pady = 20)
pred_label.grid(row = 7, column = 0, padx = 10, pady = 20)
pred_entry.grid(row = 7, column = 1, padx = 10, pady = 20)
act_label.grid(row = 7, column = 2, padx = 10, pady = 20)
act_entry.grid(row = 7, column = 3, padx = 10, pady = 20)
cal_btn.grid(row = 8, column = 0, padx = 10, pady=5)
mae_label.grid(row = 9, column = 0, padx = 10, pady = 10)
mae_entry.grid(row = 9, column = 1, padx = 10, pady = 10)
mse_label.grid(row = 10, column = 0, padx = 10, pady = 10)
mse_entry.grid(row = 10, column = 1, padx = 10, pady = 10)
rmse_label.grid(row = 9, column = 2, padx = 10, pady = 10)
rmse_entry.grid(row = 9, column = 3, padx = 10, pady = 10)
kfold_label.grid(row = 10, column = 2, padx = 10, pady = 10)
kfold_entry.grid(row = 10, column = 3, padx = 10, pady = 10)

root.mainloop()