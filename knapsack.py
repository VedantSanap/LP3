def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratios for each item
    for item in items:
        item['ratio'] = item['value'] / item['weight']

    # Sort items in non-increasing order of value-to-weight ratio
    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_value = 0
    total_weight = 0
    knapsack = []

    for item in items:
        if total_weight + item['weight'] <= capacity:
            # Take the whole item
            knapsack.append(item)
            total_value += item['value']
            total_weight += item['weight']
        else:
            # Take a fraction of the item
            fraction = (capacity - total_weight) / item['weight']
            knapsack.append({'name': item['name'], 'weight': item['weight'] * fraction, 'value': item['value'] * fraction})
            total_value += item['value'] * fraction
            total_weight += item['weight'] * fraction
            break

    return knapsack, total_value

def main():
    print("Fractional Knapsack Problem Solver")
    print(" Enter Custom Data")
    items = []
    n = int(input("Enter the number of items: "))
    for i in range(n):
        name = input("Enter item name: ")
        weight = float(input("Enter item weight: "))
        value = float(input("Enter item value: "))
        items.append({'name': name, 'weight': weight, 'value': value})
    capacity = float(input("Enter the capacity of the knapsack: "))

    knapsack_items, total_value = fractional_knapsack(items, capacity)

    print(f"\nSelected Items in Knapsack:")
    for item in knapsack_items:
        print(f"Item: {item['name']}, Weight: {item['weight']}, Value: {item['value']}")

    print(f"Total Value: {total_value}")


# TIME COMPLEXITY IS = O(nlogn)
# SPACE COMPLEXITY IS = O(n)

if __name__ == "__main__":
    main()
