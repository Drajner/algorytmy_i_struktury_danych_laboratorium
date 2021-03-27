def bubble_sort(list):
    is_not_finished = True
    while(is_not_finished):
        is_not_finished = False
        for i in range((len(list)-1)):
            if(list[i] > list[i+1]):
                is_not_finished = True
                temp = list[i+1]
                list[i+1] = list[i]
                list[i] = temp
    return list

def selection_sort(list):
    i = 0
    while i < (len(list)-1):
        j = i+1
        min_el = list[i]
        min_j = i
        while j < (len(list)):
            if(min_el>list[j]): 
                min_el = list[j]
                min_j = j
            j+=1
        list[min_j] = list[i]
        list[i] = min_el
        i+=1
    return list

def merger(list_a, list_b):
    sorted_list = []
    while list_a and list_b:
        smallest_el_a = list_a[0]
        smallest_el_b = list_b[0]
        if smallest_el_a < smallest_el_b:
            sorted_list.append(smallest_el_a)
            list_a.pop(0)
        else:
            sorted_list.append(smallest_el_b)
            list_b.pop(0)
    if not list_a:
        for element in list_b:
            sorted_list.append(element)
    if not list_b:
        for element in list_a:
            sorted_list.append(element)
    return sorted_list

def merge_sort(list):
    if not list or len(list) == 1:
        return list
    splitting_point = len(list)//2
    list_a = list[:splitting_point]
    list_b = list[splitting_point:]
    sorted_a = merge_sort(list_a)
    sorted_b = merge_sort(list_b)
    sorted_list = merger(sorted_a, sorted_b)
    return sorted_list


def partition(list, i, j):
    first_pointer = i+1
    second_pointer = j
    pivot = list[i]
    while first_pointer-1 != second_pointer:
        if list[first_pointer] >= pivot:
            while not list[second_pointer] < pivot:
                if second_pointer == first_pointer:
                    second_pointer -= 1
                    list[second_pointer], list[i] = list[i], list[second_pointer]
                    return second_pointer
                second_pointer -= 1
            list[second_pointer], list[first_pointer] = list[first_pointer], list[second_pointer]
            second_pointer -=1
        first_pointer += 1
    list[second_pointer], list[i] = list[i], list[second_pointer]
    return second_pointer


def quick_sort(list, i=0, j=None):
    if j is None:
        j = len(list)-1
    if i < j:
        q = partition(list, i, j)
        quick_sort(list, i, q-1)
        quick_sort(list, q+1, j)
    return list

ass = [5,7,3,9,2]
mmmmm = [6,8,9,1,3,5,6,3,2,1,7,10]
print(quick_sort(mmmmm))
print(quick_sort(ass))
# print(selection_sort(ass))
# print(merge_sort(ass))
# print(quick_sort([7,1,7]))
