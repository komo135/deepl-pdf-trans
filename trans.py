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
            driver.minimize_window()
            driver.maximize_window()
        except:
            pass

        # Get input fields using xpath
        text_area = driver.find_element(By.XPATH, "//*[@id='panelTranslateText']/div[3]/section[1]/div[3]/div[2]/textarea")
        # Empty input fields
        text_area.clear()

        # Accepts clipboard values as variables and removes line breaks
        text = pyperclip.paste()
        text = re.sub(r"([a-zA-Z0-9,]+)\r\n|([a-zA-Z0-9,]+)\n|([a-zA-Z0-9,]+)\r", r"\1 ", text).replace("  ", " ")
        # To remove "-¥r¥n", encode once, then remove and decode
        text = re.sub(b"\xe2\x80\x90\r\n|\xe2\x80\x90\r|\xe2\x80\x90\n", b"", text.encode()).decode()
        text = re.sub(r"\r\n|\r|\n", "\n\n", text).replace("\n\n\n", "\n")
        pyperclip.copy(text)

        text_area.click()
        pyautogui.hotkey("ctrl", "v")

        try:
            driver.find_element(By.ID, "tabTranslateText").click()
        except:
            pass

    except:
        print("An error has occurred.")


if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) == 2 else "en"
    url = f"https://www.deepl.com/{1}/translator"

    driver = webdriver.Chrome()
    driver.get(url)

    keyboard.add_hotkey("alt+c", main)
    keyboard.wait("esc")
    
