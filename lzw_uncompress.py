import sys



# найти самый длинный код в словаре
# (decoding)
def max_index():
    return len(bin(len(dictionary)).replace("0b", ""))


# get sequence from dictionary by index
# (decoding)
def get_sequence(bin_ind):
    # convert bin code to decimal index

    ind=int('0b'+bin_ind, 2)



    return dictionary[ind]
















### decoding
def lzw_decode(code):
    # расшифрованный файл
    file=''

    # предыдущая последовательность
    last_seq = ''

    # длина последнего кода в словаре
    max_num=max_index()


    # пока не закончится зашифрованный файл
    while code!='':

        # из зашифрованного файла берется часть кода,
        # длина которой равна длине последнего кода в словаре
        current_code=code[:max_num]


        # get sequence from the dictionary by code
        flag=False
        while flag==False:
            try:
                current_seq=get_sequence(current_code)
                flag=True
            except:
                current_code = current_code[:-1]

        # add new sequence to the dictionary
        if (last_seq+current_seq[0]) not in dictionary:
            dictionary.append(last_seq + current_seq[0])
            # длина самой большой записи в словаре
            max_num=max_index()

        # добавляем к расшифрованному файлу последовательность символов
        file+=current_seq

        # обновляется предыдущая последовательность символов
        last_seq = current_seq                                  ############      !!!!!!!!!!!! last seq
        # из начала файла удаляются зашифрованные символы

        code = code[len(str(current_code)):]


    return file



def decode_by_parts(archive_name, result_name):
    # creating result file
    res=open(result_name, 'w')
    res.close()

    f = open(archive_name, 'rb')

    # read format
    if f.read(8)==bytearray(b'LZW\x00'):
        print(True)

    # chunk_size = 64 * 1024 # 64KB in bytes
    chunk_size = 64


    # decode and write file by parts
    while True:

        # decoding parts
        chunk = f.read(chunk_size)
        if not chunk:
            break
        hex_chunk = ''.join('{:02x}'.format(byte) for byte in chunk)
        # print(hex_chunk)
        code = lzw_encode(hex_chunk)
        # print(code)

        bytes = bytearray(int(code[i:i + 8], 2) for i in range(0, len(code), 8))

        # writing to file
        write_to_file(bytes, file_name)


    ############################################
    # creating/cleaning file
    # res = open(file_name + '_archive4', 'w')
    # res.close()
    #
    # # write format
    # b = bytearray(b'LZW\x00')
    # write_to_file(b, file_name)
    #
    # f = open(file_name, 'rb')
    #
    # # chunk_size = 64 * 1024 # 64KB in bytes
    # chunk_size = 64
    #
    # # encode and write file by parts
    # while True:
    #
    #     # encoding parts
    #     chunk = f.read(chunk_size)
    #     if not chunk:
    #         break
    #     hex_chunk = ''.join('{:02x}'.format(byte) for byte in chunk)
    #     # print(hex_chunk)
    #     code = lzw_encode(hex_chunk)
    #     # print(code)
    #
    #     bytes = bytearray(int(code[i:i + 8], 2) for i in range(0, len(code), 8))
    #
    #     # writing to file
    #     write_to_file(bytes, file_name)



### MAIN ###

# чтение файла
archive_name = sys.argv[1]
result_name = sys.argv[2]

# create global dictionary for encoding
global dictionary
dictionary = [i for i in 'abcdef0123456789']

# кодирование файла
decode_by_parts(archive_name, result_name)


