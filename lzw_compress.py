import sys


# converts data to bytes and writes to file
def write_to_file(data, file_name):
    file = open(file_name + '_archive', 'ab')
    file.write(data)
    file.close()


# get dictionary index of sequence
# convert dictionary index of sequence to bin code
# добавить нули в начало
# (encoding)
def get_index(n):
    # количество цифр в индексе последовательности n
    current_index = str(bin(dictionary.index(n)).replace("0b", ""))

    # добавлять нули в начало, пока длина индекса
    # не равна количеству цифр в самом большом индексе
    while len(current_index) < len(bin(len(dictionary) - 1).replace("0b", "")):
        current_index = '0' + current_index

    # print("GET INDEX current index", current_index)
    # print("GET INDEX len(dictionary)", len(dictionary))
    return current_index


# find max length
# (encoding)
def max_length():
    l = 0
    for i in dictionary:
        if len(i) > l:
            l = len(i)
    return l


# encoding sequence of symbols
def lzw_encode(chunk):
    # зашифрованный файл
    code = ''

    # предыдущая последовательность
    last_seq = ''

    # длина самой большой последовательности из словаря
    max_seq = max_length()

    # пока не закончится файл
    while chunk != '':
        #print('\n')
        #print("WHILE ITERATION started")
        # из файла берется последовательность символов,
        # длина которой равна длине самой большой последовательности в словаре
        current_seq = chunk[:max_seq]

        # пока последовательности нет в словаре укорачивается на 1
        while current_seq not in dictionary:
            current_seq = current_seq[:-1]

        # print(current_seq)

        # добавляем к коду индекс последовательности
        code += get_index(current_seq)
        print('\n')
        print("code", get_index(current_seq))
        # print("get_index(current_seq)", get_index(current_seq))
        print("current_seq", current_seq)


        # # #
        # добавление новой последовательности (предыдущая+первый символ текущей)
        if (last_seq + current_seq[0]) not in dictionary:
            dictionary.append(last_seq + current_seq[0])
            # длина самой большой записи в словаре

            #print("new seq appended", '\n', last_seq + current_seq[0])

            max_seq = max_length()
        # # #


        # обновляется предыдущая последовательность символов
        last_seq = current_seq
        # из начала файла удаляются зашифрованные символы
        chunk = chunk[len(current_seq):]

        # print("WHILE ITERATION ended")

    return code





def encode_by_parts(file_name):
    # creating/cleaning file
    res = open(file_name + '_archive', 'w')
    res.close()

    # write format
    b = bytearray(b'LZW\x00')
    write_to_file(b, file_name)

    f = open(file_name, 'rb')

    # chunk_size = 64 * 1024 # 64KB in bytes
    chunk_size = 64 # 32 bytes

    # encode and write file by parts
    while True:

        # encoding parts
        chunk = f.read(chunk_size)
        if not chunk:
            break

        # hex chunk looks exactly like bytes in hex fiend
        hex_chunk = ''.join('{:02x}'.format(byte) for byte in chunk)
        print("\n", "ENCODING: HEX CHUNK", hex_chunk, '\n')
        ### reads chunks right
        ##      first
        #  313233343520616263646162636462636162636264
        #  6162636461626463626164636261646263616264636
        #  261626364616263626463626164 62636162 64626162
        ##      second
        # 64636261 6362


        code = lzw_encode(hex_chunk)
        print("binary code", code)
        ### encoded chunk written into the archive file
        # 10010111010010100001001010010100101010010010101
        # 1010000011001100001110110001000011000100101100001
        # 010011011011101011111100001100100100000011100011
        # 110100000011110100010101001100101101101100100100
        # 0101010111000111100101001000111001000101010101000
        # 1110110010010101111010111010000011000011100101110110
        # 110011011011101001110111010010011001111010011101
        # second chunk: 010011010000110111100
        # 10010111010010100001001010010100101010010010101101000001100110000111011000100001100010010110000101001101101110101111110000110010010000001110001111010000001111010001010100110010110110110010010001010101110001111001010010001110010001010101010001110110010010101111010111010000011000011100101110110110011011011101001110111010010011001111010011101010011010000110111100


        byte_array = bytearray(int(code[i:i + 8], 2) for i in range(0, len(code), 8))

        print("byte array", byte_array)
        # writing to file
        write_to_file(byte_array, file_name)




### MAIN ###

# чтение файла
file_name = sys.argv[1]
# file_name="input_file"



# create global dictionary for encoding
global dictionary
dictionary = [i for i in 'abcdef0123456789']

# кодирование файла
encode_by_parts(file_name)

print("\n", "LZW_COMPRESS - DICTIONARY", dictionary, "\n")





# 61D26361 640616 WHY






#######################
# a        b       c       d       e        f       0
# 0000  0001    0010    0011    0100    0101      0110
#  1       2       3       4       5         6          7
# 0111   1000    1001    1010    1011       1100      1101
# 8      9
# 1110  1111