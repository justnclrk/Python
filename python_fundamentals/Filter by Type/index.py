#Write a program that, given some value, tests that value for its type. Here's what you should do for each type:
#Integer
#If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
sI = 45
bI = 200
if sI <= 100:
    print "That's a small number!"
else:
    print "That's a big number!"     
if bI >= 100:
    print "That's a big number!"
else:
    print "That's a small number!"    
#String
#If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
sS = "Rubber baby buggy bumpers"
bS = "Experience is simply the name we give our mistakes"
if len(sS) <= 50:
    print "Short sentence."
else:
    print "Long sentence."
if len(bS) >= 50:
    print "Long sentence."
else:
    print "Short sentence."
#List
#If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
aL = [1,7,4,21]
bL = [3,5,7,34,3,2,113,65,8,89]
if len(aL) <= 10:
    print "Short list."
else:
    print "Big list!"
if len(bL) >= 10:
    print "Big list!"
else:
    print "Small list."