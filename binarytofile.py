binary_data = '010101001111010101010101101010101010100101111101101010101010101010101010111110110111'

# Convert binary string to bytes
byte_data = bytearray(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))

# Write bytes to file
with open('output.bin', 'wb') as file:
    file.write(byte_data)









# 0101 0100 1111 0101 0101 0101 1010 1010 1010 100101111101101010101010101010101010111110110111
#   5     4    F    5   5    5   A     A    A