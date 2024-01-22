"""
Dictionaries can have nested data too. Also, you can add a new key to a
dictionary as they are mutable (changeable). Try to add the key "work"
to dict with values shown below.

What's the key with the highest value in the dictionary

Date: 18/01/24
"""

# dict = {"a": 1, "b": 4, "c": 3} 
dict_original = {"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
my_dict = {}
for key,value in dict_original.items():
    if isinstance (value,int):
        my_dict[key] = value
# my_dict = {key:value for key,value in dict.items() if isinstance (value,int)}
# for key,value in my_dict.items():
#     if not isinstance (value,int):
#         del dict_1[key] 
print(my_dict)
#Type your answer below.
max_key = max(my_dict, key = my_dict.get)
print(max_key)
