#comma separated key value pairs enclosed with {}
# {key1:value1, key2:value2,........}

# groceries ={'milk': 60, 'biscuits':20,'rice':30,'bread':20}
# print(groceries)
# print(type(groceries))
# print(len(groceries))
#
# # does not have indexing
# print(groceries['bread'])
#
# groceries['rice'] = 20
# print(groceries)


#operation in Dictionary

# student1 = {"math": 80,"science":70,"history":9}
# print(student1)
# print(student1["math"])
# print(student1["science"])
#
# #get()
# print(student1.get("Biology")) # provide none function if key is not present
#
# emp1 = {'id':1001,'name':'john', 'salary': 10000}
# print(emp1)
#
# # membership operator
# print(1001 in emp1)
# print('name' in  emp1)

#
# sem1_marks = {'math':78,'science':70,'history':9}
# print(sem1_marks)
# sem1_marks.update({'Biology':78})
# print(sem1_marks)
#
# groceries_1 = {'milk':60,'rise':100,'biscuits':200}
# groceries_2 = {'milk':100,'rise':200,'biscuits':20}
#
# print(groceries_1)
# groceries_1.update(groceries_2)
# print(groceries_1)
#
# #pop()
# groceries_1.pop('rise')
# print(groceries_1)
#
# #clear()
# groceries_1.clear()
# print(groceries_1)
#
# groceries_1.update(groceries_2)
# print(groceries_1)
#
# groceries_3 = {'milk':60,'rise':100,'biscuits':200,'milk':300}
# print(groceries_3)
# #keys cannot be duplicated its add mostly adds recent value

# keys and values of dictionary
d1 = {1:True, 2:False, 0:False}
print(d1)

# not allowed - list,set
# allowed key - str, int, float, bool, tuple

# not allowed - list,set,dict = > mutable datatypes
#allowed keys - str,int,float,bool,tuple = > immutable datatypes







