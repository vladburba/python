# coding: utf-8

# Python. Быстрый старт.
# Занятие 1.

# Домашнее задание: установить интерпретатор;
#    выполнить действия в интерпретаторе;
#    дописать скрипт, чтобы он перед приветствием выводил название программы


# Строка, начинающаяся с решётки #  - это комментарий, т.е. не выполняется""

# Функция print выводит сообщение в командной строке


# Функция input запрашивает ввод данных у пользователя
print("Great Python Program")
print("Привет, программист!")
name = input("Введите ваше имя: ")
print(name, ", добро пожаловать в мир Python!")
answer = input("Давайте поработаем (Y/N) ")
if answer == "Y":
	print("Вам премия")
elif answer == "N":
	print("До свидания")
else:
	print("Не опознанный символ")


