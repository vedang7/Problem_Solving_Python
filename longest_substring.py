from collections import Counter
from functools import reduce
def long_substring_with_all_unique(s: str) -> int:
    # test = Counter(s)
    # keys = test.keys()
    # print(keys)
    # element_traversed = []
    # count = 0
    # # import ipdb;ipdb.set_trace()
    # for index in range(len(s)):
    #     count += 1
    #     element_traversed.append(s[index])
    #     for new_index in range(index+1, len(s)):
    #         if count >= len(keys):
    #             return count
    #         if s[index] != s[new_index]:
    #             if s[new_index] not in element_traversed:
    #                 count += 1
    #                 element_traversed.append(s[new_index])
    #         else:
    #             count = 0
    #             element_traversed.clear()
    #             break
            
    # print(count)
    elements = dict()
    left, right, maximum = 0, 0, 0

    while right < len(s):
        if s[right] not in elements.keys():
            elements[s[right]] = 1
        else:
            val = elements[s[right]]
            val += 1
            elements[s[right]] = val

        if len(elements) == right-left+1:
            maximum = max(maximum, right-left+1)
            
        while len(elements) < right-left+1:
            val = elements[s[left]]
            if val > 1:
                val -= 1
                elements[s[left]] = val
            elif val == 1:
                elements.pop(s[left])
            left += 1 
        right+=1
    
    return maximum

def long_substring_with_k_unique(s: str, k: int) -> int:
    left, right, maximum = 0, 0, 0
    elements = {}
    while right < len(s):
        if s[right] not in elements.keys():
            elements[s[right]] = 1
        else:
            val = elements[s[right]]
            val += 1
            elements[s[right]] = val
        
        if len(elements) == k:
            maximum =max(maximum, int(reduce(lambda x,y: x+y, elements.values())))
        while len(elements) > k:
            val = elements[s[left]]
            if val > 1:
                val -= 1
                elements[s[left]] = val
            elif val == 1:
                elements.pop(s[left])
            left += 1
        right+=1
    return maximum

if __name__ == "__main__":
    print(long_substring_with_all_unique("32321343"))
    print(long_substring_with_k_unique("32321343", 2))
    #32321343