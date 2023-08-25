# REPETITION_CODE
Implementation of a primitive error correction code. When encoding, the input data is repeated three times. Decoding is done based on the majority function.

Input and output text file.
The encoder repeats the input data three times.
Example: 'ABC' is repeated as 'ABCABCABC'.

The decoder compares the three parts of the input data and selects based on the majority method.
The decoder compares bits from three bytes.
Example: bits 000, 100, 010, 001 are decoded as 0; bits 111, 011, 101, 110 are decoded as 1.
