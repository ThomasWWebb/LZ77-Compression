# Lempel-Ziv compression

An implementation of the LZ77 lossless data compression algorithm for text. A set of text is converted to binary, compressed and then decompressed following LZ77. 

## Use

The file **LZ77.py** takes 3 arguments in the CLI. 

    python LZ77.py textFile.txt slidingWindowBits lookAheadBufferBits

`textFile.txt` is a string that contains the name of the file with the text to compress. The latter two arguments are both integers; `slidingWindowBits` is the number of bits used to encode the sliding window, and `lookAheadBufferBits` is the number of bits used to encode the look-ahead buffer.

Running LZ77.py will produce two text files. **compressed.bin** contains the binary produced from the text compression and **decompressed.txt** contains the decompressed text.