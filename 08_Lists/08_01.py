"""
8.1 
* Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
* Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

def chop(list):
    list.pop(0)
    list.pop()
    return None

a = ['apple','orange','kiwi','peach','lemon']

print(chop(a)) #None
print(a) #['orange', 'kiwi', 'peach']

def middle(list):
    new_list = list.copy()
    return new_list[1:len(new_list)-1]
  
b = [1, 2, 3, 4, 5, 6, 7]

print(middle(b)) #[2, 3, 4, 5, 6]
print(b) #[1, 2, 3, 4, 5, 6, 7]