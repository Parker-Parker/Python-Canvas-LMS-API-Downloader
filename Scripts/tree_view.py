# Python program to illustrate the usage
# of hierarchical treeview in python GUI
# application using tkinter

# Importing tkinter
from tkinter import * 
 
# Importing ttk from tkinter
from tkinter import ttk 
 





def create_dict_treeview(master, data):
    treeview = ttk.Treeview(master) 
    add_item_treeview(treeview, " ", data)
    return treeview

def add_dict_treeview(treeview, section_title, data):
    data = {}
    for key in data.keys():
        treeview.insert(section_title, 'end', key, text = key)
        add_item_treeview(treeview, key, data[key])
    

def add_item_treeview(treeview, section_title, data):
    data_s = f'TODO: implement handling for {data}'
    treeview.insert(section_title, 'end', data_s, text = data_s)
    #TODO: make this handle dictionaries, lists, etc
    

def reparent_treeview():
    #TODO: write method to reparent a treeview object through deepcopy
    pass



