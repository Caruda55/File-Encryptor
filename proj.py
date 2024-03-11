import pyAesCrypt
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar
import time
from config import reference, photo_way, main_photo_way, main_photo_way_2, main_photo_way_3, main_photo_way_4


# окно шифрования
def win_encrypt():
    win_en = tk.Tk()
    win_en.title('Шифровальщик файлов - шифруем')
    win_en.geometry('619x520+457+60')
    win_en['bg'] = 'navajo white'
    win_en.resizable(False, False)

# функция Progress bar
    def progress_bar_enc():
        while bar['value'] < 100:
            bar['value'] += 1
            win_en.update()
            time.sleep(0.01)

# функция шифрования
    def encrypt():
        password = parol_name.get()
        way_1 = way_name.get()
        way_2 = way_name_2.get()
        if len(password) == 0 or len(way_1) == 0 or len(way_2) == 0:
            txt.insert(0, 'Поля не заполнены!')
            txt.delete(0, tk.END)
            txt.insert(0, 'Поля не заполнены!')
        elif way_1[::-1][:3] != way_2[::-1][:3]:
            txt.insert(0, 'Тип файлов на совпадает!')
            txt.delete(0, tk.END)
            txt.insert(0, 'Тип файлов на совпадает!')
        else:
            try:
                #time.sleep(2)       # декоративная задержка исполнения функции
                progress_bar_enc()  # вызов функции progress bar
                pyAesCrypt.encryptFile(way_1, way_2, password)
                txt.delete(0, tk.END)
                txt.insert(0, 'Готово!')
            except ValueError:
                txt.insert(0, 'Неверно указан путь к файлу')
                txt.delete(0, tk.END)
                txt.insert(0, 'Неверно указан путь к файлу')
                bar['value'] = 0

# функция удаляющая значения из полей
    def clear():
        parol_name.delete(0, tk.END)
        way_name.delete(0, tk.END)
        way_name_2.delete(0, tk.END)
        txt.delete(0, tk.END)
        bar['value'] = 0

# блок виджетов в окне шифрования
    user_text = tk.Label(win_en, text=' Придумайте надёжный пароль  ', font=('Arial', 16, 'bold'), relief=tk.RAISED,
                         pady=7, padx=7, bg='gold2')
    user_text.grid(row=0, column=0, padx=7, pady=14)
    parol_name = tk.Entry(win_en, font=('Arial', 15), width=15)
    parol_name.grid(row=1, column=0, columnspan=3, sticky='we', padx=7)

    user_text_2 = tk.Label(win_en, text='Расширение и путь к файлу который шифруем', font=('Arial', 16, 'bold'), relief=tk.RAISED,
                           pady=7, padx=7, bg='gold2')
    user_text_2.grid(row=2, column=0, padx=7, pady=14)
    way_name = tk.Entry(win_en, font=('Arial', 15), width=15)
    way_name.grid(row=3, column=0, columnspan=3, padx=7, sticky='we')

    user_text_3 = tk.Label(win_en, text='Расширение и путь к зашифрованному файлу', font=('Arial', 16, 'bold'), relief=tk.RAISED,
                           pady=7, padx=7, bg='gold2')
    user_text_3.grid(row=4, column=0, padx=7, pady=14)
    way_name_2 = tk.Entry(win_en, font=('Arial', 15), width=15)
    way_name_2.grid(row=5, column=0, columnspan=3, sticky='we', padx=7)

    btn_enc = tk.Button(win_en, text='Зашифровать файл', bd=5, font=('Arial', 13, 'bold'), command=encrypt, bg='palegreen3')
    btn_enc.grid(row=6, column=0, sticky='we', padx=15, pady=14)

    txt = tk.Entry(win_en, width=30, font=('Bookman Old Style', 25), justify=tk.CENTER)
    txt.grid(row=7, column=0, padx=7, pady=7)

    btn_clear = tk.Button(win_en, text='Отчистить', bd=5, font=('Arial', 13, 'bold'), command=clear, bg='palegreen3')
    btn_clear.grid(row=8, column=0, sticky='we', padx=15, pady=7)

# Progres  bar
    style = ttk.Style()
    style.theme_use('default')
    bar = Progressbar(win_en, length=400, mode='determinate')
    bar.grid(column=0, row=9)


# окно дешифрования
def win_descript():
    win_des = tk.Tk()
    win_des.title('Шифровальщик файлов - дешифруем')
    win_des.geometry('619x520+457+60')
    win_des['bg'] = 'navajo white'
    win_des.resizable(False, False)

# функция Progress bar
    def progress_bar_des():
        while bar['value'] < 100:
            bar['value'] += 1
            win_des.update()
            time.sleep(0.01)

# функция дешифрования
    def descript():
        password = parol_name.get()
        way_1 = way_name.get()
        way_2 = way_name_2.get()
        if len(password) == 0 or len(way_1) == 0 or len(way_2) == 0:
            txt.insert(0, 'Поля не заполнены!')
            txt.delete(0, tk.END)
            txt.insert(0, 'Поля не заполнены!')
        elif way_1[::-1][:3] != way_2[::-1][:3]:
            txt.insert(0, 'Тип файлов не совпадает!')
            txt.delete(0, tk.END)
            txt.insert(0, 'Тип файлов не совпадает!')

        else:
            try:
                #time.sleep(2)
                progress_bar_des()
                pyAesCrypt.decryptFile(way_1, way_2, password)
                txt.delete(0, tk.END)
                txt.insert(0, 'Готово!')
            except ValueError:
                txt.insert(0, 'Неверно указан пароль или путь')
                txt.delete(0, tk.END)
                txt.insert(0, 'Неверно указан пароль или путь')
                bar['value'] = 0

# функция удаляющая значения из полей
    def clear():
        parol_name.delete(0, tk.END)
        way_name.delete(0, tk.END)
        way_name_2.delete(0, tk.END)
        txt.delete(0, tk.END)
        bar['value'] = 0


# блок виджетов окна дешифрования
    user_text = tk.Label(win_des, text='Введите пароль', font=('Arial', 16, 'bold'), relief=tk.RAISED, pady=7,
                         padx=7, bg='gold2')
    user_text.grid(row=0, column=0, padx=7, pady=14)
    parol_name = tk.Entry(win_des, font=('Arial', 15), width=15)
    parol_name.grid(row=1, column=0, columnspan=3, sticky='we', padx=7)

    user_text_2 = tk.Label(win_des, text='Расширение и путь к файлу который дешифруем', font=('Arial', 16, 'bold'),
                           relief=tk.RAISED, pady=7, padx=7, bg='gold2')
    user_text_2.grid(row=2, column=0, padx=7, pady=14)
    way_name = tk.Entry(win_des, font=('Arial', 15), width=15)
    way_name.grid(row=3, column=0, columnspan=3, padx=7, sticky='we')

    user_text_3 = tk.Label(win_des, text='Расширение и путь к расшифрованному файлу', font=('Arial', 16, 'bold'),
                           relief=tk.RAISED, pady=7, padx=7, bg='gold2')
    user_text_3.grid(row=4, column=0, padx=7, pady=14)
    way_name_2 = tk.Entry(win_des, font=('Arial', 15), width=15)
    way_name_2.grid(row=5, column=0, columnspan=3, sticky='we', padx=7)

    btn_enc = tk.Button(win_des, text='Расшифровать файл', bd=5, font=('Arial', 13, 'bold'), command=descript, bg='palegreen3')
    btn_enc.grid(row=6, column=0, sticky='we', padx=15, pady=14)

    txt = tk.Entry(win_des, width=30, font=('Bookman Old Style', 25), justify=tk.CENTER)
    txt.grid(row=7, column=0, padx=7, pady=7)

    btn_clear = tk.Button(win_des, text='Отчистить', bd=5, font=('Arial', 13, 'bold'), command=clear, bg='palegreen3')
    btn_clear.grid(row=8, column=0, sticky='we', padx=15, pady=7)

# progress bar
    style = ttk.Style()
    style.theme_use('default')
    bar = Progressbar(win_des, length=400, mode='determinate')
    bar.grid(column=0, row=9)


# функция выбора метода
def choice():
    if r_var.get() == 0:
        return win_encrypt()
    else:
        return win_descript()

# главное окно
win = tk.Tk()
win.title('Шифровальщик файлов')
win.geometry('320x330+397+90')
win['bg'] = 'old lace'
win.resizable(False, False)
photo = tk.PhotoImage(file=photo_way)
win.iconphoto(True, photo)

win.image = tk.PhotoImage(file=main_photo_way)
bg_logo = tk.Label(win, image=win.image)
bg_logo.grid(row=0, column=3)

win.image_2 = tk.PhotoImage(file=main_photo_way_2)
bg_logo = tk.Label(win, image=win.image_2)
bg_logo.grid(row=1, column=3)

win.image_3 = tk.PhotoImage(file=main_photo_way_3)
bg_logo = tk.Label(win, image=win.image_3)
bg_logo.grid(row=2, column=3)

win.image_4 = tk.PhotoImage(file=main_photo_way_4)
bg_logo = tk.Label(win, image=win.image_4)
bg_logo.grid(row=3, column=3)

# блок виджетов главного окна
user_text = tk.Label(win, text='Шифруем файл', font=('Arial', 16, 'bold'), relief=tk.RAISED, pady=7, padx=7, bg='gold2')
user_text.grid(row=0, column=0, padx=7, pady=14)
user_text_2 = tk.Label(win, text='Дешифруем файл', font=('Arial', 16, 'bold'), relief=tk.RAISED, pady=7, padx=7, bg='gold2')
user_text_2.grid(row=1, column=0, padx=7, pady=14)

# блок radiobutton
r_var = tk.IntVar()
r_var.set(0)
r1 = tk.Radiobutton(variable=r_var, value=0, bg='white')
r1.grid(row=0, column=1)

r2 = tk.Radiobutton(variable=r_var, value=1, bg='white')
r2.grid(row=1, column=1)

btn = tk.Button(win, text='Выбрать', bd=3, font=('Arial', 23, 'bold'), command=choice, bg='palegreen3')
btn.grid(row=2, column=0, padx=7, pady=14, sticky='we')

btn_2 = tk.Button(win, text='Справка', bd=3, font=('Arial', 15, 'bold'), command=reference, bg='palegreen3')
btn_2.grid(row=3, column=0, padx=7, pady=14, sticky='we')


if __name__ == '__main__':
    win.mainloop()




