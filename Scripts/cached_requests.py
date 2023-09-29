import requests
import json






# Opening JSON file
f = open('Downloads/cached_requests.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

# # Closing file
f.close()

# Data to be written
dictionary = {
    "name": "fghddfgh",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9hjkgh70500"
}

# json_dict = {}
data["exampleurl.com/api/getdeeznuts3"] = dictionary


with open('Downloads/cached_requests.json', "w") as outfile:
    json.dump(data, outfile)



# //////////////////////////////////////////////////
# //////////////////////////////////////////////////
# //////////////////////////////////////////////////
 
# # Opening JSON file
# f = open('data.json')
 
# # returns JSON object as
# # a dictionary
# data = json.load(f)
 
# # Iterating through the json
# # list
# for i in data['emp_details']:
#     print(i)
 
# # Closing file
# f.close()

# # //////////////////////////////////////////////////
# # //////////////////////////////////////////////////
# # //////////////////////////////////////////////////

 
# # Data to be written
# dictionary = {
#     "name": "sathiyajith",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9976770500"
# }
 
# # # Serializing json
# # json_object = json.dumps(dictionary, indent=4)
 
# # # Writing to sample.json
# # with open("sample.json", "w") as outfile:
# #     outfile.write(json_object)

# with open("sample.json", "w") as outfile:
#     json.dump(dictionary, outfile)