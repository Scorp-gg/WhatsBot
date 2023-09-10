from ast import Num
import webbrowser
import time
import pyautogui
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import base64

        
def donate():
    webbrowser.open("https://www.paypal.com/donate/?hosted_button_id=W6L7ZHFD7GDWL") 

def enviar_mensajes():
    Pais = pais_entry.get()
    numero = numero_entry.get()
    archivo = filedialog.askopenfilename(title="Seleccionar archivo de mensajes", filetypes=[("Archivos de texto", "*.txt")])
    
    if not archivo:
        messagebox.showerror("Error", "Por favor, seleccione un archivo de mensajes.")
        return
    contl = 0
    with open(archivo,"r") as file:
        for line in file:
            contl +=1


    link = "https://web.whatsapp.com/send?phone=" + Pais + numero
    cont = 0
    webbrowser.open(link)
    time.sleep(10)
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            for line in file:
                pyautogui.typewrite(line)
                pyautogui.press("enter")
                cont +=1
                if cont == contl:
                    mensaje = f"Se han enviado {cont} mensajes al {Pais}{numero} \nEsta vez te mamaste, Peter!"
                    messagebox.showinfo("Terminó", mensaje)
        resultado_label.config(text=f"Los mensajes del archivo han sido enviados a: {Pais}{numero}")

    else:
        messagebox.showerror("Error", f"El archivo '{archivo}' no existe.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Envío de Mensajes Masivos por WhatsApp")
ventana.geometry("400x400")  # Ancho x Alto

pais_label = tk.Label(ventana, text="Código de País: 'ejemplo:+52'")
pais_label.pack()

pais_entry = tk.Entry(ventana)
pais_entry.pack()

numero_label = tk.Label(ventana, text="Número Telefónico:")
numero_label.pack(padx=1)

numero_entry = tk.Entry(ventana)
numero_entry.pack(padx=1)

enviar_button = tk.Button(ventana, text="Enviar Mensajes", command=enviar_mensajes)
enviar_button.pack(padx=1)

resultado_label = tk.Label(ventana, text="")
resultado_label.pack(padx=1)

disclaime2_label = tk.Label(ventana, text="El uso indebido de esta herramienta es responsabilidad de quien la utiliza")
disclaime2_label.pack(padx=1)
disclaime_label = tk.Label(ventana, text="Desarrollado por SCORMPX",padx=30, pady=30)
disclaime_label.pack(padx=1)
marco = tk.Frame(ventana, padx=30, pady=30)
marco.pack()
donate_button = tk.Button(ventana, text="Donar en PayPal", command=donate)
donate_button.pack(side=tk.TOP, padx=30)

ventana.mainloop()

