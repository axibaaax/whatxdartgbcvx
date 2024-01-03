# @Coding：utf-8
# @Time:2024/1/3 18:59
# @Author: yfgu
# @File: Driver_document.py
# @Version:

import re


def read_hspice_dciv_lis_file(file_path):
    '''
    :param file_path: 读取lis文件内容，并将其中的数据转换成字典形式
    :return:
    '''
    data_dict = {}
    current_source = None
    reading_data = False
    current_data = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.__contains__('source'):
                current_source = line.split(':')[1].split('=')[1].replace('*', '').strip()
                current_data = []
                reading_data = True
            elif line == 'x':
                if reading_data:
                    # Skip the next 3 lines after encountering "x"
                    file.readline()
                    file.readline()
                    file.readline()
            elif line == 'y':
                if reading_data:
                    # Add data to the dictionary when encountering "y"
                    data_dict[current_source] = current_data[1:]
                    reading_data = False
            elif reading_data:
                # Extracting data columns and converting to float
                data_values = [float(value) for value in line.split()]
                current_data.append(data_values)

    return data_dict


def transfer_and_write_pms_data(data_dict, output_file_path):
    '''
    :param data_dict: 将字典数据重新组合后，生成pms形式的文件数据
    :param output_file_path: 输出pms文件
    :return:
    '''
    # Get the keys from data_dict
    sources = list(data_dict.keys())

    # Open the output file for writing
    with open(output_file_path, 'w') as output_file:

        # Write header
        header = "\t".join(["Column 1", "Column 2", "Column 3", "...\n"])
        output_file.write(header)

        for index in range(1, len(data_dict)+1):
            sentence = "******NO{}*******\n".format(index)
            output_file.write(sentence)

            # Define a format string for scientific notation with 5 decimal places
            sci_format = "{:.5e}"

            # Iterate over the range of data points (assuming all sources have the same length)
            for j in range(len(data_dict[sources[0]])):
                # Write data for each source to the output file
                output_file.write(sci_format.format(data_dict[sources[0]][j][0]))

                # Write data for each data segment
                for i, source in enumerate(sources[1:], start=1):
                    output_file.write("\t" + sci_format.format(data_dict[source][j][i]))

                output_file.write("\n")


def main():

    file_in_path = r'idvg_nmos.lis'
    # result = read_hspice_dciv_lis_file(file_in_path)

    file_out_path = r'idvg_nmos.pms'
    # transfer_and_write_pms_data(result, file_out_path)


if __name__ == "__main__":
    main()
