import heapq
from collections import Counter

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

def huffman_encoding(data):
    freq_map = Counter(data)
    nodes = []

    for char, freq in freq_map.items():
        print(f"Frequency of '{char}': {freq}")
        heapq.heappush(nodes, Node(freq, char))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = 0
        right.huff = 1
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    return nodes[0]

if __name__ == "__main__":
    user_input = input("Enter the string for Huffman encoding: ")
    root = huffman_encoding(user_input)
    print("Huffman codes:")
    printNodes(root)
