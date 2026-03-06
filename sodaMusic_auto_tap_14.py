import time
import os  # 新增：用于调用 Mac 系统底层的声音命令
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 填入你的设备配置信息
options = XCUITestOptions()
options.platform_name = 'iOS'
options.platform_version = '26.3'
options.device_name = 'iPhone 14 Pro'
options.udid = '00008120-00043DA20E40201E'
options.automation_name = 'XCUITest'
options.set_capability('usePrebuiltWDA', True)

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
print("连接成功！全面升级为【带声音警报的4级状态机模式】...")

# ==========================================
# 正式进入全自动智能死循环
# ==========================================
loop_count = 1
while True:
    print(f"\n--- 🔄 开始第 {loop_count} 轮屏幕扫描 ---")
    try:
        # 总雷达保持不变：只要有任何目标出现，就唤醒分析逻辑
        any_target_xpath = (
            "//*["
            "contains(@label, '领取奖励') or contains(@name, '领取奖励') or contains(@value, '领取奖励') or "
            "contains(@label, '开心收下') or contains(@name, '开心收下') or contains(@value, '开心收下') or "
            "contains(@label, '开宝箱得金币') or contains(@name, '开宝箱得金币') or contains(@value, '开宝箱得金币') or "
            "contains(@label, '待领取') or contains(@name, '待领取') or contains(@value, '待领取') or "
            "contains(@label, '看广告膨胀') or contains(@name, '看广告膨胀') or contains(@value, '看广告膨胀') or "
            "contains(@label, '领取成功') or contains(@name, '领取成功') or contains(@value, '领取成功')"
            "]"
        )

        radar_wait = WebDriverWait(driver, 65)
        radar_wait.until(EC.presence_of_element_located((AppiumBy.XPATH, any_target_xpath)))

        # --- 🎯 目标已出现，开始按 4 级优先级精准打击 ---

        # 【优先级 1：绝对前景弹窗】
        foreground_xpath = (
            "//*["
            "contains(@label, '开心收下') or contains(@name, '开心收下') or contains(@value, '开心收下') or "
            "contains(@label, '领取奖励') or contains(@name, '领取奖励') or contains(@value, '领取奖励') or "
            "contains(@label, '看广告膨胀') or contains(@name, '看广告膨胀') or contains(@value, '看广告膨胀')"
            "]"
        )
        foregrounds = driver.find_elements(AppiumBy.XPATH, foreground_xpath)
        if foregrounds:
            btn = foregrounds[0]
            btn_text = btn.get_attribute("label") or btn.get_attribute("name") or btn.get_attribute("value") or "未知前景弹窗"
            print(f"🎯 [优先级1] 发现绝对前景目标: 【{btn_text}】，执行点击！")
            btn.click()
            time.sleep(3)
            loop_count += 1
            continue

        # 【优先级 2：背景广告关闭】
        ad_close_xpath = "//*[contains(@label, '领取成功') or contains(@name, '领取成功') or contains(@value, '领取成功')]"
        ad_closes = driver.find_elements(AppiumBy.XPATH, ad_close_xpath)
        if ad_closes:
            btn = ad_closes[0]
            btn_text = btn.get_attribute("label") or btn.get_attribute("name") or btn.get_attribute("value") or "未知关闭按钮"
            print(f"🎯 [优先级2] 发现广告关闭目标: 【{btn_text}】，执行点击！")
            btn.click()
            time.sleep(3)
            loop_count += 1
            continue

        # 【优先级 3：主界面“开宝箱得金币”】
        treasure_xpath = "//*[contains(@label, '开宝箱得金币') or contains(@name, '开宝箱得金币') or contains(@value, '开宝箱得金币')]"
        treasures = driver.find_elements(AppiumBy.XPATH, treasure_xpath)
        if treasures:
            print(f"🎯 [优先级3] 发现主界面目标: 【开宝箱得金币】，执行点击！")
            treasures[0].click()
            time.sleep(3)
            loop_count += 1
            continue

        # 【优先级 4：主界面“待领取”】
        pending_xpath = "//*[contains(@label, '待领取') or contains(@name, '待领取') or contains(@value, '待领取')]"
        pendings = driver.find_elements(AppiumBy.XPATH, pending_xpath)
        if pendings:
            print(f"🎯 [优先级4] 发现主界面目标: 【待领取】，执行点击！")
            pendings[0].click()
            time.sleep(3)
            loop_count += 1
            continue

    except Exception as e:
        print("⚠️ 屏幕上 65 秒都没有出现任何熟悉的按钮，可能是广告卡死或遇到新弹窗。")

        # 👇 新增的警报功能 👇
        print("🔔 正在播放 Mac 警报音...")
        # 连续播放三声清脆的 Glass 提示音，确保你能听到
        for _ in range(3):
            os.system("afplay /System/Library/Sounds/Glass.aiff")
            time.sleep(0.5)

        print("🔄 等待 5 秒后雷达重新扫描...")
        time.sleep(5)