
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


ass = [5,7,3,9,2]
print(selection_sort(ass))
print(merge_sort(ass))
