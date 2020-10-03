import os


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
