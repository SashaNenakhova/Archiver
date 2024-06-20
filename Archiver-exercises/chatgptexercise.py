with open('file.gif', 'rb') as file:
    data = file.read()
    hex_data = ''.join('{:02x}'.format(byte) for byte in data)
    print(hex_data)


