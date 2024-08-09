import io
from math import e
from msilib.schema import Icon
from operator import index
from os import name
import sqlite3
import tkinter
from tkinter import CENTER, END, INSERT, RIGHT, Button, Scrollbar, filedialog
from tkinter import messagebox
from tkinter import ttk
from unittest import result
from altair import Y
from cv2 import WND_PROP_ASPECT_RATIO
from matplotlib.backend_bases import cursors
from matplotlib.pyplot import grid
from numpy import delete, imag, insert
from PIL import Image, ImageTk
from sympy import im


win = tkinter.Tk()
win.geometry("300x300")
win.title("Add Person")

def upload_image():
    e2.delete(0,tkinter.END)
    image_path = filedialog.askopenfilename()
    e2.insert(index=0, string=image_path)

def add_person():
    def convertToBinaryData(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    try:
        conn = sqlite3.connect("persondb.db")
        cursor = conn.cursor()

        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS PERSONS (
            id integer primary key,
            name varchar,
            image BLOB
            )'''
        )

        conn.commit()

        name = e1.get()
        image = e2.get()
        

        if name and image:
            image1 = convertToBinaryData(image)
            cursor.execute("SELECT * FROM persons WHERE image=?", (image1,))
            result = cursor.fetchone()
            if result:
                messagebox.showwarning("warning", "data already exists!")
                conn.close()
            else:
                insert = cursor.execute("INSERT INTO PERSONS (name, image) VALUES(?, ?)", (name, image1))
                conn.commit()
    
                if insert:
                    image = image.split("/")[-1]
                    messagebox.showinfo("success", f"{name} and {image} inserted!")
                    cursor.close()
    except sqlite3.Error as error:
        messagebox.showerror()("Error", error)
    finally:
        if conn:
            conn.close()


# Without scrrollbar show_all()
def show_all():
    top = tkinter.Toplevel()
    top.geometry("400x350")
    top.title("Persons")


    conn = sqlite3.connect("persondb.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM persons")
    persons = cursor.fetchall()
    i=0
    for row in persons:
        for j in range(len(row)-1):
            d=tkinter.Label(top, width=10, fg='blue', text=row[j], anchor='center')
            d.grid(row=i, column=j)

        img = Image.open(io.BytesIO(row[2]))
        img.thumbnail((80,80)) # resize the image to desired size
        img = ImageTk.PhotoImage(img)

        i1 = tkinter.Label(top,width=100,anchor='center')
        i1.grid(row=i, column=j+1)
        i1.image = img
        i1['image']=img

        b=Button(top, text='Delete', padx=12, command=lambda id=row[0], name=row[1]: delete(id, name))
        b.grid(row=i, column=j+2)
        i=i+1
        # img = Image.open(io.BytesIO(row[2]))
        # img.thumbnail((50,50)) # resize the image to desired size
        # img = ImageTk.PhotoImage(img)
        # tkinter.Label(top, text=row[1]).pack()
        # i1 = tkinter.Label(top)
        # i1.pack()
        # i1.image = img
        # i1['image']=img

# with scrollbar show_all()



def delete(id, name):
    m = messagebox.askyesnocancel("Delete??", f"Delete cred: id is {id} and name is {name}", icon='warning')
    if m:
        conn = sqlite3.connect("persondb.db")
        cursor = conn.cursor()
        deleteq = cursor.execute("DELETE FROM persons WHERE id ="+str(id))
        conn.commit()
        if deleteq:
            messagebox.showerror("Deleted", f"No of record deleted: {deleteq.rowcount}")
            conn.close()
            show_all()

l1 = tkinter.Label(win, text="Name")
l1.grid(row=0, column=0, sticky="e")
e1 = tkinter.Entry(win)
e1.grid(row=0, column=1)

l2 = tkinter.Label(win, text="Upload Image")
l2.grid(row=1, column=0, sticky="e")
e2 = tkinter.Entry(win)
e2.grid(row=1, column=1)
button_browse = tkinter.Button(win, text="Browse", command=upload_image)
button_browse.grid(row=1, column=2)

add_btn = tkinter.Button(win, text="Add Person", command=add_person)
add_btn.grid(row=2, column=1)

show_person = tkinter.Button(win, text="Show all persons", command=show_all)
show_person.grid(row=3, column=1)



win.mainloop()