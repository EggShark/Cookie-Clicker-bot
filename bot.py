
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
class Clicker:

    def __init__(self):
        PATH = 'C:\Program Files (x86)\chromedriver.exe'  # Path to chrome driver
        URL = 'https://orteil.dashnet.org/cookieclicker/'  # URL

        self.driver = webdriver.Chrome(PATH)  # Chrome driver

        self.driver.get(URL)  # Open URL In driver
        self.bigCookie = self.driver.find_element_by_id("bigCookie")
        self.objectList = ["Cursor","Grandma","Farm","Mine","Factory","Bank","Temple","Wizard tower","Shipment","Alchemy lab","Portal","Time machine","Antimatter condenser","Prism", "Chancemaker", "Fractal engine", "Javascript console","Idleverse"]
        self.x2UpgradeIds = [7,8,9,44,110,192,294,307,428,480,506,700,0,1,2,3,4,5,6,43,82,109,188,189,660]#every 13 upgradeds is new buidling 0-12 is Grandma 13-25 is curors 
        self.score = None
        self.upScore = None
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        self.testarr = np.array([[1,2,3], [4,5,6]])
        self.upids = np.array([list(['Cursor', 0, 1, 2]),list(['Grandma', 7, 8, 9, 44, 110, 192, 294, 307, 428, 480, 506, 662, 700]), list(['Farm', 19, 11, 12, 45, 111, 193, 295, 308, 429, 481, 507, 663, 701]), list(['Mine', 16, 17, 18, 47, 113, 195, 296, 309, 430, 482, 508, 664, 702]), list(['Factory', 13, 14, 15, 46, 112, 194, 297, 310, 483, 509, 665, 703]), list(['Bank', 323, 233, 234, 235, 236, 237, 298, 311, 432, 484, 510, 666, 704]), list(['Temple', 238, 239, 240, 241, 242, 243, 299, 312, 433, 485, 511, 667, 705]), list(['Wizard tower', 244, 245, 246, 247, 248, 249, 300, 313, 434, 486, 512, 668, 706]), list(['Shipment', 19, 20, 21, 48, 114, 196, 301, 314, 435, 487, 513, 669, 707]), list(['Alchemy lab', 22, 23, 24, 49, 115, 197, 302, 315, 436, 488, 514, 670, 708]), list(['Portal', 25, 26, 27, 50, 116, 198, 303, 316, 437, 489, 515, 671, 709]), list(['Time machine', 28, 29, 30, 51, 117, 199, 304, 317, 438, 490, 516, 672, 710]), list(['Antimatter condenser', 99, 100, 101, 102, 118, 200, 305, 318, 439, 491, 517, 673, 711]), list(['Prism', 175, 176, 177, 178, 179, 201, 306, 319, 440, 492, 518, 674, 712]), list(['Chancemaker', 416, 417, 418, 419, 420, 421, 422, 423, 441, 493, 519, 675, 713]), list(['Fractal engine', 552, 523, 524, 526, 527, 528, 529, 530, 531, 532, 676, 714]), list(['Javascript console', 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 677, 715]), list(['Idleverse', 683, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695])], dtype=object)
        print(self.testarr.ndim)
        WebDriverWait(self.driver, 3).until(lambda d: d.find_element_by_tag_name("span"))  # Wait for page to load
       
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
        self.driver.execute_script("Game.ClickCookie()")

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
            buildingToClick = optimalBuildings[len(optimalBuildings) - 1]  # Get the building with the highest cps to click


            # Check if we can click it
            if self.getCookies() >= self.getPrice(buildingToClick):
                self.driver.execute_script(f"Game.Objects[{buildingToClick}].buy()")
        
        except:
            pass

    def checkUpGet(self, i): #will check to see if you can  buy the upgrade
        return self.driver.execute_script(f"return Game.UpgradesById[{i}].canBuy()")
    def buyUpgrade(self, upId):
        self.driver.execute_script(f'Game.UpgradesById[{upId}].buy()')
    def ShimmerSpawned(self):
        return self.driver.execute_script("return Game.shimmers.length")
    def ShimmerLogic(self):
        if self.ShimmerSpawned() >= 1:
            shimmer = self.driver.find_element_by_class_name("shimmer")
            shimmer.click()
    def npUpgrade(self):
        ix = 0

        for x in self.upids:
            bestUpgrade = [] #kinda mimicing zachs orignal building code
            iy = 0
            score = 0
            for y in x:
                if iy == 0:
                    pass
                else:
                    if self.x2Upmath(self.upids[ix][0],self.upids[ix][iy]) >= score:
                        bestUpgrade.append(self.upids[ix][iy])
                        score = self.x2Upmath(self.upids[ix][0],self.upids[ix][iy])
                        self.upScore = score

                iy += 1
            ix += 1
        upgradeToBuy = bestUpgrade[len(bestUpgrade)-1]
        print("the id of the best upgrade is:", upgradeToBuy, self.upScore, self.score)
        if self.upScore > self.score and self.checkUpGet(upgradeToBuy):
            self.buyUpgrade(upgradeToBuy)