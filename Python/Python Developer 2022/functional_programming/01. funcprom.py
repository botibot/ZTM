
#! Pure Functions

def multiply_by2(li):
    new_list = []
    for i in li:
        new_list.append(i*2)
    return(new_list)

print(multiply_by2([1,2,3]))
#No side effects
