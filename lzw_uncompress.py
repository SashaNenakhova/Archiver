import sys

# writes decoded bytes to file
def write_result(seq, result_name):
    file = open(result_name, 'ab')
    file.write(seq)
    file.close()

# finds max index for bytes
def max_index():
    # return len(dictionary)
    return len(bin(len(dictionary)))-1 #####


# decodes hex chunk to binary code
def hex_to_bin(hex_chunk):
    code=''

    for i in hex_chunk:
        current_code = str(bin(dictionary.index(i)).replace("0b", ""))
        # добавлять нули в начало, пока длина индекса не равна количеству цифр в самом большом индексе
        while len(current_code) < len(bin(len(dictionary) - 1).replace("0b", "")):
            current_code = '0' + current_code
        code+=current_code
    return code




# get dictionary index of sequence
# convert dictionary index of sequence to bin code
# добавить нули в начало
# (encoding)
def get_sequence(n):
    # количество цифр в индексе последовательности n
    # current_seq = str(bin(dictionary[n.replace("0b", "")]))
    current_seq = str((dictionary[int(n, 2)]))
    pass

    # # добавлять нули в начало, пока длина индекса не равна количеству цифр в самом большом индексе
    # while len(current_seq) < len(bin(len(dictionary) - 1).replace("0b", "")):
    #     current_seq = '0' + current_seq

    return current_seq










### decoding
def lzw_decode(code):
    # расшифрованная последовательность
    seq=''

    # предыдущая последовательность
    last_seq = ''

    # длина последнего кода в словаре
    max_num=max_index()


    # пока не закончится зашифрованный чанк
    while code!='':
        print('lzw decoding chunk', code)
        print('lzw decoding dictionary', dictionary, '\n')

        # из зашифрованного чанка берется часть кода,
        # длина которой равна длине последнего кода в словаре
        current_code=code[:max_num]
        current_seq=''


        # get sequence from the dictionary by code
        flag=False
        while flag==False and current_code!='':  ######## while flag==False
            try:
                current_seq=get_sequence(current_code)
                flag=True

            except:
                current_code = current_code[:-1]
        print('current code', current_code)
        print('current seq', current_seq)


        # add new sequence to the dictionary
        if (last_seq+current_seq[0]) not in dictionary:
            dictionary.append(last_seq + current_seq[0])
            # длина самой большой записи в словаре
            max_num=max_index()

        # добавляем к расшифрованному файлу последовательность символов
        seq+=current_seq

        # обновляется предыдущая последовательность символов
        last_seq = current_seq
        # из начала файла удаляются зашифрованные символы

        code = code[len(str(current_code)):]


    return seq



def decode_by_parts(archive_name, result_name):
    # creating result file
    res=open(result_name, 'w')
    res.close()

    f = open(archive_name, 'rb')

    # read format
    if f.read(4)==bytearray(b'LZW\x00'):
        pass

    # chunk_size = 64 * 1024 # 64KB in bytes
    chunk_size = 64


    # decode and write file by parts
    while True:

        # decoding parts
        chunk = f.read(chunk_size) # bytes
        if not chunk:
            break

        print('byte chunk from file', chunk, '\n')

        # hex chunk looks exactly like bytes in hex fiend (archived file)
        hex_chunk = ''.join('{:02x}'.format(byte) for byte in chunk) # str
        print('HEX CHUNK', hex_chunk, '\n')
        # 93a5094a5495a0cc3b10c498536ebf0c9038f40f4
        # 54cb6c91571e52391551d92bd74183976cdba77499e9d4d0d1c


        # hex chunk to binary code (01100101010...)
        code=hex_to_bin(hex_chunk)
        ### outputs code from archive
        # 111110010000101101101111101000001011101
        # 011111011000001100010001010010001011101100010101
        # 01111111010111001110001000001010101100010111101101
        # 001111001011010011001011010101110100010000111000010
        # 1111011110111101011101001011100010011111011110111011
        # 01110011111110000001001111011010011111101001111111011
        # 100001000110001000011011101101011111111010011110011101
        # 000110110001101110010



        seq = lzw_decode(code)
        print('decoded seq', seq, '\n')

        print("int(seq)", int(seq[0:0+8], 16))
        bytes = bytearray(int(seq[i:i + 2], 16) for i in range(0, len(seq), 2))
        print('bytes', bytes)


        # writing to file
        write_result(bytes, result_name)




### MAIN ###

# чтение файла
archive_name = sys.argv[1]
result_name = sys.argv[2]

# create global dictionary for encoding
global dictionary
dictionary = [i for i in 'abcdef0123456789']

# кодирование файла
decode_by_parts(archive_name, result_name)

print("UNCOMPRESSING FINISHED")
