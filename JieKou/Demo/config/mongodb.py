from pymongo  import MongoClient



conn= MongoClient('mongodb://39.108.76.62:27017/')
db=conn.linkwallet
db.authenticate('walletadmin','l1Nk#Wallet')
balances=db.balances
z=0
for i in balances.find():
    m=i.get('trx')

    i=i.get('drt')

    if i==None:
        i=None
    elif m==None:
        m=None
    # z=(int(i))+z
    print(str(i)+'              '+str(m))



print(z)