import  pymysql
import  time,datetime


db=pymysql.connect('39.108.76.62','root','J1uy$08I5dB','dr_db')


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