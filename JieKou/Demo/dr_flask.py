import flask
import json
import config.mongodb
server=flask.Flask(__name__)

@server.route('/index',methods=['get'])


def index():
    res='开发接口'
    return json.dumps(res,ensure_ascii=False)
server.run(port=7777,debug=True,host='0.0.0.0')


reg=flask.Flask(__name__)
@reg.route('/reg',methods=['post'])
def reg():
    print('进入')
    username=reg.values.get('username')
    password=reg.values.get('password')
    nickname=reg.values.get('nickname')

    if username and password:
        for i in  config.mongodb.db().find({'username':username}):
            if i==None:
                res={'msg':'用户不存在','msg_code':2001}
            else:
                config.mongodb.db().update_one({'username':username},{'$set':{'nickname':nickname}})
                res={'msg':'修改成功','msg_code':1}
    else:
        res={'msg':'填写正确的数据','msg_code':'1001'}
    return json.dumps(res,ensure_ascii=False)
reg.run(port=7777,debug=True,host='0.0.0.0')