smaller_set = {1,2,3}
larger_set = {3,6,7,8}
combined_set = smaller_set.union(larger_set)
print(combined_set)

intersection_set = smaller_set.intersection(larger_set)
print(intersection_set)


difference_set = smaller_set - larger_set
print(difference_set)

second_difference = larger_set - smaller_set
print(second_difference)

symmetric_difference = smaller_set ^ larger_set
print(f"Symmetric Difference Set: {symmetric_difference}")

variable = smaller_set.issubset(larger_set)
print(f"Is the smaller set a subset of the larger set? {variable}")

set_a = {1,2,3}
set_b = {1,2,3,4,5,6}

is_set_b_a_superset_of_a = set_b.issuperset(set_a)
print(f"Is Set B, a super set of set A? {is_set_b_a_superset_of_a}")