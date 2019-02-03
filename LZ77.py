def LZ77():
    inputString = "abcadeabfabc "
    buffer = "abcadeabfabc ";
    window = "";
    encoded = "";
    while (len(buffer) != 0):
        char = buffer[0];
        buffer = buffer[1:];
        if char not in window:
            output = "00" + char;
            window += char ;
        else:
            substring = char;
            while (substring in window):
                if (len(buffer) != 0):
                    substring += buffer[0];
                    buffer = buffer[1:];                  
            print(char);
            print(substring);
            pos = len(window) - window.find(char);
            output = str(pos) + str(len(substring) - 1) + substring[-1:];
            window += (substring);
        encoded += output
        print(output);
        print("buffer " + buffer)
        print("window " + window)
    return encoded

def decode():
    buffer = LZ77();
    window = "";
    print(buffer);
    while (len(buffer) > 0):
        triplet = buffer[0:3];
        buffer = buffer[3:];
        if (triplet[0:2] == "00"):
            window += triplet[2];
        else:
            startPos = len(window) - int(triplet[0])
            endPos = startPos + int(triplet[1])
            substring = window[startPos:endPos] + triplet[2]
            print(substring)
            window += substring
        print(triplet);
    print(window);

