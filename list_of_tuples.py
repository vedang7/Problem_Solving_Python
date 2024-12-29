# Transform a list of full names (e.g., "John Doe") into a list of initials (e.g., "J.D.").

# Input: ['John Doe', 'Jane Smith']
# Output: ['J.D.', 'J.S.']

class TupleList():
    def __init__(self):
        pass

    def name_initials(self, name_list: list) -> list:
        return list(map(lambda name: "".join(n[0] + "." for n in name.split(" ")), name_list))
    
if __name__ == "__main__":
    obj = TupleList()
    print(obj.name_initials(['John Doe', 'Jane Smith']))