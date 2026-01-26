import serial
import pyautogui
import time
import serial.tools.list_ports

NOM_PORT = "COM3"  
BAUD_RATE = 115200

print(f"Recherche de l'ESP32 sur {NOM_PORT}...")

while True:
    try:
        with serial.Serial(NOM_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Connecté à l'ESP32 sur {NOM_PORT} !")
            while True:
                if ser.in_waiting > 0:
                    ligne = ser.readline().decode('utf-8').strip()
                    if ligne == "TRIGGER_A":
                        pyautogui.press('a')
                        print("Touche 'a' simulée")
                time.sleep(0.01) 
    except (serial.SerialException, FileNotFoundError):
        print(f"ESP32 non trouvé sur {NOM_PORT}. Réessai dans 2 secondes...")
        time.sleep(2)