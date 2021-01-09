import Arithmetic, time, os
start_time = time.time()
freq_table = {" ": 49460, "e": 31115, "i": 28350, "u": 24975, "t": 23360, "s": 23025,
              "a": 22390, "l": 16680, "n": 15985, "r": 15870, "m": 12795, "o": 11930,
              "c": 11655, "d": 7815, ".": 6355,"p": 6105, ",": 4460, "v": 4000, "g": 3600,
              "q": 3475, "b": 3205, "f": 2525, "h": 1470, "\n": 1094, "N": 865, "P": 725,
              "D": 710, "M": 680, "S": 640, "C": 500, "x": 475, "V": 470, "I": 470, "A": 445,
              "j": 285, "E": 210, "Q": 205, "U": 195, "F": 180, "L": 55, "O": 30, ";": 25}
AE = Arithmetic.ArithmeticEncoding(freq_table)
path = "sample1.txt"
fi = open(path,"r")
fir = fi.read()
'''print("Original Message: {msg}".format(msg=fir))
fi = open("sample.txt")
fir = fi.read().lower()'''
print("Before Arithmetic Compression the file size is", os.stat(path).st_size, "bytes")
encoder, encoded_msg = AE.encode(msg=fir, prob_table=AE.prob_table)
#print("Encoded Message: {msg}".format(msg=encoded_msg))
filename, file_extension = os.path.splitext(path)
output_path = filename + "_compressed_a.txt"
fio = open(output_path, "w")
fio.write(str(encoded_msg))
print("Compressed")
print("After Arithmetic Compression the file size is", os.stat(output_path).st_size,"bytes")
#print("Compression Ratio is", os.stat(path).st_size/os.stat(output_path).st_size)
print("This program took", time.time() - start_time, "to compress.\n")
start_time = time.time()
decoder, decoded_msg = AE.decode(encoded_msg=encoded_msg, msg_length=len(fir),prob_table=AE.prob_table)
#print("Decoded Message: {msg}".format(msg=decoded_msg))
output_path = filename + "_decompressed_a.txt"
fio = open(output_path, "w")
fio.write(decoded_msg)
fi.close()
fio.close()
#print("Message Decoded Successfully? {result}".format(result=fi == decoded_msg))
print("Decompressed")
print("This program took", time.time() - start_time, "to decompress.")