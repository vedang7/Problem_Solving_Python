# Convert a list of dictionaries containing price and quantity into a list of total costs.

# Input: [{price: 10, quantity: 2}, {price: 5, quantity: 4}]
# Output: [20, 20]

def total_cost(list_of_item: list) -> list:
    print(list_of_item)
    return list(map(lambda x: x['price']*x['quantity'], list_of_item))

print(total_cost([{'price': 10, 'quantity': 2}, {'price': 5, 'quantity': 4}]))