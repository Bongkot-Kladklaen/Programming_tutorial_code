
#* RegEx in Python
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#* RegEx Functions
"""
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
"""
#* Metacharacters
"""
[]	A set of characters	                                                            "[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	    "\d"	
.	Any character (except newline character)	                                    "he..o"	
^	Starts with	                                                                    "^hello"	
$	Ends with	                                                                    "world$"	
'*	Zero or more occurrences	                                                    "aix*"	
+	One or more occurrences	                                                        "aix+"	
{}	Exactly the specified number of occurrences	                                    "al{2}"	
|	Either or	                                                                    "falls|stays"	
()	Capture and group	 
"""
#* Special Sequences
# www.w3schools.com

#* The findall() Function
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#* The search() Function
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#* The split() Function
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#* The sub() Function
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#* Match Object
"""
.span()     returns a tuple containing the start-, and end positions of the match.
.string     returns the string passed into the function
.group()    returns the part of the string where there was a match
"""
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())