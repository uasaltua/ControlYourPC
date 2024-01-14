import telebot
from telebot import types
import pyautogui
import pyscreeze
import time
from translate import Translator
import keyboard
from threading import Thread
import PIL 
from PIL import Image, ImageTk
import tkinter
import os
import socket

def Server(ip="192.168.1.5", port=1920):
	try:
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.bind((ip, port))
		server_socket.listen(1)
		client_conn, address = server_socket.accept()
		client_conn.sendall("0.0.1".encode('utf-8'))
		while True:
			data = client_conn.recv(1024).decode("UTF-8")
			if not data:
				break
			data = data.split(",")
			if data[0] == "0":
				os.startfile("C:/Users/muz15/AppData/Local/Discord/Update.exe")
			elif data[0] == "1":
				os.startfile("C:/Users/muz15/AppData/Roaming/Telegram Desktop/Telegram.exe")
			elif data[0] == "2":
				os.startfile("C:/Users/muz15/AppData/Local/Roblox/Versions/version-48a28da848b7420d/RobloxPlayerBeta.exe")
			elif data[0] == "3":
				os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")
			elif data[0] == "4":
				os.system("shutdown /s /t 0")
			elif data[0] == "5":
				os.system("shutdown /r /t 0")
			elif data[0] == "6":
				os.startfile("C:\\Windows\\notepad.exe")
			elif data[0] == "N/A":
				pyautogui.alert("Ваша док-панель не поддерживает версию ПО")
	except:
		client_conn.close()

Thread(target=Server).start()

try:
	bot = telebot.TeleBot("6919017234:AAGn2bXeeI5WBvU4DXCqvVE0skwphNPhTLw")
	x = 0
	y = 0
	step = 15
	b1 = False
	b2 = False
	AimBot = False
	pyautogui.FAILSAFE = False
	glowny = types.ReplyKeyboardMarkup(True)
	glowny.add(types.KeyboardButton("Система"), types.KeyboardButton("Бот"), types.KeyboardButton("Быстрые клавиши"))
	system = types.ReplyKeyboardMarkup(True)
	system.add(types.KeyboardButton("Двойной клик"), types.KeyboardButton("ПКМ"), types.KeyboardButton("Заблокировать"), types.KeyboardButton("Скриншот"), types.KeyboardButton("Свернуть все окна"), types.KeyboardButton("Выполнить"), types.KeyboardButton("Диспетчер задач"), types.KeyboardButton("AimBot"))
	lbl1 = None
	typed_text = ""


	def helpp():
		keyboard.add_abbreviation("g", "evgensoletskiys@gmail.com")
		keyboard.add_abbreviation("!", "паша го в рб")
		keyboard.add_abbreviation("C", "Organized Crime Group «Red Scull»")
	Thread(target=helpp).start()
	@bot.message_handler(commands=["start"])
	def start(message):
		bot.register_next_step_handler(message, passw)
	def passw(message):
		if message.text == "599623":
			bot.send_message(message.chat.id, "И что ты от меня хочешь?", reply_markup=glowny)
	def Screen():
		while True:
			keyboard.wait("Print Screen")
			time.sleep(0)
			bot.send_photo(6026450735, pyautogui.screenshot('screenshot.png', region=(0,0, 1920, 1080)))
	Thread(target=Screen).start()
	def AimBOT():
		global AimBot
		if AimBot == False: AimBot = True
		else: AimBot = False
		while True:
			if AimBot == False:
				break
			pos = list(pyscreeze.locateAllOnScreen('SBU.png'))
			pyautogui.moveTo(pos[2], pos[3], duration=0.1, tween=pyautogui.easeInOutQuad)
			print(pos)

	@bot.message_handler(content_types=["text"])
	def on_message(message):
		try:
			if message.text == "Двойной клик":
				pyautogui.click()
				time.sleep(0.1)
				pyautogui.click()
			elif message.text == "Система":
				bot.send_message(message.chat.id, "И чо", reply_markup=system)
			elif message.text == "Скриншот":
				bot.send_photo(message.chat.id, pyautogui.screenshot('screenshot.png'))
			elif message.text == "Свернуть все окна":
				pyautogui.hotkey('win','d')
			elif message.text == "ПКМ":
				pyautogui.mouseDown(button='right')
				time.sleep(0.2)
				pyautogui.mouseUp(button='right')
			elif message.text == "Выполнить":
				pyautogui.hotkey('win','r')
			elif message.text == "Диспетчер задач":
				pyautogui.hotkey('ctrl','shift', 'esc')
			elif message.text == "AimBot":
				#AimBOT()
				#Thread(target=AimBOT).start()
				bot.send_message(message.chat.id, f"Статус AimBot`а: {AimBot}")
			else:
				txt(message)
		except Exception as ex:
			print(ex)

	def txt(message):
			translated = Translator(to_lang="en", from_lang="ru").translate(str(message.text))
			pyautogui.typewrite(translated, interval=0.05)
			pyautogui.press('Enter')

	#bot.send_message(1828480879, "Я знову на зв'язку зателефонуй мені!")
	bot.polling(none_stop=True)
except Exception as ex:
	f = tkinter.Tk()
	tkinter.Label(text=ex).pack()
	f.mainloop()