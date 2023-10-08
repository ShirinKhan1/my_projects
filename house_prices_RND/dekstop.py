import tkinter as tk
import pickle
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from tkinter import ttk
import pandas as pd

model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    loaded_scaler = pickle.load(file)

data_columns1 = ['Общая площадь', 'Площадь кухни', 'Жилая площадь', 'Этаж',
                 'Год постройки']
data_columns2 = ['балкон', 'балкон, лоджия ', 'лоджия']
data_columns3 = ['Тип дома_ блочный', 'Тип дома_ кирпичный',
                 'Тип дома_ монолитно-кирпичный', 'Тип дома_ монолитный',
                 'Тип дома_ панельный']
data_columns4 = ['Парковка_ за шлагбаумом во дворе',
                 'Парковка_ наземная многоуровневая',
                 'Парковка_ наземная многоуровневая, за шлагбаумом во дворе',
                 'Парковка_ наземная многоуровневая, открытая во дворе',
                 'Парковка_ наземная многоуровневая, открытая во дворе, за шлагбаумом во дворе',
                 'Парковка_ открытая во дворе',
                 'Парковка_ открытая во дворе, за шлагбаумом во дворе',
                 'Парковка_ подземная',
                 'Парковка_ подземная, за шлагбаумом во дворе',
                 'Парковка_ подземная, наземная многоуровневая',
                 'Парковка_ подземная, наземная многоуровневая, за шлагбаумом во дворе',
                 'Парковка_ подземная, наземная многоуровневая, открытая во дворе',
                 'Парковка_ подземная, наземная многоуровневая, открытая во дворе, за шлагбаумом во дворе',
                 'Парковка_ подземная, открытая во дворе',
                 'Парковка_ подземная, открытая во дворе, за шлагбаумом во дворе']
data_columns5 = ['В доме_ газ', 'В доме_ консьерж', 'В доме_ консьерж, газ',
                 'В доме_ консьерж, мусоропровод', 'В доме_ консьерж, мусоропровод, газ',
                 'В доме_ мусоропровод', 'В доме_ мусоропровод, газ']
data_columns6 = ['Двор_ детская площадка', 'Двор_ детская площадка, спортивная площадка',
                 'Двор_ закрытая территория',
                 'Двор_ закрытая территория, детская площадка',
                 'Двор_ закрытая территория, детская площадка, спортивная площадка',
                 'Двор_ спортивная площадка']
data_columns7 = ['Грузовой лифт_ 1', 'Грузовой лифт_ 2',
                 'Грузовой лифт_ 3', 'Грузовой лифт_ 4', 'Грузовой лифт_ нет']
data_columns8 = ['Ремонт_ дизайнерский', 'Ремонт_ евро', 'Ремонт_ косметический',
                 'Ремонт_ требует ремонта']
data_columns9 = ['Санузел_ раздельный',
                 'Санузел_ совмещенный']

all_data = data_columns1 + data_columns2 + data_columns3 + data_columns4 + data_columns5 + data_columns6 + data_columns7 + data_columns8 + data_columns9

# def process_input():
#     input_data = entry.get()  # Получаем данные из входного поля
#     # Здесь можно выполнить действия с полученными данными
#     print("Введенные данные:", input_data)


# Создание экземпляра главного окна
window = tk.Tk()
window.title("price")
window.geometry("800x600")

# entry = tk.Entry(window)
# entry.grid(column=0, row=0)
list_data_columns1 = []
list_labels_columns1 = []
for i in range(len(data_columns1)):
    list_data_columns1.append(tk.Entry(window))
    list_data_columns1[i].grid(column=1, row=i + 3)
    list_labels_columns1.append(tk.Label(window, text=data_columns1[i]))
    list_labels_columns1[i].grid(row=i + 3)

list_data_columns2 = []
list_labels_columns2 = []
y_row = len(data_columns1) + 3

combo1 = Combobox(window, state="readonly")
data_columns2_ = data_columns2
data_columns2_.append('нет')
combo1['values'] = data_columns2_
combo1.grid(column=1)
label_data_columns2 = tk.Label(window, text='балкон или лоджия')
label_data_columns2.grid(row=y_row)
y_row += 1
combo1.grid()

combo2 = Combobox(window, state="readonly")
combo2.grid(column=1)
data_columns3_ = []
for i in data_columns3:
    k = i.split('_ ')
    data_columns3_.append(k[1])
combo2['values'] = data_columns3_
label_data_columns3 = tk.Label(window, text='тип дома')
label_data_columns3.grid(row=y_row)
y_row += 3
# combo2.grid()

combo3 = Combobox(window, state="readonly")
combo3.grid(row=y_row, column=1)
combo3['values'] = data_columns7
label_data_columns4 = tk.Label(window, text='Грузовой лифт')
label_data_columns4.grid(row=y_row, column=0)
y_row += 3

combo4 = Combobox(window, state="readonly")
combo4.grid(row=y_row, column=1)
combo4['values'] = data_columns8
label_data_columns5 = tk.Label(window, text='Ремонт')
label_data_columns5.grid(row=y_row, column=0)
y_row += 3

combo5 = Combobox(window, state="readonly")
combo5.grid(row=y_row, column=1)
combo5['values'] = data_columns9
label_data_columns6 = tk.Label(window, text='Санузел')
label_data_columns6.grid(row=y_row, column=0)
y_row += 3

data_columns4_ = [
    'Парковка_ подземная',
    'наземная многоуровневая',
    'открытая во дворе',
    'за шлагбаумом во дворе'
]
dict_column4 = {
    '0001': 'Парковка_ за шлагбаумом во дворе',
    '0100': 'Парковка_ наземная многоуровневая',
    '0101': 'Парковка_ наземная многоуровневая, за шлагбаумом во дворе',
    '0110': 'Парковка_ наземная многоуровневая, открытая во дворе',
    '0111': 'Парковка_ наземная многоуровневая, открытая во дворе, за шлагбаумом во дворе',
    '0010': 'Парковка_ открытая во дворе',
    '0011': 'Парковка_ открытая во дворе, за шлагбаумом во дворе',
    '1000': 'Парковка_ подземная',
    '1001': 'Парковка_ подземная, за шлагбаумом во дворе',
    '1100': 'Парковка_ подземная, наземная многоуровневая',
    '1101': 'Парковка_ подземная, наземная многоуровневая, за шлагбаумом во дворе',
    '1110': 'Парковка_ подземная, наземная многоуровневая, открытая во дворе',
    '1111': 'Парковка_ подземная, наземная многоуровневая, открытая во дворе, за шлагбаумом во дворе',
    '1010': 'Парковка_ подземная, открытая во дворе',
    '1011': 'Парковка_ подземная, открытая во дворе, за шлагбаумом во дворе'
}

enabled = []
[enabled.append(tk.IntVar()) for _ in range(4)]
list_enabled_checkbutton = []
for i, index in zip(data_columns4_, range(4)):
    list_enabled_checkbutton.append(ttk.Checkbutton(text=i, variable=enabled[index]))
    list_enabled_checkbutton[index].grid(row=y_row, column=index)
y_row += 3
data_columns5_ = [
    'консьерж',
    'мусоропровод',
    'газ'
]
dict_column5 = {
    '001': 'В доме_ газ',
    '100': 'В доме_ консьерж',
    '101': 'В доме_ консьерж, газ',
    '110': 'В доме_ консьерж, мусоропровод',
    '111': 'В доме_ консьерж, мусоропровод, газ',
    '010': 'В доме_ мусоропровод',
    '011': 'В доме_ мусоропровод, газ'
}
enabled1 = []
[enabled1.append(tk.IntVar()) for _ in range(3)]
list_enabled_checkbutton1 = []
for i, index in zip(data_columns5_, range(3)):
    list_enabled_checkbutton1.append(ttk.Checkbutton(text=i, variable=enabled1[index]))
    list_enabled_checkbutton1[index].grid(row=y_row, column=index)

data_columns6_ = [
    'закрытая территория',
    'детская площадка',
    'спортивная площадка'
]
dict_column6 = {
    '010': 'Двор_ детская площадка',
    '011': 'Двор_ детская площадка, спортивная площадка',
    '100': 'Двор_ закрытая территория',
    '110': 'Двор_ закрытая территория, детская площадка',
    '111': 'Двор_ закрытая территория, детская площадка, спортивная площадка',
    '001': 'Двор_ спортивная площадка'
}
y_row += 3
enabled2 = []
[enabled2.append(tk.IntVar()) for _ in range(3)]
list_enabled_checkbutton2 = []
for i, index in zip(data_columns6_, range(3)):
    list_enabled_checkbutton2.append(ttk.Checkbutton(text=i, variable=enabled2[index]))
    list_enabled_checkbutton2[index].grid(row=y_row, column=index)


def parce():
    df = {}
    for name in all_data:
        df[name] = [0]
    try:
        for e, j in zip(list_data_columns1, data_columns1):
            # print(j)
            if j == 'Этаж' or j == 'Год постройки':

                df[j] = [int(e.get())]
            else:
                df[j] = [float(e.get())]
            # print(e.get())
        data2 = combo1.get()
        if not (data2 == 'нет'):
            df[data2] = 1
        data3 = combo2.get()
        df[f'Тип дома_ {data3}'] = [1]
        data4 = combo3.get()
        df[data4] = [1]
        data5 = combo4.get()
        df[data5] = [1]
        data6 = combo5.get()
        df[data6] = [1]

        str_ = ''
        for e in enabled:
            str_ += str(e.get())
        str_ = dict_column4.get(str_)
        df[str_] = [1]

        str_ = ''
        for e in enabled1:
            str_ += str(e.get())
        str_ = dict_column5.get(str_)
        df[str_] = [1]

        str_ = ''
        for e in enabled2:
            str_ += str(e.get())
        str_ = dict_column6.get(str_)
        df[str_] = [1]

    except Exception as e:
        print(e)
        return
    return df


def genenerate_price():
    df = parce()

    # df = pd.DataFrame(columns=list(df.keys()), data=df.values())
    # df = loaded_scaler.transform(df)
    df = loaded_scaler.transform(pd.DataFrame(df))
    price = model.predict(df)
    showinfo(title="Цена", message=f"{int(price)} rub")


button = ttk.Button(text='Узнать цену', command=genenerate_price)
button.grid(row=4, column=10)

window.mainloop()
