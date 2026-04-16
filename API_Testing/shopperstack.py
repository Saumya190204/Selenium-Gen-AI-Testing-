""" Task1 : Perform API Testing for the ShopperStack
1. Post a request to register a user
2. Post a request to login the user
3. Get a request to get the user  """
# import requests
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# # post request to register a user
# def register():
#     payload = {
#     "city": "Jaipur",
#     "country": "India",
#     "email": "saumy23411@gmail.com",
#     "firstName": "Rohan",
#     "gender": "MALE",
#     "lastName": "Verma",
#     "password": "123557876",
#     "phone": 9876573242,
#     "state": "Rajasthan",
#     "zoneId": "ALPHA"
#     }
#
#     response = requests.post("https://www.shoppersstack.com/shopping/shoppers", json=payload,verify=False) # verify = False to pass SSl certificate
#     print(response.text)
#     # checking the status code
#     assert response.status_code==201, "Register failed"
#     print("User Registered with status code 201")
#     return response.json()['data']['userId'] # returning the userId
#
# userId = register()
#
# # post request to log in
# def login():
#     payload = {
#     "email": "saumy23411@gmail.com",
#     "password": "123557876",
#     "role": "SHOPPER"
#     }
#     # making the request
#     response = requests.post("https://www.shoppersstack.com/shopping/users/login", json=payload,verify=False)
#     # printing the response
#     print(response.text)
#     # checking the status code
#     assert response.status_code==200, "login Failed"
#     return response.json()['data']['jwtToken'] # returning the jwtToken
#
# Token = login()
#
# #setting up the bearer token for authorization
# headers = {
#     "Authorization": "Bearer " + Token
# }
#
# # get request to fetch user
# # making the request
# response = requests.get("https://www.shoppersstack.com/shoppers/userId",headers=headers,verify=False)
# #printing the response
# print(response.text)
# # checking status code
# assert response.status_code==200, "Failed"
















#
# import requests
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# base_url = "https://www.shoppersstack.com/shopping"
# session = requests.Session()
# payload = {
#     "city": "Jaipur",
#     "country": "India",
#     "email": "sa03@gmail.com",
#     "firstName": "Rohit",
#     "gender": "MALE",
#     "lastName": "Verma",
#     "password": "9982",
#     "phone": 9630458412,
#     "state": "Rajasthan",
#     "zoneId": "ALPHA"
# }
# response=session.post(f"{base_url}/shoppers",
#     json=payload,
#     verify=False)
# print(response.text)
#
# # #Checking status code
# assert response.status_code == 201, "Register failed"
#
# print("User Registered with status code 201")
#
# user_id = response.json()['data']['userId']
# print("User ID:", user_id)
#
# #
# #
# #
# #
# # post request to log in
# def login():
#     payload1= {
#     "email": "sa03@gmail.com",
#     "password": "9982",
#     "role": "SHOPPER"
#     }
#     # making the request
#     response1 = session.post(f"{base_url}/users/login",
#                             json=payload1,
#                             verify=False)
#     print(response1.text)
#     assert response1.status_code==200, "login Failed"
#     return response1.json()['data']['jwtToken'] # returning the jwtToken
#
# Token = login()
#
# #
# #
# headers = {
#     "Authorization": "Bearer " + Token
# }
# # # GET request using base_url variable
# response = session.get(
#     f"{base_url}/shoppers/{user_id}",
#     headers=headers,
#     verify=False
# )
#
# print(response.text)
# print(response.status_code)
#
# # Checking status code
# assert response.status_code == 200, "Failed"
#
# print("Request successful")

















import requests
import urllib3

# Hide SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Base URL
base_url = "https://www.shoppersstack.com/shopping"

# Create session
session = requests.Session()

# Register payload
payload = {
    "city": "Jaipur",
    "country": "India",
    "email": "sa032@gmail.com",
    "firstName": "Rohit",
    "gender": "MALE",
    "lastName": "Verma",
    "password": "99825",
    "phone": 9430458412,
    "state": "Rajasthan",
    "zoneId": "ALPHA"
}

# Register shopper
response = session.post(
    f"{base_url}/shoppers",
    json=payload,
    verify=False
)

print("Register Response:")
print(response.text)
print("Register Status Code:", response.status_code)

# Check registration success
assert response.status_code == 201, "Register failed"

print("User Registered Successfully")

# Fetch user ID
user_id = response.json()['data']['userId']
print("Fetched User ID:", user_id)


# Login function
def login():
    payload1 = {
        "email": "sa032@gmail.com",
        "password": "99825",
        "role": "SHOPPER"
    }

    response1 = session.post(
        f"{base_url}/users/login",
        json=payload1,
        verify=False
    )

    print("\nLogin Response:")
    print(response1.text)
    print("Login Status Code:", response1.status_code)

    assert response1.status_code == 200, "Login Failed"

    return response1.json()['data']['jwtToken']


# Fetch token
Token = login()
print("Fetched Token:", Token)

# Authorization header
headers = {
    "Authorization": "Bearer " + Token
}

# Get shopper details using user ID
response3 = session.get(
    f"{base_url}/shoppers/{user_id}",
    headers=headers,
    verify=False
)

print("\nGet Shopper Details Response:")
print(response3.text)
print("Get Shopper Details Status Code:", response3.status_code)

# Check GET request success
assert response3.status_code == 200, "Failed"

print("Request successful")