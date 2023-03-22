

print('Welcome to Online IDE!! Happy Coding :)')
Replit_john56 = "sup"
print(Replit_john56)
print(20 % 3)


def john():
  print("John Cena")


john()


def color(x):
  print("my favorite color is " + x)


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
#This compared letters toeach other by their ASCII values. 
x = 'a' > 'A'
print(x)
#This will tell you the ASCII value of a String. 
print(ord('b'))
#operators can be combined with logical operators
print(1 > 2 or 10 > 5)
#if and else can ba used to control flow of the program. 
def legal_age(age):
  if (age>18):
    print("They are   legal age ")
  elif (age<18):
    print("They are underaged")
  else:
    print("they are 18 and legal") 
  
legal_age(45) 
legal_age(18)
legal_age(13)

def hurry_out_of_bed(overslept, workday):
    if overslept and workday:
        print('HURRY! Get out of bed!')
    elif not overslept and not workday:
        print("Keep sleeping!")
    else:
        print("You're ok!")

hurry_out_of_bed(True, False)

x = [5]
y = [5]
print(x is y)
print(id(x))
print(id(y))
#practice problem ahead
def incr(sal):
  if (sal<100000):
    print("No raise!")
  elif (100000<sal<150000):
    print("You get a raise of 2.5K!")
  else:
    print("You get a $5K raise!")
incr(500000)
#for loop example below
for name in range(3):# main syntax: for ___ in range()
  print("john")
# this can be used to print items in an array
namez = ['joe', 'sam', 'jake', 'sarah']
for name in namez:
  print(name) 
  #you can also use if statements in a for loop
for number in range(5): #this prints multiplies of 3. 
    if number % 3 == 0:
        print(number)
    else: #else is not needed for this for loop
        pass 
# An example of a nested for loop
for item in [1, 2]:
    print(item)
    for subitem in ['a']:
        print(subitem)

