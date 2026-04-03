import requests
# response=requests.get("https://petstore.swagger.io/v2/store/inventory")
# print(response.text)
# print(response.status_code)
# print(response.json())
# a=response.json()
# print(a['available'])
# expected=200
# actual=response.status_code
# assert actual==expected,"Error Found"
# payload={
#   "id": 800,
#   "category": {
#     "id": 0,
#     "name": "string"
#   },
#   "name": "Lion",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 60,
#       "name": "string"
#     }
#   ],
#   "status": "available"
# }
# response=requests.post("https://petstore.swagger.io/v2/pet",json=payload)
# actual=200
# expected=response.status_code
# assert actual==expected,"ERROR FOUND"
# print(response.json())
# payload1={
#   "id": 1800,
#   "category": {
#     "id": 0,
#     "name": "string"
#   },
#   "name": "Tiger",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 70,
#       "name": "string"
#     }
#   ],
#   "status": "available"
# }
# res1=requests.put("https://petstore.swagger.io/v2/pet",json=payload1)
# print(res1.status_code)
# print(res1.json())


# res2=requests.delete("https://petstore.swagger.io/v2/pet/1800")
#
# res3=requests.get("https://petstore.swagger.io/v2/pet/1800")
# print(res3.status_code)
# print(res3.text)


# def post():
#     payload = {
#         "id": 800,
#         "category": {
#             "id": 0,
#             "name": "string"
#         },
#         "name": "Lion",
#         "photoUrls": [
#             "string"
#         ],
#         "tags": [
#             {
#                 "id": 60,
#                 "name": "string"
#             }
#         ],
#         "status": "available"
#     }
#     response = requests.post("https://petstore.swagger.io/v2/pet", json=payload)
#     # print(response.status_code)
#     #print(response.json())
#     a=response.json()
#     id1=a["id"]
#     #print(id1)
#     return id1
#
# id2=post()
#
#
#
#
# def get():
#     res1=requests.get(f"https://petstore.swagger.io/v2/pet/{id2}")
#     print(res1.status_code)
#     print(res1.text)
#
# def delete():
#     res2 = requests.delete(f"https://petstore.swagger.io/v2/pet/{id2}")
#     print(res2.status_code)
#     print(res2.json())
#
# post()
# get()
# delete()





