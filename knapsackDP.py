def knapSack(W, wt, val, n, K):
    items_included = []

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # Backtrack to find the items included in the knapsack
    i, j = n, W
    while i > 0 and j > 0:
        if K[i][j] != K[i-1][j]:
            items_included.append(i - 1)
            j -= wt[i - 1]
        i -= 1

    return K[n][W], items_included

def main():
        print("0/1 Knapsack Problem Solver")
        print("2. Enter Custom Data")

        n = int(input("Enter the number of items: "))
        val = []
        wt = []
        for i in range(n):
            val.append(int(input(f"Enter value of item {i+1}: ")))
            wt.append(int(input(f"Enter weight of item {i+1}: ")))
        W = int(input("Enter the maximum weight capacity of the knapsack: "))
    
        K = [[0 for x in range(W+1)] for x in range(n+1)]
        max_value, included_items = knapSack(W, wt, val, n, K)

        print("\nDynamic Programming Matrix:")
        for row in K:
            print(row)

        print("\nSelected Items in Knapsack:")
        for i in included_items:
            print(f"Item {i+1}: Value = {val[i]}, Weight = {wt[i]}")

        print(f"Total Value: {max_value}")

if __name__ == "__main__":
    main()
