
# reading file
# (encoding)
def read_file(file_name):
    try:
        file=open(file_name, 'r')
        dict=[]
        a=file.readline()
        while 'Coded file:' not in a:
            if a!='\n':
                a=a.rstrip('\n')
            dict.append(a)
            a=file.readline()
        code=file.readline()
        return dict, code

    except:
        pass


# найти самый длинный код в словаре
# (decoding)
def max_index(dictionary):
    return len(bin(len(dictionary)).replace("0b", ""))


# get sequence from dictionary by index
# (decoding)
def get_sequence(dictionary, bin_ind):
    # convert bin code to decimal index
    # bin_ind=int(bin(int(bin_ind)), 2)
    ind=int('0b'+bin_ind, 2)
    # print('get_sequence: ', ind)


    return dictionary[ind]


# creating uncompressed file
# (decoding)
def uncompress_file(decoded_file, file_name):
    file = open(file_name+'_uncompressed', 'w')
    file.write(decoded_file)
    file.close()














### decoding
def lzw_decode(code, dictionary):
    # расшифрованный файл
    file=''

    # предыдущая последовательность
    last_seq = ''

    # длина последнего кода в словаре
    max_num=max_index(dictionary)

    # steps
    # step=0

    # пока не закончится зашифрованный файл
    while code!='':
        # steps
        # print('step № '+str(step))

        # из зашифрованного файла берется часть кода,
        # длина которой равна длине последнего кода в словаре
        current_code=code[:max_num]
        # print('index: ' + str(current_code))

        # get sequence from the dictionary by code
        flag=False
        while flag==False:
            try:
                current_seq=get_sequence(dictionary, current_code)
                flag=True
            except:
                current_code = current_code[:-1]

        # add new sequence to the dictionary
        if (last_seq+current_seq[0]) not in dictionary:
            dictionary.append(last_seq + current_seq[0])
            # длина самой большой записи в словаре
            max_num=max_index(dictionary)

        # добавляем к расшифрованному файлу последовательность символов
        file+=current_seq

        # print
        # print('current sequence: ' + current_seq)
        # print('current index: ' + str(current_code))
        # print('code: '+code)
        # print('file: '+file)
        # print('dictionary: '+str(dictionary))

        # обновляется предыдущая последовательность символов
        last_seq = current_seq                                  ############      !!!!!!!!!!!! last seq
        # из начала файла удаляются зашифрованные символы
        # code = code[max_num + 1:-1]
        code = code[len(str(current_code)):]

        # steps
        # step+=1
        # print('\n')

    return file






### MAIN ###

# чтение заархивированного файла
file_name='input_file_archive'
initial_dictionary, code=read_file(file_name)

# чтение кода и начального словаря из файла
# code=file[1]
# initial_dictionary=[]
# initial_dictionary.extend(file[0])

print('CODE: '+code+'\n')
print('INIT DICT: '+str(initial_dictionary))




# расшифровка файла
decoded_file=lzw_decode(code, initial_dictionary)

print('DECODED CODE: '+decoded_file+'\n')

# создать расшифрованный файл
uncompress_file(decoded_file, file_name)

