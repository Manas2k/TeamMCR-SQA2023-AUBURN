#Author: manas Kothamasu 
#Fuzzer
# Team MCR
from scanner import isValidUserName
from scanner import isValidPasswordName
from scanner import isValidKey
from scanner import checkIfValidSecret
from scanner import checkIfValidKeyValue
import sys
import traceback

def doFuzz(inputList, method):
    for inputItem in inputList:
        try:
            result = method(inputItem)
        except Exception:
            print("Exception in user code:")
            print(f'Fuzz:{method.__qualname__} failed!')
            print("-"*80)
            traceback.print_exc(file=sys.stdout)
            print("-"*80)
        else:
            if result == True:
                print(f'Fuzz:{method.__qualname__} passed!')
                print(f'Detect input value is valid:')
                print(f'Test value is {inputItem}')
                print("-"*50)
            else:
                print(f'Fuzz:{method.__qualname__} passed!')
                print(f'Detect input value is invalid:')
                print(f'Test value is {inputItem}')
                print("-"*50)

def generateFuzzValues(funcName):
    returnList = []
    validFuncNameList = ['isValidUserName','isValidPasswordName','isValidKey',\
                     'checkIfValidSecret', 'checkIfValidKeyValue']
    if (isinstance(funcName, str)==False) or (funcName not in validFuncNameList):
        print("Input function name is invalid!")
    else:
        if funcName == validFuncNameList[0]:
            returnList = [0,'undefined',None,'undef','null',\
                        'NULL','nil',\
                        'true',\
                        'hasOwnProperty',[]]
        elif funcName == validFuncNameList[1]:
            returnList = [10,'1E02','-2147483648/-1','-0',\
                        True,None,'1#IND',\
                        '0xabad1dea',\
                        '<>?:\"{}|_+',{}]
        elif funcName == validFuncNameList[2]:
            returnList = [10,'LPT1','$ENV{HOME}','`ls -al /`',\
                         True,None,'CLOCK$',\
                         '<foo val=“bar” />',\
                         '!@#$%^&*()`~',{} ]
        elif funcName == validFuncNameList[3]:
            returnList = [10,'⅛⅜⅝⅞','ÅÍÎÏ˝ÓÔÒÚÆ☃','œ∑´®†¥¨ˆøπ“‘',\
                        True,None,'和製漢語',\
                        '울란바토르',\
                        '( ͡° ͜ʖ ͡°)',[]]
        elif funcName == validFuncNameList[4]:
            returnList = [0,'﷽','<img src=x onerror=alert(123) />','http://a/%%30%30',\
                        True,None,'<plaintext>',\
                        '--version',\
                        '/dev/null; touch /tmp/blns.fail ; echo',{}]
        else:
            print("Input function name is invalid!")
    return returnList
if __name__=="__main__":
    method = [isValidUserName,isValidPasswordName,isValidKey,\
            checkIfValidSecret, checkIfValidKeyValue]
    testFuncCount = 1
    for funcNameDenote in method:
        print("*"*50)   
        print(" "*10,f'{testFuncCount}.{funcNameDenote.__qualname__}:')
        print("*"*50)
        returnedList = generateFuzzValues(funcNameDenote.__qualname__)
        doFuzz(returnedList, funcNameDenote)
        testFuncCount+=1