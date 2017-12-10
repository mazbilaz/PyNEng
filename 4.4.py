command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
#coding=utf-8
#

vlans1 = command1.split()[-1].split(',')
vlans2 = command2.split()[-1].split(',')

common_vlans = set(vlans1) & set(vlans2)

print(list(common_vlans))

