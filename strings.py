name = "Sangeetha"
full_name = "jadamal sangeetha"

print(name.upper())  # this will change all the letters into uppercase 
print(name) # this will print same as what we had given because the the above line is not changing the actual variable

print(name.lower()) # this will cahnge all the letters into lowercase

print(name.find('S')) # this is to find anything in my string and this will return me the value of index 
print(name.find('n'))
print(full_name.find('s')) # the space has also an index value
#I can also find sub sting
print(full_name.find('jadamal'))

print(name.find('i'))# if it doesn't that cahracter in my string then this will result me -1

print(name.replace("Sangeetha", "geetha")) # replacing the name in the string 
#this will not change my original string
# I can also replace the character or substring in my string
print(name.replace("g", "G"))