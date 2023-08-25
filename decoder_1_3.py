#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu June 27 19:56:10 2023

@author: kkuznetzov
"""

from os.path import dirname, join as pjoin
import numpy as np
import os

# Primitive Decoder Implementation

# Input data file
# Имя файла с входными данными, в текстовом файле
data_file_in_name = 'coded_data.txt'
data_file_in_name = os.path.join(os.path.dirname(__file__), data_file_in_name)

# Name of the output data file
# Имя выходного файла с данными
data_file_out_name = 'decoded_data.txt'
data_file_out_name = os.path.join(os.path.dirname(__file__), data_file_out_name)

# Open input txt file for reading
# Открываем файл на чтение
data_in_file = open(data_file_in_name, "rb")

# Reading input file
# Читаем входной файл
input_signal_data = bytearray(data_in_file.read())
input_signal_length_bytes = len(input_signal_data)

# Длина выходного файла
output_signal_length_bytes = input_signal_length_bytes // 3

# Empty array for output
# Пустой массив для выходных данных
output_signal_data = bytearray(output_signal_length_bytes)

# Bytes and bites
# Байты и биты
byte_a = 0
byte_b = 0
byte_c = 0
bit_a = 0
bit_b = 0
bit_c = 0
out_byte = 0
out_bit_a = 0
out_bit_b = 0
out_bit_c = 0
out_bit = 0

# Implementation method, 0 - Compare, 1 - Majority function
# Метод реализации, 0 - сравнение, > 1  - мажоритарная фукнция
code_method = 1

# See what method is selected
# Смотрим какой метод выбран
if code_method == 0:
    # Compare bits

    # Decoder 3:1
    # Compare method
    # Loop through bytes
    for i in range(int(output_signal_length_bytes)):
        byte_a = input_signal_data[i]
        byte_b = input_signal_data[i + output_signal_length_bytes]
        byte_c = input_signal_data[i + output_signal_length_bytes * 2]

        # Reset
        out_byte = 0

        # Loop through bites
        for j in range(0x08):
            # Get low bit value
            bit_a = byte_a & 0x01
            bit_b = byte_b & 0x01
            bit_c = byte_c & 0x01

            # Right shift
            byte_a = byte_a >> 0x01
            byte_b = byte_b >> 0x01
            byte_c = byte_c >> 0x01

            # Compare bits
            if bit_a == bit_b:
                out_bit = bit_a
            if bit_a == bit_c:
                out_bit = bit_a
            if bit_b == bit_c:
                out_bit = bit_c

            # Save bit to output byte
            out_byte = out_byte + (out_bit << j)

        # Save to output byte array
        output_signal_data[i] = out_byte

else:
    # Majority function

    # Decoder 3:1
    # Majority method
    # Loop through bytes
    for i in range(int(output_signal_length_bytes)):
        byte_a = input_signal_data[i]
        byte_b = input_signal_data[i + output_signal_length_bytes]
        byte_c = input_signal_data[i + output_signal_length_bytes * 2]

        # Reset
        out_byte = 0

        # Loop through bites
        for j in range(0x08):
            # Get low bit value
            bit_a = byte_a & 0x01
            bit_b = byte_b & 0x01
            bit_c = byte_c & 0x01

            # Right shift
            byte_a = byte_a >> 0x01
            byte_b = byte_b >> 0x01
            byte_c = byte_c >> 0x01

            # Majority method
            out_bit_a = ~(bit_a & bit_b)
            out_bit_b = ~(bit_a & bit_c)
            out_bit_c = ~(bit_b & bit_c)
            out_bit = ~(out_bit_a & out_bit_b & out_bit_c)

            # Save bit to output byte
            out_byte = out_byte + (out_bit << j)

        # Save to output byte array
        output_signal_data[i] = out_byte

# Write the data file
# Записываем файл с данными
file = open(data_file_out_name, "wb")
file.write(output_signal_data)
file.close()