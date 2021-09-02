
"""
Made by TheEggShark in colaboration with Zachary-d-Robison
And ty ben for the critzims
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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
        self.upScore = 0
        self.milkLevel = None
        self.Milkfactor = 0.0
        WebDriverWait(self.driver, 3).until(lambda d: d.find_element_by_tag_name("span"))  # Wait for page to load
        self.newthing = True
        self.UpgradeToBuy = None
        self.basePrices = {
        "Cursor": 15,
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
        "Idleverse": 12000000000000000000000
        }
        self.buildingAmt = {
            "Cursor": 0,
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
            "Idleverse": 0
        }
        self.BaseCps = {
            "Cursor": .1,
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
            "Idleverse": 8300000000000
        }
        self.upgrades = [
            {"building":"Cursor","id":0,"price":100,"function":self.x2Upmath,"args":("Cursor",0),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Cursor", "id":1, "price":500,"function":self.x2Upmath,"args":("Cursor",1),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Cursor","id":2,"price":10000, "function":self.x2Upmath,"args":("Cursor",2),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":7,"price":1000,"function":self.x2Upmath,"args":("Grandma",3),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":8,"price":5000,"function":self.x2Upmath,"args":("Grandma",4),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":9,"price":50000,"function":self.x2Upmath,"args":("Grandma",5),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":44,"price":5000000,"function":self.x2Upmath,"args":("Grandma",6),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":110,"price":500_000_000,"function":self.x2Upmath,"args":("Grandma",7),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":192,"price":50_000_000_000,"function":self.x2Upmath,"args":("Grandma",8),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":294,"price":50_000_000_000_000,"function":self.x2Upmath,"args":("Grandma",9),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":307,"price":50_000_000_000_000_000,"function":self.x2Upmath,"args":("Grandma",10),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":428,"price":50_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Grandma",11),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":480,"price":50_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Grandma",12),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":506,"price":500_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Grandma",13),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":662,"price":5_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Grandma",14),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Grandma","id":700,"price":50_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Grandma",15),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":10,"price":11_000,"function":self.x2Upmath,"args":("Farm",16),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":11,"price":55_000,"function":self.x2Upmath,"args":("Farm",17),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":12,"price":550_000,"function":self.x2Upmath,"args":("Farm",18),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":13,"price":55_000_000,"function":self.x2Upmath,"args":("Farm",19),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":45,"price":5_500_000_000, "function":self.x2Upmath,"args":("Farm",20),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":111,"price":550_000_000_000,"function":self.x2Upmath,"args":("Farm",21),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":193,"price":550_000_000_000_000,"function":self.x2Upmath,"args":("Farm",22),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":295,"price":550_000_000_000_000_000,"function":self.x2Upmath,"args":("Farm",23),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":308,"price":550_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Farm",24),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":429,"price":550_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Farm",25),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":481,"price":550_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Farm",26),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":507,"price":5_500_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Farm",27),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":663,"price":55_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Farm",28),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Farm","id":701,"price":550_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Farm",29),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":16,"price":120_000,"function":self.x2Upmath,"args":("Mine",30),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":17,"price":600_000,"function":self.x2Upmath,"args":("Mine",31),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":18,"price":6_000_000,"function":self.x2Upmath,"args":("Mine",32),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":47,"price":600_000_000,"function":self.x2Upmath,"args":("Mine",33),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":113,"price":60_000_000_000,"function":self.x2Upmath,"args":("Mine",34),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":195,"price":6_000_000_000_000,"function":self.x2Upmath,"args":("Mine",35),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":296,"price":6_000_000_000_000_000,"function":self.x2Upmath,"args":("Mine",35),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":309,"price":6_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Mine",37),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":430,"price":6_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Mine",38),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":482,"price":6_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Mine",39),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":508,"price":60_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Mine",40),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":664,"price":600_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Mine",41),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Mine","id":702,"price":6_000_000_000_0000_0000_0000_000_000_000_000_000,"function":self.x2Upmath,"args":("Mine",42),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":13,"price":1_300_000,"function":self.x2Upmath,"args":("Factory",43),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":14,"price":6_500_000,"function":self.x2Upmath,"args":("Factory",44),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":15,"price":65_000_000,"function":self.x2Upmath,"args":("Factory",45),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":46,"price":6_500_000_000,"function":self.x2Upmath,"args":("Factory",46),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":112,"price":650_000_000_000,"function":self.x2Upmath,"args":("Factory",47),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":194,"price":65_000_000_000_000,"function":self.x2Upmath,"args":("Factory",48),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":297,"price":65_000_000_000_000_000,"function":self.x2Upmath,"args":("Factory",49),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":310,"price":65_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Factory",50),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":431,"price":65_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Factory",51),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":483,"price":65_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Factory",52),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":509,"price":650_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Factory",53),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":665,"price":6_500_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Factory",54),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Factory","id":703,"price":6_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Factory",55),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":232,"price":14_000_000,"function":self.x2Upmath,"args":("Bank",56),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":233,"price":70_000_000,"function":self.x2Upmath,"args":("Bank",57),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":234,"price":700_000_000,"function":self.x2Upmath,"args":("Bank",58),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":235,"price":70_000_000_000,"function":self.x2Upmath,"args":("Bank",59),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":236,"price":7_000_000_000_000,"function":self.x2Upmath,"args":("Bank",60),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":237,"price":700_000_000_000_000,"function":self.x2Upmath,"args":("Bank",61),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":298,"price":700_000_000_000_000_000,"function":self.x2Upmath,"args":("Bank",62),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":311,"price":700_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Bank",63),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":432,"price":700_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Bank",64),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":484,"price":700_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Bank",65),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":510,"price":7_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Bank",66),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":666,"price":70_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Bank",67),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Bank","id":704,"price":700_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Bank",68),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":238,"price":200_000_000,"function":self.x2Upmath,"args":("Temple",69),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":239,"price":1_000_000_000,"function":self.x2Upmath,"args":("Temple",70),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":240,"price":10_000_000_000,"function":self.x2Upmath,"args":("Temple",71),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":241,"price":1_000_000_000_000,"function":self.x2Upmath,"args":("Temple",72),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":242,"price":100_000_000_000_000,"function":self.x2Upmath,"args":("Temple",73),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":243,"price":10_000_000_000_000_000,"function":self.x2Upmath,"args":("Temple",74),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":299,"price":10_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Temple",75),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":312,"price":10_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Temple",76),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":433,"price":10_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Temple",77),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":485,"price":10_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Temple",78),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":511,"price":100_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Temple",79),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":667,"price":1_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Temple",80),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Temple","id":705,"price":10_000_000_000_000_000_000_000_000_000_000_000_000_000 ,"function":self.x2Upmath,"args":("Temple",81),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":244,"price":3_300_000_000,"function":self.x2Upmath,"args":("Wizard tower",82),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":245,"price":16_500_000_000,"function":self.x2Upmath,"args":("Wizard tower",83),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":246,"price":165_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",84),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":247,"price":16_500_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",85),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":248,"price":1_650_000_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",86),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":249,"price":165_000_000_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",87),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":300,"price":165_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",88),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":313,"price":165_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",89),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":434,"price":165_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",90),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":486,"price":165_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",91),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":512,"price":1_650_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",92),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":668,"price":16_500_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",93),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Wizard tower","id":706,"price":165_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Wizard tower",94),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":19,"price":51_000_000_000,"function":self.x2Upmath,"args":("Shipment",95),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":20,"price":255_000_000_000,"function":self.x2Upmath,"args":("Shipment",96),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":21,"price":2_550_000_000_000,"function":self.x2Upmath,"args":("Shipment",97),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":48,"price":255_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",98),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":114,"price":25_500_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",99),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":196,"price":2_550_000_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",100),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":301,"price":2_550_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",101),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":314,"price":2_550_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",102),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":435,"price":2_550_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",103),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":487,"price":2_550_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",104),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":513,"price":25_500_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",105),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":669,"price":255_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",106),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Shipment","id":707,"price":2_550_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Shipment",107),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":22,"price":750_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",108),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":23,"price":3_750_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",109),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":24,"price":37_500_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",110),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":49,"price":3_750_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",111),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":115,"price":375_000_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",112),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":197,"price":37_500_000_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",113),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":302,"price":37_500_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",114),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":315,"price":37_500_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",115),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":436,"price":37_500_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",116),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":488,"price":37_500_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",117),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":514,"price":375_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",118),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":670,"price":3_750_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",119),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Alchemy lab","id":708,"price":37_500_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Alchemy lab",120),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":25,"price":10_000_000_000_000,"function":self.x2Upmath,"args":("Portal",121),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":26,"price":50_000_000_000_000,"function":self.x2Upmath,"args":("Portal",122),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":27,"price":500_000_000_000_000,"function":self.x2Upmath,"args":("Portal",123),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":50,"price":50_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",124),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":116,"price":5_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",125),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":198,"price":500_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",126),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":303,"price":500_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",127),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":316,"price":500_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",128),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":437,"price":500_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",129),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":489,"price":500_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",130),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":515,"price":5_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",131),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":617,"price":50_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",132),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Portal","id":709,"price":500_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Portal",133),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":28,"price":140_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",134),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":29,"price":700_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",135),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":30,"price":7_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",136),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":51,"price":700_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",137),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":117,"price":70_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",138),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":199,"price":7_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",139),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":304,"price":7_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",140),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":317,"price":7_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",141),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":438,"price":7_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",142),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":490,"price":7_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",143),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":516,"price":70_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",144),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":672,"price":700_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",145),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Time machine","id":710,"price":7_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Time machine",146),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":99,"price":1_700_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",147),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Anitmatter condenser","id":100,"price":8_500_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",148),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":101,"price":85_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",149),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":102,"price":8_500_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",150),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Anitmatter condenser","id":118,"price":850_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",151),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":200,"price":85_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",152),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":305,"price":85_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",153),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":318,"price":85_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",154),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":439,"price":85_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",155),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":491,"price":85_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",156),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":517,"price":850_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",157),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":673,"price":8_500_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",158),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Antimatter condenser","id":711,"price":85_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Antimatter condenser",159),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":175,"price":21_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",160),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":176,"price":105_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",161),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":177,"price":1_050_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",162),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":178,"price":105_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",163),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":179,"price":10_500_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",164),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":201,"price":1_050_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",165),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":306,"price":1_050_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",166),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":319,"price":1_050_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",167),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":440,"price":1_050_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",168),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":492,"price":1_050_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",169),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":518,"price":10_500_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",170),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":674,"price":105_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",171),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Prism","id":712,"price":1_050_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Prism",172),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":416,"price":260_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",173),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":417,"price":1_300_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",174),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":418,"price":13_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",175),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":419,"price":1_300_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",176),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":420,"price":130_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",177),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":421,"price":13_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",178),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":422,"price":13_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",179),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":423,"price":13_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",180),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":441,"price":13_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",181),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":493,"price":13_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",182),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":519,"price":130_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",183),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":675,"price":1_300_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",184),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Chancemaker","id":713,"price":13_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Chancemaker",185),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":552,"price":3_100_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",186),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":523,"price":15_500_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",187),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":524,"price":155_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",188),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":525,"price":15_500_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",189),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":526,"price":1_550_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",190),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":527,"price":155_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",191),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":528,"price":155_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",192),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":529,"price":155_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",193),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":530,"price":155_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",194),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":531,"price":155_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",195),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":532,"price":1_550_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",196),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":676,"price":15_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",197),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Fractal engine","id":714,"price":155_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Fractal engine",198),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":594,"price":710_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",199),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":595,"price":3_550_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",200),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":596,"price":35_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",201),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":597,"price":3_550_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",202),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":598,"price":355_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",203),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":599,"price":35_500_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",204),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":600,"price":35_500_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",205),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":601,"price":35_500_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",206),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":602,"price":35_500_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",207),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":603,"price":35_500_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",208),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":604,"price":355_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",209),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":677,"price":3_550_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",210),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Javascript console","id":715,"price":35_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Javascript console",211),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":683,"price":120_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",212),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":685,"price":600_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",213),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":686,"price":6_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",214),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":687,"price":600_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",215),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":688,"price":60_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",216),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":689,"price":6_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",217),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":690,"price":6_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",218),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":691,"price":6_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",219),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":692,"price":6_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",220),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":693,"price":6_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",221),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":694,"price":600_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",222),"purchased":False,"buyFunc":self.x2Bought},
            {"building":"Idleverse","id":715,"price":6_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"function":self.x2Upmath,"args":("Idleverse",223),"purchased":False,"buyFunc":self.x2Bought},
            #QWOOOOO I DID IT GRANDMA TYPES NOW
            {"building":"Farm","id":57,"price":5000,"function":self.GrandmaTypesMath,"args":("Farm",1,224),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Mine","id":58,"price":600000,"function":self.GrandmaTypesMath,"args":("Mine",2,225),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Factory","id":59,"price":6_500_000,"function":self.GrandmaTypesMath,"args":("Factory",3,226),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Bank","id":250,"price":70_000_000,"function":self.GrandmaTypesMath,"args":("Bank",4,227),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Temple","id":251,"price":1_000_000_000,"function":self.GrandmaTypesMath,"args":("Temple",5,228),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Wizard tower","id":252,"price":16_500_000_000,"function":self.GrandmaTypesMath,"args":("Wizard tower",6,229),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Shipment","id":60,"price":255_000_000_000,"function":self.GrandmaTypesMath,"args":("Shipment",7,230),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Alchemy lab","id":61,"price":3_750_000_000_000,"function":self.GrandmaTypesMath,"args":("Alchemy lab",8,231),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Portal","id":62,"price":50_000_000_000_000,"function":self.GrandmaTypesMath,"args":("Portal",9,232),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Time machine","id":63,"price":700_000_000_000_000,"function":self.GrandmaTypesMath,"args":("Time machine",10,233),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Antimatter condenser","id":103,"price":8_500_000_000_000_000,"function":self.GrandmaTypesMath,"args":("Antimatter condenser",11,234),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Prism","id":180,"price":105_000_000_000_000_000,"function":self.GrandmaTypesMath,"args":("Prism",12,235),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Chancemaker","id":415,"price":1_300_000_000_000_000_000,"function":self.GrandmaTypesMath,"args":("Chancemaker",13,236),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Fractal engine","id":521,"price":15_500_000_000_000_000_000,"function":self.GrandmaTypesMath,"args":("Fractal engine",14,237),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Javascript console","id":593,"price":3_550_000_000_000_000_000_000,"function":self.GrandmaTypesMath,"args":("Javascript console",15,238),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            {"building":"Idleverse","id":684,"price":60_000_000_000_000_000_000_000,"function":self.GrandmaTypesMath,"args":("Idleverse",16,239),"purchased":False,"buyFunc":self.GrandmaTypeBought},
            #Milk upgrades are next but will test now
            {"id":31,"price":9_000_000,"milk factor":0.1,"function":self.kittenMath,"args":(0.1,240),"purchased":False},
            {"id":32,"price":9_000_000_000,"milk factor":0.125,"function":self.kittenMath,"args":(0.125,241),"purchased":False},
            {"id":54,"price":90_000_000_000_000,"milk factor":0.15,"function":self.kittenMath,"args":(0.15,242),"purchased":False},
            {"id":108,"price":90_000_000_000_000_000,"milk factor":0.175,"function":self.kittenMath,"args":(0.175,243),"purchased":False},
            {"id":187,"price":900_000_000_000_000_000_000,"milk factor":0.2,"function":self.kittenMath,"args":(0.2,244),"purchased":False},
            {"id":320,"price":900_000_000_000_000_000_000_000,"milk factor":0.2,"function":self.kittenMath,"args":(0.2,245),"purchased":False},
            {"id":322,"price":900_000_000_000_000_000_000_000_000,"milk factor":0.2,"function":self.kittenMath,"args":(0.2,246),"purchased":False},
            {"id":425,"price":900_000_000_000_000_000_000_000_000_000,"milk factor":0.2,"function":self.kittenMath,"args":(0.2,247),"purchased":False},
            {"id":442,"price":900_000_000_000_000_000_000_000_000_000_000,"milk factor":0.175,"function":self.kittenMath,"args":(0.175,248),"purchased":False},
            {"id":462,"price":900_000_000_000_000_000_000_000_000_000_000_000,"milk factor":0.15,"function":self.kittenMath,"args":(0.15,249),"purchased":False},
            {"id":494,"price":900_000_000_000_000_000_000_000_000_000_000_000_000,"milk factor":0.125,"function":self.kittenMath,"args":(0.125,250),"purchased":False},
            {"id":612,"price":900_000_000_000_000_000_000_000_000_000_000_000_000_000,"milk factor":0.115,"function":self.kittenMath,"args":(0.115,251),"purchased":False}
        ]
        self.unfactoredCPS = {
            "Cursor": .1,
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
            "Idleverse": 8300000000000
        }


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

    def getUpgradePrice(self,location): #Gets upgrade prices
        return self.upgrades[location]["price"]

    def getMilkLevel(self):
        return self.driver.execute_script(f"return Game.milkProgress")

    def x2Upmath(self, Object, location): #The math for calculating efficency of upgrades
        return(((self.getBuildingAmt(Object) * self.getCPS(Object)) *2)/self.getUpgradePrice(location))

    def GrandmaTypesMath(self, building, incremetnal, location):
        a = (self.BaseCps["Grandma"] * 2) + (self.BaseCps[building] * (.01 *(math.floor(self.buildingAmt["Grandma"]/ incremetnal))))
        b = a/self.upgrades[location]["price"]
        return b

    def kittenMath(self, milkFactor,location):
        milklevel = self.getMilkLevel()
        tempdict = self.unfactoredCPS
        before = 0
        after = 0
        for x in self.unfactoredCPS:
            before += self.unfactoredCPS[x]
        for x in tempdict:
            tempdict[x] = tempdict[x] * 1 + milkFactor * milklevel
            after += tempdict[x]
        return((after - before)/self.upgrades[location]["price"])

    def clickCookie(self): #Clicks the cookie
        self.driver.execute_script("Game.ClickCookie()")

    def buyUpgrade(self, upId):
        self.driver.execute_script(f'Game.UpgradesById[{upId}].buy()')

    def buyBuilding(self, Object):
        self.driver.execute_script(f"Game.Objects[\"{Object}\"].buy()")
        self.buildingAmt[Object] += 1

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
        
    def GrandmaTypeBought(self, building, incremetnal, location): #location added so I can use upgrades[x]["args"] im lazy and this is bad code ik
        self.BaseCps["Grandma"] = self.BaseCps["Grandma"] * 2
        self.BaseCps[building] = self.BaseCps[building] * (.01 *(math.floor(self.buildingAmt["Grandma"]/ incremetnal)))
        self.unfactoredCPS["Grandma"] = self.unfactoredCPS["Grandma"] * 2
        self.unfactoredCPS[building] = self.unfactoredCPS[building] * (.01 *(math.floor(self.buildingAmt["Grandma"]/ incremetnal)))

    def x2Bought(self, building, location):
        self.BaseCps[building] = self.BaseCps[building] * 2
        self.unfactoredCPS[building] = self.unfactoredCPS[building]

    def milkBuy(self, milkFactor,location):
        self.Milkfactor += milkFactor
        self.updateCPS()

    def updateCPS(self):
        for i in self.unfactoredCPS:
            self.unfactoredCPS[i] = self.BaseCps[i]
            
    def setMilkLevel(self):
        self.milkLevel = self.getMilkLevel()

    def milkBoost(self):
        return  1 + self.Milkfactor * self.getMilkLevel()

    def updateCPS(self):
        for key in self.unfactoredCPS:
            self.BaseCps[key] = self.unfactoredCPS[key] * self.milkBoost()

    def upgrade(self):
        score = 0

        if self.newthing:
            for x in range(len(self.upgrades)):
                if self.upgrades[x]["purchased"] == False:
                    if self.upgrades[x]["function"](*self.upgrades[x]["args"]) >= score:
                        self.bestupgrade = self.upgrades[x]["id"]
                        self.listlocation = x
                        score = self.upgrades[x]["function"](*self.upgrades[x]["args"])
                        self.upScore = score
                    
            self.newthing = False

        if self.upScore >= self.score and self.canBuyUpgrade(self.bestupgrade):
            self.buyUpgrade(self.bestupgrade)
            self.upgrades[self.listlocation]["buyFunc"](*self.upgrades[self.listlocation]["args"])
            self.upgrades[self.listlocation]["purchased"] = True
            self.newthing = True

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
        
