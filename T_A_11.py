"""
Dictionaries can have nested data too. Also, you can add a new key to a
dictionary as they are mutable (changeable). Try to add the key "work"
to dict with values shown below.

What's the key with the lowest value in the dictionary

Date: 18/01/24
"""

dict= {"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
#Type your answer below.
my_dict = {}
for key,value in dict.items():
    if isinstance (value,int):
        my_dict[key] = value
min_key=min(my_dict, key=my_dict.get)
print(min_key)
