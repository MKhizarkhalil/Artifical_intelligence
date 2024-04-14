#I. a Python program to square and cube every number in a given list of integers using Lambda.
list = [1,2,3,4,5,6,7,8,9,10]

square =lambda a:a*a
cube =lambda a:a*a*a

for i in list:
   print( square(i), cube(i))


#II. a Python program to find if a given string starts with a given character using Lambda.     

string ="my name is khizar"
character ="m"
b=lambda  ch : print(ch ,"is given character") if string[0]==ch else print("is not given character")
b(character)


#III. a Python program to extract year, month, date and time using Lambda.
import datetime




extract_info = lambda dt: (dt.year, dt.month, dt.day, dt.time())
year, month, day, time = extract_info( datetime.datetime.now())


print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Time:", time)


