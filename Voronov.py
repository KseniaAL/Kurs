import tkinter as tk
import random
import tkinter.filedialog as tfd

file_name = ""


def generate_table_dat(count_row: int) -> None:
    """
    Генерирует рандомный table.dat
    шифр группы|день недели|время начала занятия|предмет|номер аудитории|фамилия преподавателя
    :param count_row: количество записей
    :return: None
    """
    text = ""
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    times = ["7:30", "9:10", "10:50", "13:00", "14:40", "16:20", "18:00"]
    subjects = ["Теория вер-сти", "ООАиП", "Численные методы", "ТССА", "Менджмент", "Статистика"]
    cab = ["123", "435", "564", "321", "567", "233", "345"]
    surnames = ["Иванов", "Петров", "Сидоров", "Пароходов", "Орлов", "Маринина", "Катышев"]
    for i in range(count_row):
        text += f"{random.randint(1,10)}|{random.choice(days)}|{random.choice(times)}|{random.choice(subjects)}|{random.choice(cab)}|{random.choice(surnames)}\n"

    with open("table.dat", "w", encoding="windows-1251") as f:
        f.write(text)


def read_table_dat() -> list:
    """
    """

    with open("table.dat") as f:
        file_list = f.read().split("\n")
        l = len(file_list)
        return file_list[:l - 1]


def open_file():
    text.delete(1.0, "end")
    global file_name
    file_name = tfd.askopenfilename()
    with open(file_name) as file:
        text.insert(1.0, file.read())
    read_table_dat()


def save_file():
    global file_name
    content = text.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(content)
    read_table_dat()

#1
def timetable_for_teacher():
    data = read_table_dat()
    surname = entry_surname.get()
    result_list = []
    for record in data:
        record = record.split("|")
        if surname == record[5]:
            result_list += record[1] + record[2] + '\n'

    label_table["text"] = f"{' '.join(result_list)}"


def number_of_cab():
    group = entry_group.get()
    day = entry_day.get()
    time = entry_time.get()
    data = read_table_dat()
    for record in data:
        record = record.split("|")
        if group==record[0] and day==record[1] and time==record[2]:
            label_cab["text"] = f"Номер аудитории:{record[4]}"


def weekend():
    surname = entry_surname3.get()
    data = read_table_dat()

    days_weekend = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    for record in data:
        record = record.split("|")
        if record[5] == surname:
            days_weekend.remove(record[1])
    label_weekend["text"] = f"Выходные:{' '.join(days_weekend)}"


def list_group():
    day = entry_day4.get()
    cab = entry_cab4.get()
    data = read_table_dat()
    numbers_group = []
    for record in data:
        record = record.split("|")
        if day==record[1] and cab==record[4]:
            numbers_group.append(record[0])
    label_group4["text"] = f"Группы:{'  '.join(numbers_group)}"




window = tk.Tk()
window.title("Расписание занятий")
window.geometry("1200x800")

text = tk.Text(window, width=50, height=100)
text.place(x=0, y=0)
main_menu = tk.Menu(window)
window.configure(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open", command=open_file)

# 1
label_surname = tk.Label(window, text="Фамилия преподавателя:")
label_surname.place(x=450, y=50)
entry_surname = tk.Entry(window)
entry_surname.place(x=600, y=50)
label_table = tk.Label(window, text="Расписание на неделе:")
label_table.place(x=750, y=50)
button_1 = tk.Button(window, text="Узнать расписание", command=timetable_for_teacher)
button_1.place(x=450, y=75)

#2
label_group = tk.Label(window, text = "Номер группы:")
label_group.place(x = 450, y = 125)
entry_group = tk.Entry(window)
entry_group.place(x = 550, y = 125)

label_day = tk.Label(window, text = "День занятия:")
label_day.place(x = 450, y = 150)
entry_day = tk.Entry(window)
entry_day.place(x = 590, y = 150)

label_time = tk.Label(window, text = "Время начала занятия:")
label_time.place(x = 450, y = 175)
entry_time = tk.Entry(window)
entry_time.place(x = 590, y = 175)


label_cab = tk.Label(window, text = "Номер аудитории:")
label_cab.place(x = 750, y = 150)

button_2 = tk.Button(window, text="Узнать расписание", command=number_of_cab)
button_2.place(x=750, y = 175)
#3
label_surname3 = tk.Label(window, text = "Фамилия преподавателя:")
label_surname3.place(x=450, y = 225)
entry_surname3 = tk.Entry(window)
entry_surname3.place(x = 600, y = 225)
label_weekend = tk.Label(window, text = "Выходные:")
label_weekend.place(x = 750, y = 225)
button_3 = tk.Button(window, text="Узнать выходные", command=weekend)
button_3.place(x=750, y = 250)
#4
label_day4 = tk.Label(window, text = "День недели:")
label_day4.place(x = 450, y = 325)
entry_day4 = tk.Entry(window)
entry_day4.place(x = 530, y = 325)
label_cab4 = tk.Label(window, text = "Номер аудитории:")
label_cab4.place(x=450, y = 350)
entry_cab4 = tk.Entry(window)
entry_cab4.place(x = 560, y = 350)
label_group4 = tk.Label(window, text = "Группы:")
label_group4.place(x=750, y = 300)
button_4 = tk.Button(window, text="Узнать группы", command=list_group)
button_4.place(x=750, y = 325)
# generate_table_dat(12)

window.mainloop()
