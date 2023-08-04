
#lists
hajjats=["Rema","Hadijah","Haulah","Rahmah","Zaharah"]
print(hajjats[1])

#changing the value

hajjats[0]="Shifrah"
print(hajjats)
#add an item
hajjats.append("Rahmah")
print(hajjats)
#add to a certain item
hajjats.insert(2,"Bathel")
print(hajjats)
#remove
hajjats.remove("Rahmah")
print(hajjats)
#last element
print(hajjats[-1])

#new list
MOSQUE=["Red","Green","Blue","yellow","orange","purple","black"]

print(MOSQUE[2:5])

Country=["Uganda","Kenya","Rwanda","Tanzania"]
city=Country.copy()
print(city)

#loop through the list
for lady in Country:
    print(lady)

#Animal lists
animal=["dog","cat","rat","goat"]
ascend = sorted(animal)
print( ascend)

# Sort the animal names in descending order
order = sorted(animal, reverse=True)
print(order)



fname=["Shema","karole"]
other=["Rema","Cate"]

fullN=fname + other
print(fullN)

#Eladyercise 2
lady = ("samsung","iphone","tecno","redmi")
print(lady)
print(lady[1])
#print the secondlast element
print(lady[-2])
#update
me=list(lady)
me[1]="itel"
print(me)


year = lady + ("Huawei",)

print(year)

#loop through the turple
for whom in lady:
    print(whom)

#delete an item
tupling = lady[1:]

print(tupling)

#tuple constructor

Country_town= tuple(["Mbarara", "Kiboga", "Hoima", "Masaka", "Ntungamo"])

print(Country_town)

#unpack a turple
(Honey,Baby,Gone,Plus)=lady
print(Honey)
print(Baby)
print(Gone)
print(Plus)

#range 
man = lady[1:4]

print(man)

first_names = ("Cate", "Jane", "Daphine")
second_names = ("NaKatande", "Mirambe", "Mutyamba")

fullnames = first_names + second_names

print(fullnames)
# Create a tuple of colors and multiply it by 3

colors = ("red", "blue", "green")

multiplied_colors = colors * 3

print(multiplied_colors)

 #Number of times 8 appears in this tuple 
tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

count_8 = tuple.count(8)

print(count_8)
#Exercise 3
set = set(["BSSE", "CHS", "CHUSS"])

print(set)
#update
set.update(['COCIS', 'Senate'])

print(set)

MySet = {"oven","kettle","microwave","refrigerator"}
if "microwave" in MySet:
    print("The item exists")
else:
    print("The item doesn't exist")
    #remove an item
    MySet.remove("kettle")
    print(MySet)
    #loop
for my in MySet:
    print(my)

#Two sets

ages = {20, 22, 23}
first_names = {"Kato", "Wasswa", "David"}

set = ages.union(first_names)

print(set)
#xercise 4
aryan=10
toss = "Hello"

n = str(aryan) + toss

print(n)
#output the string
lady_t = "    Hello,       Uganda!       "
tell = lady_t.strip()
print(tell) 

#Convert the value of ‘tladyt’ to uppercase. 
print(lady_t.upper())
#Replaceing character ‘U’ with ‘V’
mum=lady_t.replace('U', 'V')

print(mum)
#Range
y = "I am proudly Ugandan"
rank=y[1:4]
print(rank) 

lady = 'All "Data Scientists" are cool!'
print(lady)

#Eladyercise 5
#shoe size
Shoes = {"brand" : "Nick",  "color" : "black",  "size" : 40  }
print(Shoes["size"])

#Change the value “Nick” to “Adidas” 
Shoes["brand"]="Nick"
print(Shoes["brand"])



#Add a key
Shoes["type"]="sneakers"
print(Shoes["type"])

#return keys
mane=Shoes.keys()
print(mane)
#return values
stuart=Shoes.values()
print(stuart)
 
#checking the size
if "size" in Shoes.keys():
    print("Get the size")
else:
    print("Not available")

    #removing a certain item
    del Shoes["color"]
print(Shoes)
 


    #looping through
for rate in Shoes:
        print(rate)

for rat in Shoes.values():
        print(rat)


for rate, rat in Shoes.items():
    print(rate, ":", rat)

#Empty the Shoes
del Shoes
    
    #Copy of Dictionary
student = {
  "name": "Fatuma",
  "Getter": "Penalty",
  "year": 2024
}
first=student.copy()
print(first)

