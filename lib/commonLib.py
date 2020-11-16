import json
import re

from constants.common import month_arr, state_list


def verifyGstinNo(gstin):
    gstin = re.search('[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9][0-9A-Z]{2}', gstin)
    if gstin:
        gstin = gstin.group(0)
    return gstin


def getMonthStr(month_num, returnStrLen=-1):
    return month_arr[month_num][0:returnStrLen]


def getStateCode(state_name):
    state_code = '-1'
    state_name = state_name.strip()
    if state_name in state_list:
        state_code = '%02d' % (state_list.index(state_name) + 1)
    return state_code


def loadJsonData(json_file_name):
    with open(json_file_name, 'r') as filePtr:
        json_obj = json.loads(filePtr.read())
    return json_obj
