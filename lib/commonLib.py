import re


def verifyGstinNo (gstin):
    gstin = re.search ('[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9][0-9A-Z]{2}', gstin)
    if gstin:
        gstin = gstin.group(0)
    return gstin

def getMonthStr (monthNum, returnStrLen=-1):
    monthArr = []
    monthArr.append ('Invalid')
    monthArr.append ('January')
    monthArr.append ('Febuary')
    monthArr.append ('March')
    monthArr.append ('April')
    monthArr.append ('May')
    monthArr.append ('June')
    monthArr.append ('July')
    monthArr.append ('August')
    monthArr.append ('September')
    monthArr.append ('October')
    monthArr.append ('November')
    monthArr.append ('December')

    return monthArr[monthNum][0:returnStrLen]

def getStateList ():
    stateList = []
    stateList.append ('Jammu & Kashmir')    # 01
    stateList.append ('Himachal Pradesh')   # 02
    stateList.append ('Punjab')             # 03
    stateList.append ('Chandigarh')         # 04
    stateList.append ('Uttarakhand')        # 05
    stateList.append ('Haryana')            # 06
    stateList.append ('Delhi')              # 07
    stateList.append ('Rajasthan')          # 08
    stateList.append ('Uttar Pradesh')      # 09
    stateList.append ('Bihar')              # 10
    stateList.append ('Sikkim')             # 11
    stateList.append ('Arunachal Pradesh')  # 12
    stateList.append ('Nagaland')           # 13
    stateList.append ('Manipur')            # 14
    stateList.append ('Mizoram')            # 15
    stateList.append ('Tripura')            # 16
    stateList.append ('Meghalaya')          # 17
    stateList.append ('Assam')              # 18
    stateList.append ('West Bengal')        # 19
    stateList.append ('Jharkhand')          # 20
    stateList.append ('Orissa')             # 21
    stateList.append ('Chhattisgarh')       # 22
    stateList.append ('Madhya Pradesh')     # 23
    stateList.append ('Gujarat')            # 24
    stateList.append ('Daman & Diu')        # 25
    stateList.append ('Dadra & Nagar Haveli')   # 26
    stateList.append ('Maharashtra')    # 27
    stateList.append ('Andhra Pradesh') # 28
    stateList.append ('Karnataka')      # 29
    stateList.append ('Goa')            # 30
    stateList.append ('Lakshadweep')    # 31
    stateList.append ('Kerala')         # 32
    stateList.append ('Tamil Nadu')     # 33
    stateList.append ('Puducherry')     # 34
    stateList.append ('Andaman & Nicobar Islands')  # 35
    stateList.append ('Telangana')      # 36
    stateList.append ('Others')         # 37
    stateList.append ('')
    return stateList

def getStateCode (stateName):
    stateCode = '-1'
    stateName = stateName.strip()
    stateList = getStateList ()
    if stateName in stateList:
        stateCode = '%02d' % (stateList.index (stateName) + 1)
    return stateCode
