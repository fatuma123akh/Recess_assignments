# Exception Handling
try:
  print(word)
except NameError:
  print("The variable word is not defined")
except:
  print("Their's something else wrong")



# FILE HANDLING
filename = "work.txt"
f = open(filename,"wt")
# Write on the file
f.write("Now our file has some work on it")

# Close our file
f.close()