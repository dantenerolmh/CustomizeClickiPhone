import time
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 设备配置信息
options = XCUITestOptions()
options.platform_name = 'iOS'
options.platform_version = '26.3'
options.device_name = 'iPhone 17 Pro'
options.udid = '00008150-0016215C149A401C'
options.automation_name = 'XCUITest'

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
print("连接成功！开始分析当前页面入口...")

entry_wait = WebDriverWait(driver, 5)

# ==========================================
# 【启动逻辑升级】: 加入直接检测动态膨胀弹窗
# ==========================================
try:
    # 优先级 0：可能一打开屏幕就已经有“看广告膨胀”的弹窗挡着了
    print("🔍 优先级 0: 检测是否已有『看广告膨胀』弹窗...")
    # 使用 contains 语法，无视 458 或 508 等动态数字
    inflate_btn_start = entry_wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//*[contains(@label, '看广告膨胀') or contains(@name, '看广告膨胀')]"))
    )
    print("✅ 找到现有『看广告膨胀』弹窗！点击直接进入广告流。")
    inflate_btn_start.click()
    time.sleep(2)

except Exception:
    try:
        # 优先级 1：寻找“开宝箱得金币”
        print("🔍 优先级 1: 检测是否存在『开宝箱得金币』按钮...")
        treasure_btn = entry_wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//*[contains(@label, '开宝箱得金币') or contains(@name, '开宝箱得金币')]"))
        )
        print("✅ 找到『开宝箱得金币』！点击进入广告流。")
        treasure_btn.click()
        time.sleep(2)

    except Exception:
        print("⚠️ 未找到宝箱，尝试寻找备用入口『待领取』...")
        try:
            # 优先级 2：寻找列表里的“待领取”
            pending_btn = entry_wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//*[contains(@label, '待领取') or contains(@name, '待领取')]"))
            )
            print("✅ 找到『待领取』按钮！点击打开弹窗...")
            pending_btn.click()
            time.sleep(2)

            # 点击弹窗中的“看广告膨胀”动态按钮
            print("🎁 正在弹窗中点击『看广告膨胀』...")
            inflate_btn = entry_wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//*[contains(@label, '看广告膨胀') or contains(@name, '看广告膨胀')]"))
            )
            inflate_btn.click()
            print("✅ 成功点击『看广告膨胀』！正式进入广告流。")
            time.sleep(2)

        except Exception:
            print("❌ 警告：所有入口均未找到！脚本将强行尝试进入主循环接管...")
            pass

# ==========================================
# 正式进入全自动死循环
# ==========================================
loop_count = 1
while True:
    print(f"\n--- 开始第 {loop_count} 轮循环 ---")
    try:
        # 【步骤 1】: 等待倒计时结束，点击右上角的“领取成功”
        print("📺 盯着右上角等待『领取成功』出现...")
        wait_for_ad = WebDriverWait(driver, 65)
        success_btn = wait_for_ad.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//*[contains(@label, '领取成功') or contains(@name, '领取成功')]"))
        )
        success_btn.click()
        print("✅ 点击『领取成功』！")
        time.sleep(2)

        # 【步骤 2 升级】: 兼容普通“领取奖励”和动态“看广告膨胀领XXX”
        print("🎁 等待后续弹窗...")
        wait_for_popup = WebDriverWait(driver, 10)
        # 这里的 XPath 使用了 OR 逻辑，无论出哪种按钮都能抓到并点击
        reward_btn = wait_for_popup.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//*[contains(@label, '领取奖励') or contains(@name, '领取奖励') or contains(@label, '看广告膨胀') or contains(@name, '看广告膨胀')]"))
        )
        reward_btn.click()
        print("✅ 成功点击继续领奖/膨胀按钮！")
        time.sleep(2)

        # 【步骤 3】: 智能检测“开心收下”阶段大奖弹窗
        print("🕵️ 开始检测是否触发阶段大奖...")
        try:
            short_wait = WebDriverWait(driver, 4)
            happy_btn = short_wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//*[contains(@label, '开心收下') or contains(@name, '开心收下')]"))
            )
            print("🎉 触发了阶段大奖！点击『开心收下』")
            happy_btn.click()
            time.sleep(2)

            # 回到主界面后，寻找并点击“待领取”
            print("🔍 寻找主界面的『待领取』按钮...")
            pending_btn = short_wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//*[contains(@label, '待领取') or contains(@name, '待领取')]"))
            )
            pending_btn.click()
            print("✅ 成功点击『待领取』，重新接上广告流！")
            time.sleep(2)

        except Exception:
            print("（常规循环，未触发阶段大奖，继续平稳运行）")
            pass

        loop_count += 1

    except Exception as e:
        print(f"⚠️ 发生异常卡住了，等待 5 秒后重试...")
        time.sleep(5)