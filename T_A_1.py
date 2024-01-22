"""
Dictionaries don't have index orders, so speaking about them regarding 
their first item or last item is not very correct. Next time you print a
dictionary it may have a different order than you saw before. Instead
they have keys, and we can use keys to call their values.

When was Plato born?

Date: 18/01/24
"""

my_dict = { "name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
answer_1 = my_dict["born"]
answer_1 = my_dict.get("age")
print(answer_1)