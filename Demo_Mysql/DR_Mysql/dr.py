import  pymysql
import  time,datetime


db=pymysql.connect('39.108.76.62','root','J1uy$08I5dB','dr_db')

def game():
    cursor=db.cursor()
    # for id in range(1,10):
    x=0
    for id in range(1,127):

        t=id+x
        ontime=(datetime.datetime.now()+datetime.timedelta(minutes=2+t)).strftime("%H:%M")+':00'
        print(ontime)
        offTime=(datetime.datetime.now()+datetime.timedelta(minutes=3+t)).strftime("%H:%M")+':00'
        print(offTime)
        dateTime=(datetime.datetime.now()+datetime.timedelta(minutes=3+t)).strftime("%H:%M")+':30'
        print(dateTime)
        endTime=(datetime.datetime.now()+datetime.timedelta(minutes=4+t)).strftime("%H:%M")+':30'
        print(endTime)
        x=x+2

        try:
    # cursor.execute('select * from dr_user where phoneNumber="17780508427"')
            sql1="UPDATE dr_minigame_item set onTime='%s',offTime='%s',dateTime='%s',endTime='%s' WHERE id= '%s'"%(ontime,offTime,dateTime,endTime,id)
            sql2="UPDATE dr_minigame_item set onTime=ontime,offTime=offTime,dateTime=dateTime,endTime=endTime WHERE id='12'"
            cursor.execute(sql1)
        except Exception as e:
            db.rollback()
            print(e)
        else:
            db.commit()
        print(cursor.rowcount)



    cursor.close()

    db.close()


def setMyDevice(start,end):
    nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%m:%S')

    userID=200
    cursor=db.cursor()
    sql='insert into dr_device values ("%s",' \   
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
        '1)'%(start,nowtime,nowtime,start,start,nowtime,userID)
    cursor.execute(sql)
    db.commit()
    print(cursor.rowcount)
    cursor.close()

    db.close()

if __name__ == '__main__':
    setMyDevice(200,100)