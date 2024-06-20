import sys
import subprocess


# this file reads "input_file", runs lzw files, encodes input file and returns decoded file


### run lzw_compress.py
arg1 = "input_file"
subprocess.run(['python3', 'lzw_compress.py', arg1])


### run lzw_uncompress.py
arg2 = "input_file_archive"
arg3 = "input_file_decoded"
subprocess.run(['python3', 'lzw_uncompress.py', arg2, arg3])





# 000000010010001101000101011000111010000100110000100101000110100001111001110001110010100101000001110011011100011110001001010110011000011101010100011001011101100000011111100011100010010000101001011101



