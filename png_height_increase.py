#!/usr/bin/python3

import sys
import struct
import zlib

if __name__ == '__main__':
    
    if len(sys.argv) != 4:
        print(f'Usage: python3 {sys.argv[0]} image.png output.png new_height_int')
        sys.exit(1)

    original = sys.argv[1]
    enlarged = sys.argv[2]
    height = int(sys.argv[3])
    
    with open(original, 'rb') as f:
        data = f.read()

    header = data[:33]
    height_bytes = struct.pack('>i',  height)
    header_new_height = header[:20] + height_bytes + header[24:]
    crc32 = zlib.crc32(header_new_height[12:29])
    crc32_bytes = struct.pack('>i', crc32)
    new_header = header_new_height[:29] + crc32_bytes

    with open(enlarged, 'wb') as f:
        f.write(new_header + data[33:])
