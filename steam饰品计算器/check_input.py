def input_check_str(prompt=""):
        input_string = input(prompt)
        try:
            input_string = input_string[0]
        except IndexError:
            return IndexError
        return input_string
    
def input_check_float(prompt="", abs=None, errorType=None):
    while True:
        input_float = input(prompt)
        if input_float == 'r':
            return 'r'
        else:
            try:
                input_float = float(input_float)
            except ValueError:
                if errorType == True:
                    return ValueError
                elif errorType == None:
                    print('\'%s\'这不是一个浮点数!' % input_float)
                    continue
            else:
                if abs == True:
                    if input_float >= 0:
                        return input_float
                    elif input_float < 0:
                        return -1
                else:
                    return input_float
                
def input_check_int(prompt="", max=None, min=None, abs=None, errorType=None):
    while True:
        input_int = input(prompt)
        if input_int == 'r':
            return 'r'
        else:
            try:
                input_int = int(input_int)
            except ValueError:
                if errorType == True:
                    return ValueError
                elif errorType == None:
                    print('\'%s\'这不是一个整数!' % input_int)
                    continue
            else:
                if abs == True:
                    if input_int >= 0:
                        return input_int
                    elif input_int < 0:
                        return -1
                if max != None or min != None:
                    if input_int > max or input_int < min:
                        if errorType == True:
                            return ValueError
                        elif errorType == False:
                            print('请输入在%s~%s的值' % (min, max))
                            continue
                    else:
                        return input_int
                else:
                    return input_int



def input_check_yes_no(prompt="", YesValue="", NoValue=""):
    input_string = input(prompt)
    if input_string == 'yes' or input_string == YesValue:
        return input_string
    elif input_string == 'no' or input_string == NoValue:
        return input_string
    else:
        return 0