from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import re
import keyboard
import pyautogui
import sys


def main():
    try:
        pyautogui.hotkey("ctrl", "c")  # Copy text from select text
        try:
            # Make selenium the top screen
            # driver.minimize_window()
            driver.maximize_window()
        except:
            pass

        # Accepts clipboard values as variables and removes line breaks
        text = pyperclip.paste()
        text = re.sub(r"([\w,')''(']+)\r\n|([\w,')''(']+)\n|(\w,')''(']+)\r", r"\1 ", text).replace("  ", " ")
        text = re.sub(b"\xe2\x80\x90\r\n|\xe2\x80\x90\r|\xe2\x80\x90\n", b"", text.encode()).decode()
        text = re.sub(r"\r\n|\r|\n", "\n\n", text).replace("\n\n\n", "\n")
        pyperclip.copy(text)

        # Get input fields using xpath
        text_area = driver.find_element(By.XPATH, "//*[@id='panelTranslateText']/div[3]/section[1]/div[3]/div[2]/textarea")
        # Empty input fields
        text_area.clear()
        text_area.click()
        pyautogui.hotkey("ctrl", "v")

        driver.find_element(By.ID, "tabTranslateText").click()

    except:
        print("An error has occurred.")


if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) == 2 else "en"
    url = f"https://www.deepl.com/{lang}/translator"

    driver = webdriver.Chrome()
    driver.get(url)

    keyboard.add_hotkey("無変換", main)
    keyboard.wait("esc")

    driver.quit()
