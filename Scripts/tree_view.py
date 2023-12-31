# Python program to illustrate the usage
# of hierarchical treeview in python GUI
# application using tkinter

# Importing tkinter
from tkinter import * 
 
# Importing ttk from tkinter
from tkinter import ttk 
 





def create_treeview(master:Tk, data):
    treeview = ttk.Treeview(master)
    treeview.grid(row=0,column=0,sticky="nsew")
    add_item_treeview(treeview, "", data)
    return treeview

def add_dict_treeview(treeview:ttk.Treeview, section_title:str, data:dict):
    for key in data.keys():
        treeview.insert(section_title, 'end', section_title+key, text = key)
        add_item_treeview(treeview, section_title+key, data[key])
    
def add_list_treeview(treeview:ttk.Treeview, section_title:str, data:list):
    index = 0
    for item in data:
        treeview.insert(section_title, 'end', section_title+str(index), text = f'[{index}]')
        add_item_treeview(treeview, section_title+str(index), item)
        index+=1

def add_item_treeview(treeview:ttk.Treeview, section_title:str, data):
    if isinstance(data, dict):
        add_dict_treeview(treeview,section_title,data)
    elif isinstance(data, list):
        add_list_treeview(treeview,section_title,data)
    else:
        # data_s = f'TODO: implement handling for {data}'
        data_s = f'{type(data)}:{data}'
        treeview.insert(section_title, 'end', section_title+data_s, text = data_s)
        #TODO: make this handle dictionaries, lists, etc



    
    

def reparent_treeview():
    #TODO: write method to reparent a treeview object through deepcopy
    pass



