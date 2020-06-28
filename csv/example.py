import csv


"""Example_1: reader"""
# read file posts.csv
# f = open("posts.csv", "r")
# reader = csv.reader(f)
# for line in reader:
#     print(line)
# f.close()


"""Example_2: reader"""
# print the first line
# f = open("posts.csv", "r")
# reader = csv.reader(f)
# print(reader.__next__())
# f.close()

"""Example_3: reader"""
# replace delimiter . with ?

# f = open("posts.csv", "r")
# reader = csv.reader(f, delimiter="?", skipinitialspace=True)
# for line in reader:
#     print(line)
# f.close()


"""Example_4: reader"""
# add '2 spaces' between columns
# f = open("posts.csv", "r")
# reader = csv.reader(f, delimiter="?", skipinitialspace=True)
# for line in reader:
#     print(line)
# f.close()


"""Example_5:DictReader"""
# # read  value with header(first row id header isn't specified) from  posts.csv
# f = open("posts.csv", "r")
# reader = csv.DictReader(f)
# for line in reader:
#     print(line)
# f.close()


"""Example_6:DictReader"""
# read  'body' from  posts.csv
# f = open("posts.csv", "r")
# reader = csv.DictReader(f)
# for line in reader:
#     print(line['title'])
#     # print(line['body'])
# f.close()


"""Example_7:DictReader"""
# if .csv doesn't have header, header element can be specified as 'fieldnames'
# f = open("posts_ex_7.csv", "r")
# reader = csv.DictReader(f, fieldnames=["title", "body", "author"])
# for line in reader:
#     print(line['title'])
#     # print(line['body'])
# f.close()


"""Example_8"""
#  read from posts.csv => write in output.csv file
f = open("posts.csv", "r")
output_f = open("output.csv", "w")
reader = csv.reader(f)
writer = csv.writer(output_f)
# writer = csv.writer(output_f, delimiter = "?")
for row in reader:
    print(row)
    writer.writerow(row)

f.close()




