import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys







# 1. Khai báo browser
browser = webdriver.Chrome(executable_path="./chromedriver")

# mo fb
browser.get("http://facebook.com")
sleep(5)
txtUser = browser.find_element_by_id("email")
txtUser.send_keys("tuanhung0601@live.com") # <---  Điền username thật của các bạn vào đây
sleep(random.randint(3, 5))

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("hatranglovetuanhung")
sleep(random.randint(3, 5))

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)
sleep(random.randint(3, 6))

# 2. Mở URL của post
browser.get("https://www.facebook.com/groups/chogaminggear2nd/permalink/2169598406511283/?__cft__[0]=AZUi5hRa44AAyx93ysAXuQNjYTYIl8_eMeEMHA97_v6U360TmRdkPAJdGEdzjpCw4oe1EVNoGmJr_TAGX9oyPNtVn03WzDar-EnuEOu9P5cABC70-HIsEVWHHpUcEcOlX44ROhpzjT21q5XE4lECUyIPGPZsfZGM4b1wlM7vIO5GrRYGySU4Vusyw9svvsSJftQ&__tn__=%2CO%2CP-R")
sleep(random.randint(5, 10))
load_more = 1
# Bam vao lay comment

# try:
#     show_comment = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div/div/span")
#     show_comment.click()
#     sleep(random.randint(5, 10))
# except:
#     print("Cant find the element")

sleep(5)

while(load_more==1):
    try:
        load_more_comment = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div[2]")
        load_more_comment.click()
        print("Click load comment")
        sleep(random.randint(5, 10))
    except:
        load_more = 0
        print("No more comment to show")

sleep(random.randint(5, 10))
comment_list = browser.find_elements_by_xpath("//li")


for comment in comment_list:
    poster = comment.find_element_by_class_name("0c111c07-53b6-490a-9193-f45b270bccfc")
    content = comment.find_element_by_class_name("0c111c07-53b6-490a-9193-f45b270bccfc")
    print("*", poster.text, ":", content.text)

sleep(10)
browser.close()
