f=open('cat.gif', 'rb')
data=f.read()

res_file = open('cat_5.gif', 'wb')
res_file.close()


f = open('cat_5.gif', 'ab')
while data != b'':

    part=data[:64]
    data=data[64:]

    f.write(part)