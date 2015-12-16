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
#====================================================

from splinter import Browser
from time import sleep

browser = Browser()

def getTicket():
    global browser
    browser.visit(url)
    while True :
        if browser.is_element_present_by_text(u"登录") and browser.is_element_present_by_text(u"注册"):
            print "need login"
            #login in
            browser.find_by_text(u"登录").click()
            browser.fill("loginUserDTO.user_name",username)
            browser.fill("userDTO.password",password)
            sleep(10)
            if browser.is_element_present_by_id("loginSub"):
                browser.find_by_id("loginSub").click()
        else:
            print "alread login"
            break

    if browser.url != url :
        browser.visit(url)
    browser.cookies.add({"_jc_save_fromStation":_from_position})
    browser.cookies.add({"_jc_save_toStation":_to_position})
    browser.cookies.add({"_jc_save_fromDate":_date})
    browser.reload()

    browser.find_by_id("query_ticket").click()
    browser.find_by_text("_type_1").click()
    browser.find_by_text("_type_2").click()

    return True
    #browser.quit()

if __name__ == '__main__':
    i = 0
    while True :
        try :
            result = getTicket()
            if result :
                break

        except Exception :
            if i == 3 :
                print u"错误",i,u"次"
                break
            else:
                i = i+1
                sleep(3)
                continue