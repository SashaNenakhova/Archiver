import sys

if len(sys.argv)<3:
    pass
else:
    input_file=sys.argv[1]
    output_file=sys.argv[2]


    f=open(input_file, 'rb')
    data=f.read()

    res_file = open(output_file, 'wb')
    res_file.close()


    f = open(output_file, 'ab')
    while data != b'':

        part=data[:64]
        data=data[64:]

        f.write(part)