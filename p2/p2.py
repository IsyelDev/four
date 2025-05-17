import yfinance
import pyautogui
import pyperclip
import webbrowser
import time
ticker = input("Digita el codigo de accion")
data = yfinance.Ticker(ticker).history("6mo")
cierre = data.Close

maxima = round(cierre.max(),2)
minima = round(cierre.min(),2)
valor_medio = round(cierre.mean(),2)

destinatario = "isyelalways@gmail.com"
asunto = "Analisis acciones ultimos 6 meses"

mensaje = f"""
Hola Papu
aca te envio {ticker}
cotizacion maxima = {maxima}
cotizacion minima = {minima}
valor medio = {valor_medio}

cualquier cosa que me cuentas

Nico
"""

webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(3)

pyautogui.PAUSE =3

pyautogui.click(2027,224)
time.sleep(4)
#print(pyautogui.position())
# Escribir el destinatario
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Escribir el asunto
pyperclip.copy (asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Escribir el mensaje
pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey ("tab")
# Click en el botón de "Enviar"
pyautogui.click(2499,1835)
#Cerrar gmail
pyautogui.hotkey("ctrl", "f4")