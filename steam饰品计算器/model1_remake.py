import os
import check_input as ci
import json_load_and_save as jls
class Model1():
    def __init__(self):
        '''初始化所需数据'''                                  
        self.dict = {'area_exchange_rate': [0.06413, 0.08174, 1.1557, 0.4700],  #汇率
                     'money_remain': None,                                      #steam余额
                     'total_game_cost': None,                                   #总游戏价格
                     'shopping_car': []}                                        #购物车    
        self.filename = './Data/save_data.json'
        if not(os.path.exists(self.filename)):
            jls.json_write_file(self.dict, self.filename)



    def model1_menu(self, area_name):
        print('作者:AlanYLM13'.center(52, '-'))
        print('Steam饰品计算器'.center(49, '-'))
        print('%s'.center(48, '*') % area_name)
        print('计算购买饰品价格'.center(46, '-'))
        print('s)开始计算\t\ti)将游戏加入至购物车')
        print('l)列出购物车列表\td)删除购物车的游戏')
        print('q)返回模式选择\t\tr)重新选择功能或退出当前输入')
    
    def model1_choose_menu(self, area):
        if area == 1:
            self.model1_menu('阿根廷服')
        elif area == 2:
            self.model1_menu('俄罗斯服')
        elif area == 3:
            self.model1_menu('巴西服')
        elif area == 4:
            self.model1_menu('土耳其')
    
    def model1_choose(self, area):
        choose_response = ci.input_check_str('请输入您的选择(s、i、l、d、q):')
        while True:
            if choose_response == 'd':               #删除购物车中指定的游戏
                self.del_game_data(area)
                choose_response = ci.input_check_str('请输入您的选择(s、i、l、d、q):')
                continue
            elif choose_response == 'q':             #退出当前模式
                break
            elif choose_response == 'i':             #将游戏加入至购物车
                self.input_game_data(area)
                choose_response = ci.input_check_str('请输入您的选择(s、i、l、d、q)?')
                continue
            elif choose_response == 's':
                os.system('cls')
                self.model1_choose_menu(area)
                q_or_c_flag = self.start_cal(area)
                if q_or_c_flag == 0:
                    break
                elif q_or_c_flag == -1:
                    choose_response = ci.input_check_str('请输入您的选择(s、i、l、d、q):')
                    continue
            elif choose_response == 'l':            #列出已经输入的数据
                os.system('cls')
                self.model1_choose_menu(area)               
                self.list_game_data(area)
                choose_response = ci.input_check_str('请输入您的选择?(s、i、l、d、q):')
                continue
            elif choose_response == 'r':
                os.system('cls')
                self.model1_choose_menu(area)
                choose_response = ci.input_check_str('请输入您的选择?(s、i、l、d、q):')
                continue
            else:
                os.system('cls')
                self.model1_choose_menu(area)
                choose_response = ci.input_check_str('请输入正确的选择(s、i、l、d、q):')
                continue
           
    def start_cal(self, area):
        while True:
            total_game_cost = 0
            shopping_game_num = len(self.dict['shopping_car'])
            if shopping_game_num > 0:
                for index in range(shopping_game_num):
                    total_game_cost += self.dict['shopping_car'][index]
            else:
                os.system('cls')
                self.model1_choose_menu(area)
                print('购物车没有游戏!')
                return -1                               #出现错误就返回-1
            while True:
                money_remain = self.input_money_remain(area)
                if money_remain == 'r':
                    return -1
                else:
                    break
            while True:
                goods_rate = self.input_good_rate(area)
                if goods_rate == 'r':
                    return -1
                else:
                    break

            need_cost = 0
            if total_game_cost < money_remain:                     #游戏价格与Steam余额比较确定计算差额
                need_cost = money_remain - total_game_cost
            elif total_game_cost > money_remain:
                need_cost = total_game_cost - money_remain
            elif total_game_cost == money_remain:
                need_cost = total_game_cost

            for i in range(1, len(self.dict['area_exchange_rate'])+1):
                if area == i:
                    need_cost = need_cost * self.dict['area_exchange_rate'][i-1] \
                                    * goods_rate
            
            print('应购买的饰品价格是%.2f人民币' % need_cost)

            choose_continue = ci.input_check_yes_no('是否需要继续使用该模式(y/n):', 'y', 'n')
            while True:
                if choose_continue == 'yes' or choose_continue == 'y':
                    os.system('cls')
                    self.model1_choose_menu(area)
                    self.dict['money_remain'] = money_remain
                    self.dict['total_game_cost'] = total_game_cost
                    jls.json_write_file(self.dict, self.filename)
                    return -1
                elif choose_continue == 'no' or choose_continue == 'n':
                    self.dict['money_remain'] = money_remain
                    self.dict['total_game_cost'] = total_game_cost
                    jls.json_write_file(self.dict, self.filename)
                    return 0
                else:
                    os.system('cls')
                    self.model1_choose_menu(area)
                    choose_continue = ci.input_check_yes_no('是否需要继续使用该模式(y/n):', 'y', 'n')
                    continue
    
    def input_money_remain(self, area):   
        money_remain = None
        while True:                                 #检查输入的Steam余额是否正确
            os.system('cls')
            self.model1_choose_menu(area)
            if money_remain == None:
                money_remain = ci.input_check_float('请输入Steam余额:', abs=True, errorType=True)
            elif money_remain == ValueError or money_remain == -1:
                money_remain = ci.input_check_float('输入Steam余额数值错误!请输入非负小数点:',
                                                    abs=True, errorType=True)
            elif money_remain == 'r':
                return 'r'
            else:
                return money_remain

    def input_game_cost(self, area, prompt=""):
        current_area_game_cost = None
        while True:                                 #检查输入的游戏价格是否正确    
            os.system('cls')
            self.model1_choose_menu(area)
            if current_area_game_cost == None:
                current_area_game_cost = ci.input_check_float(prompt, abs=True, errorType=True)
            elif current_area_game_cost == 'r':
                return 'r'
            elif current_area_game_cost == ValueError or current_area_game_cost == -1:
                current_area_game_cost = ci.input_check_float('输入游戏价格数值错误!请输入非负小数点:',
                                                                        abs=True, errorType=True)
                continue
            else:
                return current_area_game_cost
    
    def input_good_rate(self, area):
        goods_rate = None
        while True:                                 #检查输入的饰品比例是否正确
            os.system('cls')
            self.model1_choose_menu(area)
            if goods_rate == None:
                goods_rate = ci.input_check_float('请输入购买饰品的比例:', abs=True, errorType=True)
            elif goods_rate == ValueError or goods_rate == -1:
                goods_rate = ci.input_check_float('输入饰品比例数值错误!请输入非负小数点:',
                                                abs=True, errorType=True)
                continue
            elif goods_rate == 'r':
                return 'r'
            else:
                return goods_rate
    
    def input_game_data(self, area):
        game_num = None
        while True:                                 #检查输入的游戏数量是否正确
            os.system('cls')
            self.model1_choose_menu(area)
            if game_num == None:
                game_num = ci.input_check_int('请输入您想加入多少款游戏到购物车:', abs=True, errorType=True)
                continue
            elif game_num == 'r':
                break
            elif game_num == ValueError or game_num == -1:
                game_num= ci.input_check_int('输入游戏数量数值错误!请输入非负整数:',
                                                    abs=True, errorType=True)
                continue
            else:
                break
        
        if game_num == 'r':
            return 0
        else:
            for index in range(game_num):
                os.system('cls')
                self.model1_choose_menu(area)
                game_cost = self.input_game_cost(area, prompt='请输入当前区服游戏%d价格:' % (index+1))
                if game_cost == 'r':
                    return 0
                else:
                    self.dict['shopping_car'].append(game_cost)
                if index == game_num-1 :
                    os.system('cls')
                    self.model1_choose_menu(area)
                    print('已将所有游戏加入购物车!')
    
    def list_game_data(self, area):
        shopping_game_num = len(self.dict['shopping_car'])
        area_money_list = ['ARS$', '₽', 'R$', '₺']        #以列表的形式存储各国货币名称

        if shopping_game_num > 0:
            for index in range(shopping_game_num):
                print('游戏%d: %.2f%s' % (index+1, self.dict['shopping_car'][index],
                                        area_money_list[area-1]))
        elif shopping_game_num <= 0:
            print('购物车没有游戏!')
    
    def del_game_data(self, area):
        game_position = None
        choose_clear = None
        shopping_game_num = len(self.dict['shopping_car'])
        if shopping_game_num > 0:
            while True:
                os.system('cls')
                self.model1_choose_menu(area)
                if choose_clear == None:
                    choose_clear = ci.input_check_yes_no('是否清空购物车(y/n):', 
                                                        YesValue='y', NoValue='n')
                elif choose_clear == 0:
                    choose_clear = ci.input_check_yes_no('请输入(y/n)是否清空购物车:',
                                                        YesValue='y', NoValue='n')
                    continue
                else:
                    break

            if choose_clear == 'n':
                while True:                                 #检查输入的游戏位置是否正确
                    os.system('cls')
                    self.model1_choose_menu(area)
                    self.list_game_data(area)
                    if game_position == None:
                        game_position = ci.input_check_int('请输入删除第几个游戏:', 
                                                                abs=True, errorType=True)
                    elif game_position == ValueError or game_position == -1:
                        game_position = ci.input_check_int('输入游戏标号错误!请输入非负小数点:',
                                                                abs=True, errorType=True)
                    elif game_position < 1 or game_position > len(self.dict['shopping_car']):
                        game_position = ci.input_check_int('不存在此游戏!请输入购物车里的游戏:',  
                                                                abs=True, errorType=True)     
                    else:
                        break  
                del self.dict['shopping_car'][game_position-1]
                os.system('cls')
                self.model1_choose_menu(area)
                print('已将游戏移除购物车!')
            elif choose_clear == 'y':
                self.dict['shopping_car'].clear()
                os.system('cls')
                self.model1_choose_menu(area)
                print('已成清空购物车!')
        elif shopping_game_num <= 0:
            os.system('cls')
            self.model1_choose_menu(area)
            print('购物车没有游戏!')
    