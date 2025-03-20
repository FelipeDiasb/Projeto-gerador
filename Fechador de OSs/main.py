import csv
import pyautogui 
import time


time.sleep(1)

with open("./OSs.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    os_number = row[0]
    print(os_number)
    pyautogui.typewrite(str(os_number))
    pyautogui.press('enter')
    pyautogui.typewrite('02125773') #CRACHA
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.typewrite(str(os_number))
    pyautogui.press('enter')
    pyautogui.press('enter')
   # time.sleep(0.1) #APAGAR ESSA LINHA PRA SER MAIS RAPIDO
