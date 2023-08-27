from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 注意这里的导入

# 创建一个 Service 对象
chrome_service = Service(executable_path=r"/Users/handongqian/Downloads/chromedriver-mac-arm64/chromedriver")

# 使用 Service 对象来启动 Chrome 浏览器
wd = webdriver.Chrome(service=chrome_service)

# 之后可以进行其他操作，比如打开网页等
wd.get("https://www.google.com")

# 最后暂停程序，防止窗口关闭
input()

# 关闭浏览器窗口和服务
# wd.quit()
