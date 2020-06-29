"""Example_1:Lambda"""
# anonymous function
# def power(a,b):
#     return a ** b
#
# # 1st way to call lambda func
# print((lambda a,b : a ** b)(2,3))
#
# # 2nd way to call lambda func
# power_func = lambda a,b : a ** b
# print(power_func(3,2))


"""Example_2:Lambda"""
# def func(num_of_iteration, add_func):
#     for i in range(num_of_iteration):
#         print(i, add_func(i,i))
#
# func(5,lambda x,y : x + y )


"""Example_3: Filter"""
# Filter function => design for iterating over the list + applying function to each element and
# filter the list based on condition
# num_list = [12,45,2,6,90,13,17]
# filtered_list = list(filter(lambda x: x > 20, num_list))
# print(filtered_list)


"""Example_4: Map"""
# # Map => take the list , apply the func and return the list
# num_list = [2,6,9,11,13]
# mapped_list = list(map(lambda x : x+2, num_list))
# print(mapped_list)

"""Example_5:Reduce"""
# The reduce() function accepts a function and a sequence and returns a single value calculated
import functools

# num_list = [1,2,3,4,5]
# # 10 - is an initial value, can be removed
# res = functools.reduce((lambda x,y : x * y), num_list, 10)
# print(res)

"""Example_6: Map + Filter"""
num_list = [2,3,4,7,8,3]
res = list(filter(lambda x: x < 20 , list(map(lambda x : x ** 2, num_list))))
print(res)


"""Example_7:"""
num_list = [2,3,4,7,8,3]
res = functools.reduce(lambda x,y : x + y,  list(filter(lambda x: x < 20 , list(map(lambda x : x ** 2, num_list)))))
print(res)