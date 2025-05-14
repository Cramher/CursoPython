import yfinance as yf
import pyautogui
import pyperclip
import webbrowser
import time

# Pedir al usuario el ticker de la acción
ticker = input("Digita el codigo de la accion: ")

# Obtener los datos de la acción
data = yf.Ticker(ticker).history("6mo")
cierre = data.Close

# Calcular la cotización máxima, mínima y media
cmax = round(cierre.max(), 2)
cmin = round(cierre.min(), 2)
cprom = round(cierre.mean(), 2)

# Crear el correo
destinatario = "camilo.ra.he95@gmail.com"
asunto = "Informe de acciones ultimos 6 meses"

mensaje = f"""
Buenas noches,

Envio el informe de acciones de los ultimos 6 meses de {ticker}:

Cotizacion maxima: USD {cmax}
Cotizacion minima: USD {cmin}
Cotizacion media: USD {cprom}

Cualquier cosa quedo pendeinte

Saludos,
Nombre Apellido
"""
# Abrir el navegador y Gmail
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

time.sleep(3)

pyautogui.PAUSE = 3

# Hacer clic en el botón "Redactar"
pyautogui.click(87, 213)

# Pegar el correo del destinatario
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Pegar el asunto
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Pegar el mensaje
pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl", "v")

# Enviar el correo y cerrar la ventana
pyautogui.hotkey("ctrl", "enter")
pyautogui.hotkey("ctrl", "f4")
print("El mensaje fue enviado")