import csv
import time
from lxml import html
from selenium import webdriver
from com.SendMailUtil import SendMail

etree = html.etree


def parser():
    driver = webdriver.Chrome("chromedriver.exe")
    return driver


def login(url):
    driver = parser()
    driver.get(url)
    time.sleep(5)
    get_data(driver)
    return driver


def get_data(driver):
    for _ in range(10): # 可根据群成员的数量大小调整此数值，数值越大耗时越长
        scroller(driver)
        time.sleep(1)
    data = driver.page_source
    html = etree.HTML(data)
    mem_info_list = html.xpath('//*[@id="groupMember"]/tbody[@class="list"]/tr')  # TODO  QQ群成员列表

    with open('QQ.csv', 'a+', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, dialect="excel")
        writer.writerow(['成员', 'QQ号', '性别', 'Q龄', '入群时间', '最后发言'])

        for mem_info in mem_info_list:

            data = {'成员': str(mem_info.xpath('./td[3]//text()')[3]).replace('\U0001f60a', '').strip(),
                    'QQ号': str(mem_info.xpath('./td[5]//text()')[0]).replace('\U0001f60a', '').strip(),
                    '性别': str(mem_info.xpath('./td[6]//text()')[0]).replace('\U0001f60a', '').strip(),
                    'Q龄': str(mem_info.xpath('./td[7]//text()')[0]).replace('\U0001f60a', '').strip(),
                    '入群时间': str(mem_info.xpath('./td[8]//text()')[0]).replace('\U0001f60a', '').strip(),
                    '最后发言': str(mem_info.xpath('./td[9]//text()')[0]).replace('\U0001f60a', '').strip()}
            print(data)

            if data:
                # writer.writerow(['成员', 'QQ号', '性别', 'Q龄', '入群时间', '最后发言'])
                # writer.writerow(
                #     [data['成员'].replace('\xa0', ''), data['QQ号'].replace('\xa0', ''),
                #      data['性别'].replace('\xa0', ''), data['Q龄'].replace('\xa0', ''),
                #      data['入群时间'].replace('\xa0', ''), data['最后发言'].replace('\xa0', '')])
                writer.writerow(
                    [data['成员'], data['QQ号'],
                     data['性别'], data['Q龄'],
                     data['入群时间'], data['最后发言']])

                # 发送邮件
                sendmail(data['QQ号'] + "@qq.com");


def sendmail(user):
    SendMail().sendmail("are you ok", "最近过的还好吗，加我微信聊聊天吧WX666", user)


def logout(driver):
    driver.find_element_by_class_name("logout").click()
    # driver.close()需要在driver.quit()前面，因为driver.quit()方法会先关闭所有窗口并退出驱动，如果再次调用close则会报错
    driver.close()
    driver.quit()


def scroller(driver):
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)


def run():
    QQnum = input('请输入一个【一个或多个QQ群号】:')
    for num in QQnum.split(','):
        url = "https://qun.qq.com/member.html#gid=" + num
        driver = login(url)

    logout(driver)  # TODO  退出登录


if __name__ == '__main__':
    run()
