import os
import check_input as ci
import json_load_and_save as jls

class Model2():
    '''初始化必需数值'''
    def __init__(self):
        self.filename = './Data/save_data.json'
        self.dict = jls.json_read_file(self.filename)
    
    def model2_menu(self, area_name):
        print('作者:AlanYLM13'.center(56, '-'))
        print('Steam饰品计算器'.center(53, '-'))
        print('%s'.center(52, '*') % area_name)
        print('计算交易后金额'.center(51, '-'))
        print('s)开始新的计算\t\tc)使用模式1购物车和余额进行计算')
        print('q)返回模式选择\t\tr)重新选择功能或退出当前输入')
    
    def model2_choose_menu(self, area):
        if area == 1:
            self.model2_menu('阿根廷服')
        elif area == 2:
            self.model2_menu('俄罗斯服')
        elif area == 3:
            self.model2_menu('巴西服')
        elif area == 4:
            self.model2_menu('土耳其')

    def model2_choose(self, area):
        choose_response = ci.input_check_str('请输入您的选择(s、c、q、r):')
        while True:
            if choose_response == 's':
                os.system('cls')
                self.model2_choose_menu(area)
                q_or_c_flag = self.start_cal1(area)
                if q_or_c_flag == -1:
                    choose_response = ci.input_check_str('请输入您的选择(s、c、q、r):')
                    continue
                elif q_or_c_flag == 0:
                    break
            elif choose_response == 'c':
                os.system('cls')
                self.model2_choose_menu(area)
                flag = self.start_cal2(area)
                if flag == -2:
                    choose_response = ci.input_check_str('请输入您的选择(s、c、q、r):')
                    continue
                elif flag == -1:
                    print('没有将游戏加入购物车或没输入Steam余额!')
                    choose_response = ci.input_check_str('请重新输入您的选择(s、c、q、r):')
                elif flag == 0:
                    break
            elif choose_response == 'q':
                break
            elif choose_response == 'r':
                os.system('cls')
                self.model2_choose_menu(area)
                choose_response = ci.input_check_str('请输入您的选择(s、c、q、r):')
                continue
            else:
                os.system('cls')
                self.model2_choose_menu(area)
                choose_response = ci.input_check_str('请输入正确的选择(s、c、q、r):')
                continue
    
    def start_cal1(self, area):
        '''功能1计算函数'''
        exchange_rate = 0.87
        money_remain = 0
        while True:
            while True:
                goods_cost = self.input_good_cost(area)
                if goods_cost == 'r':
                    return -1
                else:
                    break
            while True:
                current_game_cost = self.input_current_game_cost(area)
                if current_game_cost == 'r':
                    return -1
                else:
                    break
            mark_price = goods_cost * exchange_rate + money_remain
            self.area_output(area, mark_price, money_remain, current_game_cost)

            choose_continue = ci.input_check_yes_no('是否需要继续使用该模式:', 'y', 'n')
            if choose_continue == 'yes' or choose_continue == 'y':
                os.system('cls')
                self.model2_choose_menu(area)
                return -1
            elif choose_continue == 'no' or choose_continue == 'n':
                return 0

    def start_cal2(self, area):
        dict = jls.json_read_file(self.filename)
        current_game_cost = dict['total_game_cost']
        money_remain = dict['money_remain']
        exchange_rate = 0.87
        while True:
            if current_game_cost == None or money_remain == None:   #检查在模式1当中是否存在游戏价格以及Steam余额
                return -1                                        
            else:
                while True:
                    good_cost = self.input_good_cost(area)
                    if good_cost == 'r':
                        return 'r'
                    else:
                        break
                mark_price = good_cost * exchange_rate 
                self.area_output(area, mark_price, money_remain, current_game_cost)

                choose_continue = ci.input_check_yes_no('是否需要继续使用该模式(y/n):', 
                                                    YesValue='y', NoValue='n')
                if choose_continue == 'yes' or choose_continue == 'y':
                    os.system('cls')
                    self.model2_choose_menu(area)
                    return -2
                elif choose_continue == 'no' or choose_continue == 'n':
                    return 0
                
    def area_output(self, area, get_good_cost, money_remain, current_game_cost):
        '''按照输入地区，进行相应的字符打印'''
        area_money_list = ['ARS$', '₽', 'R$', '₺']          #以列表的形式存储各国货币名称

        print('当前的Steam余额是%.2f%s' % (money_remain, area_money_list[area-1]))
        print('交易后Steam余额是%.2f%s' % (money_remain+get_good_cost, area_money_list[area-1]))
        print('该饰品交易后价格是%.2f%s' % (get_good_cost, area_money_list[area-1]))
        
        if get_good_cost+money_remain >= current_game_cost:
            print('这个饰品非常适合入手，进行Steam市场交易!')
        else:
            print('这个饰品不适合入手，请另行选择!')
    
    def input_good_cost(self, area):
        goods_cost = None
        while True:                                 #检查值是否正确
            os.system('cls')
            self.model2_choose_menu(area)
            if goods_cost == None:
                goods_cost = ci.input_check_float('请输入饰品在Steam市场上的价格:', 
                                                            abs=True, errorType=True)
            elif goods_cost == ValueError or goods_cost == -1:
                goods_cost = ci.input_check_float('输入Steam市场上饰品的价格数值错误!请输入非负小数点:', 
                                                            abs=True, errorType=True)
                continue
            elif goods_cost == 'r':
                return 'r'
            else:
                return goods_cost
    
    def input_current_game_cost(self, area):
        current_game_cost = None
        while True:                                 #检查值是否正确
                os.system('cls')
                self.model2_choose_menu(area)
                if current_game_cost == None:
                    current_game_cost = ci.input_check_float('请输入当前区服游戏的价格:',
                                                                    abs=True, errorType=True)
                elif current_game_cost == ValueError or current_game_cost == -1:
                    current_game_cost= ci.input_check_float('输入游戏价格数值错误!请输入非负小数点:',
                                                                        abs=True, errorType=True)
                elif current_game_cost == 'r':
                    return 'r'
                else:
                    return current_game_cost






