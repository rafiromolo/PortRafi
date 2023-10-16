from tkinter import *
from tkinter import messagebox	
from tkinter.ttk import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import serial
import time
import pandas as pd

root = Tk()
root.geometry('325x110')
root.title("Microalgae")

com = 'COM4'

def led_red():
    ser = serial.Serial(com, 9600, timeout=1)
    time.sleep(2)

    var = '1';
    arr_redC = []

    print("Turning on the Red Light...")
    time.sleep(1)

    for i in range(100):
        ser.write(bytes(var, 'utf-8'))
        line = ser.readline()
        if line:
            string = line.decode()
            num = int(string)
            print(num)
            arr_redC.append(num)
    
    data_redC = {'light': arr_redC}
    df_redC = pd.DataFrame(data_redC)
    df_redC.to_csv('data-red-color.csv')

    time.sleep(1)
    messagebox.showinfo("Info", "Data has been taken.")
    ser.close()

def led_green():
    ser = serial.Serial(com, 9600, timeout=1)
    time.sleep(2)

    var = '2';
    arr_greenC = []

    print("Turning on the Green Light...")
    time.sleep(1)

    for i in range(100):
        ser.write(bytes(var, 'utf-8'))
        line = ser.readline()
        if line:
            string = line.decode()
            num = int(string)
            print(num)
            arr_greenC.append(num)

    data_greenC = {'light': arr_greenC}
    df_greenC = pd.DataFrame(data_greenC)
    df_greenC.to_csv('data-green-color.csv')

    time.sleep(1)
    messagebox.showinfo("Info", "Data has been taken.")
    ser.close()

def led_blue():
    ser = serial.Serial(com, 9600, timeout=1)
    time.sleep(2)

    var = '3';
    arr_blueC = []

    print("Turning on the Blue Light...")
    time.sleep(1)

    for i in range(100):
        ser.write(bytes(var, 'utf-8'))
        line = ser.readline()
        if line:
            string = line.decode()
            num = int(string)
            print(num)
            arr_blueC.append(num)
    
    data_blueC = {'light': arr_blueC}
    df_blueC = pd.DataFrame(data_blueC)
    df_blueC.to_csv('data-blue-color.csv')
    
    time.sleep(1)
    messagebox.showinfo("Info", "Data has been taken.")
    ser.close()


def cam_red():
    i=0
    meanR = []
    meanG = []
    meanB = []
    arr_cam = []
    
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
            b_mean = np.mean(b)
            g_mean = np.mean(g)
            r_mean = np.mean(r)

            meanR.append(r_mean)
            meanG.append(g_mean)
            meanB.append(b_mean)
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            elif len(meanR) == 100:
                break
            elif cv2.waitKey(25) & 0xFF == ord('s'):
                cv2.imwrite(f'{i+1}.jpg', frame)
                print(f"saving file{i+1}")
                i += 1
        else:
            break

    data_cam = {'R-mean': meanR, 'G-mean': meanG, 'B-mean': meanB}
    df_cam = pd.DataFrame(data_cam)
    df_cam.to_csv('data-cam.csv')

    time.sleep(1)
    messagebox.showinfo("Info", "Data has been taken.")
    
    vid.release()
    cv2.destroyAllWindows()

def cok():
    print("cok")

# Buttons
ledR_btn = Button(root, text = 'Red Color Data', command = led_red, width = 20)
ledG_btn = Button(root, text = 'Green Color Data', command = led_green, width = 20)
ledB_btn = Button(root, text = 'Blue Color Data', command = led_blue, width = 20)
camR_btn = Button(root, text = 'Light Intensity Data', command = cam_red, width = 20)

exit_btn = Button(root, text="Exit", command=root.destroy)

# Grids
ledR_btn.grid(row = 0, column = 0, padx = 10, pady=5)
ledG_btn.grid(row = 0, column = 1, padx = 10, pady=5)
ledB_btn.grid(row = 1, column = 0, padx = 10, pady=5)
camR_btn.grid(row = 1, column = 1, padx = 10, pady=5)

exit_btn.grid(row = 7, column = 0, padx = 10, pady=5)

root.mainloop()