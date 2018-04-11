import requests


# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response.
print(response.status_code)

# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)


#The above code prints:

# (HelloPipRequests-hbC3-s8j) ➜  HelloPipRequests python3 test.py
# 200
# <class 'dict'>
# {'message': 'success', 'request': {'altitude': 100, 'datetime': 1523378411, 'latitude': 37.78, 'longitude': -122.41, 'passes': 5}, 'response': [{'duration': 526, 'risetime': 1523388959}, {'duration': 639, 'risetime': 1523394668}, {'duration': 547, 'risetime': 1523400534}, {'duration': 472, 'risetime': 1523406436}, {'duration': 559, 'risetime': 1523412254}]}
# (HelloPipRequests-hbC3-s8j) ➜  HelloPipRequests 