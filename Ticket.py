#!/bin/python
#encoding=utf-8

#====================================================
#config
url = 'https://kyfw.12306.cn/otn/leftTicket/init'
username = "ty6412001"
password = "6632358"
_from_position = "%u6DF1%u5733%2CSZQ"
_to_position = "%u6B66%u6C49%2CWHN"
_date = "2016-02-05"
_type_1 = u"GC-高铁/城际"
_type_2 = u"D-动车"
_type_1_id = "checkbox_FKbgXEW2fk"
#=====================================================


from splinter import Browser
from time import sleep

class Ticket():
    """
    do Ticked
    """
    browser = Browser()
    ERROR_TIMES = 3
    login_times = 0

    def __init__(self):
        pass

    def doLogin(self) :
        login_times = self.login_times
        try :
            if self.browser.is_element_present_by_text(u"登录") or self.browser.is_element_present_by_text(u"注册"):
                self.browser.find_by_text(u"登录").click()
                self.browser.fill("loginUserDTO.user_name",username)
                self.browser.fill("userDTO.password",password)
                sleep(10)
                if self.browser.is_element_present_by_id("loginSub"):
                    self.browser.find_by_id("loginSub").click()
        except Exception :
            print "Error times --->%d<------"%login_times
            login_times += 1
            sleep(3)


    def doSearching(self):
        print "searching..."
        browser = self.browser
        error_time = 0
        Error_Times = self.ERROR_TIMES
        while error_time < Error_Times:
            try :
                if browser.url != url:
                    browser.visit(url)
                browser.cookies.add({"_jc_save_fromStation":_from_position})
                browser.cookies.add({"_jc_save_toStation":_to_position})
                browser.cookies.add({"_jc_save_fromDate":_date})
                browser.reload()
                sleep(0.5)
                browser.find_by_text(_type_1).click()
                browser.find_by_text(_type_2).click()

                browser.find_by_id("query_ticket").click()
                break
            except AttributeError:
                print AttributeError.args
                error_time += 1

    def isLogin(self):
        browser = self.browser
        if browser.url != url:
            browser.visit(url)
        if self.browser.is_element_present_by_text(u"登录") and self.browser.is_element_present_by_text(u"注册"):
            print "logining......"
            return False
        else:
            print  "already Login"
            return True

    def goingToBuy(self):
        browser = self.browser

    def getHtml(self):
        return self.browser.html

if __name__ == '__main__':
    ticket = Ticket()
    # while not ticket.isLogin():
    #     ticket.doLogin()
    while True:
        ticket.doSearching()
        print ticket.getHtml()
        sleep(5 * 60)  #5min