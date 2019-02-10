def lz77():
    readFile = open("inputFile.txt", "r")
    inputString = readFile.read()
    print(len(inputString));
    compressed = compress(inputString);
    print(len(compressed)/8);
    decompressed = decompress(compressed);
    if (inputString == decompressed):
        print("Success");
    else:
        print("fail");
def compress(inputString):
    buffer = inputString;
    window = "";
    compressed = "";
    zero16 = '{0:016b}'.format(0);
    zero8 = bin(0)[2:].zfill(8);
    while (len(buffer) != 0):
        char = buffer[0];  
        buffer = buffer[1:];
        if char not in window or len(buffer) == 0:
            triplet = "00" + char;
            window += char ;
            encodedTriplet = zero16 + zero8 + bin(ord(triplet[2]))[2:].zfill(8)
        else:
            substring = char;
            while (substring in window):
                if (len(buffer) != 0):
                    substring += buffer[0];
                    buffer = buffer[1:];
                else:
                    break;
            pos = len(window) - window.find(substring[:-1]);
            triplet = str(pos) + "," + str(len(substring) - 1) + "," + substring[-1:];
            length = len(substring) - 1
            window += (substring);
            encodedTriplet = '{0:016b}'.format(pos) + bin(length)[2:].zfill(8) + bin(ord(substring[-1:]))[2:].zfill(8)
        compressed += encodedTriplet;
    return compressed

def decompress(compressed):
    window = "";
    i = 0;
    plaintext = ""
    while i in range(len(compressed) - 9):
        byte = compressed[i:(i+16)]
        pos = int(byte, 2);
        i += 16;
        byte = compressed[i:(i+8)]
        length = int(byte, 2);
        i += 8;
        byte = compressed[i:(i+8)]
        char = chr(int(byte, 2));
        i += 8;
        if (pos == 0 and length == 0):
            window += char;
        else:
            startPos = len(window) - int(pos)
            endPos = startPos + int(length)
            substring = window[startPos:endPos] + char
            window += substring
    return window;

