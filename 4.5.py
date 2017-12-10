##Sort vlans by increasing order and exclude repeats

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

vlans_set=set(VLANS)
vlans_list=list(vlans_set)
vlans_sorted=sorted(vlans_list)
print vlans_sorted

