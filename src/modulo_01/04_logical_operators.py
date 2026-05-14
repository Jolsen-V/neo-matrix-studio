# Module 01: lesson 04

#======== logical operators ========

# topic: AND operator
print(True and True)  # True
print((20+5) and (5**2)) # True

print(True and False)  # False
print((10%3) and (20//6)) #false


#topic: OR operator 
print(True or False)   # True 
print((8**2) or (4**3)) # True

print(False or False) # False
print((10>43) or (0.5 < 0.1)) # False


#topic: NOT operator 
print(not True)  # False
print(not (322 >54))  # False

print(not False) # True
print(not (84 < 23)) # True 


# PRACTICE AND COMBINATION 

dni = 4982393
name = True
print(dni <= 5938948 and name )
print(dni > 5938948 or name)