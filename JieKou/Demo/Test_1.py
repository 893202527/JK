import  requests
import  urllib3
import  json
import  urllib
import sys


def dr_RAS ():
    url='http://39.108.76.62:7502/dr-game/mobile/rsa/public_key'
    headers={"Accept": "*/*"}
    data={'mobileCode':1111}
    r=requests.get(url=url,json=data,headers=headers)
    result=r.text
    zd=json.loads(result)
    str=zd.get('data').get('modulus')
    return str


def dr_get_sms_code(phoneNum):
    url = 'http://39.108.76.62:7502/dr-game/mobile/pre_user/get_sms_code'
    data={'phoneNum':phoneNum,
          'captchaType':'login'
          }#login 登陆  weixin 微信登陆  changephone 修改手机号  tradePwd 修改密码  coinWithdraw 钱包
    ras=dr_RAS()
    headers = {"Accept": "*/*",
               'User-Agent': 'DragonBox/1.3.2 (iPhone; iOS 11.0.3; Scale/2.00)',
               'Accept-Language': 'zh-Hans-CN;q=1',
               'Accept-Encoding': 'gzip, deflate',
                'Authorization': '%s'%(ras),
               # 'Connection': 'keep-alive',
               # 'dr': '{"mobileCode": "4938945A-59BE-4E37-B25D-3D0626DF2895", '
               #        '"random": "NDUwNDAyOQ==",'
               #        '"loginType": "mobile", '
               #       '"token": "OWMxMjViMjktZmM3Ny00ZTIwLWIyNjEtNTdlOTc1MDBhMDA2"}'
               }
    # http=urllib3.PoolManager()
    # r=http.request('get',url=url,fields=data,headers=headers)
    # print(r.data)
    # strr=json.dumps(data)
    # strr1=json.dumps(headers)
    # con=urllib.request.Request(url,data=data,headers=headers,method='get')
    # print(con.read())
    rq=requests.request('get',url=url,headers=headers,data=data)
    print(rq.text)


    rqget=requests.get(url=url,params=data,headers=headers)
    print(rqget.text)
    # dict= {'phoneNum':'17780508427','captchaType':'longin'}
    # r = requests.get(url=url,params=data,headers=headers)
    # print(r.url)


def dr_sms_login():
    url = 'http://39.108.76.62:7502/dr-game/mobile/pre_user/sms_login'
    ras = dr_RAS()
    dr={"token":"OWMxMjViMjktZmM3Ny00ZTIwLWIyNjEtNTdlOTc1MDBhMDA2",
        "loginType":"mobile",
        "mobileCode":"2A73B5FE-391D-4EC5-8B21-CC7E2D939795",
        "random":"NzQ2OTQ2Mg=="}
    headers = {'Accept': '*/*',
               'User-Agent':'DragonBox/1.3.2 (iPhone; iOS 11.0.3; Scale/2.00)',
               'Accept-Language':'zh-Hans-CN;q=1',
               'Accept-Encoding':'gzip, deflate',
                'Authorization':'%s'%(ras),
               'Content-Length':'214',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Connection': 'keep-alive',
               'Connection': 'keep-alive',
               'dr':'%s'%(json.dumps(dr))
               }
    dict={  'phoneNum':'17780508427',
            'deviceType':'Ios',
            'mobileCode':'4938945A-59BE-4E37-B25D-3D0626DF2895',
            'loginType':'mobile',
            'verifyCode':'1111',
            'address':'四川省成都市',
            'coordinate':'11584914.3,3569251.03'
          }
    # http=urllib3.PoolManager()
    #
    # r=http.request('post',url=url,fields=dict,headers=headers)
    # print(json.loads(r.data))
    # print(http.headers)

    rq=requests.request('post',url=url,data=dict,headers=headers)
    print(json.dumps(rq.text))

def dinosaur_list():
    url='http://39.108.76.62:7502/dr-game/mobile/user/dinosaur/list'
    dr = {"token":"OWMxMjViMjktZmM3Ny00ZTIwLWIyNjEtNTdlOTc1MDBhMDA2",
          "loginType": "mobile",
          "mobileCode": "2A73B5FE-391D-4EC5-8B21-CC7E2D939795",
          "random": "MzAwMjcxNg=="}

    headers={
        'Accept': '*/*',
        'User-Agent': 'DragonBox/1.3.6 (iPhone; iOS 12.2; Scale/2.00)',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Accept-Encoding': 'gzip, deflate',
        'Authorization': dr_RAS(),
        'Connection': 'keep-alive',
        'dr':json.dumps(dr),

    }
    data={
        'pageNum':'1',
        'pageSize':'20',

    }
    rq=requests.request('get',url=url,headers=headers,params=data)
    print(rq.url)
    print(rq.text)
    # dirt=json.loads()
    return rq.json().get('data')



def set_device():#
    for i in range(200,201):
        id=i
        print(id)
    data={
        'name':'device_200',
        'userId':'200'
    }
    rq=requests.request('get',url='http://39.108.76.62:7502/dr-game/mobile/test/set_device',params=data)
    print(rq.text)



def lian():
    rq=requests.request('get',url='https://app-dr.jiuyuesoft.cn:30443/dr-ethereum/web3_info/get_user_transactions?accountAddr=&contractType=Dragon&pageNum=1&pageSize=50')
    rq1=requests.request('get',url='https://app-dr.jiuyuesoft.cn:30443/dr-ethereum/web3_info/get_user_transactions?accountAddr=&contractType=Bone&pageNum=1&pageSize=50')
    # print(rq.text)
    # print(rq1.text)
    print(rq1.status_code)
    print(rq.status_code)


def str(str,str2):
    for i in str:
        for k in str2:
            if (i==k):
                print(i)
    f = [ x + y*2 for x in 'ABCDE1' for y in '1234567']
    print(f)
    f = [x ** 2 for x in range(1, 100)]
    print(f)
    print(sys.getsizeof(f))


def my_bone_new():
    url='http://39.108.76.62:7502/dr-game/mobile/user/bone/my_bone_new'
    dr = {"token":"OWMxMjViMjktZmM3Ny00ZTIwLWIyNjEtNTdlOTc1MDBhMDA2",
          "loginType": "mobile",
          "mobileCode": "2A73B5FE-391D-4EC5-8B21-CC7E2D939795",
          "random": "MzAwMjcxNg=="}

    headers={
        'Accept': '*/*',
        'User-Agent': 'DragonBox/1.3.6 (iPhone; iOS 12.2; Scale/2.00)',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Accept-Encoding': 'gzip, deflate',
        'Authorization': dr_RAS(),
        'Connection': 'keep-alive',
        'dr':json.dumps(dr),

    }
    data={
        
    }
    requests.request('post',url=url,headers=headers,data='')

if __name__ == '__main__':
    # dr_RAS()
    print(dinosaur_list())

    # set_device()
    # i=0
    # while 1==1:
    #     i = i + 1
    #     print('访问次数:%s'%i)
    #     lian()
    # str('123','我')