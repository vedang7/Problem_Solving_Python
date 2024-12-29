from functools import reduce
# Filter out all prime numbers from a list of integers.

# Input: [1, 2, 3, 4, 5, 6, 7]
# Output: [2, 3, 5, 7]

def prime_number(list_number: list) -> list:
    return list(filter(lambda number: number > 1 and  all(number % i != 0 for i in range(2, number)), list_number))

    
print(prime_number([1, 2, 3, 4, 5, 6, 7]))


# Find all strings in a list that are palindromes.

# Input: ['radar', 'hello', 'level', 'world']
# Output: ['radar', 'level']


# for i in range(len(word)/2):
#     if word[i] == word[len-i]

def palindrome(list_of_words):
    return list(filter(lambda word: all(word[i] == word[len(word)-i-1] for i in range(len(word)//2)), list_of_words))

print(palindrome(['radar', 'hello', 'level', 'world']))


# Calculate the difference between the product of all even numbers and the product of all odd numbers in a list.

# Input: [1, 2, 3, 4]
# Output: 8 (2 * 4 - 1 * 3)


# Given a list of strings, concatenate them to form a single string in reverse order.

# Input: ['one', 'two', 'three']
# Output: 'threetwoone'

def concat(list_of_str):
    list_of_str.reverse()
    return(reduce(lambda x,y: x+y, list_of_str))

print(concat(['one', 'two', 'three']))
    