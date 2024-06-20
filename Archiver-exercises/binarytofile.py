# byte data
f=open('input_file_2', 'rb')
byte_data=f.read()
print(byte_data)

# convert bytes to bits
# import sys
# bin_data=bin(int.from_bytes(byte_data, byteorder=sys.byteorder))  # => 17 => '0b10001'
# print(bin_data)
# bin_data=bin_data[2:]
# for i in range(0, len(bin_data)-1, 8):
#     print(bin_data[i:i+8])
bits = ''.join(format(ord(byte), '08b') for byte in byte_data)
print(bits)


# Convert binary string to bytes
byte_data = bytearray(int(bin_data[i:i+8], 2) for i in range(0, len(bin_data), 8))
print(byte_data)

# Write bytes to file
with open('output.bin', 'wb') as file:
    file.write(byte_data)


# 0101 0100 1111 0101 0101 0101 1010 1010 1010 100101111101101010101010101010101010111110110111
#   5     4    F    5   5    5   A     A    A


