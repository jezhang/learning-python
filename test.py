# -*- coding:utf-8 -*-

import random

def test():    
    guess_list = ["石头","剪刀","布"]
    guize = [["布","石头"],["石头","剪刀"],["剪刀","布"]]
    while True:        
        computer = random.choice(guess_list)
        people =  raw_input('请输入：石头,剪刀,布\n').strip()
        # people = people.encode("utf-8")
        if people not in  guess_list:
            people =  raw_input('重新请输入：石头,剪刀,布\n').strip()
            continue
        if computer ==  people:
            print "平手，再玩一次！"
        elif [computer,people] in guize :
            print "电脑获胜！"
        else:
            print "人获胜！"
            break
            
def main():
    test()

if __name__ == '__main__':
    main()