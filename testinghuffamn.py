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


def print_nodes(node, val=''):

    newVal = val + str(node.huff)
    if node.left is None and node.right is None:
        print(f"{node.symbol} -> {newVal}")
        return
    if node.left:
        print_nodes(node.left, newVal)
    if node.right:
        print_nodes(node.right, newVal)

def generate_huffman_codes(node, val=''):
    new_val = val + str(node.huff)
    if node.left:
        generate_huffman_codes(node.left, new_val)
    if node.right:
        generate_huffman_codes(node.right, new_val)
    if not node.left and not node.right:
        huffman_codes[node.symbol] = new_val

def encode_string(text, huffman_codes):
    encoded_text = ''
    for char in text:
        encoded_text += huffman_codes[char]
    return encoded_text

def decode_string(encoded_text, huffman_tree):
    decoded_text = ''
    current_node = huffman_tree
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_text += current_node.symbol
            current_node = huffman_tree

    return decoded_text


text = " سلام خوبی سلام"  # Input text


char_freqs = dict(Counter(text))

sorted_dict = dict(sorted(char_freqs.items(), key=lambda item: item[0]))
# print(sorted_dict)


chars = list(sorted_dict.keys())
freq = list(sorted_dict.values())

nodes = []
for i in range(len(chars)):
    # print(freq[i],chars[i])
    heapq.heappush(nodes, Node(freq[i], chars[i]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    
    right = heapq.heappop(nodes)
    
    left.huff = '0'
    right.huff = '1'
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newNode)

print_nodes(nodes[0])
huffman_codes = {}
generate_huffman_codes(nodes[0])
encoded_string = encode_string(text, huffman_codes)
print(f"Encoded string: {encoded_string}")
decoded_string = decode_string(encoded_string, nodes[0])
print(f"Decoded string: {decoded_string}")