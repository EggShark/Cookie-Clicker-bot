from bs4 import BeautifulSoup as soup
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
        self.x2UpgradeIds = [7,8,9,44,110,192,294,307,428,480,506,700,0,1,2,3,4,5,6,43,82,109,188,189,660]#every 13 upgradeds is new buidling 0-12 is Grandma 13-25 is curors 
        self.score = None
    # Return number of cookies player has
    def getCookies(self): #Returns the ammout of cookies the player currently has
        return self.driver.execute_script("return Game.cookies")
    def giveCookies(self, x):
        self.driver.execute_script(f"Game.cookies += {x}")
    def getPrice(self, Object): #finds the price of the specified building

        for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return self.driver.execute_script(f'return Game.Objects[\"{self.objectList[i]}\"].bulkPrice')

    def getCPS(self, Object): #finds the Cookies per secoond of the specified building

       for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return self.driver.execute_script(f'return Game.Objects[\"{self.objectList[i]}\"].storedCps')

    def GetCpsPerC(self,Object): #Finds and give a decimal of how many cookies per second / cost the building will give so if a building costs 100 cookies and produces 1cps it will return .01

        for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return(self.getCPS(self.objectList[i])/self.getPrice(self.objectList[i]))

    def getBuildingAmt(self, Object): #gives the total amount of buildings
        for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return self.driver.execute_script(f'return Game.Objects[\"{self.objectList[i]}\"].amount')

    def getUpgradePrice(self,upId): #Gets upgrade prices
        return self.driver.execute_script(f'return Game.UpgradesById[{upId}].basePrice')

    def x2Upmath(self, Object, UpId): #The math for calculating efficency of upgrades
        return(((self.getBuildingAmt(Object) * self.getCPS(Object)) *2)/self.getUpgradePrice(UpId))

    def clickCookie(self): #Clicks the cookie
        self.bigCookie.click()

    def ChooseBuilding(self): #algorithm for choosing wiich building to buy
        
        optimalBuildings = []  # If the building is within certain paramaters it will appear here
        score = 0

        # If we can purchase the building in less than timeThreshold and is optimal based off of crabtrees equasion, add it to the optimalBuildings list
        for i in range(len(self.objectList)):
            if(self.getCPS(self.objectList[i]) / self.getPrice(self.objectList[i])) >= score:
                optimalBuildings.append(self.objectList[i])

                score = (self.getCPS(self.objectList[i]) / self.getPrice(self.objectList[i]))#ALL OF THIS CODE IS ZACHS's EXEPECT THIS LINE FUCK YOU
                self.score = score
            # Exit out of the loop once you can't get a building in <timeThreshold seconds
            else:
                break

        try:
            buildingToClick = f'product{self.objectList.index(optimalBuildings[len(optimalBuildings) - 1])}'  # Get the building with the highest cps to click


            # Check if we can click it
            if self.getCookies() >= self.getPrice(optimalBuildings[len(optimalBuildings)-1]):
                self.driver.find_element_by_id(buildingToClick).click()
        
        except:
            pass

    def checkUpGet(self, i): #will check to see if you can  buy the upgrade
        return self.driver.execute_script(f"return Game.UpgradesById[{i}].canBuy()")
    def getUpgrade(self):
        
            for i in range(len(self.x2UpgradeIds)):
                if self.checkUpGet(i):
                    if i in range(0,12): #Decides if its a grandma or not as in the list self.x2UpgradeIds[] 0-12 would be the grandma Ids
                        if self.x2Upmath("Grandma", self.x2UpgradeIds[i]) >= self.score:#do some math
                            self.driver.execute_script(f"Game.UpgradesById[{i}].buy()")
                            print("grandma purchased")                        
                        if i in range(12,25):
                            if self.x2Upmath("Cursor", self.x2UpgradeIds[i]) >= self.score:
                                self.driver.execute_script(f"Game.UpgradesById[{i}].buy()")
                                print("Cursour purchased")
                else:
                    pass
                

                    
                
