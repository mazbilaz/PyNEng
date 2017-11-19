NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
#I need to replace FastEthernet0/1 to GigabytEthernet0/1
NAT_list=("ip nat inside source list ACL interface FastEthernet0/1 overload").split()
number=NAT_list.index('FastEthernet0/1')
NAT_list.remove('FastEthernet0/1')
NAT_list.insert(number,'GigabitEthernet0/1')
NAT_changed=' '.join(NAT_list)
print(NAT_changed)


#Do the same, but use only string methods
NAT_changed2=NAT.replace('Fast', 'Gigabit')
print(NAT_changed2)
#OMG.....