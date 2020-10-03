import json
import re


def verifyGstinNo(gstin):
    gstin = re.search('[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9][0-9A-Z]{2}', gstin)
    if gstin:
        gstin = gstin.group(0)
    return gstin


def getMonthStr(month_num, returnStrLen=-1):
    month_arr = ['Invalid',
                 'January', 'Febuary', 'March', 'April',
                 'May', 'June', 'July', 'August',
                 'September', 'October', 'November', 'December']
    return month_arr[month_num][0:returnStrLen]


def getStateList():
    state_list = list()
    state_list.append('Jammu & Kashmir')    # 01
    state_list.append('Himachal Pradesh')   # 02
    state_list.append('Punjab')             # 03
    state_list.append('Chandigarh')         # 04
    state_list.append('Uttarakhand')        # 05
    state_list.append('Haryana')            # 06
    state_list.append('Delhi')              # 07
    state_list.append('Rajasthan')          # 08
    state_list.append('Uttar Pradesh')      # 09
    state_list.append('Bihar')              # 10
    state_list.append('Sikkim')             # 11
    state_list.append('Arunachal Pradesh')  # 12
    state_list.append('Nagaland')           # 13
    state_list.append('Manipur')            # 14
    state_list.append('Mizoram')            # 15
    state_list.append('Tripura')            # 16
    state_list.append('Meghalaya')          # 17
    state_list.append('Assam')              # 18
    state_list.append('West Bengal')        # 19
    state_list.append('Jharkhand')          # 20
    state_list.append('Orissa')             # 21
    state_list.append('Chhattisgarh')       # 22
    state_list.append('Madhya Pradesh')     # 23
    state_list.append('Gujarat')            # 24
    state_list.append ('Daman & Diu')        # 25
    state_list.append('Dadra & Nagar Haveli')   # 26
    state_list.append('Maharashtra')    # 27
    state_list.append('Andhra Pradesh') # 28
    state_list.append('Karnataka')      # 29
    state_list.append('Goa')            # 30
    state_list.append('Lakshadweep')    # 31
    state_list.append('Kerala')         # 32
    state_list.append('Tamil Nadu')     # 33
    state_list.append('Puducherry')     # 34
    state_list.append('Andaman & Nicobar Islands')  # 35
    state_list.append('Telangana')      # 36
    state_list.append('Others')         # 37
    state_list.append('')
    return state_list


def getStateCode(state_name):
    state_code = '-1'
    state_name = state_name.strip()
    state_list = getStateList()
    if state_name in state_list:
        state_code = '%02d' % (state_list.index(state_name) + 1)
    return state_code


def loadJsonData(json_file_name):
    with open(json_file_name, 'r') as filePtr:
        json_obj = json.loads(filePtr.read())
    return json_obj
