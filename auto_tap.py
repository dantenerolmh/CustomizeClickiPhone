from appium import webdriver
from appium.options.ios import XCUITestOptions
import time

# 1. 填入你的设备配置信息
options = XCUITestOptions()
options.platform_name = 'iOS'
options.platform_version = '26.3'      # 你的 iOS 版本
options.device_name = 'iPhone 17 Pro'  # 你的手机名称
options.udid = '00008150-0016215C149A401C' # <--- 务必替换成你的真实 UDID！
options.automation_name = 'XCUITest'

# 2. 连接 Appium 服务
print("正在连接手机，这可能需要几秒钟...")
# 注意：第一次连接时，手机屏幕可能会闪烁一下，或者自动打开一个透明的 App，这是正常的
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
print("连接成功！准备执行计划...")

# 3. 自定义时间节点 (这里演示等待 5 秒，你可以改成任何你想要的逻辑)
wait_seconds = 5
print(f"倒计时 {wait_seconds} 秒后触发点击...")
time.sleep(wait_seconds)

# 4. 执行屏幕任意区域点击
# 假设我们要点击屏幕坐标 (x: 200, y: 500) 的位置
target_x = 200
target_y = 500
print(f"正在点击坐标: ({target_x}, {target_y})")

# iOS 推荐的精确坐标点击方法 (mobile: tap)
driver.execute_script('mobile: tap', {'x': target_x, 'y': target_y})

print("点击指令已发送！")

# 5. 休息 2 秒后断开连接
time.sleep(2)
driver.quit()
print("任务结束。")