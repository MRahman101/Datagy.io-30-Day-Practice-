

print('Welcome to Online IDE!! Happy Coding :)')
Replit_john56 = "sup"
print(Replit_john56)
print(20 % 3)


def john():
  print("John Cena")


john()


def color(x):
  print("my favorite color is   " + x)


color("sunshine")


#This does calculations
def add_nums(x, y):

  mod = x % y
  print(x + y)
  print(mod)


add_nums(35, 20)

# help(add_nums) --> This helps describe what python function does.

#Building A Python Top Calculator 
def tip_calc(princip, tipcent):
  return princip*tipcent
  
  #you could use the return keyword by itself for the function in some cases.  
tip_calc(10.99,.15)

#Day 4:
x = True
print(type(x))
#This will show bool value of a value:
print(bool("Sup"))
#The folllowing will use operators to determine if a paramenter in a function is met. 
def can_drive(age):
    return age >= 16
print(can_drive(33))
