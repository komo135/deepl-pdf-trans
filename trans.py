from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import re
import keyboard
import pyautogui
import sys
from selenium.webdriver.common.keys import Keys
# from pynput import keyboard


def start():
    global driver
    driver = webdriver.Chrome()
    driver.get(url)


def trans():
    try:
        pyautogui.hotkey("ctrl", "c")  # Copy text from select text
        try:
            # Make selenium the top screen
            # driver.minimize_window()
            driver.maximize_window()
        except:
            pass

        # Accepts clipboard values as variables and removes line breaks
        text = False
        while not text:
            try:
                text = pyperclip.paste()
            except:
                pass
        text = re.sub(r"([\w,')''('=]+)\r\n|([\w,')''('=]+)\n|(\w,')''('=]+)\r", r"\1 ", text).replace("  ", " ")
        # text = re.sub(r"([a-zA-Z0-9,')''(']+)\r\n|([a-zA-Z0-9,')''(']+)\n|([a-zA-Z0-9,')''(']+)\r", r"\1 ",
        # text).replace("  ", " ") To remove "-¥r¥n", encode once, then remove and decode
        text = re.sub(b"\xe2\x80\x90\r\n|\xe2\x80\x90\r|\xe2\x80\x90\n", b"", text.encode()).decode()
        text = re.sub(r"\r\n|\r|\n", "\n\n", text).replace("\n\n\n", "\n")
        pyperclip.copy(text)

        # Get input fields using xpath
        text_area = driver.find_element(By.XPATH, "//*[@id='panelTranslateText']/div[3]/section[1]/div[3]/div[2]/textarea")
        # Empty input fields
        text_area.clear()
        text_area.send_keys(Keys.CONTROL, 'v')

        driver.find_element(By.ID, "tabTranslateText").click()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    driver: webdriver.Chrome
    lang = sys.argv[1] if len(sys.argv) == 2 else "ja"
    url = f"https://www.deepl.com/{lang}/translator"

    while True:
        if keyboard.is_pressed("ctrl+shift+a"):
            # start selenium and open deepl translator
            start()
        if keyboard.is_pressed("ctrl+shift+b"):
            # translate text
            trans()
        if keyboard.is_pressed("esc"):
            # close selenium
            driver.quit()
