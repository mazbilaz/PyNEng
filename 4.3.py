CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
#coding=utf-8
#Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100']
CONFIG_list=CONFIG.split()
CONFIG_len=len(CONFIG_list)
print "["+CONFIG_list[CONFIG_len-1]+"]"