def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else: 
            c.append(a[0])
            a.pop(0)
    while len(a) == 0 and len(b) != 0:
        c.append(b[0])
        b.pop(0)
    while len(b) == 0 and len(a) != 0:
        c.append(a[0])
        a.pop(0)
    return c 
def merge_sort(list):
    if len(list) == 1:
        return list
    a = list[:len(list)//2]
    b = list[len(list)//2:]
    a = merge_sort(a) #when len(list) is 1, [integer] is returned
    b = merge_sort(b) #after that merged lists are returned 
    return merge(a,b)

if __name__ == "__main__":
    import random
    list = random.sample(range(0,500),100)
    print(list[:len(list)])
    print(merge_sort(list))