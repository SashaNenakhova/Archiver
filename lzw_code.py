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



# convert index of char to bin code
def bin_code(dictionary, n):
    return bin(dictionary.index(n)).replace("0b", "")


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
def sequence_legth(dictionary):
    l=0
    for i in dictionary:
        if len(i)>l
            l=len(i)
    return l


### encoding sequence of symbols
def encode_file(symbols, dictionary):
    while symbols!='':
        if symbols[:max_seq] in dictionary:
            pass

    


    return code, dictionary



#### MAIN ####

symbols=read_file('input_file') # последовательность символов
dictionary=init_dict(symbols) # начальный словарь
# code=''
max_seq=sequence_legth(dictionary) # длина самой большой записи в словаре

print(dictionary)
print(dictionary[3] + '    '+str(bin_code(dictionary, 'c')))
print(str(max_seq)+'  last sequence length')


code, dictionary=encode_file(symbols, dictionary)

print(dictionary)
print(code)












