#To understand regular expression more use (Regular expression.txt) file

import re

mystr= "Tata limited Dr. David lannnnndsman, executive Director 18, Grosvenor place london SWIX 7HSc Phone: +91 88500 8727 Email: tatata@tata.co.uk website: www.europe.tata.com Directions: View map"
a=re.search("tata",mystr) #It searches a particular element in a string
print(a)    
x=re.search("^Tata.*map$",mystr) #It represents start and last of string
print(x)
if x:
    print("Yes, it is there")
else:
    print("It is not there")

y=re.split("tata",mystr) #split returns a list where the string has been split at each match
print(y)

z=re.sub("tata","shubh",mystr) #sub replaces one or many matches with a string
print(z)

b=re.findall("Direc",mystr) #It returns a list containing all matches
print(b)

#patt=re.compile(r'tata')
#print(patt)
#patt=re.compile(r'.')
#patt=re.compile(r'.vid')
#patt=re.compile(r'^Tata')
#patt=re.compile(r'ap$')
#patt=re.compile(r'an*')
#patt=re.compile(r't*a*d*c*')
#patt=re.compile(r'an+')
#patt=re.compile(r'ta+')
#patt=re.compile(r'ta{1}')
#patt=re.compile(r'(ta){1}')
#patt=re.compile(r'ta{1}|David')

#Special sequences
#patt=re.compile(r'\ATata')
#patt=re.compile(r'\Btata')
#patt=re.compile(r'\bmap')
#patt=re.compile(r'\d')
#patt=re.compile(r'\D')
#patt=re.compile(r'tata\b')
#patt=re.compile(r'\s')
patt=re.compile(r'\d{5} \d{4}')
matches = patt.finditer(mystr)
#print(matches)
for i in matches:
    print(i)


str="+918850093749, +918424898318, +4 9867 8345 +919167934017"
pattern=re.compile(r'[+]\d[91]\d{10}')
mat=pattern.finditer(str)
for i in mat:
    print(i)

str="+918850093749, +918424898318, +4 9867 8345 +919167934017"
pattern=re.compile(r'\+91+\d{10}')
mat=pattern.finditer(str)
for i in mat:
    print(i)
# findall, search, split, sub, finditer

mine = "I love you Bappa88$ Batta Potter Goat Batter"
put=re.compile(r'l+')
mat=put.finditer(mine)
for j in mat:
    print(j)