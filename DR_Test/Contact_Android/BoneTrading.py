import time
import unittest
import random
import Login


class Bone_Collect(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr_phone=Login.MyPhone.dr_phone
        # print('=======================骨头开始====================')
        time.sleep(1)


    def test_2getBone(self):

        # print('************************领骨头**********************')
        # print(self.dr_phone.find_element_by_id('com.juddata.dragon:id/unpick'))
        self.boneMun = self.dr_phone.find_element_by_id('com.juddata.dragon:id/unpick').text#获取领取骨头数量
        # print(type(self.boneMun))
        self.boneMun = int(self.boneMun)
        if self.boneMun>0:#判断领取骨头的数量是否大于0
            # print('进入判断')
            time.sleep(2)
            self.dr_phone.find_element_by_id('com.juddata.dragon:id/pick_tv').click()
            time.sleep(3)
            self.dr_phone.find_element_by_id('com.juddata.dragon:id/confirm').click()
            time.sleep(1)



    def test_BoneSell(self):
        # print('====================================出售龙骨==================================================')
        self.dr_phone.find_element_by_id('com.juddata.dragon:id/b_iv').click()#点击龙巢
        self.boneMun=int(self.dr_phone.find_element_by_id('com.juddata.dragon:id/male_sum').text)#获取公龙龙骨的数量
        if self.boneMun>0:#判断恐龙龙骨的数量是否为0,为0话,选择其性别的龙骨
            self.dr_phone.find_element_by_id('com.juddata.dragon:id/male_layout').click()
        else:
            self.dr_phone.find_element_by_id('com.juddata.dragon:id/female_layout').click()


        for mun in range(1,5):#循环查看恐龙部位龙骨的数量,如果部位骨头为0,不做操作
            # print(mun)
            #获取不同部位的数量
            xpath='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout[1]/android.widget.TextView[1]'%(mun)
            # print(xpath)
            self.BonePartNum =int (self.dr_phone.find_element_by_xpath(xpath).text)
            if self.BonePartNum > 0:#判断部位数量是否为0
                self.dr_phone.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout[2]/android.widget.TextView[2]'%(mun)).click()
                self.dr_phone.find_element_by_id('com.juddata.dragon:id/tv_pop_amount').send_keys(random.randint(101, 1000))#输入价格
                self.dr_phone.find_element_by_id('com.juddata.dragon:id/tv_pop_public').click()#点击确认
                #self.dr_phone.find_element_by_id('com.juddata.dragon:id/usepwd_tv').click()#选择手动输入交易密码
                self.dr_phone.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText').send_keys('a1234567')#输入交易密码
                #/ hierarchy / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.RelativeLayout / android.widget.LinearLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.EditText
                self.dr_phone.find_element_by_id('com.juddata.dragon:id/confirm_tv').click()#去让人交易密码
                self.dr_phone.find_element_by_id('com.juddata.dragon:id/cancel_tv').click()#选择取消前往其他地方
                self.dr_phone.find_element_by_id('com.juddata.dragon:id/back_btn').click()
                self.dr_phone.find_element_by_id('com.juddata.dragon:id/back_btn').click()

                break

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)


if __name__=='__main__':
    unittest.main()