import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import bot as c

clicker = c.Clicker()  # Clicker object
print(clicker.x2Upmath("Grandma", clicker.x2UpgradeIds[0]))
def main():
    clicker.getUpgrade()
    clicker.clickCookie()
    clicker.ChooseBuilding()



# Idk what it does but its important
if __name__ == '__main__':
    while True:
        main()