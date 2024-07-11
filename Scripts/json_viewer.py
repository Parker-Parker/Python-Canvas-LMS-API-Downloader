import json
import threading
from tkinter import * 
from tkinter import ttk 
 


from cached_requests import request_cached
import tree_view


def new_window(data):
    x = threading.Thread(target=view_this, args=(data,))
    x.start()
    return x


def view_this(data):
   # Creating app window
    app = Tk()
    app.rowconfigure(0, weight=1)
    app.columnconfigure(0, weight=1)
    app.geometry("1000x1000")

    
    # Defining title of the app
    app.title("GUI JSON viewer ") 



    # print(json.dumps(data))

    tree_view.create_treeview(app,data)
     
    app.mainloop()

