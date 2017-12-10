MAC = 'AAAA:BBBB:CCCC'
#coding=utf-8
#Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
MAC_list=MAC.split(':')
MAC_changed=".".join(MAC_list)
print (MAC_list)