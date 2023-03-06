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
def get_index(dictionary, n):
    # максимальное количество цифр в индексе
    max_index=len(bin(len(dictionary)-1).replace("0b", ""))
    # print(str(max_index)+' max_index')

    # количество цифр в индексе
    current_index=str(bin(dictionary.index(n)).replace("0b", ""))

    # добавить нули в начало
    while len(current_index)<max_index:
        current_index='0'+current_index
    return current_index


# reading file
def read_file(file_name):
    try:
        file=open(file_name, 'r')
        return file.read()
    except: 
        pass


# creating initial dict
def init_dict(symbols):
    dictionary=[]
    for i in symbols:
        if i not in dictionary:
            dictionary.append(i)
    return dictionary


# find max length 
def sequence_length(dictionary):
    l=0
    for i in dictionary:
        if len(i)>l:
            l=len(i)
    return l


### encoding sequence of symbols
def encode_file(file, dictionary):
    last_seq='' # предыдущая последовательность
    max_seq=sequence_length(dictionary)

    step=0

    code='' # зашифрованный файл

    ### пока не закончится файл
    while file!='':
        # steps
        print('step № '+str(step))

        # current sequence max length
        current_seq=file[:max_seq]
        print('current sequence: '+current_seq)

        # если самая большая последовательность уже есть в словаре

        # if current_seq in dictionary:
        #     pass
        # else:
        #     dictionary.append(last_seq+current_seq[0])
        #     max_seq = sequence_length(dictionary)  # длина самой большой записи в словаре
        #     last_seq=current_seq

        while current_seq not in dictionary:
            current_seq=current_seq[1:]
        if (last_seq+current_seq[0]) not in dictionary:
            dictionary.append(last_seq + current_seq[0])
            max_seq = sequence_length(dictionary)  # длина самой большой записи в словаре


        # добавляем к коду индекс последовательности
        # сокращаем последовательность
        # last seq=cur seq
        # max seq

        code+=get_index(dictionary, current_seq)+'  '

        # print(current_seq)
        print('code: '+code)
        print('file: '+file)
        # print(str(max_seq)+' max seq')
        print('dictionary: '+str(dictionary))

        last_seq = current_seq
        file = file[max_seq + 1:-1]

        # print debug steps
        step+=1
        print('\n')




            

    


    return code, dictionary








#### MAIN ####

file=read_file('input_file') # последовательность символов
dictionary=init_dict(file) # начальный словарь
# code=''

# print(dictionary)
# print(dictionary[3] + '    '+str(get_index(dictionary, 'c')))
# print(str(max_seq)+'  max sequence length')


code, dictionary=encode_file(file, dictionary)

# print(dictionary)
# print(code)














