
import json
from cached_requests import request_cached
import json_viewer



f = open('Downloads/cached_requests.json')
data = json.load(f)
f.close()
json_viewer.new_window(data)

data = request_cached("http://ip-api.com/json/23.43.252.19")
json_viewer.new_window(data)

data = request_cached('https://api.github.com/events')
json_viewer.new_window(data)







# ////////////////////////////////////////////////////////////////
# ////example treeview with lib////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
    # import json
    # from cached_requests import request_cached
    # import json_viewer



    # f = open('Downloads/cached_requests.json')
    # data = json.load(f)
    # f.close()
    # json_viewer.new_window(data)

    # data = request_cached("http://ip-api.com/json/23.43.252.19")
    # json_viewer.new_window(data)

    # data = request_cached('https://api.github.com/events')
    # json_viewer.new_window(data)







# ////////////////////////////////////////////////////////////////
# ////example treeview window////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////


    # import json
    # import requests

    # # Importing tkinter
    # from tkinter import * 
    
    # # Importing ttk from tkinter
    # from tkinter import ttk 
    


    # from cached_requests import request_cached
    # import tree_view




    # # Creating app window
    # app = Tk()
    # app.rowconfigure(0, weight=1)
    # app.columnconfigure(0, weight=1)
    # app.geometry("1000x1000")

    
    # # Defining title of the app
    # app.title("GUI JSON viewer ") 




    # # # sample data

    # # f = open('Downloads/cached_requests.json')
    # # data = json.load(f)
    # # f.close()

    # data = request_cached("http://ip-api.com/json/23.43.252.19")

    # # data = request_cached('https://api.github.com/events')

    # # # end sample data

    # print(json.dumps(data))

    # tree_view.create_treeview(app,data)
    
    # # Calling main() 
    # app.mainloop()

    # #print(request_cached("http://ip-api.com/json/23.43.252.19"))


# ////////////////////////////////////////////////////////////////
# ////example api calls////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////


    # # r = requests.get('https://api.github.com/events')
    # # print("\n===newline===\n")
    # # print(r.text)

    # # print("\n===newline===\n")
    # # print(r.json()[])

    # # print("\n===newline===\n")
    # # print(r.json())
    # # print("\n===newline===\n")
    # # print(json.dumps(r.json(),indent=2))
    # # print("\n===newline===\n")





    # r = requests.get('https://api.github.com/events')
    # rj = r.json()

    # print(r.headers)

    # print(len(rj))       # <-- List
    # print("\n\n\n") 

    # walmart_IP = "23.43.252.19"
    # geo_data = requests.get(f'http://ip-api.com/json/{walmart_IP}').json()
    # print(geo_data.keys())             # <-- object
    # print(geo_data["status"])




    # # http://ip-api.com/json/23.43.252.19




















