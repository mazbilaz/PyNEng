MAC = 'AAAA:BBBB:CCCC'
#Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
MAC_list=MAC.split(':')
MAC_changed=MAC_list.join('.')
print (MAC_changed)