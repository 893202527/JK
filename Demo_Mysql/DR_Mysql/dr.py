import pymysql
import time, datetime

db = pymysql.connect('39.108.76.62', 'root', 'J1uy$08I5dB', 'dr_db')
nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%m:%S')

def game():
    cursor = db.cursor()
    # for id in range(1,10):
    x = 0
    for id in range(1, 127):

        t = id + x
        ontime = (datetime.datetime.now() + datetime.timedelta(minutes=2 + t)).strftime("%H:%M") + ':00'
        print(ontime)
        offTime = (datetime.datetime.now() + datetime.timedelta(minutes=3 + t)).strftime("%H:%M") + ':00'
        print(offTime)
        dateTime = (datetime.datetime.now() + datetime.timedelta(minutes=3 + t)).strftime("%H:%M") + ':30'
        print(dateTime)
        endTime = (datetime.datetime.now() + datetime.timedelta(minutes=4 + t)).strftime("%H:%M") + ':30'
        print(endTime)
        x = x + 2

        try:
            # cursor.execute('select * from dr_user where phoneNumber="17780508427"')
            sql1 = "UPDATE dr_minigame_item set onTime='%s',offTime='%s',dateTime='%s',endTime='%s' WHERE id= '%s'" % (
            ontime, offTime, dateTime, endTime, id)
            sql2 = "UPDATE dr_minigame_item set onTime=ontime,offTime=offTime,dateTime=dateTime,endTime=endTime WHERE id='12'"
            cursor.execute(sql1)
        except Exception as e:
            db.rollback()
            print(e)
        else:
            db.commit()
        print(cursor.rowcount)

    cursor.close()

    db.close()

class sql():
    def sql(userID,nowtime):
        sql2='insert  into dr_team values ("%s","%s","%s","%s","team_1",1,1,0)' % (userID, nowtime, nowtime, userID)
        sql3='insert into dr_team_user values ("%s","%s","%s","%s",0,1,1,1,0,0)' % (userID, nowtime, nowtime, userID)
        sql4='insert into dr_team_device values ("%s","%s","%s","devices_%s",1,"%s","%s","%s","%s","%s")'%(userID,
                                                   nowtime, nowtime, userID,nowtime,userID,userID,userID,userID)
        sql5='insert into dr_team_relation values ("%s","%s","%s","devices_%s","%s","%s","%s",0,"%s")'%(userID,
                                        nowtime, nowtime, userID,userID,userID,userID,userID)

        sql1 = 'insert into dr_device values ("%s",' \
               '"%s",' \
               '"%s",' \
               '0,' \
               '"devices_%s",' \
               '"lanya_%s",' \
               '1,' \
               '"%s",' \
               '"%s",' \
               '"14400000001",' \
               '"0x3de14dde56a9c78704bcd7648f7a8c9ff104e59d",' \
               '"30199386c4f84ba005f5988d26c7e8a117947943",1,' \
               '1)' % (userID, nowtime, nowtime, userID, userID, nowtime, userID)

        List=[sql1,sql2,sql3,sql4,sql5]
        return  List


def mysql_test(sql,*nosql):
    cursor = db.cursor()
    nosql=list(nosql)
    if len(nosql)==0:
        for i in sql:
            cursor.execute(i)
    else:
        for x in nosql:  #获取下标的数据
            print(x)
            sqlweizhi=sql[x]
            list2= [sqlweizhi]
        for c in list2:  #删除相应的数据
            sql.remove(c)
        for z in sql:
            print(z)
            cursor.execute(z)

    db.commit()
    print(cursor.rowcount)
    cursor.close()

    db.close()

if __name__ == '__main__':
    print("he")
    sql=sql.sql(202, nowtime)
    mysql_test(sql,1,2,3,4)
