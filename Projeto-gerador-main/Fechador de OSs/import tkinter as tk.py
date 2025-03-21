

from ftplib import FTP
import sv_ttk
import time
import csv
import tkinter as tk
from tkinter import ttk
import pyautogui
import flet  as ft
from flet import IconButton, Page, Row, TextField, icons


def main(page: ft.Page):
    page.title = "Fechador de OS's"
 
    # pass

    # def textbox_changed(e):
    #     t.value = e.control.value
    #     page.update()
    
    

    #   t = ft.Text()
    #  tbel = ft.TextField(label="Campo de texto com evento 'change'", on_change=textbox_changed)
     
    #   #page.add(tb, t)
    
    

 #ft.app(target=main)



 #flet.app(target=main)
 #flet.app(target=main, view=flet.AppView.WEB_BROWSER) #Para abrir na Web app



    

def tksleep(self, time:float) -> None:
    
    self.after(int(time*1000), self.quit)
    self.mainloop()
tk.Misc.tksleep = tksleep
 
def fecharOS():
    cracha = entry_cracha.get()
    if(len(cracha)) < 1:
        output_string.set('Digite o crachá acima.')
    else:
        cracha_numerico = 0
        success = True
        try:
            cracha_numerico = int(cracha)
        except:
            output_string.set('O crachá digitado é realmente numérico? Procure por letras e espaços vazios.')
            success = False
        if(success):
            output_string.set('Abra o \"Gera OS\" em até 3 segundos.')
            window.tksleep(3)
            with open("./OSs.csv", 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    window.tksleep(0.3) 
                    try:
                        os_number = row[0]
                        pyautogui.typewrite(str(os_number))
                        pyautogui.press('enter')
                        pyautogui.typewrite(cracha_numerico) #CRACHA
                        pyautogui.press('enter')
                        pyautogui.press('enter')
                        pyautogui.typewrite(str(os_number))
                        pyautogui.press('enter')
                        pyautogui.press('enter')
                        texto = "A OS " + str(os_number) + " foi fechada no crachá " + str(cracha_numerico) + "."
                        output_string.set(texto)
                    except:          
                        output_string.set('ERRO! Verifique se a formatação da tabela está correta. A OS ' + str(os_number) + ' foi a última fechada')
#window
window = tk.Tk()
window.title('Fechador de OSs') #titulo da janela
window.geometry('500x300') # tamanho da janela 
 
# title - definindo formatação de janela e tamanho da letras 
title_label = ttk.Label(master=window, text="Fechador de OS", font='Calibri 14 bold')
title_label.pack()
 

# # Crachá
input_frame = ttk.Frame(master=window)
entry_cracha = tk.StringVar()
entry = ttk.Entry(master= input_frame, textvariable=entry_cracha)
button = ttk.Button(master=input_frame,text='Crachá', command= fecharOS)


# input field
input_frame = ttk.Frame(master=window)
entry_cracha = tk.StringVar()
entry = ttk.Entry(master= input_frame, textvariable=entry_cracha)
button = ttk.Button(master=input_frame,text='Fechar OSs', command= fecharOS)
 
entry.pack(side='left', padx=1)
button.pack(side='left')
input_frame.pack(pady=10)
 
# output
output_string = tk.StringVar()
output_label = ttk.Label(master= window, text='Output',font='Calibri 10', textvariable=output_string, wraplength=200)
output_label.pack()

button = ttk.Button(master=input_frame,text='iniciar', command= fecharOS)
button.pack()
# run
sv_ttk.set_theme("dark") 
window.mainloop()

