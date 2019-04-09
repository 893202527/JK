import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import smtplib
from email.mime.text import MIMEText
import BoneTrading



#Suite=unittest.TestSuite()
#Suite.addTest(Login.MyPhone('test_1login'))
#Suite.addTest(BoneTrading.Bone_Collect('test_2getBone'))
#Suite.addTest(BoneTrading.Bone_Collect('test_BoneSell'))


now=time.strftime("%Y-%m-%d %H_%M_%S")



def senderEmail ():
    sender = '893202527@qq.com'
    password = 'pzdbnedfvbsrbbcj'
    receive = '1084353375@qq.com'
    smtp_server = 'smtp.qq.com'
    sendfile = open('../Text/'+now+'text.html','rb').read()#读取邮件文本
    message = MIMEText(sendfile,_subtype="html",_charset='utf-8')

    message['Content-Type']='text/html'
    message['Content-disposition']='attachment; filename=Text.html'



    subject = '邮件测试'


    message['Subject'] = subject
    message['From'] =sender # 发送者
    message['To'] =receive # 接收者



    try:
        Smtp_eMail = smtplib.SMTP()
        Smtp_eMail.connect(smtp_server, 25)
        Smtp_eMail.set_debuglevel(1)
        Smtp_eMail.login(sender, password)#发送者的账号密码
        Smtp_eMail.sendmail(sender, receive, message.as_string())
        Smtp_eMail.quit()
        print('发送邮件')
    except smtplib.SMTPException as e:
        print('发送失败:'+e)


if __name__=='__main__':
    while True:
        Suite = unittest.TestSuite()
        Suite.addTest(BoneTrading.Bone_Collect('test_BoneSell'))
        filename='../Text/'+now+'text.html'


        with open(filename, "wb") as f:
            runner = unittest.TextTestRunner()
            runner=HTMLTestRunner(
                stream=f,
                title='测试报告',
                description='用例执行情况'

            )

            runner.run(Suite)
    #senderEmail()