# 000 001 000 010 101 0000 0011 0101 0100 1011 0001 0100 1001  01000 01000 01110 01010 01101 01100 01000
#  a   b   a   c   ab   a   d     ab    e   da   b    e   aba    ca     ca  dab     ad   ed   abe    ca



# dict
# a=000
# b=001
# c=010
# d=011
# e=100

# ab=101
# ba=110
# ac=111

# ca=1000
# aba=1001
# ad=1010
# da=1011
# abe=1100
# ed=1101
# dab=1110
# be=1111

# ea=10000
# abac=10001
# cac=10010
# cad=10011
# daba=10100
# ade=10101
# eda=10111
# abec=11000


# abacabadabedabeabacacadabadedabeca

############################################################


# reading file
# (encoding)
def read_file(file_name):
    try:
        file=open(file_name, 'r')
        return file.read()
    except:
        pass


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









### encoding sequence of symbols
def encode(file):
    # создание начального словаря
    dictionary=init_dict(file)

    # зашифрованный файл
    code = ''

    # предыдущая последовательность
    last_seq=''

    # длина самой большой последовательности из словаря
    max_seq=max_length(dictionary)

    # steps
    step=0

    ### пока не закончится файл
    while file!='':
        # steps
        print('step № '+str(step))

        # из файла берется последовательность символов,
        # длина которой равна длине самой большой последовательности в словаре
        current_seq=file[:max_seq]
        print('sequence: '+current_seq)

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
        print('current sequence: ' + current_seq)
        print('index: '+get_index(dictionary, current_seq))
        print('code: '+code)
        print('file: '+file)
        print('dictionary: '+str(dictionary))

        # обновляется предыдущая последовательность символов
        last_seq = current_seq
        # из начала файла удаляются зашифрованные символы
        file = file[len(current_seq):]

        # steps
        step+=1
        print('\n')

    return code









### decoding
def decode(code, dictionary):
    # расшифрованный файл
    file=''

    # предыдущая последовательность
    last_seq = ''

    # длина последнего кода в словаре
    max_num=max_index(dictionary)

    # steps
    step=0

    # пока не закончится зашифрованный файл
    while code!='':
        # steps
        print('step № '+str(step))

        # из зашифрованного файла берется часть кода,
        # длина которой равна длине последнего кода в словаре
        current_code=code[:max_num]
        print('index: ' + str(current_code))

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
        print('current sequence: ' + current_seq)
        print('current index: ' + str(current_code))
        print('code: '+code)
        print('file: '+file)
        print('dictionary: '+str(dictionary))

        # обновляется предыдущая последовательность символов
        last_seq = current_seq                                  ############      !!!!!!!!!!!! last seq
        # из начала файла удаляются зашифрованные символы
        # code = code[max_num + 1:-1]
        code = code[len(str(current_code)):]

        # steps
        step+=1
        print('\n')

    return file








#### MAIN ####

# чтение файла
file=read_file('input_file')
# file=read_file('angry-cat-original.gif')
# кодирование файла
code=encode(file)

print('ENCODED FILE: '+code+'\n')

# расшифровка кода
dictionary=init_dict(file)
decoded_file=decode(code, dictionary)

print('DECODED CODE: '+decoded_file+'\n')


# daecbeadcebadbcedabcedeebbabedbebbeabababaedbcdeabcdeabcedacbedabcedebacbabedcbea
# decoded:
# daecbeadcebadbcedabcedeebbabedbebbeabababaedbcdeabcdeabcedacbedabcedebacbabedcbea
#
# dictionary: ['d', 'a', 'e', 'c', 'b', 'de', 'ea', 'ae', 'ed', 'eb', 'be',
#               'ede', 'ebe', 'edb', 'ba', 'ab', 'bac', 'ca', 'abe', 'eae']



# abcdedf
# ['a', 'b', 'c', 'd', 'e', 'f', 'ab', 'bd', 'de', 'ef', 'ff']
#  ['a', 'b', 'c', 'd', 'e', 'f', 'ab', 'bd', 'dc', 'cf', 'ff']










