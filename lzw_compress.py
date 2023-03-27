
# reading file
# (encoding)
def read_file(file_name):
    try:
        file=open(file_name, 'r')
        return file.read()
    except:
        pass


# creating compressed file
# writing initial dictionary and coded file
# (encoding)
def compress_file(code, initial_dictionary, file_name):
    file=open(file_name+'_archive', 'w')
    # initial_dictionary=initial_dictionary.replace("\n", "\\n").split('')


    # file.write(str(initial_dictionary)+'\n')
    for i in initial_dictionary:
        if i!='\n':
            file.write(i+'\n')
        else:
            file.write(i)

    file.write('Coded file:'+'\n')
    file.write(code)
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
    # current_index = str(bin(dictionary.index(n)))

    # добавлять нули в начало, пока длина индекса не равна количеству цифр в самом большом индексе
    while len(current_index)<len(bin(len(dictionary)-1).replace("0b", "")):
    # while len(current_index) < len(bin(len(dictionary) - 1)):
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










### encoding sequence of symbols
def lzw_encode(file):
    # создание начального словаря
    dictionary=init_dict(file)

    # сохранение начального словаря для записи в зашифрованный файл
    # initial_dictionary=''.join(init_dict(file))
    initial_dictionary=init_dict(file)

    # зашифрованный файл
    code = ''

    # предыдущая последовательность
    last_seq=''

    # длина самой большой последовательности из словаря
    max_seq=max_length(dictionary)

    # steps
    # step=0

    ### пока не закончится файл
    while file!='':
        # steps
        # print('step № '+str(step))

        # из файла берется последовательность символов,
        # длина которой равна длине самой большой последовательности в словаре
        current_seq=file[:max_seq]
        # print('sequence: '+current_seq)

        # пока последовательности нет в словаре укорачивается на 1
        while current_seq not in dictionary:
            current_seq=current_seq[:-1]

        # добавление новой последовательности (предыдущая+первый символ текущей)
        if (last_seq+current_seq[0]) not in dictionary:
            dictionary.append(last_seq + current_seq[0])
            # длина самой большой записи в словаре
            max_seq = max_length(dictionary)


        # добавляем к коду индекс последовательности
        code+=get_index(dictionary, current_seq)

        # print
        # print('current sequence: ' + current_seq)
        # print('index: '+get_index(dictionary, current_seq))
        # print('code: '+code)
        # print('file: '+file)
        # print('dictionary: '+str(dictionary))

        # обновляется предыдущая последовательность символов
        last_seq = current_seq
        # из начала файла удаляются зашифрованные символы
        file = file[len(current_seq):]

        # steps
        # step+=1
        # print('\n')

    return code, initial_dictionary













### MAIN ###

### прочитать файл, создать в зашифрованном файле начальный словарь в виде строки ('abcdef')

# чтение файла
file_name='input_file'
file=read_file(file_name)

print('FILE: '+file+'\n')



# кодирование файла
code, dict=lzw_encode(file)

print('CODE: '+code+'\n')
print('INIT DICTIONARY: '+str(dict)+'\n')

# change compressed_file
# записать словарь и код в зашифрованный файл
compress_file(code, dict, file_name)