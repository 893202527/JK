import flask
import json
import config.mongodb
import datetime
server=flask.Flask(__name__)
server.config['secret_key']='gooo'



@server.route('/',methods=['get'])
def index():
    res='开发接口'
    return json.dumps(res,ensure_ascii=False)




@server.route('/reg',methods=['post'])
def reg():
    print('进入')
    username=flask.request.values.get('username')
    password=flask.request.values.get('password')
    nickname=flask.request.values.get('nickname')

    if username and password:
        for i in  config.mongodb.db().find({'username':username}):
            if i==None:
                res={'msg':'用户不存在','msg_code':2001}
            else:
                config.mongodb.db().update_one({'username':username},{'$set':{'nickname':nickname}})
                res={'msg':'修改成功','msg_code':1}
    else:
        res={'msg':'填写正确的数据','msg_code':1001}
    return json.dumps(res,ensure_ascii=False)

@server.route('/')
def rootpath():
    return flask.redirect('/index')

@server.route('/user/<username>')
def user(username):
    db=None
    for i in  config.mongodb.db().find({'username': username}):
        db=i
    if db!=None:
        res={'msg':str(db),'msg_code':1}
        return json.dumps(res, ensure_ascii=False)
    else:
        # flask.abort(401)
        res = {'msg':'输入错误的%s'%(username), 'msg_code': 1}
        return flask.redirect('/error')

@server.route('/login',methods=['get','post'])
def login():
    if flask.request.method=='post':
        res={'msg':'post请求','msg_code':1}
    else:
        res={'msg':'get请求','msg_code':1}
    return json.dumps(res,ensure_ascii=False)


@server.route('/error/')
def error():
    flask.abort(401)

@server.errorhandler(401)
def error_errorhandler_401(error):
    return flask.render_template_string('请联系管理员')

@server.route('/go/')
def go():
    flask.session['time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return flask.session['time']



@server.route('/out/')
def out():
    return flask.session.get('time')
server.run(port=7777,debug=True,host='0.0.0.0')