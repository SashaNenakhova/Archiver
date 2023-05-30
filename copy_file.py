import sys

if len(sys.argv)<3:
    pass
else:
    input_file=sys.argv[1]
    output_file=sys.argv[2]

    res_file = open(output_file, 'wb')
    res_file.close()

    f=open(input_file, 'rb')
    res_file = open(output_file, 'ab')

    # chunk_size = 64 * 1024 # 64KB in bytes
    chunk_size = 64
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        # do something with the chunk
        print(chunk)
        res_file.write(chunk)