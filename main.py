import pyautogui as pag
import keyboard
import pyperclip
import openpyxl as opx
from time import sleep as sl
from datetime import datetime

WORKBOOK_PATH = 'D:\python\spamer\контакты.xlsx'  # Путь к вашей базе которую вы импортировали в эмулятор , но лучше
# чтобы база и скрипт были в одной папке
workbook = opx.load_workbook(WORKBOOK_PATH)

first_sheet = workbook.worksheets[0]

'''
pos = pag.position()
print(pos)
'''

how_many = 0
start_time = datetime.now()

for row in first_sheet.rows:
    phone = row[1].value  # Телефон
    name = row[0].value  # Название

    sl(1)

    # speach = f"Здравствуйте , на насчёт объявления '{name}' , ещё актуально ?"  # Спич
    speach = 'Можно доп. фото ?'
    pyperclip.copy(phone)

    pag.click(x=1832, y=82, interval=2)  # Поиск по контакту , 1 значение
    keyboard.press_and_release('ctrl+v')  # Вставляем номер
    sl(1)

    pag.click(x=1250, y=193, interval=2)  # Входим в личку , 2 значение
    sl(1)

    pyperclip.copy(speach)  # Копируем спич
    keyboard.press_and_release('ctrl+v')  # Вставляем спич
    sl(1)
    keyboard.press_and_release('enter')
    sl(1)

    pag.click(x=1032, y=84, interval=2)  # Выход с лички , 3 значение
    how_many += 1
    print(f'Кол-во сообщений: {how_many}\nПрошло времени: {datetime.now() - start_time}')
