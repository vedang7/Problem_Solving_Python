# Given a list of strings, replace all vowels in each string with an asterisk (*).

# Input: ['hello', 'world']
# Output: ['h*ll*', 'w*rld']

class Stringss():
    def __init__(self):
        pass

    # def __new__(cls):
    #     pass

    def parse_string(self, list_of_string: list) -> list:
        # v = ''
        # v.replace()
        # return map(lambda x: )
        # import ipdb;ipdb.set_trace()
        return_list = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        # for words in list_of_string:
        #     stripped_word = words.strip()
        #     for letter in stripped_word:
        #         if letter in vowels:
        #             words = words.replace(letter, "*")
        #     # print(words)
        #     return_list.append(words)
        # return return_list
    
        return list(map(lambda x: "".join('*' if char in vowels else char for char in x), list_of_string))


if __name__ == "__main__":
    obj = Stringss()
    print(obj.parse_string(['hello', 'world']))