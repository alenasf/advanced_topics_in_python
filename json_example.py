import json


"""Example_1: Using JSON with Python

json.loads(convert JSON string into Python dict)
json.load(convert JSON file into Python dict)

json.dumps(convert Python dict into JSON string)
json.dump(convert Python dict into JSON file)
"""

# open the file example.json. Convert JSON file to dict
f = open("example.json")
# load and print the data from example.json file
print(json.load(f))

# save data as var 'json_data'.
json_data = json.load(f)
print(type(json_data))


"""Example_2:"""
# GET List of the countries.Convert JSON file to dict
f = open("example.json")
json_data = json.load(f)
countries = json_data['countries']
# print(countries)
# loop for all countries
for country in countries:
    print(country)

# print individual country
for country in countries:
    print(country['name'], country['capital'])


"""Example_3"""
# Convert JSON string to dict
json_string = '''
    {
  "countries" : [
      {

       "name": "usa",
        "capital": "Washington",
        "west": true

      },
      {

       "name": "canada",
        "capital": "Ottava",
        "west": true

      },
    {
       "name": "japan",
        "capital": "Tokyo",
        "west": false
    }
    ]

    }
'''

json_data = json.loads(json_string)
countries = json_data['countries']
for country in countries:
    print(country['name'],country['capital'])


"""Example_4"""
# Convert Python dict to JSON string
json_string = '''
    {
  "countries" : [
      {

       "name": "usa",
        "capital": "Washington",
        "west": true

      },
      {

       "name": "canada",
        "capital": "Ottava",
        "west": true

      },
    {
       "name": "japan",
        "capital": "Tokyo",
        "west": false
    }
    ]

    }
'''
json_data = json.loads(json_string)
json_string_from_dict = json.dumps(json_data, indent=4, sort_keys=True)
print(json_string_from_dict)


"""Example_5"""
# Convert Python dict to JSON file dump.json
json_string = '''
    {
  "countries" : [
      {

       "name": "usa",
        "capital": "Washington",
        "west": true

      },
      {

       "name": "canada",
        "capital": "Ottava",
        "west": true

      },
    {
       "name": "japan",
        "capital": "Tokyo",
        "west": false
    }
    ]

    }
'''
json_data = json.loads(json_string)
f = open("dump.json", "w")
json.dump(json_data, f, indent=4, sort_keys=True)









