import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Khai báo browser
browser = webdriver.Chrome(executable_path="./chromedriver")

# # mo fb
# browser.get("http://facebook.com")
# sleep(5)
# txtUser = browser.find_element_by_id("email")
# txtUser.send_keys("tuanhung0601@live.com") # <---  Điền username thật của các bạn vào đây
# sleep(random.randint(3, 5))
#
# txtPass = browser.find_element_by_id("pass")
# txtPass.send_keys("hatranglovetuanhung")
# sleep(random.randint(3, 5))
#
# # 2b. Submit form
#
# txtPass.send_keys(Keys.ENTER)
# sleep(random.randint(3, 6))

# 2. Mở URL của post
browser.get("https://www.facebook.com/groups/chogaminggear2nd/permalink/2175104455960678/?__cft__[0]=AZU9WHBNgsr_r4j7HOlofscfDHWhn5uJAK1bhbOPYuCx6GZ3l0QslseNI_47FlHk1l7SEu-62X7AR9T_J7REuMFRwSax3lFMPAZSzjJEvdBUqkuQoFwfvwk69qVg4ug4wvCHz9CT_HiJ5RKxEyxQc5gze3nU_jX3kTjqmk2Rzh5BD-G_jEhTB-NzSnYCyRA2QD0&__tn__=%2CO%2CP-R")
sleep(random.randint(5, 10))

# flag
load_more_comment = True
pop_up_login = True
load_comment_if_still_hidden = True
####################

while pop_up_login:
    try:
        close_pop_up = browser.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[4]/a")
        close_pop_up.click()
        print("Closed pop up")
        sleep(random.randint(3, 6))
    except:
        pop_up_login = False
        print("Popup login already close ")

# Bam vao lay comment

try:
    click_show_comment = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div/div/div[1]/div/div[2]")
    click_show_comment.click()
    sleep(random.randint(5, 10))
except:
    print("Cant show comment")

sleep(random.randint(3, 6))

while load_more_comment:
    try:
        click_load_more_comment = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div[2]")
        click_load_more_comment.click()
        print("Click load comment")
        sleep(random.randint(5, 10))
    except:
        load_more_comment = False

sleep(random.randint(2, 5))

while load_comment_if_still_hidden:
    try:
        click_load_comment = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/ul/li[2]/div[2]/div/a/div")
        click_load_comment.click()
        print("Showing hidden comment")
    except:
        load_comment_if_still_hidden = False
        print("No more comment to show")

sleep(random.randint(2, 5))

#comment_list = browser.find_elements_by_xpath("//li")
comment_list = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")

for comment in comment_list:
    poster = comment.find_element_by_class_name("_6qw4")
    content = comment.find_element_by_class_name("_3l3x")
    print("*", poster.text, ":", content.text)

sleep(10)
browser.close()
