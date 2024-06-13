import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json

def autofill_and_submit(form_url, user_field_name, pass_field_name, username, password):
    # 初始化选项
    chrome_options = Options()
    chrome_options.binary_location = "C:\\Users\\jack\\Desktop\\mycode\\autoprogram\\chrome-win64\\chrome.exe"
    # 使用指定的ChromeDriver路径和选项初始化webdriver
    driver = webdriver.Chrome(options=chrome_options)

    # 访问指定的网页
    driver.get(form_url)
    time.sleep(5)

    # 填写登录表单
    username_field = driver.find_element_by_name(user_field_name)
    password_field = driver.find_element_by_name(pass_field_name)
    username_field.send_keys(username)
    password_field.send_keys(password)

    # 提交表单
    driver.find_element_by_css_selector('button[type="submit"]').click()
    # 获取并打印session
    print("Session ID: ", driver.session_id)
    # 获取cookies
    all_cookies = driver.get_cookies()

    # 关闭driver
    driver.quit()

    # 创建一个新的session
    s = requests.Session()
    

    # 将cookies添加到session中
    for cookie in all_cookies:
        s.cookies.set(cookie['name'], cookie['value'])
    
    # 发送Get请求
    response = s.get('http://localhost:8069/web#action=311&model=webgis.webgis&view_type=list&cids=1&menu_id=221')
    print(response.text)

    # 打印请求结果
    # print(json.dumps(response.json(), indent=4))
    # 其他操作...
    
if __name__ == "__main__":
    # 使用程序
    url='http://localhost:8069'
    username='login'
    password='password'
    myname= '1'
    myps= '1'
    submit='submit'
    autofill_and_submit(url, username, password, myname,myps)