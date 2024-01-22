"""
Dictionaries don't have index orders, so speaking about them regarding 
their first item or last item is not very correct. Next time you print a
dictionary it may have a different order than you saw before. Instead
they have keys, and we can use keys to call their values.

Change Plato's birth year from B.C. 427 to B.C. 428.

Date: 18/01/24
"""

my_dict = { "name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
my_dict["born"] = -428
print(my_dict)