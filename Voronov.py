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
        text += f"00{i}|{random.choice(days)}|{random.choice(times)}|{random.choice(subjects)}|{random.choice(cab)}|{random.choice(surnames)}\n"

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


def timetable_for_teacher():
    data = read_table_dat()
    surname = entry_surname.get()
    result_list = []
    for record in data:
        record = record.split("|")
        if surname == record[5]:
            result_list += record[1] + record[2] + '\n'

    label_table["text"] = f"{' '.join(result_list)}"


window = tk.Tk()
window.title("Расписание занятий")
window.geometry("1000x800")

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

generate_table_dat(12)
print(read_table_dat())
window.mainloop()
