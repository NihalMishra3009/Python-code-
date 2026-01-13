#String and its function s in Python

# Generally there are 3 type of string in python
# 1. Single Quote
str1 = "THis is string"
# 2. Double Quote
str2 = 'This is also string'
# 3. Triple Quote
str3 = """This is also a new type of string"""




# escape sequence character
str4 = "This is my String.\n we are creating it in python " # \n is used to give new line
print (str4)

str5 = "This is my String.\t we are creating it in python " # \t is used to give tab space
print (str5)

#Basic Operations on String
# String Concatination
str1 = "Hello "
print(len(str1)) # to find length of string
str2 = "Nihal"
length = len(str2)
print (length)

Finalstr = (str1+" "+str2)
print (Finalstr) # Hello Nihal
print ("Total length of str1 and str 2 :",len(Finalstr))





# Indexing in String
str = "PythonProgramming"
ch = str[3]# it will give character at index 3
print (ch)

str7 = "Nihal Mishra"
print(str7[8])





# Slicing in String
str8 = "HelloWorld"
sub_str = str8[1:5] # it will give substring from index 0
print(sub_str)





#negative indexing
str9 = "PythonProgramming"
ch = str9[-4] # it will give 4th character from last
print (ch)
sub_str2 = str9[-7:-1] # it will give substring from index -7 to -1
print (sub_str2)




#String Functions
str = "i am Studing Python Programming Language"


#Endswith function
print(str.endswith("age")) # it will return true if string ends with given substring else false
print(str.endswith("ts")) # it will return count of given substring in string

#Capitalize function
print (str.capitalize()) # it will capitalize first character of string
str = str.capitalize()
print (str)

#Replace function
str10 = "I love Python. Python is great."
print (str10.replace("Python", "Java")) # it will replace all occurrence of given substring with new substring  

#Find function
print (str10.find("i")) # it will return starting index of given substring else -1 if not found
print (str10.find("Java")) # it will return -1 as substring not found

#Count function
print (str10.count("t")) # it will return count of given substring in string
print (str10.count("Python")) # it will return count of given substring in string

