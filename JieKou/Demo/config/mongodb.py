from pymongo import MongoClient



def db():
    conn= MongoClient('mongodb://39.108.76.62:27017/')
    db=conn.linkwallet
    db.authenticate('walletadmin','l1Nk#Wallet')
    balances=db.balances
    return  db.users
#
#     z=0
#     for i in balances.find():
#         m=i.get('trx')
#         i=i.get('drt')
#         if i==None:
#             i=0
#         elif m==None:
#                 m=0
#         z=(int(i))+z
#         # print(str(i)+''+str(m))
#
#
#     print(0.217396*58669.720829)
#     print(z)
#
# db()