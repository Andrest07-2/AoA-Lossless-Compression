from Huffman import HuffmanCoding
import os, time
start_time = time.time()
path = "sample1.txt"
h = HuffmanCoding(path)
print("Before Huffman Compression the file size is", os.stat(path).st_size, "bytes")
output_path = h.compress()
print("After Huffman Compression the file size is", os.stat(output_path).st_size, "bytes")
try:
    print("Compression Ratio is", os.stat(path).st_size/os.stat(output_path).st_size)
except:
    print("Compression Ratio is undefined, output size is 0 bytes.")
print("This program took", time.time() - start_time, "to compress.\n")
start_time = time.time()
h.decompress(output_path) #Just used to decompress the file
print("This program took", time.time() - start_time, "to decompress.")