import time
import os
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================
# 1. 填入你的设备配置信息 (专为 iPhone 7 Plus 隔离配置)
# ==========================================
options = XCUITestOptions()
options.platform_name = 'iOS'
options.platform_version = '15.8.5'  # 已修改为 iPhone 7 的系统版本
options.device_name = 'iPhone 7 Plus' # 已修改设备名
options.udid = '6f66d4e90b71d0e823ccc6a8281fb6e0f27885c3' # 已替换为你的 UDID
options.automation_name = 'XCUITest'
options.set_capability('usePrebuiltWDA', True)

# 【关键新增】隔离 WDA 通讯端口，防止与 iPhone 17 冲突 (默认是 8100)
options.set_capability('wdaLocalPort', 8101)

# 【关键修改】指向 4724 端口的第二个 Appium 服务
driver = webdriver.Remote('http://127.0.0.1:4724', options=options)
print("连接成功！iPhone 7 Plus 专属路线已接通，全面升级为【带声音警报的6级状态机模式 (贪婪双选版)】...")

# ==========================================
# 2. 正式进入全自动智能死循环 (逻辑与原版完全一致)
# ==========================================
loop_count = 1
while True:
    print(f"\n--- 🔄 开始第 {loop_count} 轮屏幕扫描 (iPhone 7) ---")
    try:
        # 总雷达：新增对 '看广告视频再赚' 和 '我知道了' 的监控
        any_target_xpath = (
            "//*["
            "contains(@label, '看广告视频再赚') or contains(@name, '看广告视频再赚') or contains(@value, '看广告视频再赚') or "
            "contains(@label, '我知道了') or contains(@name, '我知道了') or contains(@value, '我知道了') or "
            "contains(@label, '评价并关闭') or contains(@name, '评价并关闭') or contains(@value, '评价并关闭') or "
            "contains(@label, '领取奖励') or contains(@name, '领取奖励') or contains(@value, '领取奖励') or "
            "contains(@label, '开心收下') or contains(@name, '开心收下') or contains(@value, '开心收下') or "
            "contains(@label, '开宝箱得金币') or contains(@name, '开宝箱得金币') or contains(@value, '开宝箱得金币') or "
            "contains(@label, '待领取') or contains(@name, '待领取') or contains(@value, '待领取') or "
            "contains(@label, '看广告膨胀') or contains(@name, '看广告膨胀') or contains(@value, '看广告膨胀') or "
            "contains(@label, '领取成功') or contains(@name, '领取成功') or contains(@value, '领取成功') or "
            "contains(@label, '点击领') or contains(@name, '点击领') or contains(@value, '点击领') or "
            "contains(@label, '秒后领') or contains(@name, '秒后领') or contains(@value, '秒后领')"
            "]"
        )

        radar_wait = WebDriverWait(driver, 65)
        radar_wait.until(EC.presence_of_element_located((AppiumBy.XPATH, any_target_xpath)))

        # --- 🎯 目标已出现，开始按 6 级优先级精准打击 ---

        # 【优先级 1：高优奖励与绝对前景弹窗】(绝对不放过看视频再赚)
        foreground_xpath = (
            "//*["
            "contains(@label, '看广告视频再赚') or contains(@name, '看广告视频再赚') or contains(@value, '看广告视频再赚') or "
            "contains(@label, '评价并关闭') or contains(@name, '评价并关闭') or contains(@value, '评价并关闭') or "
            "contains(@label, '开心收下') or contains(@name, '开心收下') or contains(@value, '开心收下') or "
            "contains(@label, '领取奖励') or contains(@name, '领取奖励') or contains(@value, '领取奖励') or "
            "contains(@label, '看广告膨胀') or contains(@name, '看广告膨胀') or contains(@value, '看广告膨胀')"
            "]"
        )
        foregrounds = driver.find_elements(AppiumBy.XPATH, foreground_xpath)
        if foregrounds:
            btn = foregrounds[0]
            btn_text = btn.get_attribute("label") or btn.get_attribute("name") or btn.get_attribute("value") or "未知前景弹窗"
            print(f"🎯 [优先级1] 发现高优目标: 【{btn_text}】，执行点击！")
            btn.click()
            time.sleep(3)
            loop_count += 1
            continue

        # 【优先级 2：背景广告关闭与普通确认】(把“我知道了”贬到第二级，只有没额外奖励时才点它)
        ad_close_xpath = (
            "//*["
            "contains(@label, '领取成功') or contains(@name, '领取成功') or contains(@value, '领取成功') or "
            "contains(@label, '我知道了') or contains(@name, '我知道了') or contains(@value, '我知道了')"
            "]"
        )
        ad_closes = driver.find_elements(AppiumBy.XPATH, ad_close_xpath)
        if ad_closes:
            btn = ad_closes[0]
            btn_text = btn.get_attribute("label") or btn.get_attribute("name") or btn.get_attribute("value") or "未知关闭按钮"
            print(f"🎯 [优先级2] 发现普通关闭/确认目标: 【{btn_text}】，执行点击！")
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

        # 【优先级 5：主界面“动态奖励”宝箱】
        click_claim_xpath = "//*[contains(@label, '点击领') or contains(@name, '点击领') or contains(@value, '点击领')]"
        click_claims = driver.find_elements(AppiumBy.XPATH, click_claim_xpath)
        if click_claims:
            btn = click_claims[0]
            btn_text = btn.get_attribute("label") or btn.get_attribute("name") or btn.get_attribute(
                "value") or "未知动态奖励宝箱"
            print(f"🎯 [优先级5] 发现动态奖励目标: 【{btn_text}】，执行点击！")
            btn.click()
            time.sleep(3)
            loop_count += 1
            continue

        # 【优先级 6：主界面“动态倒计时”宝箱】
        countdown_xpath = "//*[contains(@label, '秒后领') or contains(@name, '秒后领') or contains(@value, '秒后领')]"
        countdowns = driver.find_elements(AppiumBy.XPATH, countdown_xpath)
        if countdowns:
            btn = countdowns[0]
            btn_text = btn.get_attribute("label") or btn.get_attribute("name") or btn.get_attribute(
                "value") or "未知倒计时宝箱"
            print(f"🎯 [优先级6] 发现倒计时宝箱目标: 【{btn_text}】，执行点击！")
            btn.click()
            time.sleep(3)
            loop_count += 1
            continue

    except Exception as e:
        print("⚠️ 屏幕上 65 秒都没有出现任何熟悉的按钮，可能是广告卡死或遇到新弹窗。")

        print("🔔 正在播放 Mac 警报音...")
        for _ in range(3):
            os.system("afplay /System/Library/Sounds/Glass.aiff")
            time.sleep(0.5)

        print("🔄 等待 5 秒后雷达重新扫描...")
        time.sleep(5)