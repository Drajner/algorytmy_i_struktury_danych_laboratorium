
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

def merge_sort()

ass = [5,7,3,9,2]
print(selection_sort(ass))
