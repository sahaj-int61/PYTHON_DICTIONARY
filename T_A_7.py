"""
Dictionaries can have nested data too. Also, you can add a new key to a
dictionary as they are mutable (changeable). Try to add the key "work"
to dict with values shown below.

.get() method can be used just to get the value of a key. But it has more
tricks up its sleeve. 
Try to look for key: "son's age" and if nothing comes up make the .get()
return "2"

Date: 18/01/24
"""

dict= {"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
#Type your answer below.
age = dict.get("son's age", "2")
print(age)