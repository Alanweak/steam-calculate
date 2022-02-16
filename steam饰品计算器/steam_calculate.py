import sys, os
from model1_remake import Model1
from model2_remake import Model2
import check_input as ci

def main_menu():
    #菜单栏
    print('作者:AlanYLM13'.center(52, '-'))
    print('Steam饰品计算器'.center(49, '-'))
    print('区服选择'.center(50, '-'))
    print('1)阿根廷'.ljust(20) + '2)俄罗斯')
    print('3)巴西服'.ljust(20) + '4)土耳其')
    print('5)退出')

def model_menu(area_name):
    #模块菜单栏
    print('作者:AlanYLM13'.center(52, '-'))
    print('Steam饰品计算器'.center(49, '-'))
    print('%s'.center(50, '*') % area_name)
    print('模式选择'.center(50, '-'))
    print('1)计算购买饰品价格\t2)计算市场交易后金额')
    print('3)更换区服\t\t4)退出')

def area_model_menu(area):
    #判断对应区服的菜单栏
    if area == 1:
        model_menu('阿根廷')
    elif area == 2:
        model_menu('俄罗斯')
    elif area == 3:
        model_menu('巴西')
    elif area == 4:
        model_menu('土耳其')

def main_menu_choose():
    main_menu()
    main_choose = input_choose()
    os.system('cls')
    if main_choose == 1:
        area_model_menu(main_choose)
        return main_choose
    elif main_choose == 2:
        area_model_menu(main_choose)
        return main_choose
    elif main_choose == 3:
        area_model_menu(main_choose)
        return main_choose
    elif main_choose == 4:
        area_model_menu(main_choose)
        return main_choose
    elif main_choose == 5:
        os.remove('./Data/save_data.json')
        sys.exit()

def model_choose(area):
    model1 = Model1()
    model2 = Model2()
    model_choose = input_choose('model_menu', model_area=area)
    os.system('cls')
    while True:
        os.system('cls')
        if model_choose == 1:       #选择-模块1       
            model1.model1_choose_menu(area)
            model1.model1_choose(area)
            os.system('cls')
            area_model_menu(area)
            model_choose = input_choose('model_menu',model_area=area)
        elif model_choose == 2:     #选择-模块2
            model2.model2_choose_menu(area)
            model2.model2_choose(area)
            os.system('cls')
            area_model_menu(area)
            model_choose = input_choose('model_menu',model_area=area)
        elif model_choose == 3:     #选择-更换区服
            break                   
        elif model_choose == 4:
            os.remove('./Data/save_data.json')
            sys.exit()
        elif model_choose == 'r':
            os.system('cls')
            area_model_menu(area)
            model_choose = input_choose('model_menu',model_area=area)

def input_choose(mode='main_menu', model_area=None):
    input_int = None
    if mode == 'main_menu' and model_area == None:
        while True:
            os.system('cls')
            main_menu()
            if input_int == None:
                input_int = ci.input_check_int('请输入(1~5)数值进行选择:', 
                                            max= 5, min= 1, errorType=True)
            elif input_int == ValueError or input_int == -1:
                input_int = ci.input_check_int('输入错误!请输入(1~5)数值进行选择:',
                                            max=5, min=1, errorType=True)
                continue
            else:
                return input_int
    elif mode == 'model_menu' and model_area != None:
        while True:
            os.system('cls')
            area_model_menu(model_area)
            if input_int == None:
                input_int = ci.input_check_int('请输入(1~4)数值进行选择:', 
                                            max= 5, min= 1, errorType=True)
            elif input_int == ValueError or input_int == -1:
                input_int = ci.input_check_int('输入错误!请输入(1~4)数值进行选择:',
                                            max=5, min=1, errorType=True)
                continue
            else:
                return input_int

if __name__ == '__main__':
    while True:             #程序主循环
        os.system('cls')
        area = main_menu_choose()
        model_choose(area)
    
        
