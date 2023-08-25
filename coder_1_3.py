#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu June 27 19:56:10 2023

@author: kkuznetzov
"""

from os.path import dirname, join as pjoin
import numpy as np
import os

# Primitive Encoding Implementation

# Input data file
# Имя файла с входными данными, в текстовом файле
data_file_in_name = 'raw_data.txt'
data_file_in_name = os.path.join(os.path.dirname(__file__), data_file_in_name)

# Name of the output data file
# Имя выходного файла с данными
data_file_out_name = 'coded_data.txt'
data_file_out_name = os.path.join(os.path.dirname(__file__), data_file_out_name)

# Open input txt file for reading
# Открываем файл на чтение
data_in_file = open(data_file_in_name, "rb")

# Reading input file
# Читаем входной файл
input_signal_data = bytearray(data_in_file.read())
input_signal_length_bytes = len(input_signal_data)

# Длина выходного файла
output_signal_length_bytes = input_signal_length_bytes * 3

# Empty array for output
# Пустой массив для выходных данных
output_signal_data = bytearray(output_signal_length_bytes)

# Implementation method, 0 - C, 1 - Python
# Метод реализации, 0 - C, > 1  - Python
code_method = 1

# See what method is selected
# Смотрим какой метод выбран
if code_method == 0:
    # C style

    # Coding 3:1
    for i in range(int(input_signal_length_bytes)):
        output_signal_data[i] = input_signal_data[i]
        output_signal_data[input_signal_length_bytes * 2 + i] = input_signal_data[i]
        output_signal_data[input_signal_length_bytes + i] = input_signal_data[i]

else:
    # Python style

    # Coding 3:1
    output_signal_data[0:input_signal_length_bytes:1] = input_signal_data
    output_signal_data[input_signal_length_bytes:input_signal_length_bytes * 2:1] = input_signal_data
    output_signal_data[input_signal_length_bytes * 2::1] = input_signal_data

# Write the data file
# Записываем файл с данными
file = open(data_file_out_name, "wb")
file.write(output_signal_data)
file.close()






