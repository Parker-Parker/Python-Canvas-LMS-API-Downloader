import json
import requests

# Importing tkinter
from tkinter import * 
 
# Importing ttk from tkinter
from tkinter import ttk 
 


from cached_requests import request_cached
import tree_view



# Opening JSON file
f = open('Downloads/cached_requests.json')
cache = json.load(f)
f.close()

# Creating app window
app = Tk()
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)
app.geometry("1000x1000")

 
# Defining title of the app
app.title("GUI JSON viewer ") 




print(cache)
tree_view.create_treeview(app,cache)
 
# Calling main() 
app.mainloop()

#print(request_cached("http://ip-api.com/json/23.43.252.19"))



















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




















