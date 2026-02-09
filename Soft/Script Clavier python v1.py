import serial
import pyautogui
from time import sleep
import serial.tools.list_ports
import pygetwindow as gw

NOM_PORT = "COM3"  
BAUD_RATE = 14400


while True:
    try:
        with serial.Serial(NOM_PORT, BAUD_RATE, timeout=1) as ser:

            while True:
                if ser.in_waiting > 0:
                    ligne = ser.readline().decode('utf-8').strip()

                    if ligne == "TRIGGER_F13": # SW1
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F13')
                        sleep(0.5)

                    if ligne == "TRIGGER_F14": # SW2
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F14')
                        sleep(0.5)

                    if ligne == "TRIGGER_F15": # SW3
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F15')
                        sleep(0.5)

                    if ligne == "TRIGGER_F16": # SW4
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F16')
                        sleep(0.5)

                    if ligne == "TRIGGER_F17": # SW5
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F17')
                        sleep(0.5)

                    if ligne == "TRIGGER_F18": # SW6
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F18')
                        sleep(0.5)

                    if ligne == "TRIGGER_F19": # SW7
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F19')
                        sleep(0.5)

                    if ligne == "TRIGGER_F20": # SW8
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F20')
                        sleep(0.5)

                    if ligne == "TRIGGER_F21": # SW9
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F21')
                        sleep(0.5)

                    if ligne == "TRIGGER_F22": # SWTR
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F22')
                        sleep(0.5)

                    if ligne == "TRIGGER_F23": # SWFD
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F23')

                    if ligne == "TRIGGER_F24": # SWFG
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.press('F24')

                    if ligne == "TRIGGER_F25": #SWFH
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.hotkey('altright','F13')

                    if ligne == "TRIGGER_F26": #SWFB
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.hotkey('altright','F14')

                    if ligne == "TRIGGER_F27": #SWZP
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.hotkey('altright','F15')

                    if ligne == "TRIGGER_F28": #SWFM
                        try:
                            win = gw.getWindowsWithTitle('OBS Studio')[0]
                            win.activate()
                        except:
                            print("Obs Studio not activated")
                        pyautogui.hotkey('altright','F16')


                    sleep(0.02)
    except (serial.SerialException, FileNotFoundError):

        sleep(2)