import requests


"""Example_1: GET  """
def getSummary(users):
    result = {}
    for user in users:
        result[user['id']] = user['name'] + " , " + user['phone']
    return result


# GET on API's
response = requests.get("http://jsonplaceholder.typicode.com/users", timeout = 4)
print(response.ok)

#  print response json format as a string
print(response.text)

# convert response into JSON object.Print list where individual element in JSON format]
users_list = response.json()
# print(users_list)

# check if the response is successful
if (response.ok):
    summary = getSummary(users_list)
    print(summary)
else:
    print("some error happened", response.status_code)


"""Example 2: GET"""
# # make getSummary() more configurable
def getSummary(users, keys):
    result = {}
    for user in users:
        #  save corresponding values as ['name', 'email', 'phone', 'website'] in valueList
        valueList = []
        for key in keys:
            valueList.append(user[key])
        result[user['id']] = valueList
    return result

response = requests.get("http://jsonplaceholder.typicode.com/users", timeout = 4)
users_list = response.json()

if (response.ok):
    summary = getSummary(users_list, ['name', 'email', 'phone', 'website'])
    print(summary)
else:
    print("some error happened", response.status_code)


"""Example_3: POST"""
post = {"userId":1, "title": "my title example", "body": "this is post body"}

response = requests.post("http://jsonplaceholder.typicode.com/posts", data=post)
print(response.text)
