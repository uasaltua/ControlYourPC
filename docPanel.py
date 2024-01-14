import tkinter
import socket

root = tkinter.Tk()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.1.5", 1920))
data = client_socket.recv(1024).decode("UTF-8")

Discord = tkinter.Button(text="Дс", command=lambda: client_socket.send("0,0".encode("UTF-8")))
Telegram = tkinter.Button(text="Тг", command=lambda: client_socket.send("1,0".encode("UTF-8")))
Roblox = tkinter.Button(text="Рб", command=lambda: client_socket.send("2,0".encode("UTF-8")))
Chrome = tkinter.Button(text="Хром", command=lambda: client_socket.send("3,0".encode("UTF-8")))
shutdown = tkinter.Button(text="Выключение", command=lambda: client_socket.send("4,0".encode("UTF-8")))
restart = tkinter.Button(text="Рестарт", command=lambda: client_socket.send("5,0".encode("UTF-8")))
notSupport = tkinter.Label(text="Обновите ПО док-панели")

if data == "0.0.0":
	Discord.place(x=0, y=0)
	Telegram.place(x=25, y=0)
	Roblox.place(x=47, y=0)
	Chrome.place(x=72, y=0)
	shutdown.place(x=113, y=0)
	restart.place(x=0, y=30)
else:
	client_socket.send("N/A,0".encode("UTF-8"))
	notSupport.pack()

root.mainloop()