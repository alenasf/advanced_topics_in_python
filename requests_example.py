import requests

"""Example_1"""
response_data = requests.get("http://www.facebook.com")
print(response_data.status_code)
if response_data.status_code >=200 and response_data.status_code<400:
    print("success")

# property 'ok' validate the If statement
response_data = requests.get("http://www.facebook.com")
print(response_data.ok)

# print response from the request
print(response_data.text)

# print bite representation(images)
print(response_data.content)

# print header from the response
print(response_data.headers['content-type'])

# help function
print(help(response_data))


"""Example_2"""
# GET on URL to image (bites)
response_data = requests.get("https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_960_720.jpg")
print(response_data.content)
# insert bites into a file
f = open("my_image.jpeg", "wb")
f.write(response_data.content)
