
def linear_search(li,val):
    for index,v in enumerate(li):
        if v == val:
            return index
    else:
        return None


def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

li = [1,2,3,4,5,5,6,7,8,9]
# print(binary_search(li,3))

def selete_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]

li = [3,4,2,1,5,6,7,8,9]

print(li)
selete_sort(li)
