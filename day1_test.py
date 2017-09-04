# _*_ coding:utf-8 _*_
# 测试git

import csv

fp = open(r'/Users/huixing/desktop/jiance_list.xlsx','r')
# contents = fp.read()
# print(contents)

# contents = fp.readlines()
# for content in contents:
#     print(content.strip())

# fp.write('PYTHON LOVE ME')
# fp.close()

# writer = csv.writer(fp)
# writer.writerow(('name','sex'))
# writer.writerow(('huixing','nan'))

contents = csv.reader(fp)
for content in contents:
    # print(type(content))

     list_a = content
     # list_a=['sssss','ece','sf']
     dict={}
     for i in range(len(list_a)):
          dict[list_a[i]]=len(list_a[i])
     print(dict)
     c=sorted(dict.items(),key=lambda item:item[1],reverse=True)[:1]
     print(c)

fp.close()