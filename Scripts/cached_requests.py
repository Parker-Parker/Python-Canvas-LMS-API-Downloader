import datetime
import requests
import json


def request_cached(url_string, header=False):

    # Opening JSON file
    f = open('Downloads/cached_requests.json')
    cache = json.load(f)
    f.close()

    new_request = {}

    if url_string in cache:
        #Grab local copy
        print(f"retrieved cached copy of {url_string}")
        
        r = open(cache[url_string]["local_copy_location"])
        new_request = json.load(r)
        r.close()

    else:
        #Grab web copy
        print(f"retrieved web copy of {url_string}")

        if header == False:
            r = requests.get(url_string)
        else:
            r = requests.get(url_string, headers=header)


        new_request = r.json()
        #Add to cache

        new_cache_file_string = f'Downloads/JSON/{datetime.datetime.utcnow()}.json'
        with open(new_cache_file_string, "w") as outfile:
            json.dump(new_request, outfile)
            
        f = open('Downloads/cached_requests.json')
        cache = json.load(f)
        f.close()

        cache[url_string] = {"local_copy_location": new_cache_file_string}
        with open('Downloads/cached_requests.json', "w") as cache_file:
            json.dump(cache, cache_file)
          
    
    # f.close()

    return new_request



# # Opening JSON file
# f = open('Downloads/cached_requests.json')
 
# # returns JSON object as
# # a dictionary
# data = json.load(f)

# # # Closing file
# f.close()

# # Data to be written
# dictionary = {
#     "name": "fghddfgh",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9hjkgh70500"
# }

# # json_dict = {}
# data["exampleurl.com/api/getdeeznuts3"] = dictionary


# with open('Downloads/cached_requests.json', "w") as outfile:
#     json.dump(data, outfile)



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