
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
import math
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
        self.upids = np.array([list(['Cursor', 0, 1, 2]),list(['Grandma', 7, 8, 9, 44, 110, 192, 294, 307, 428, 480, 506, 662, 700]), list(['Farm', 19, 11, 12, 45, 111, 193, 295, 308, 429, 481, 507, 663, 701]), list(['Mine', 16, 17, 18, 47, 113, 195, 296, 309, 430, 482, 508, 664, 702]), list(['Factory', 13, 14, 15, 46, 112, 194, 297, 310, 483, 509, 665, 703]), list(['Bank', 323, 233, 234, 235, 236, 237, 298, 311, 432, 484, 510, 666, 704]), list(['Temple', 238, 239, 240, 241, 242, 243, 299, 312, 433, 485, 511, 667, 705]), list(['Wizard tower', 244, 245, 246, 247, 248, 249, 300, 313, 434, 486, 512, 668, 706]), list(['Shipment', 19, 20, 21, 48, 114, 196, 301, 314, 435, 487, 513, 669, 707]), list(['Alchemy lab', 22, 23, 24, 49, 115, 197, 302, 315, 436, 488, 514, 670, 708]), list(['Portal', 25, 26, 27, 50, 116, 198, 303, 316, 437, 489, 515, 671, 709]), list(['Time machine', 28, 29, 30, 51, 117, 199, 304, 317, 438, 490, 516, 672, 710]), list(['Antimatter condenser', 99, 100, 101, 102, 118, 200, 305, 318, 439, 491, 517, 673, 711]), list(['Prism', 175, 176, 177, 178, 179, 201, 306, 319, 440, 492, 518, 674, 712]), list(['Chancemaker', 416, 417, 418, 419, 420, 421, 422, 423, 441, 493, 519, 675, 713]), list(['Fractal engine', 552, 523, 524, 526, 527, 528, 529, 530, 531, 532, 676, 714]), list(['Javascript console', 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 677, 715]), list(['Idleverse', 683, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695])], dtype=object)
        self.upIdsPrices = np.array([list(['Cursor', 100, 500, 10000]),list(['Grandma', 1000, 5000, 50000, 5000000, 500000000, 50000000000, 50000000000000, 50000000000000000, 50000000000000000000, 50000000000000000000000, 5000000000000000000000000000, 5000000000000000000000000000000, 50000000000000000000000000000000000]), list(['Farm', 11000, 55000, 550000, 55000000, 5500000000, 550000000000, 550000000000000, 550000000000000000, 550000000000000000000 , 550000000000000000000000 , 5500000000000000000000000000 , 55000000000000000000000000000000 , 550000000000000000000000000000000000 ]), list(['Mine', 120000, 600000, 6000000, 600000000, 60000000000, 6000000000000, 6000000000000000, 6000000000000000000, 6000000000000000000000, 6000000000000000000000000, 60000000000000000000000000000 , 600000000000000000000000000000000 , 6000000000000000000000000000000000000 ]), list(['Factory', 1300000, 6500000, 65000000, 6500000000, 650000000000, 65000000000000, 65000000000000000, 65000000000000000000 , 65000000000000000000000 , 650000000000000000000000000000 , 6500000000000000000000000000000000 , 6000000000000000000000000000000000000 ]), list(['Bank', 14000000, 70000000, 700000000, 70000000000, 70000000000000, 70000000000000000, 70000000000000000000, 70000000000000000000000, 70000000000000000000000000, 700000000000000000000000000 , 7000000000000000000000000000000 , 70000000000000000000000000000000000 , 700000000000000000000000000000000000000]), list(['Temple', 200000000, 1000000000, 10000000000, 1000000000000, 100000000000000, 10000000000000000, 10000000000000000000, 10000000000000000000000, 10000000000000000000000000, 10000000000000000000000000000, 100000000000000000000000000000000, 1000000000000000000000000000000000000, 10000000000000000000000000000000000000000]), list(['Wizard tower', 3300000000, 16500000000, 165000000000, 16500000000000, 1650000000000000, 165000000000000000, 165000000000000000000, 165000000000000000000000, 165000000000000000000000000, 165000000000000000000000000000, 1650000000000000000000000000000000 , 16500000000000000000000000000000000000 , 165000000000000000000000000000000000000000 ]), list(['Shipment', 51000000000, 255000000000, 2550000000000, 255000000000000, 25500000000000000, 2550000000000000000, 2550000000000000000000, 2550000000000000000000000, 2550000000000000000000000000, 2550000000000000000000000000000, 2550000000000000000000000000000000, 655000000000000000000000000000000000000 , 2550000000000000000000000000000000000000000]), list(['Alchemy lab', 750000000000, 3750000000000, 37500000000000, 3750000000000000, 37500000000000000, 3750000000000000000, 3750000000000000000000, 3750000000000000000000000, 3750000000000000000000000000, 3750000000000000000000000000000, 37500000000000000000000000000000000, 375000000000000000000000000000000000, 3750000000000000000000000000000000000000]), list(['Portal', 10000000000, 50000000000, 500000000000, 50000000000000, 5000000000000000, 5000000000000000000, 5000000000000000000000, 5000000000000000000000000, 5000000000000000000000000000, 5000000000000000000000000000000, 5000000000000000000000000000000000000 , 50000000000000000000000000000000000000000, 500000000000000000000000000000000000000000000]), list(['Time machine', 140000000000, 700000000000, 7000000000000, 700000000000000, 70000000000000000, 7000000000000000000, 7000000000000000000000, 7000000000000000000000000, 7000000000000000000000000, 700000000000000000000000000000, 7000000000000000000000000000000000, 70000000000000000000000000000000000000, 7000000000000000000000000000000000000000000000 ]), list(['Antimatter condenser', 1700000000000, 8500000000000, 85000000000000, 8500000000000000, 850000000000000000, 85000000000000000000, 85000000000000000000000, 85000000000000000000000000000, 85000000000000000000000000000000, 85000000000000000000000000000000000, 850000000000000000000000000000000000000, 8500000000000000000000000000000000000000000, 85000000000000000000000000000000000000000000000]), list(['Prism', 21000000000000, 105000000000000, 1050000000000000, 105000000000000000, 10500000000000000000, 1050000000000000000000, 1050000000000000000000000, 1050000000000000000000000000, 1050000000000000000000000000000, 1050000000000000000000000000000000, 10500000000000000000000000000000000000, 105000000000000000000000000000000000000000, 1050000000000000000000000000000000000000000000000]), list(['Chancemaker', 260000000000000, 1300000000000000, 13000000000000000, 1300000000000000000, 130000000000000000000, 13000000000000000000000, 13000000000000000000000000, 13000000000000000000000000000, 13000000000000000000000000000000, 13000000000000000000000000000000000, 130000000000000000000000000000000000000, 1300000000000000000000000000000000000000000000, 13000000000000000000000000000000000000000000000000]), list(['Fractal engine', 3100000000000000, 15500000000000000, 155000000000000000, 15500000000000000000, 1550000000000000000000, 1550000000000000000000000, 1550000000000000000000000000, 1550000000000000000000000000000, 1550000000000000000000000000000000, 1550000000000000000000000000000000000000000, 15500000000000000000000000000000000000000000000, 155000000000000000000000000000000000000000000000000]), list(['Javascript console', 710000000000000000, 3550000000000000000, 35500000000000000000, 3550000000000000000000, 355000000000000000000000, 35500000000000000000000000, 35500000000000000000000000000, 35500000000000000000000000000000, 35500000000000000000000000000000000, 35500000000000000000000000000000000000, 355000000000000000000000000000000000000000000, 35500000000000000000000000000000000000000000000, 3550000000000000000000000000000000000000000000000]), list(['Idleverse', 120000000000000000000, 600000000000000000000, 6000000000000000000000, 600000000000000000000000, 60000000000000000000000000, 6000000000000000000000000000, 6000000000000000000000000000, 6000000000000000000000000000000, 6000000000000000000000000000000000, 6000000000000000000000000000000000000, 60000000000000000000000000000000000000000, 600000000000000000000000000000000000000000])], dtype=object)
        WebDriverWait(self.driver, 3).until(lambda d: d.find_element_by_tag_name("span"))  # Wait for page to load
        self.newthing = True
        self.UpgradeToBuy = None
        self.basePrices = {"Cursor": 15,
        "Grandma": 100,
        "Farm": 1100,
        "Mine": 12000,
        "Factory": 130000,
        "Bank": 1400000,
        "Temple": 20000000,
        "Wizard tower": 330000000,
        "Shipment": 5100000000,
        "Alchemy lab": 75000000000,
        "Portal": 1000000000,
        "Time machine": 14000000000000,
        "Antimatter condenser": 170000000000000,
        "Prism": 2100000000000000,
        "Chancemaker": 26000000000000000,
        "Fractal engine": 310000000000000000,
        "Javascript console": 71000000000000000000,
        "Idleverse": 12000000000000000000000}
        self.buildingAmt = {"Cursor": 0,
        "Grandma": 0,
        "Farm": 0,
        "Factory": 0,
        "Mine": 0,
        "Bank": 0,
        "Temple": 0,
        "Wizard tower": 0,
        "Shipment": 0,
        "Alchemy lab": 0,
        "Portal": 0,
        "Time machine": 0,
        "Antimatter condenser": 0,
        "Prism": 0,
        "Chancemaker": 0,
        "Fractal engine": 0,
        "Javascript console": 0,
        "Idleverse": 0}
        self.BaseCps = {"Cursor": .1,
        "Grandma": 1,
        "Farm": 8,
        "Factory": 260,
        "Mine": 47,
        "Bank": 1400,
        "Temple": 7800,
        "Wizard tower": 44000,
        "Shipment": 260000,
        "Alchemy lab": 1600000,
        "Portal": 10000000,
        "Time machine": 65000000,
        "Antimatter condenser": 430000000,
        "Prism": 2900000000,
        "Chancemaker": 21000000000,
        "Fractal engine": 150000000000,
        "Javascript console": 1100000000000,
        "Idleverse": 8300000000000}
        self.GrandmaTypesInfo = [
            {"name": "Farm", "id":57, "price":55000},
            {"name":"Factory", "id":58, "price":600000}, 
            {"name":"Mine","id":59 , "price":6500000}, 
            {"name":"Bank","id":250, "price":70000000},
            {"name":"Temple","id":251, "price":1000000000},
            {"name":"Wizard tower","id":252, "price":16500000000},
            {"name":"Shipment","id":60, "price":255000000000},
            {"name":"Alchemy lab","id":61, "price":3750000000},
            {"name":"Portal","id":62, "price":50000000000},
            {"name": "Time machine","id":63, "price":700000000000},
            {"name":"Antimatter condenser","id":103, "price":8500000000000},
            {"name":"Prism","id":180, "price":105000000000000},
            {"name":"Chancemaker","id":415, "price":1300000000000000},
            {"name":"Fractal engine","id":521, "price":15500000000000000},
            {"name":"Javascript console","id":593, "price": 3550000000000000000},
            {"name":"Idleverse","id":684, "price":60000000000000000000}
        ]
        # Return number of cookies player has
    def getCookies(self): #Returns the ammout of cookies the player currently has
        return self.driver.execute_script("return Game.cookies")

    def giveCookies(self, x):
        self.driver.execute_script(f"Game.cookies += {x}")

    def getPrice(self, Object): #finds the price of the specified building

        for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return math.ceil(self.basePrices[Object]*(1.15**self.getBuildingAmt(Object)))

    def getCPS(self, Object): #finds the Cookies per secoond of the specified building

       for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return self.BaseCps[Object]

    def GetCpsPerC(self,Object): #Finds and give a decimal of how many cookies per second / cost the building will give so if a building costs 100 cookies and produces 1cps it will return .01

        for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return(self.getCPS(self.objectList[i])/self.getPrice(self.objectList[i]))

    def getBuildingAmt(self, Object): #gives the total amount of buildings
        for i in range(len(self.objectList)):
            if self.objectList[i].__contains__(Object):
                return self.buildingAmt[Object]

    def getUpgradePrice(self,upX,UpY): #Gets upgrade prices
        return self.upIdsPrices[upX][UpY]

    def x2Upmath(self, Object, UpX, UpY): #The math for calculating efficency of upgrades
        return(((self.getBuildingAmt(Object) * self.getCPS(Object)) *2)/self.getUpgradePrice(UpX, UpY))

    def clickCookie(self): #Clicks the cookie
        self.driver.execute_script("Game.ClickCookie()")

    def buyUpgrade(self, upId):
        self.driver.execute_script(f'Game.UpgradesById[{upId}].buy()')

    def buyBuilding(self, Object):
        self.driver.execute_script(f"Game.Objects[\"{Object}\"].buy()")
        self.buildingAmt[Object] += 1

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

        buildingToClick = optimalBuildings[len(optimalBuildings) - 1]  # Get the building with the highest cps to click


        # Check if we can click it
        if self.getCookies() >= self.getPrice(buildingToClick):
            self.buyBuilding(buildingToClick)
            self.newthing = True
        


    def checkUpGet(self, i): #will check to see if you can  buy the upgrade
        return self.driver.execute_script(f"return Game.UpgradesById[{i}].unlocked")

    def canBuyUpgrade(self, upid):
        return self.driver.execute_script(f'return Game.UpgradesById[{upid}].canBuy()')

    def ShimmerSpawned(self):
        return self.driver.execute_script("return Game.shimmers.length")

    def ShimmerLogic(self):
        if self.ShimmerSpawned() >= 1:
            shimmer = self.driver.find_element_by_class_name("shimmer")
            shimmer.click()

    def npUpgrade(self):
        ix = 0
        score = 0
        bestUpgrade = None
        if self.newthing == True:
            for x in self.upids:
                #kinda mimicing zachs orignal building code
                iy = 0
                for y in x:
                    if iy == 0:
                        pass
                    elif self.x2Upmath(self.upids[ix][0],ix, iy) >= score:
                        bestUpgrade = self.upids[ix][iy]
                        self.UpgradeToBuy = bestUpgrade
                        score = self.x2Upmath(self.upids[ix][0],ix, iy)
                        self.upScore = score
                        self.buildingGroup = ix
                        self.IdLocation = iy

                    iy += 1
                ix += 1
            self.newthing = False
        #print("the id of the best upgrade is:", self.UpgradeToBuy, self.upids[self.buildingGroup][self.IdLocation] ,self.upScore, self.score, self.buildingGroup, self.IdLocation)
        if self.upScore > self.score and self.canBuyUpgrade(self.UpgradeToBuy):
            self.buyUpgrade(self.UpgradeToBuy)
            self.BaseCps[self.upids[self.buildingGroup][self.IdLocation]] = self.BaseCps[self.upids[self.buildingGroup][0]] * 2
            self.upids[self.buildingGroup].pop(self.IdLocation)
            self.upIdsPrices[self.buildingGroup].pop(self.IdLocation)
            self.newthing = True
    def GrandmaTypesMath(self, building, incremetnal, price):
        print(((self.BaseCps["Grandma"] * 2) + (self.BaseCps[building] * (.01 *(math.floor(self.buildingAmt["Grandma"]/ incremetnal))))/ price))
        return ((self.BaseCps["Grandma"] * 2) + (self.BaseCps[building] * (.01 *(math.floor(self.buildingAmt["Grandma"]/ incremetnal))))/ price)
    def Grandmatypes(self):
        score = 0
        bestGrandmaType = []
        for i in range(len(self.GrandmaTypesInfo)):
            if self.GrandmaTypesMath(self.GrandmaTypesInfo[i]["name"], i + 1, self.GrandmaTypesInfo[i]["price"]) >= score:
                score = self.GrandmaTypesMath(self.GrandmaTypesInfo[i]["name"], i + 1, self.GrandmaTypesInfo[i]["price"])
                print(score)
