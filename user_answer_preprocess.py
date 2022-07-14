def user_AGEG5YR(user_age):
    age_level = [17, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79]
    if user_age > age_level[-1]:
        return 13
    for i in range(len(age_level)):
        if age_level[i] < user_age <= age_level[i+1]:
            return i+1
def user_MENT14D(var_MENT14D):
    option = ['0 days', '1-13 days', '14-31 days']
    return 9 if var_MENT14D not in option else option.index(var_MENT14D)+1
def userDECIDE(varDECIDE):
    option = ['Yes', 'No']
    return 7 if varDECIDE not in option else option.index(varDECIDE)+1
def userDIFFALON(varDIFFALON):
    option = ['Yes', 'No']
    return 7 if varDIFFALON not in option else option.index(varDIFFALON)+1
def userACEDEPRS(varACEDEPRS):
    option = ['Yes', 'No']
    return 7 if varACEDEPRS not in option else option.index(varACEDEPRS)+1
def userEMPLOY1(varEMPLOY1):
    option = ['Employed for wages', 'Self-employed', 'Out of work for 1 year or more', 'Out of work for less than 1 year', \
        'A homemaker', 'A student', 'Retired', 'Unable to work', 'Refused']
    return option.index(varEMPLOY1)+1
def userGENHLTH(varGENHLTH):
    option = ['Excellent', 'Very good', 'Good', 'Fair', 'Poor']
    return 7 if varGENHLTH not in option else option.index(varGENHLTH)+1
def userMARITAL(varMARITAL):
    option = ['Married', 'Divorced', 'Widowed', 'Separated', 'Never married', 'A member of an unmarried couple']
    return 9 if varMARITAL not in option else option.index(varMARITAL)+1
def user_SMOKER3(var_SMOKER3):
    option = ['Current smoker - now smokes every day', 'Current smoker - now smokes some days', 'Former smoker', 'Never smoked']
    return 9 if var_SMOKER3 not in option else option.index(var_SMOKER3)+1
def user_DRDXAR2(var_DRDXAR2):
    option = ['Diagnosed with arthritis', 'Not diagnosed with arthritis']
    return 0 if var_DRDXAR2 not in option else option.index(var_DRDXAR2)+1
def userSOFEMALE(varSOFEMALE):
    option = ['Lesbian or Gay', 'Straight, that is, not gay', 'Bisexual', 'Something else']
    return 9 if varSOFEMALE not in option else option.index(varSOFEMALE)+1
def userRENTHOM1(varRENTHOM1):
    option = ['Own', 'Rent', 'Other arrangement']
    return option.index(varRENTHOM1)+1
def user_TOTINDA(var_TOTINDA):
    option = ['Yes', 'No']
    return 9 if var_TOTINDA not in option else option.index(var_TOTINDA)+1
def userEDUCA(varEDUCA):
    option = ['Never attended school or only kindergarten', 'Elementary', 'Some high school', 'High school graduate', \
                'Some college or technical school', 'College graduate']
    return 9 if varEDUCA not in option else option.index(varEDUCA)+1
def userPERSDOC2(varPERSDOC2):
    option = ['Yes, only one', 'More than one', 'No']
    return 7 if varPERSDOC2 not in option else option.index(varPERSDOC2)+1
def userINCOME2(varINCOME2):
    option = ['Less than $10,000', '$10,000 to less than $15,000', '$15,000 to less than $20,000', '$20,000 to less than $25,000', '$25,000 to less than $35,000', \
                '$35,000 to less than $50,000', '$50,000 to less than $75,000', '$75,000 or more']
    if varINCOME2 == 'Not Sure':
        return 77
    return 99 if varINCOME2 not in option else option.index(varINCOME2)+1
def user_URBSTAT(var_URBSTAT):
    option = ['Yes', 'No']
    return 0 if var_URBSTAT not in option else option.index(var_URBSTAT)+1