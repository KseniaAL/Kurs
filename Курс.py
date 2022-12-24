import tkinter as tk
import random
import tkinter.filedialog as tfd


def generate_apteka_dat(count_pharmacy: int) -> None:
    """
    Генерирует рандомный apteka.dat
    номер аптеки|название лекарства|цена|количество
    :param count_pharmacy: количество записей
    :return: None
    """
    text = ""
    med_names = ["Корвалол", "Эспумизан", "Йод", "Ношпа", "Найз Гель", "Валерианка", "Нурофен", "Арбидол", "Зеленка"]
    med_name = random.choice(med_names)
    for i in range(count_pharmacy):
        text += f"{i}|{med_names[random.randint(0, 8)]}|{random.randint(10, 100)}|{random.randint(0, 20)}\n"
    with open("apteka.dat", "w") as f:
        f.write(text)


def read_apteka_dat() -> list:
    """
    """

    with open("apteka.dat") as f:
        file_list = f.read().split("\n")
        l = len(file_list)
        return file_list [:l-1]


def get_info_about_a_medicine_at_a_specific_pharmacy():
    data = read_apteka_dat()
    availability = False
    pharmacy = entry_name_pharmacy.get()
    medicine = entry_name_medicine.get()
    for record in data:
        record = record.split("|")
        print(record)
        if record[0] == pharmacy and medicine == record[1] and int(record[3]) > 0:
            availability = True
    if availability:
        label_availability_medicine["text"] = "Есть в наличии"
    else:
        label_availability_medicine["text"] = "Отсутствует"


def sum_all_medicine():
    data = read_apteka_dat()
    summa = 0
    for record in data:
        record = record.split("|")
        summa += int(record[2])

    label_amount["text"] = f"Общая стоимость: {summa}"


def list_pharmacy_on_name_medicine():
    data = read_apteka_dat()
    medicine = text_medicine_name.get()
    result_list = []
    for record in data:
        record = record.split("|")
        if medicine == record[1] and int(record[3]) > 0:
            result_list += record[0]
    label_pharmacies["text"] = f"Список аптек: {' '.join(result_list)}"


def get_the_cheapest():
    data = read_apteka_dat()
    the_cheapest = 100000
    for record in data:
        record = record.split("|")
        if int(record[2]) < int(the_cheapest):
            the_cheapest = record[2]
    label_cheap_medicine["text"] = f"Самое дешевое лекарство стоит: {the_cheapest}"

def open_file():

    text.delete(1.0, "end")
    global file_name
    file_name = tfd.askopenfilename()
    with open(file_name) as file:
        text.insert(1.0, file.read())
    read_apteka_dat()

def save_file():
    content = text.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(content)
    read_apteka_dat()
file_name = ""
window = tk.Tk()
window.geometry("1000x500")
window.title("Аптека")

text = tk.Text(window, width = 50, height = 100)
text.place(x = 0, y = 0)

main_menu = tk.Menu(window)
window.configure(menu = main_menu)
file_menu = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_command(label = "Open", command = open_file)

label_name_medicine = tk.Label(window, text="Название лекарства: ")
label_name_medicine.place(x=430, y=30)
entry_name_medicine = tk.Entry(window)
entry_name_medicine.place(x=550, y=30)

label_name_pharmacy = tk.Label(window, text="Номер аптеки: ")
label_name_pharmacy.place(x=430, y=50)
entry_name_pharmacy = tk.Entry(window)
entry_name_pharmacy.place(x=550, y=50)

button1 = tk.Button(window, text="Проверить наличие", command=get_info_about_a_medicine_at_a_specific_pharmacy)
button1.place(x=480, y=90)

label_availability_medicine = tk.Label(window, text="Результат: ")
label_availability_medicine.place(x=700, y=40)

label_amount = tk.Label(window, text="Общая стоимость: ")
label_amount.place(x=430, y=150)

button2 = tk.Button(window, text="Получить стоимость", command=sum_all_medicine)
button2.place(x=480, y=180)

label_medicine_name = tk.Label(window, text="Название лекарства: ")
label_medicine_name.place(x=430, y=230)
text_medicine_name = tk.Entry(window)
text_medicine_name.place(x=550, y=230)

label_pharmacies = tk.Label(window, text="Список аптек: ")
label_pharmacies.place(x=700, y=230)

button3 = tk.Button(window, text="Выдать список аптек", command=list_pharmacy_on_name_medicine)
button3.place(x=480, y=270)

label_cheap_medicine = tk.Label(window, text="Самое дешевое лекарство стоит: ")
label_cheap_medicine.place(x=430, y=330)

button4 = tk.Button(window, text="Поиск самого дешевого", command=get_the_cheapest)
button4.place(x=480, y=360)
# generate_apteka_dat(10)
print(read_apteka_dat())

window.mainloop()
