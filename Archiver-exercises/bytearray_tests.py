byte_array = bytearray([75, 76, 77, 78, 79])
# print(type(byte_array)) #bytearray

# bytes_result = bytes([byte for byte in byte_array])
# print(bytes_result)
# print(type(bytes_result)) #bytes


chunk=open("input_file", "rb")
chunk2=chunk.read()
print(chunk2)