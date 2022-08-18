def highest_even(li):
    li.sort()
    li.reverse()
    for num in li:
        if num % 2 == 0:
            break

    return num


print(highest_even([10, 2, 3, 4, 8, 11]))


def highest_even_solved(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even_solved([10, 2, 3, 4, 8, 11]))
