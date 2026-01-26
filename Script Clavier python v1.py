import serial
import pyautogui
from time import sleep
import serial.tools.list_ports

NOM_PORT = "COM3"  
BAUD_RATE = 115200


while True:
    try:
        with serial.Serial(NOM_PORT, BAUD_RATE, timeout=1) as ser:

            while True:
                if ser.in_waiting > 0:
                    ligne = ser.readline().decode('utf-8').strip()
                    if ligne == "TRIGGER_F13": # SW1
                        pyautogui.press('F13')
                    if ligne == "TRIGGER_F14": # SW2
                        pyautogui.press('F14')
                    if ligne == "TRIGGER_F15": # SW3
                        pyautogui.press('F15')
                    if ligne == "TRIGGER_F16": # SW4
                        pyautogui.press('F16')
                    if ligne == "TRIGGER_F17": # SW5
                        pyautogui.press('F17')
                    if ligne == "TRIGGER_F18": # SW6
                        pyautogui.press('F18')
                    if ligne == "TRIGGER_F19": # SW7
                        pyautogui.press('F19')
                    if ligne == "TRIGGER_F20": # SW8
                        pyautogui.press('F20')
                    if ligne == "TRIGGER_F21": # SW9
                        pyautogui.press('F21')
                    if ligne == "TRIGGER_F22": # SWTR
                        pyautogui.press('F22')
                    if ligne == "TRIGGER_F23": # SWFD
                        pyautogui.press('F23')
                    if ligne == "TRIGGER_F24": # SWFG
                        pyautogui.press('F24')
                    if ligne == "TRIGGER_LA1": #SWFH
                        pyautogui.press('LaunchApplication1')
                    if ligne == "TRIGGER_LA2": #SWFB
                        pyautogui.press('LaunchApplication2')
                    if ligne == "TRIGGER_LM": #SWZP
                        pyautogui.press('LaunchMail	')
                    if ligne == "TRIGGER_KM": #SWFM
                        pyautogui.press('KanjiMode')

                    sleep(0.01)
    except (serial.SerialException, FileNotFoundError):

        sleep(2)