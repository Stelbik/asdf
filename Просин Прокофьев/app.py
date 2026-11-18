import tkinter as tk
import os
tasks = 0
root = tk.Tk()
root.title("Планировщик задач")
root.geometry("460x520")
try: root.iconbitmap("icon.ico")
except: pass
folder = os.path.dirname(__file__)# Находим папку, где лежит сам файл app.py, чтобы картинка точно нашлась
img_path = os.path.join(folder, "images.png")
img = tk.PhotoImage(file="images.png")
try:
    img = tk.PhotoImage(file=img_path)
    tk.Label(root, image=img).pack(pady=10)
except:
    tk.Label(root, text="[изображение]").pack(pady=10) # заглушка, если файла image.png нет
tk.Label(root, text="Название задачи:").pack(anchor="w", padx=20) # подпись поля
e1 = tk.Entry(root)
e1.pack(fill="x", padx=20)
tk.Label(root, text="Длительность (дней):").pack(anchor="w", padx=20) # подпись поля
e2 = tk.Entry(root)
e2.pack(fill="x", padx=20, pady=(0, 12)) # поле ввода длительности
lbl = tk.Label(root, text="Задач добавлено: 0", anchor="w", relief="solid", borderwidth=1, padx=6, pady=4) # сложный виджет: счётчик с рамкой
lbl.pack(fill="x", padx=20, pady=(0, 8))
def add(): # обработчик кнопки «Добавить»
    global tasks
    tasks += 1 # увеличиваем счётчик
    lbl["text"] = f"Задач добавлено: {tasks}\nПоследняя: {e1.get()} - {e2.get()} дн." # get() + обновление метки
b = tk.Button(root, text="Добавить задачу", bg="#38761d", fg="white", command=add) # новая кнопка: command=add без скобок
b.pack(pady=10) # размещаем кнопку на экране
root.mainloop()
# Ошибка при сборке: создал PhotoImage до главного окна root = tk.Tk(), изза чего была ошибка Too early to create image
# img = tk.PhotoImage(file="image.png")