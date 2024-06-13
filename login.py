import requests
from bs4 import BeautifulSoup

# 定义token提取函数(这里只是一个基础模版，需要根据实际情况进行修改)
def extract_token(res_text):
    soup = BeautifulSoup(res_text, 'html.parser')
    return soup.find('input', {'name': 'csrf_token'})['value']

url = 'http://localhost:8069/web/login'
s = requests.Session()
# 先GET登录页面
login_page = s.get(url)

# 从返回的HTML中提取token
token = extract_token(login_page.text)

# 提交表单
form_data = {
    'login': '1',
    'password': '1',
    'csrf_token': token   # 添加token到表单数据
}

res = s.post(url, data=form_data)

print(res.text)