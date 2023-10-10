# clear(): Removes all items from the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(f"clear(): {my_dict}")  # Output: clear(): {}

# copy(): Returns a shallow copy of the dictionary.
original_dict = {'a': 1, 'b': 2, 'c': 3}
copy_dict = original_dict.copy()
print(f"copy(): {copy_dict}")  # Output: copy(): {'a': 1, 'b': 2, 'c': 3}

# fromkeys(keys, value): Returns a new dictionary with keys from the given iterable and values set to a specified value.
keys = ['a', 'b', 'c']
value = 0
new_dict = dict.fromkeys(keys, value)
print(f"fromkeys(): {new_dict}")  # Output: fromkeys(): {'a': 0, 'b': 0, 'c': 0}

# get(key, default): Returns the value for the specified key or a default value if the key is not found.
value = original_dict.get('b')
print(f"get('b'): {value}")  # Output: get('b'): 2

# items(): Returns a view of the dictionary's key-value pairs as a list of tuples.
items_list = original_dict.items()
print(f"items(): {items_list}")  # Output: items(): dict_items([('a', 1), ('b', 2), ('c', 3)])

# keys(): Returns a view of the dictionary's keys as a list.
keys_list = original_dict.keys()
print(f"keys(): {keys_list}")  # Output: keys(): dict_keys(['a', 'b', 'c'])

# pop(key, default): Removes the specified key and returns its associated value. Raises KeyError if the key is not found.
removed_value = original_dict.pop('b')
print(f"pop('b'): {removed_value}, {original_dict}")  # Output: pop('b'): 2, {'a': 1, 'c': 3}

# popitem(): Removes and returns the last key-value pair as a tuple. Raises KeyError if the dictionary is empty.
last_item = original_dict.popitem()
print(f"popitem(): {last_item}, {original_dict}")  # Output: popitem(): ('c', 3), {'a': 1}

# setdefault(key, default): Returns the value for the specified key. If the key is not found, inserts the key with the specified default value.
value = original_dict.setdefault('b', 0)
print(f"setdefault('b', 0): {value}, {original_dict}")  # Output: setdefault('b', 0): 0, {'a': 1, 'b': 0}

# update(iterable): Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
update_dict = {'b': 5, 'd': 4}
original_dict.update(update_dict)
print(f"update(): {original_dict}")  # Output: update(): {'a': 1, 'b': 5, 'd': 4}

# values(): Returns a view of the dictionary's values as a list.
values_list = original_dict.values()
print(f"values(): {values_list}")  # Output: values(): dict_values([1, 5, 4])
