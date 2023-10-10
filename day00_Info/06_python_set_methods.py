# add(element): Adds the specified element to the set.
set_example = {1, 2, 3}
set_example.add(4)
print(f"add(4): {set_example}")  # Output: add(4): {1, 2, 3, 4}

# clear(): Removes all elements from the set.
set_example.clear()
print(f"clear(): {set_example}")  # Output: clear(): set()

# copy(): Returns a shallow copy of the set.
set_example = {1, 2, 3}
set_copy = set_example.copy()
print(f"copy(): {set_copy}")  # Output: copy(): {1, 2, 3}

# difference(set): Returns a new set containing the difference between two or more sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff_set = set1.difference(set2)
print(f"difference(set1, set2): {diff_set}")  # Output: difference(set1, set2): {1, 2}

# difference_update(set): Removes all elements of another set from this set.
set1.difference_update(set2)
print(f"difference_update(set2): {set1}")  # Output: difference_update(set2): {1, 2}

# discard(element): Removes the specified element from the set if present.
set_example = {1, 2, 3}
set_example.discard(2)
print(f"discard(2): {set_example}")  # Output: discard(2): {1, 3}

# intersection(set): Returns a new set containing the intersection of two or more sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = set1.intersection(set2)
print(f"intersection(set1, set2): {intersection_set}")  # Output: intersection(set1, set2): {3, 4}

# intersection_update(set): Updates the set with the intersection of itself and another set.
set1.intersection_update(set2)
print(f"intersection_update(set2): {set1}")  # Output: intersection_update(set2): {3, 4}

# isdisjoint(set): Returns True if two sets have a null intersection.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
disjoint = set1.isdisjoint(set2)
print(f"isdisjoint(set1, set2): {disjoint}")  # Output: isdisjoint(set1, set2): True

# issubset(set): Returns True if another set contains this set.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
subset = set1.issubset(set2)
print(f"issubset(set1, set2): {subset}")  # Output: issubset(set1, set2): True

# issuperset(set): Returns True if this set contains another set.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
superset = set1.issuperset(set2)
print(f"issuperset(set1, set2): {superset}")  # Output: issuperset(set1, set2): True

# pop(): Removes and returns an arbitrary element from the set.
set_example = {1, 2, 3}
popped_element = set_example.pop()
print(f"pop(): {popped_element}, {set_example}")  # Output: pop(): 1, {2, 3}

# remove(element): Removes the specified element from the set.
set_example = {1, 2, 3}
set_example.remove(2)
print(f"remove(2): {set_example}")  # Output: remove(2): {1, 3}

# symmetric_difference(set): Returns a new set with the symmetric differences of two sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_diff = set1.symmetric_difference(set2)
print(f"symmetric_difference(set1, set2): {symmetric_diff}")  # Output: symmetric_difference(set1, set2): {1, 2, 5, 6}

# symmetric_difference_update(set): Updates the set with the symmetric difference of itself and another set.
set1.symmetric_difference_update(set2)
print(f"symmetric_difference_update(set2): {set1}")  # Output: symmetric_difference_update(set2): {1, 2, 5, 6}

# union(set): Returns a new set with elements from the set and all specified sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(f"union(set1, set2): {union_set}")  # Output: union(set1, set2): {1, 2, 3, 4, 5}

# update(set): Updates the set with elements from itself and another set or sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(f"update(set2): {set1}")  # Output: update(set2): {1, 2, 3, 4, 5}
