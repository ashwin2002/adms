import os

from data.excel import HeadersJul2020Current, HeadersTillJun2020


def is_row_blank(d_row):
    for data in d_row:
        if data is not None:
            return False
    return True


def is_file_exists(input_file_name, logger=None):
    file_exists = True
    if not(os.path.isfile(input_file_name)):
        file_exists = False
        if logger:
            logger.error("File '%s' does not exists !" % input_file_name)
    return file_exists


def get_next_col(curr_col):
    new_col = ""
    if len(curr_col) != 1:
        new_col = curr_col[0:-1]

    if curr_col[-1] != 'Z':
        new_col += chr(ord(curr_col[-1]) + 1)
    else:
        new_col += "AA"
    return new_col


def get_target_excel_class(gst_2yrm_val):
    if int(gst_2yrm_val[4:6]) < 7 and int(gst_2yrm_val[0:4]) <= 2020:
        return HeadersTillJun2020
    return HeadersJul2020Current

