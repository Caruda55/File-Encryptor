import tkinter as tk

# пути к логотипам
photo_way = ('C:\\1.png')

main_photo_way = ('C:\\pic.png')

main_photo_way_2 = ('C:\\pic2.png')

main_photo_way_3 = ('C:\\pic3.png')

main_photo_way_4 = ('C:\\pic4.png')

# функция справочного окна
def reference():
    win_ref = tk.Tk()
    win_ref.title('Справка')
    win_ref.geometry('651x490+457+60')
    win_ref['bg'] = 'sienna1'
    win_ref.resizable(False, False)

    ref_text = tk.Label(win_ref, font=('Arial', 18),
                        text='Шифровальщик создаёт\n зашифрованные копии файлов\n'
                             'таких форматов как TXT, PDF, PNG, JPEG.\n Так же возможно шифрование документов\n '
                             'Microsoft Office (Word, Excel) и видеофайлов.\n После того, как будут созданы\n зашифрованные копии файлов\n'
                             'оригиналы можно удалить\n или перенести в безопасное место.\r'
                             'В полях необходимо указать полный путь к файлу\n и его расширение (C\Рабочий стол\Файл.txt)\r'
                             'Название зашифрованной копии должно отличаться\n от оригинала (С\Рабочий стол\Файл2.txt)\r'
                             'То же самое при дешифровании файла'
                             ,padx=15, pady=15, relief=tk.RAISED, bg='light blue')
    ref_text.grid(row=0, column=1, padx=15, pady=15)


