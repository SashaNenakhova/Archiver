# chunk_size = 64 * 1024 # 64KB in bytes
chunk_size = 64
with open('input_file.txt', 'rb') as f:
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        # do something with the chunk
        print(chunk)