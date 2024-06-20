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


# decodes hex chunk to code
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

        hex_chunk = ''.join('{:02x}'.format(byte) for byte in chunk) # str
        print('hex chunk', hex_chunk, '\n')

        # hex chunk to binary code (01100101010...)
        # code=bin(int(hex_chunk, 16))[2:].zfill(8)
        code=hex_to_bin(hex_chunk)

        seq = lzw_decode(code)
        print('decoded seq', seq, '\n')


        bytes = bytearray(int(seq[i:i + 8], 2) for i in range(0, len(seq), 8))
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


