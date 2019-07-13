permit_fqnid = [
    {'fqnid':'fib:123', 
    'permit':'permit:123'
    },
    {'fqnid':'fib:456', 
    'permit':'permit:123'
    },
    {'fqnid':'fib:789', 
    'permit':'permit:124'
    },
    {'fqnid':'fib:125', 
    'permit':'permit:124'
    },
    {'fqnid':'fib:128', 
    'permit':'permit:125'
    },
]

unique_list = {}

for item in permit_fqnid:
    for key, value in item.items():
        if item['permit'] in unique_list.keys():
            unique_list['permit'] = [item['fqnid']append(item['fqnid'])
        else:
            unique_list[item['permit']] = [item['fqnid']]
            print(unique_list)
      



#for row in permit_fqnid:
 #   for fqnid, permit in row.items():
  #      print(row[fqnid]['permit'])













        




