from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tkinter import *
from file_manager import *
from validator import *

product_list = read_from_file("product.dat")

def load_data(peroduct_list):
    product_list = read_from_file("product.dat")
    for row in table.get_children():
        table.delete(row)

    for product in product_list:
        table.insert("", END, values=product)


def reset_form():
    id.set(len(product_list) + 1)
    name.set("")
    brand.set("")
    buyprice.set("")
    sellprice.set("")

    load_data(product_list)


def save_btn_click():
    product = (id.get(), name.get(), brand.get(), buyprice.get(),sellprice(),quantity())
    errors = product_validator(product)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Product saved")
        product_list.append(product)
        write_to_file("product.dat", product_list)
        reset_form()


def table_select(x):
    selected_product = table.item(table.focus())["values"]
    if selected_product:
        id.set(selected_product[0])
        name.set(selected_product[1])
        brand.set(selected_product[2])
        buyprice.set(selected_product[3])
        sellprice.set(selected_product[4])
        quantity.set(selected_product[5])


def edit_btn_click():
    pass


def remove_btn_click():
    pass


window = Tk()
window.title("product Info")
window.geometry("610x270")

# Id
Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

# Name
Label(window, text="Name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=80, y=60)

# Brand
Label(window, text="brand").place(x=20, y=100)
brand = StringVar()
Entry(window, textvariable=brand).place(x=80, y=100)

# Buy price
Label(window, text="buyprice").place(x=20, y=140)
buyprice = IntVar()
Entry(window, textvariable=buyprice).place(x=80, y=140)

#Sellprice
Label(window, text="sellprice").place(x=20, y=140)
sellprice = IntVar()
Entry(window, textvariable=sellprice).place(x=80, y=140)

#quantity
Label(window, text="quantity").place(x=20, y=140)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=80, y=140)

table = ttk.Treeview(window, columns=[1, 2, 3, 4], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="brand")
table.heading(4, text="buyprice")
table.heading(4, text="sellprice")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=230, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=220)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=220)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=220)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=180, width=190)

reset_form()

window.mainloop()
