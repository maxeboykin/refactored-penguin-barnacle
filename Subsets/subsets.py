print("----------------------")

print("Subsets")

input = [1, 3]
input2 = [1, 5, 3]

print(f'Given a set with distinct elements, find all of its distinct subsets" '
      f'Input:'
      f'${input}')


def find_subsets(arr):
    subsets = []
    subsets.append([])  # adding empty subset
    for i in range(len(arr)):
        cur_num = arr[i]
        n = len(subsets)
        for j in range(n):
            set_with_new_elem = list(subsets[j])
            set_with_new_elem.append(cur_num)
            subsets.append(set_with_new_elem)

    return subsets


print("----------------------")
print(find_subsets(input))

print("----------------------")
print(find_subsets(input2))
