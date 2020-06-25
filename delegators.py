from beem.account import Account
from beem.instance import set_shared_steem_instance
from beem import Steem
import re

stm = Steem("https://anyx.io")
set_shared_steem_instance(stm)
acc = Account("[the account you want to check]",steem_instance=stm)

c_list = []
names=[]
for c in acc.history_reverse(only_ops=["delegate_vesting_shares"]):
    data=re.findall("'delegator': '(.+?)'",str(c)),re.findall("'delegatee': '(.+?)'",str(c)),re.findall("'amount': '(.+?)'",str(c))
    name=re.findall("'delegator': '(.+?)'",str(c))
    if name not in names:
        print(re.findall("'delegator': '(.+?)'",str(c)),re.findall("'delegatee': '(.+?)'",str(c)),re.findall("'amount': '(.+?)'",str(c)))
        c_list.append(data)
        names.append(name)
active=[]
removed=[]
for i in c_list:
    if str(i[2])=="['0']":
        data=i[0][0],i[2][0]
        removed.append(data)
    else:
        hive=stm.vests_to_sp(i[2][0])#.split(' ')[0]))
        data=i[0][0], hive #i[2][0]
        #print ('DATA 2', data)
        active.append(data)
for i in active:
    print (i[0],':',round(i[1]/1000000,3),'HIVE')
print ('ACTIVE:',len(active))
print ('LOST:',len(removed))
a=input ('Do you want to print the undelgator list?')
if a=='y':
    for i in removed:
        print (i[0][0],':',i[1],'HIVE')
else:
    exit
