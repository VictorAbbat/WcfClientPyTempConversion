from tkinter import *
from tkinter import ttk
import data as data
from suds.client import Client
from pymongo import MongoClient

url = "http://localhost:8733/Design_Time_Addresses/WcfServiceTempConversion/Service1/?wsdl"
client = Client(url)

connection = MongoClient('localhost', 1701)
collection = connection.dbTemp.appels

"""
db = connection["dbTemp"]
collection = db['appels']

print(collection)
print("Connection Successful")
"""

print("\n----------------------Reading All Documents----------------------\n")
for item in collection.find():
    print(item)


fenetre = Tk()
fenetre.title("WcfClientPythonTempConversion")
fenetre.resizable(width=True, height=True)
fenetre.geometry("600x350")

# label
label = Label(fenetre, text="Saisir la valeur à convertir ")
label.pack()

# entrée
value = StringVar()
# value.set("texte par défaut")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

# radiobutton
b = IntVar(fenetre, 1)
values = {"Celcius": 1, "Fahrenheit": 2}
for (text, value) in values.items():
    Radiobutton(fenetre, text=text, variable=b, value=value).pack(side=LEFT)

tree = ttk.Treeview(fenetre)
# Inserted at the root, program chooses id:
# tree.insert('', 'end', 'widgets', text='Widget Tour')
# tree.move('widgets', 'gallery', 'end')  # move widgets under gallery
# tree = ttk.Treeview(fenetre, columns=('size', 'modified'))
# tree['columns'] = ('size', 'modified', 'owner')


tree["columns"] = ("1", "2", "3", "4")
tree['show'] = 'headings'
tree.heading("1", text="UserName")
tree.heading("2", text="MachineName")
tree.heading("3", text="Valeur")
tree.heading("4", text="Date")
tree.pack()

## bouton de sortie
bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

"""
cels_value = client.service.ConvertirVersCelcius(10, "Victor", "PC-victor")
print(cels_value)
cels_value = client.service.ConvertirVersFarh(-16, "Victor", "PC-victor")
print(cels_value)

"""

# print(client)

fenetre.mainloop()

## Press Maj+F10 to execute it or replace it with your code.
## Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
## Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


## Press the green button in the gutter to run the script.
# if __name__ == '__main__':
# print_hi('PyCharm')

## See PyCharm help at https://www.jetbrains.com/help/pycharm/
