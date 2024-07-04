import sys

# writes decoded bytes to file
def write_result(seq, result_name):
    file = open(result_name, 'ab')
    file.write(seq)
    file.close()


# finds max index for bytes
def max_index():

    return len(bin(len(dictionary)-1).replace("0b", ""))


# decodes hex chunk to binary code
def hex_to_bin(hex_chunk):
    code = ''

    # for i in hex_chunk:
    #     ###!!! current_code = str(dictionary.index(bin(int(i, 16)).replace("0b", "")))
    #     current_code = bin(int(i, 16)).replace("0b", "")
    #     # print("i in hex chunk", i)
    #
    #     # добавлять нули в начало, пока длина индекса не равна
    #     # количеству цифр в самом большом индексе
    #     while len(current_code) < len(bin(len(dictionary) - 1).replace("0b", "")):
    #         current_code = '0' + current_code
    #     code += current_code
    #
    #
    #     ### with current_code = bin(int(i, 16)).replace("0b", "")

    ##################################
    for i in range(1, len(hex_chunk)-1, 2):
        current_code= bin(int(hex_chunk[i-1:i+1], 16)).replace("0b", "")
        print(hex_chunk[i-1:i+1])

        # while len(current_code) < len(bin(len(dictionary) - 1).replace("0b", "")):
        while len(current_code) < 8:
            current_code = '0' + current_code
            print("PLUS ZERO")
        print(len(bin(len(dictionary)-1)))

        print("HEX TO BIN CUR CODE", current_code)
        code+=current_code

    print("HEX TO BIN CHUNK TO BINARY FINAL", code)
    ##################################
    return code








# get dictionary index of sequence
# (encoding)
def get_sequence(n):
    # current_seq = str(bin(dictionary[n.replace("0b", "")]))

    #
    #print('\n', "index to int", int(n, 2))
    #
    #


    return str( (dictionary[int(n, 2)]) )











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
        # print('lzw decoding chunk', code)
        # print('lzw decoding dictionary', dictionary, '\n')
        # print('\n', "WHILE CODE iteration start")



        # из зашифрованного чанка берется часть кода,
        # длина которой равна длине последнего кода в словаре
        current_code=code[:max_num]
        current_seq=''


        # get sequence from the dictionary by code
        flag=False
        while flag==False and current_code!='':
            # print("tryin to get seq with current code", current_code)
            try:
                current_seq=get_sequence(current_code)
                flag=True

            except:
                current_code = current_code[:-1]
           # # print('\n', 'current code', current_code)
       ## print("current code after cycle", current_code)
       # print('current seq', current_seq)
        # print("max_num", max_num)


        # add new sequence to the dictionary
        if (last_seq+current_seq[0]) not in dictionary:
            dictionary.append(last_seq + current_seq[0])
            # длина самой большой записи в словаре
            max_num=max_index()
            # print("ADDED NEW SEQ TO DICTIONARY max index called")



        # добавляем к расшифрованному чанку последовательность символов
        seq+=current_seq

        # обновляется предыдущая последовательность символов
        last_seq = current_seq

        # из начала файла удаляются зашифрованные символы
        code = code[len(str(current_code)):]

       # print("decoded", seq)
        # print("WHILE CODE iteration ended")


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
        # 974a1294a92b4198762189614dbafc3240e3d
        # 03d1532db2455c7948e4554764af5d061cbb66dd3ba4cf41d4d0d1c
        # (974a1294a92b4198762189614dbafc3240e3d03d1532db2455c7948e4554764af5d061cbb66dd3ba4cf41d4d0d1c )

        # hex chunk to binary code (01100101010...)
        code=hex_to_bin(hex_chunk)
        ### outputs code from archive
        # 1001011101001010000100101001010010101001001
        # 010110100000110011000011101100010000110001001
        # 011000010100110110111010111111000011001001000
        # 000111000111101000000111101000101010011001011
        # 011011001001000101010111000111100101001000111
        # 001000101010101000111011001001010111101011101
        # 0000011000011100101110110110011011011101001110
        # 1110100100110011110100    eror here>> 00011101010011010000110100011100
        ## (10010111010010100001001010010100101010010010101101000001100110000111011000100001100010010110000101001101101110101111110000110010010000001110001111010000001111010001010100110010110110110010010001010101110001111001010010001110010001010101010001110110010010101111010111010000011000011100101110110110011011011101001110111010010011001111010000011101010011010000110100011100)
        ## == 974a1294a92b4198762189614dbafc3240e3d03d1532db2455c7948e4554764af5d061cbb66dd3ba4cf41d4d0d1c

        print("CODE AFTER HEX TO BIN", code)


        seq = lzw_decode(code)
        # print('decoded seq', seq, '\n')

        # print("int(seq)", int(seq[0:0+8], 16))
        bytes = bytearray(int(seq[i:i + 2], 16) for i in range(0, len(seq), 2))
        # print('bytes', bytes)


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


#####
# print("dictionary", dictionary)
# print(bin(dictionary.index("36261")))
# print(dictionary.index("36261"))

print("UNCOMPRESSING FINISHED")
