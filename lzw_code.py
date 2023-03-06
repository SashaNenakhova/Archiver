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







# convert index of sequence to bin code
# добавить нули в начало
# (encoding)
def get_index(dictionary, n):
    # максимальное количество цифр в индексе
    max_index=len(bin(len(dictionary)-1).replace("0b", ""))

    # количество цифр в индексе
    current_index=str(bin(dictionary.index(n)).replace("0b", ""))

    # добавлять нули в начало, пока длина индекса не равна максимальному количеству цифр
    while len(current_index)<max_index:
        current_index='0'+current_index
    return current_index


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


# find max length
# (encoding)
def max_length(dictionary):
    l=0
    for i in dictionary:
        if len(i)>l:
            l=len(i)
    return l








### encoding sequence of symbols
def encode_file(file):
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

        # пока последовательности нет в словаре укорачивается на 1
        while current_seq not in dictionary:
            current_seq=current_seq[1:]

        # добавление новой последовательности (предыдущая+первый символ текущей)
        if (last_seq+current_seq[0]) not in dictionary:
            dictionary.append(last_seq + current_seq[0])
            # длина самой большой записи в словаре
            max_seq = max_length(dictionary)


        # добавляем к коду индекс последовательности
        code+=get_index(dictionary, current_seq)

        print('current sequence: ' + current_seq)
        print('code: '+code)
        print('file: '+file)
        print('dictionary: '+str(dictionary))

        # обновляется предыдущая последовательность символов
        last_seq = current_seq
        # из начала файла удаляются зашифрованные символы
        file = file[max_seq + 1:-1]

        # steps
        step+=1
        print('\n')

    return code









### decoding
def decode(code):
    pass








#### MAIN ####

# чтение файла
file=read_file('input_file')

# кодирование файла
code=encode_file(file)

print('ENCODED FILE: '+code+'\n')














