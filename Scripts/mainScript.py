import json
import requests

from cached_requests import request_cached





# Opening JSON file
f = open('Downloads/cached_requests.json')
cache = json.load(f)
f.close()


















print(request_cached("http://ip-api.com/json/23.43.252.19"))



















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




















