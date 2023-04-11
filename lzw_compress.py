# read hex data (bytes) from file
# (encoding)
def read_file_data(file_name):
    try:
        file = open(file_name, 'rb')
        data = file.read()
        hex_data = ''.join('{:02x}'.format(byte) for byte in data)
        return hex_data
    except:
        pass


# def compress_file(code, initial_dictionary, file_name):
#     file = open(file_name + '_archive', 'wb')
#
#     ### initial dictionary
#     # write length of initial dictionary in 4 bytes
#     l=len(initial_dictionary)
#     l=format(l, '0>32b')
#     # print('l', l)
#     l=bytearray(int(l, 2))
#     file.write(l)
#
#     # write initial dictionary in binary format
#     for i in initial_dictionary:
#         # file.write(bytearray(format(ord(i), 'b')))
#         file.write(bytearray(int(format(ord(i), 'b'), 2)))
#
#     ### binary code
#     # Convert binary string to bytes
#
#     code = bytearray(int(code[i:i + 8], 2) for i in range(0, len(code), 8))
#     # file.write('Coded file:' + '\n')
#     # file = open(file_name + '_archive', 'ab')
#     file.write(code)
#     file.close()


# converts data to bytes and writes to file
def write_to_file(data, file_name):
    file = open(file_name + '_archive', 'ab')


    # data = bytearray(int(data[i:i + 8], 2) for i in range(0, len(data), 8))

    # print(data)
    # print('\n')

    file.write(data)
    file.close()





# creating initial dict
# (encoding)
def init_dict(symbols):
    dictionary=[]
    for i in symbols:
        if i not in dictionary:
            dictionary.append(i)
    return dictionary


# get dictionary index of sequence
# convert dictionary index of sequence to bin code
# добавить нули в начало
# (encoding)
def get_index(dictionary, n):
    # количество цифр в индексе последовательности n
    current_index=str(bin(dictionary.index(n)).replace("0b", ""))

    # добавлять нули в начало, пока длина индекса не равна количеству цифр в самом большом индексе
    while len(current_index)<len(bin(len(dictionary)-1).replace("0b", "")):
        current_index='0'+current_index

    return current_index


# find max length
# (encoding)
def max_length(dictionary):
    l=0
    for i in dictionary:
        if len(i)>l:
            l=len(i)
    return l


# encoding sequence of symbols
def lzw_encode(file):
    # создание начального словаря
    dictionary = init_dict(file)

    # зашифрованный файл
    code = ''

    # предыдущая последовательность
    last_seq = ''

    # длина самой большой последовательности из словаря
    max_seq = max_length(dictionary)

    # пока не закончится файл
    while file != '':

        # из файла берется последовательность символов,
        # длина которой равна длине самой большой последовательности в словаре
        current_seq=file[:max_seq]

        # пока последовательности нет в словаре укорачивается на 1
        while current_seq not in dictionary:
            current_seq=current_seq[:-1]

        # добавление новой последовательности (предыдущая+первый символ текущей)
        if (last_seq+current_seq[0]) not in dictionary:
            dictionary.append(last_seq + current_seq[0])
            # длина самой большой записи в словаре
            max_seq = max_length(dictionary)

        # добавляем к коду индекс последовательности
        code += get_index(dictionary, current_seq)

        # обновляется предыдущая последовательность символов
        last_seq = current_seq
        # из начала файла удаляются зашифрованные символы
        file = file[len(current_seq):]

    return code



def encode_by_parts(hex_data, file_name):
    # creating/cleaning file
    f=open(file_name+'_archive', 'w')
    f.close()

    # write format
    # letters to bytes

    b=bytearray(b'LZW\x00')
    write_to_file(b, file_name)


    # write len init dictionary
    # write init dictionary
    initial_dictionary = init_dict(hex_data)
    l=len(initial_dictionary)
    write_to_file(bytearray([l])+b'\x00\x00\x00', file_name)

    print(initial_dictionary)
    for i in initial_dictionary:
        print(bytearray([ord(i)]))
        write_to_file(bytearray([ord(i)]), file_name)



    # encode and write file by parts
    while hex_data != '':

        # encoding parts
        part = hex_data[:64]
        hex_data = hex_data[64:]
        code = lzw_encode(part)
        # print(code)

        bytes= bytearray(int(code[i:i + 8], 2) for i in range(0, len(code), 8))

        # writing parts
        write_to_file(bytes, file_name)











### MAIN ###

### прочитать файл, создать в зашифрованном файле начальный словарь в виде строки ('abcdef')

# чтение файла
file_name='input_file'
hex_data=read_file_data(file_name)

print('\n'+'FILE: '+str(hex_data)+'\n')

# кодирование файла
encode_by_parts(hex_data, file_name)