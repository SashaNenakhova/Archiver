
# hex data from file
hex_data='d09fd0bed182d0bed0' \
         'bcd181d182d0b2d0b020d0bed18220d181d183d189d0b5d181d182d0b220d0bfd180d0b5d0bad180d0b0d181d0bdd18bd18520d0' \
         'b2d181d0b520d185d0bed182d18fd1822c0ad0a7d182d0bed0b120d0b220d0bcd0b8d180d0b520d0bad180d0b0d181d0bed182d0b02' \
         '0d186d0b2d0b5d0bbd0b020e2809420d0bdd0b520d183d0bcd0b8d180d0b0d0bbd0b03a0ad09fd183d181d182d18c20d0b7d180d0b' \
         '5d0bbd0b0d18f20d0bad180d0b0d181d0b020d0bed18220d0b2d180d0b5d0bcd0b5d0bdd0b820d183d0b2d18fd0bbd0b020e28094' \
         '0ad095d0b520d180d0bed181d182d0bad0b820d0be20d0bdd0b5d0b920d0bdd0b0d0bc20d0bfd0b0d0bcd18fd182d18c20d181d0be' \
         'd185d180d0b0d0bdd18fd1822e0a0ad09dd0be20d182d18b2c20d187d0b5d0b920d0b3d0bed180d0b4d18bd0b920d0b2d0b7d0bed1' \
         '8020d0bdd0b8d0bad182d0be20d0bdd0b520d0bfd180d0b8d0b2d0bbd0b5d0bad0b0d0b5d1822c0ad09020d181d0b2d0b5d182d0bbd' \
         '18bd0b920d0bfd0bbd0b0d0bcd0b5d0bdd18c20d181d0b0d0bc20d181d0b2d0bed0b920d0bfd18bd0bb20d0b220d181d0b5d0b1d0b5' \
         '20d0bfd0b8d182d0b0d0b5d1822c0ad0a2d0b0d0bc20d0b3d0bed0bbd0bed0b420d181d0b5d18f2c20d0b3d0b4d0b520d0b8d0b7d0b1' \
         'd18bd182d0bed0ba20d0b4d0bed0bbd0b6d0b5d0bd20d0b1d18bd182d18c20e280940ad0a2d18b20d181d0b0d0bc20d181d0b2d0bed0b' \
         '920d0b7d0bbd0b5d0b9d188d0b8d0b920d0b2d180d0b0d0b32c20d0b3d0bed182d0bed0b2d18bd0b920d0b2d181d0b520d181d0b3d183' \
         'd0b1d0b8d182d18c2e0a0ad0a2d18b2c20d0bbd183d187d188d0b8d0b920d0b8d0b720d0bbd18ed0b4d0b5d0b92c20d0bfd180d0b8d180' \
         'd0bed0b4d18b20d183d0bad180d0b0d188d0b5d0bdd18cd0b52c0ad09820d0b2d0b5d181d182d0bdd0b8d0ba20d0bcd0bed0bbd0bed0b4d0' \
         'bed0b920d0bfd0bbd0b5d0bdd0b8d182d0b5d0bbd18cd0bdd0bed0b920d0b2d0b5d181d0bdd18b2c0ad097d0b0d0bcd0bad0bdd183d0' \
         'b2d188d0b8d181d18c2c20d181d0b0d0bc20d0b220d181d0b5d0b1d0b520d185d0bed180d0bed0bdd0b8d188d18c20d181d187d0b0d1' \
         '81d182d18cd18f20d181d0bdd18b2e0ad09820d181d0b5d0b5d188d18c20d0b2d0bad180d183d0b320d181d0b5d0b1d18f20d0bed0b4' \
         'd0bdd0be20d0bed0bfd183d181d182d0bed188d0b5d0bdd18cd0b52e0a0ad0a2d18b20d0bfd0bed0b6d0b0d0bbd0b5d0b920d185d0be' \
         'd182d18c20d0bcd0b8d18020e2809420d183d0bfd0b0d181d182d18c20d0b5d0bcd18320d0bdd0b520d0b4d0b0d0b90ad0982c20d0ba' \
         'd0b0d0ba20d0b7d0b5d0bcd0bbd18f2c20d0b4d0b0d180d0bed0b220d0b5d0b3d0be20d0bdd0b520d0bfd0bed0b6d0b8d180d0b0d0b92e20'

print(hex_data, '\n')



## hex data to binary data
binary_data=''
for i in range(0, len(hex_data)-1, 2):
    # hex byte
    a=hex_data[i:i+2]
    print(a, end=' ')

    # int
    b=int(a, 16)
    print(b, end=' ')

    # bin
    c=format(b, '0>8b')
    print(c)

    binary_data+=c
print(binary_data, '\n')


######################################################################################################################






# binary_data = '010101001111010101010101101010101010100101111101101010101010101010101010111110110111'




# Convert binary string to bytes
byte_data = bytearray(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))

# Write bytes to file
with open('output.bin', 'wb') as file:
    file.write(byte_data)


# 0101 0100 1111 0101 0101 0101 1010 1010 1010 100101111101101010101010101010101010111110110111
#   5     4    F    5   5    5   A     A    A






##########################
# for i in range(0, len(binary_data)):
#     b=binary_data[i:i + 8]
#     a=int(b, 2)
#     print(b)
#     print(a)
#     print(bytearray(a))