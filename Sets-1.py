#Operations on sets
#The set we are to work on
clients= {"Rahmah","Tiffah","Djamillah","Djalia"}
#To find the length of a set
print(len(clients))
#How to access an element of a set

client_list=list(clients)
print(client_list[1])
clients=set(client_list)
print(clients)
#Add items in a set
clients.add("Fridausi")
print(clients)
#Removing an element
clients.remove("Rahmah")
print(clients)
#Checking for the datatype of your set
print(type(clients))
# Adding two sets together
customers = {"Mutumba","Katende","Gafabusa"}
all_users= clients.union(customers)
print(all_users)