import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Clicker:

    def __init__(self):
        PATH = 'C:\Program Files (x86)\chromedriver.exe'  # Path to chrome driver
        URL = 'https://orteil.dashnet.org/cookieclicker/'  # URL

        self.driver = webdriver.Chrome(PATH)  # Chrome driver

        self.driver.get(URL)  # Open URL In driver
        self.bigCookie = self.driver.find_element_by_id("bigCookie")
        WebDriverWait(self.driver, 3).until(lambda d: d.find_element_by_tag_name("span"))  # Wait for page to load
        self.objectList = ["Cursor","Grandma","Farm","Mine","Factory","Bank","Temple","Wizard tower","Shipment","Alchemy lab","Portal","Time machine","Antimatter condenser","Prism", "Chancemaker", "Fractal engine", "Javascript console","Idleverse"]
        print(self.GetCpsPerC("Grandma"))
    # Return number of cookies player has
    def getCookies(self):
        return self.driver.execute_script("return Game.cookies")
    def getPrice(self, Object):

        for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return self.driver.execute_script(f'return Game.Objects[\"{self.objectList[i]}\"].bulkPrice')

    def getCPS(self, Object):

       for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return self.driver.execute_script(f'return Game.Objects[\"{self.objectList[i]}\"].storedCps')

    def GetCpsPerC(self,Object):

        for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return(self.getCPS(self.objectList[i])/self.getPrice(self.objectList[i]))
    def clickCookie(self):
        self.bigCookie.click()
    def ChooseBuilding(self):
        self.CpsCList = []
        for i in range(len(self.objectList)):
            self.CpsCList.append(self.GetCpsPerC(self.objectList[i]))
        if max(self.CpsCList) == self.CpsCList[0]:
            return "product0"
        elif max(self.CpsCList) == self.CpsCList[1]:
            return "product1"
        elif max(self.CpsCList) == self.CpsCList[2]:
            return "product2"
        elif max(self.CpsCList) == self.CpsCList[3]:
            return "product3"
        elif max(self.CpsCList) == self.CpsCList[4]:
            return "product4"
        elif max(self.CpsCList) == self.CpsCList[5]:
            return "product5"
        elif max(self.CpsCList) == self.CpsCList[6]:
            return "product6"
        elif max(self.CpsCList) == self.CpsCList[7]:
            return "product7"
        elif max(self.CpsCList) == self.CpsCList[8]:
            return "product8"
        elif max(self.CpsCList) == self.CpsCList[9]:
            return "product9"
        elif max(self.CpsCList) == self.CpsCList[10]:
            return "product10"
        elif max(self.CpsCList) == self.CpsCList[11]:
            return "product11"
        elif max(self.CpsCList) == self.CpsCList[12]:
            return "product12"
        elif max(self.CpsCList) == self.CpsCList[13]:
            return "product13"
        elif max(self.CpsCList) == self.CpsCList[14]:
            return "product13"
        elif max(self.CpsCList) == self.CpsCList[15]:
            return "product15"
        elif max(self.CpsCList) == self.CpsCList[16]:
            return "product16"
        elif max(self.CpsCList) == self.CpsCList[17]:
            return "product17"
        elif max(self.CpsCList) == self.CpsCList[18]:
            return "product18"
        elif max(self.CpsCList) == self.CpsCList[19]:
            return "product19"
    def buyBuilding(self):
        if self.ChooseBuilding() == "product0":
            if self.getCookies() >= self.getPrice(self.objectList[0]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product1":
            if self.getCookies() >= self.getPrice(self.objectList[1]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product2":
            if self.getCookies() >= self.getPrice(self.objectList[2]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product3":
            if self.getCookies() >= self.getPrice(self.objectList[3]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product4":
            if self.getCookies() >= self.getPrice(self.objectList[4]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product5":
            if self.getCookies() >= self.getPrice(self.objectList[5]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product6":
            if self.getCookies() >= self.getPrice(self.objectList[6]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product7":
            if self.getCookies() >= self.getPrice(self.objectList[7]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product8":
            if self.getCookies() >= self.getPrice(self.objectList[8]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product9":
            if self.getCookies() >= self.getPrice(self.objectList[9]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product10":
            if self.getCookies() >= self.getPrice(self.objectList[10]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product11":
            if self.getCookies() >= self.getPrice(self.objectList[11]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product12":
            if self.getCookies() >= self.getPrice(self.objectList[12]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product13":
            if self.getCookies() >= self.getPrice(self.objectList[13]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product14":
            if self.getCookies() >= self.getPrice(self.objectList[14]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product15":
            if self.getCookies() >= self.getPrice(self.objectList[15]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product16":
            if self.getCookies() >= self.getPrice(self.objectList[16]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product17":
            if self.getCookies() >= self.getPrice(self.objectList[17]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product18":
            if self.getCookies() >= self.getPrice(self.objectList[18]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass
        elif self.ChooseBuilding() == "product19":
            if self.getCookies() >= self.getPrice(self.objectList[19]):
                item = self.driver.find_element_by_id(self.ChooseBuilding())
                item.click()
            else:
                pass