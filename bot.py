
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
        self.upgrades = [
            {"building":"Cursor","id":0,"price":100,"score":self.x2Upmath("Cursor",0),"purchased":False},
            {"building":"Cursor", "id":1, "price":500,"score":self.x2Upmath("Cursor",1),"purchased":False},
            {"building":"Cursor","id":2,"price":10000, "score":self.x2Upmath("Cursor",2),"purchased":False},
            {"building":"Grandma","id":7,"price":1000,"score":self.x2Upmath("Grandma",3),"purchased":False},
            {"building":"Grandma","id":8,"price":5000,"score":self.x2Upmath("Grandma",4),"purchased":False},
            {"building":"Grandma","id":9,"price":50000,"score":self.x2Upmath("Grandma",5),"purchased":False},
            {"building":"Grandma","id":44,"price":5000000,"score":self.x2Upmath("Grandma",6),"purchased":False},
            {"building":"Grandma","id":110,"price":500_000_000,"score":self.x2Upmath("Grandma",7),"purchased":False},
            {"building":"Grandma","id":192,"price":50_000_000_000,"score":self.x2Upmath("Grandma",8),"purchased":False},
            {"building":"Grandma","id":294,"price":50_000_000_000_000,"score":self.x2Upmath("Grandma",9),"purchased":False},
            {"building":"Grandma","id":307,"price":50_000_000_000_000_000,"score":self.x2Upmath("Grandma",10),"purchased":False},
            {"building":"Grandma","id":428,"price":50_000_000_000_000_000_000,"score":self.x2Upmath("Grandma",11),"purchased":False},
            {"building":"Grandma","id":480,"price":50_000_000_000_000_000_000_000,"score":self.x2Upmath("Grandma",12),"purchased":False},
            {"building":"Grandma","id":506,"price":500_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Grandma",13),"purchased":False},
            {"building":"Grandma","id":662,"price":5_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Grandma",14),"purchased":False},
            {"building":"Grandma","id":700,"price":50_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Grandma",15),"purchased":False},
            {"building":"Farm","id":10,"price":11_000,"score":self.x2Upmath("Farm",16),"purchased":False},
            {"building":"Farm","id":11,"price":55_000,"score":self.x2Upmath("Farm",17),"purchased":False},
            {"building":"Farm","id":12,"price":550_000,"score":self.x2Upmath("Farm",18),"purchased":False},
            {"building":"Farm","id":13,"price":55_000_000,"score":self.x2Upmath("Farm",19),"purchased":False},
            {"building":"Farm","id":45,"price":5_500_000_000, "score":self.x2Upmath("Farm",20),"purchased":False},
            {"building":"Farm","id":111,"price":550_000_000_000,"score":self.x2Upmath("Farm",21),"purchased":False},
            {"building":"Farm","id":193,"price":550_000_000_000_000,"score":self.x2Upmath("Farm",22),"purchased":False},
            {"building":"Farm","id":295,"price":550_000_000_000_000_000,"score":self.x2Upmath("Farm",23),"purchased":False},
            {"building":"Farm","id":308,"price":550_000_000_000_000_000_000,"score":self.x2Upmath("Farm",24),"purchased":False},
            {"building":"Farm","id":429,"price":550_000_000_000_000_000_000_000,"score":self.x2Upmath("Farm",25),"purchased":False},
            {"building":"Farm","id":481,"price":550_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Farm",26),"purchased":False},
            {"building":"Farm","id":507,"price":5_500_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Farm",27),"purchased":False},
            {"building":"Farm","id":663,"price":55_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Farm",28),"purchased":False},
            {"building":"Farm","id":701,"price":550_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Farm",29),"purchased":False},
            {"building":"Mine","id":16,"price":120_000,"score":self.x2Upmath("Mine",30),"purchased":False},
            {"building":"Mine","id":17,"price":600_000,"score":self.x2Upmath("Mine",31),"purchased":False},
            {"building":"Mine","id":18,"price":6_000_000,"score":self.x2Upmath("Mine",32),"purchased":False},
            {"building":"Mine","id":47,"price":600_000_000,"score":self.x2Upmath("Mine",33),"purchased":False},
            {"building":"Mine","id":113,"price":60_000_000_000,"score":self.x2Upmath("Mine",34),"purchased":False},
            {"building":"Mine","id":195,"price":6_000_000_000_000,"score":self.x2Upmath("Mine",35),"purchased":False},
            {"building":"Mine","id":296,"price":6_000_000_000_000_000,"score":self.x2Upmath("Mine",35),"purchased":False},
            {"building":"Mine","id":309,"price":6_000_000_000_000_000_000,"score":self.x2Upmath("Mine",37),"purchased":False},
            {"building":"Mine","id":430,"price":6_000_000_000_000_000_000_000,"score":self.x2Upmath("Mine",38),"purchased":False},
            {"building":"Mine","id":482,"price":6_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Mine",39),"purchased":False},
            {"building":"Mine","id":508,"price":60_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Mine",40),"purchased":False},
            {"building":"Mine","id":664,"price":600_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Mine",41),"purchased":False},
            {"building":"Mine","id":702,"price":6_000_000_000_0000_0000_0000_000_000_000_000_000,"score":self.x2Upmath("Mine",42),"purchased":False},
            {"building":"Factory","id":13,"price":1_300_000,"score":self.x2Upmath("Factory",43),"purchased":False},
            {"building":"Factory","id":14,"price":6_500_000,"score":self.x2Upmath("Factory",44),"purchased":False},
            {"building":"Factory","id":15,"price":65_000_000,"score":self.x2Upmath("Factory",45),"purchased":False},
            {"building":"Factory","id":46,"price":6_500_000_000,"score":self.x2Upmath("Factory",46),"purchased":False},
            {"building":"Factory","id":112,"price":650_000_000_000,"score":self.x2Upmath("Factory",47),"purchased":False},
            {"building":"Factory","id":194,"price":65_000_000_000_000,"score":self.x2Upmath("Factory",48),"purchased":False},
            {"building":"Factory","id":297,"price":65_000_000_000_000_000,"score":self.x2Upmath("Factory",49),"purchased":False},
            {"building":"Factory","id":310,"price":65_000_000_000_000_000_000,"score":self.x2Upmath("Factory",50),"purchased":False},
            {"building":"Factory","id":431,"price":65_000_000_000_000_000_000_000,"score":self.x2Upmath("Factory",51),"purchased":False},
            {"building":"Factory","id":483,"price":65_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Factory",52),"purchased":False},
            {"building":"Factory","id":509,"price":650_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Factory",53),"purchased":False},
            {"building":"Factory","id":665,"price":6_500_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Factory",54),"purchased":False},
            {"building":"Factory","id":703,"price":6_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Factory",55),"purchased":False},
            {"building":"Bank","id":232,"price":14_000_000,"score":self.x2Upmath("Bank",56),"purchased":False},
            {"building":"Bank","id":233,"price":70_000_000,"score":self.x2Upmath("Bank",57),"purchased":False},
            {"building":"Bank","id":234,"price":700_000_000,"score":self.x2Upmath("Bank",58),"purchased":False},
            {"building":"Bank","id":235,"price":70_000_000_000,"score":self.x2Upmath("Bank",59),"purchased":False},
            {"building":"Bank","id":236,"price":7_000_000_000_000,"score":self.x2Upmath("Bank",60),"purchased":False},
            {"building":"Bank","id":237,"price":700_000_000_000_000,"score":self.x2Upmath("Bank",61),"purchased":False},
            {"building":"Bank","id":298,"price":700_000_000_000_000_000,"score":self.x2Upmath("Bank",62),"purchased":False},
            {"building":"Bank","id":311,"price":700_000_000_000_000_000_000,"score":self.x2Upmath("Bank",63),"purchased":False},
            {"building":"Bank","id":432,"price":700_000_000_000_000_000_000_000,"score":self.x2Upmath("Bank",64),"purchased":False},
            {"building":"Bank","id":484,"price":700_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Bank",65),"purchased":False},
            {"building":"Bank","id":510,"price":7_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Bank",66),"purchased":False},
            {"building":"Bank","id":666,"price":70_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Bank",67),"purchased":False},
            {"building":"Bank","id":704,"price":700_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath("Bank",68),"purchased":False},
            {"building":"Temple","id":238,"price":200_000_000,"score":self.x2Upmath(self.upgrades[69]["building"],69),"purchased":False},
            {"building":"Temple","id":239,"price":1_000_000_000,"score":self.x2Upmath(self.upgrades[70]["building"],70),"purchased":False},
            {"building":"Temple","id":240,"price":10_000_000_000,"score":self.x2Upmath(self.upgrades[71]["building"],71),"purchased":False},
            {"building":"Temple","id":241,"price":1_000_000_000_000,"score":self.x2Upmath(self.upgrades[72]["building"],72),"purchased":False},
            {"building":"Temple","id":242,"price":100_000_000_000_000,"score":self.x2Upmath(self.upgrades[73]["building"],73),"purchased":False},
            {"building":"Temple","id":243,"price":10_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[74]["building"],74),"purchased":False},
            {"building":"Temple","id":299,"price":10_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[75]["building"],75),"purchased":False},
            {"building":"Temple","id":312,"price":10_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[76]["building"],76),"purchased":False},
            {"building":"Temple","id":433,"price":10_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[77]["building"],77),"purchased":False},
            {"building":"Temple","id":485,"price":10_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[78]["building"],78),"purchased":False},
            {"building":"Temple","id":511,"price":100_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[79]["building"],79),"purchased":False},
            {"building":"Temple","id":667,"price":1_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[80]["building"],80),"purchased":False},
            {"building":"Temple","id":705,"price":10_000_000_000_000_000_000_000_000_000_000_000_000_000 ,"score":self.x2Upmath(self.upgrades[81]["building"],81),"purchased":False},
            {"building":"Wizard tower","id":244,"price":3_300_000_000,"score":self.x2Upmath(self.upgrades[82]["building"],82),"purchased":False},
            {"building":"Wizard tower","id":245,"price":16_500_000_000,"score":self.x2Upmath(self.upgrades[83]["building"],83),"purchased":False},
            {"building":"Wizard tower","id":246,"price":165_000_000_000,"score":self.x2Upmath(self.upgrades[84]["building"],84),"purchased":False},
            {"building":"Wizard tower","id":247,"price":16_500_000_000_000,"score":self.x2Upmath(self.upgrades[85]["building"],85),"purchased":False},
            {"building":"Wizard tower","id":248,"price":1_650_000_000_000_000,"score":self.x2Upmath(self.upgrades[86]["building"],86),"purchased":False},
            {"building":"Wizard tower","id":249,"price":165_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[87]["building"],87),"purchased":False},
            {"building":"Wizard tower","id":300,"price":165_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[88]["building"],88),"purchased":False},
            {"building":"Wizard tower","id":313,"price":165_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[89]["building"],89),"purchased":False},
            {"building":"Wizard tower","id":434,"price":165_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[90]["building"],90),"purchased":False},
            {"building":"Wizard tower","id":486,"price":165_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[91]["building"],91),"purchased":False},
            {"building":"Wizard tower","id":512,"price":1_650_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[92]["building"],92),"purchased":False},
            {"building":"Wizard tower","id":668,"price":16_500_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[93]["building"],93),"purchased":False},
            {"building":"Wizard tower","id":706,"price":165_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[94]["building"],94),"purchased":False},
            {"building":"Shipment","id":19,"price":51_000_000_000,"score":self.x2Upmath(self.upgrades[95]["building"],95),"purchased":False},
            {"building":"Shipment","id":20,"price":255_000_000_000,"score":self.x2Upmath(self.upgrades[96]["building"],96),"purchased":False},
            {"building":"Shipment","id":21,"price":2_550_000_000_000,"score":self.x2Upmath(self.upgrades[97]["building"],97),"purchased":False},
            {"building":"Shipment","id":48,"price":255_000_000_000_000,"score":self.x2Upmath(self.upgrades[98]["building"],98),"purchased":False},
            {"building":"Shipment","id":114,"price":25_500_000_000_000_000,"score":self.x2Upmath(self.upgrades[99]["building"],99),"purchased":False},
            {"building":"Shipment","id":196,"price":2_550_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[100]["building"],100),"purchased":False},
            {"building":"Shipment","id":301,"price":2_550_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[101]["building"],101),"purchased":False},
            {"building":"Shipment","id":314,"price":2_550_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[102]["building"],102),"purchased":False},
            {"building":"Shipment","id":435,"price":2_550_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[103]["building"],103),"purchased":False},
            {"building":"Shipment","id":487,"price":2_550_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[104]["building"],104),"purchased":False},
            {"building":"Shipment","id":513,"price":25_500_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[105]["building"],105),"purchased":False},
            {"building":"Shipment","id":669,"price":255_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[106]["building"],106),"purchased":False},
            {"building":"Shipment","id":707,"price":2_550_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[107]["building"],107),"purchased":False},
            {"building":"Alchemy lab","id":22,"price":750_000_000_000,"score":self.x2Upmath(self.upgrades[108]["building"],108),"purchased":False},
            {"building":"Alchemy lab","id":23,"price":3_750_000_000_000,"score":self.x2Upmath(self.upgrades[109]["building"],109),"purchased":False},
            {"building":"Alchemy lab","id":24,"price":37_500_000_000_000,"score":self.x2Upmath(self.upgrades[110]["building"],110),"purchased":False},
            {"building":"Alchemy lab","id":49,"price":3_750_000_000_000_000,"score":self.x2Upmath(self.upgrades[111]["building"],111),"purchased":False},
            {"building":"Alchemy lab","id":115,"price":375_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[112]["building"],112),"purchased":False},
            {"building":"Alchemy lab","id":197,"price":37_500_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[113]["building"],113),"purchased":False},
            {"building":"Alchemy lab","id":302,"price":37_500_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[114]["building"],114),"purchased":False},
            {"building":"Alchemy lab","id":315,"price":37_500_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[115]["buiilding"],115),"purchased":False},
            {"building":"Alchemy lab","id":436,"price":37_500_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[116]["building"],116),"purchased":False},
            {"building":"Alchemy lab","id":488,"price":37_500_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[117]["building"],117),"purchased":False},
            {"building":"Alchemy lab","id":514,"price":375_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[118]["building"],118),"purchased":False},
            {"building":"Alchemy lab","id":670,"price":3_750_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[119]["building"],119),"purchased":False},
            {"building":"Alchemy lab","id":708,"price":37_500_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[120]["building"],120),"purchased":False},
            {"building":"Portal","id":25,"price":10_000_000_000_000,"score":self.x2Upmath(self.upgrades[121]["building"],121),"purchased":False},
            {"building":"Portal","id":26,"price":50_000_000_000_000,"score":self.x2Upmath(self.upgrades[122]["building"],122),"purchased":False},
            {"building":"Portal","id":27,"price":500_000_000_000_000,"score":self.x2Upmath(self.upgrades[123]["building"],123),"purchased":False},
            {"building":"Portal","id":50,"price":50_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[124]["building"],124),"purchased":False},
            {"building":"Portal","id":116,"price":5_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[125]["building"],125),"purchased":False},
            {"building":"Portal","id":198,"price":500_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[126]["building"],126),"purchased":False},
            {"building":"Portal","id":303,"price":500_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[127]["building"],127),"purchased":False},
            {"building":"Portal","id":316,"price":500_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[128]["building"],128),"purchased":False},
            {"building":"Portal","id":437,"price":500_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[129]["building"],129),"purchased":False},
            {"building":"Portal","id":489,"price":500_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[130]["building"],130),"purchased":False},
            {"building":"Portal","id":515,"price":5_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[131]["building"],131),"purchased":False},
            {"building":"Portal","id":617,"price":50_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[132]["building"],132),"purchased":False},
            {"building":"Portal","id":709,"price":500_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[133]["building"],133),"purchased":False},
            {"building":"Time machine","id":28,"price":140_000_000_000_000,"score":self.x2Upmath(self.upgrades[134]["building"],134),"purchased":False},
            {"building":"Time machine","id":29,"price":700_000_000_000_000,"score":self.x2Upmath(self.upgrades[135]["building"],135),"purchased":False},
            {"building":"Time machine","id":30,"price":7_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[136]["building"],136),"purchased":False},
            {"building":"Time machine","id":51,"price":700_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[137]["building"],137),"purchased":False},
            {"building":"Time machine","id":117,"price":70_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[138]["building"],138),"purchased":False},
            {"building":"Time machine","id":199,"price":7_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[139]["building"],139),"purchased":False},
            {"building":"Time machine","id":304,"price":7_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[140]["building"],140),"purchased":False},
            {"building":"Time machine","id":317,"price":7_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[141]["building"],141),"purchased":False},
            {"building":"Time machine","id":438,"price":7_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[142]["building"],142),"purchased":False},
            {"building":"Time machine","id":490,"price":7_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[143]["building"],143),"purchased":False},
            {"building":"Time machine","id":516,"price":70_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[144]["building"],144),"purchased":False},
            {"building":"Time machine","id":672,"price":700_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[145]["building"],145),"purchased":False},
            {"building":"Time machine","id":710,"price":7_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[146]["building"],146),"purchased":False},
            {"building":"Antimatter condenser","id":99,"price":1_700_000_000_000_000,"score":self.x2Upmath(self.upgrades[147]["building"],147),"purchased":False},
            {"building":"Anitmatter condenser","id":100,"price":8_500_000_000_000_000,"score":self.x2Upmath(self.upgrades[148]["building"],148),"purchased":False},
            {"building":"Antimatter condenser","id":101,"price":85_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[149]["building"],149),"purchased":False},
            {"building":"Antimatter condenser","id":102,"price":8_500_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[150]["building"],150),"purchased":False},
            {"building":"Anitmatter condenser","id":118,"price":850_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[151]["building"],151),"purchased":False},
            {"building":"Antimatter condenser","id":200,"price":85_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[152]["building"],152),"purchased":False},
            {"building":"Antimatter condenser","id":305,"price":85_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[153]["building"],153),"purchased":False},
            {"building":"Antimatter condenser","id":318,"price":85_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[154]["building"],154),"purchased":False},
            {"building":"Antimatter condenser","id":439,"price":85_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[155]["building"],155),"purchased":False},
            {"building":"Antimatter condenser","id":491,"price":85_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[156]["building"],156),"purchased":False},
            {"building":"Antimatter condenser","id":517,"price":850_000_000_000_000_000_000_000_000_000_000_000_000,"price":self.x2Upmath(self.upgrades[157]["building"],157),"purchased":False},
            {"building":"Antimatter condenser","id":673,"price":8_500_000_000_000_000_000_000_000_000_000_000_000_000_000,"price":self.x2Upmath(self.upgrades[158]["building"],158),"purchased":False},
            {"building":"Antimatter condenser","id":711,"price":85_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[159]["building"],159),"purchased":False},
            {"building":"Prism","id":175,"price":21_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[160]["building"],160),"purchased":False},
            {"building":"Prism","id":176,"price":105_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[161]["building"],161),"purchased":False},
            {"building":"Prism","id":177,"price":1_050_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[162]["building"],162),"purchased":False},
            {"building":"Prism","id":178,"price":105_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[163]["building"],163),"purchased":False},
            {"building":"Prism","id":179,"price":10_500_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[164]["building"],164),"purchased":False},
            {"building":"Prism","id":201,"price":1_050_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[165]["building"],165),"purchased":False},
            {"building":"Prism","id":306,"price":1_050_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[166]["building"],166),"purchased":False},
            {"building":"Prism","id":319,"price":1_050_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[167]["building"],167),"purchased":False},
            {"building":"Prism","id":440,"price":1_050_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[168]["building"],168),"purchased":False},
            {"building":"Prism","id":492,"price":1_050_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[169]["building"],169),"purchased":False},
            {"building":"Prism","id":518,"price":10_500_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[170]["building"],170),"purchased":False},
            {"building":"Prism","id":674,"price":105_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[171]["building"],171),"purchased":False},
            {"building":"Prism","id":712,"price":1_050_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[172]["building"],172),"purchased":False},
            {"building":"Chancemaker","id":416,"price":260_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[173]["building"],173),"purchased":False},
            {"building":"Chancemaker","id":417,"price":1_300_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[174]["building"],174),"purchased":False},
            {"building":"Chancemaker","id":418,"price":13_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[175]["building"],175),"purchased":False},
            {"building":"Chancemaker","id":419,"price":1_300_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[176]["building"],176),"purchased":False},
            {"building":"Chancemaker","id":420,"price":130_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[177]["building"],177),"purchased":False},
            {"building":"Chancemaker","id":421,"price":13_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[178]["building"],178),"purchased":False},
            {"building":"Chancemaker","id":422,"price":13_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[179]["building"],179),"purchased":False},
            {"building":"Chancemaker","id":423,"price":13_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[180]["building"],180),"purchased":False},
            {"building":"Chancemaker","id":441,"price":13_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[181]["building"],181),"purchased":False},
            {"building":"Chancemaker","id":493,"price":13_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[182]["building"],182),"purchased":False},
            {"building":"Chancemaker","id":519,"price":130_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[183]["building"],183),"purchased":False},
            {"building":"Chancemaker","id":675,"price":1_300_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[184]["building"],184),"purchased":False},
            {"building":"Chancemaker","id":713,"price":13_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[185]["building"],185),"purchased":False},
            {"building":"Fractal engine","id":552,"price":3_100_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[186]["building"],186),"purchased":False},
            {"building":"Fractal engine","id":523,"price":15_500_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[187]["building"],187),"purchased":False},
            {"building":"Fractal engine","id":524,"price":155_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[188]["building"],188),"purchased":False},
            {"building":"Fractal engine","id":525,"price":15_500_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[189]["building",189]),"purchased":False},
            {"building":"Fractal engine","id":526,"price":1_550_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[190]["building"],190),"purchased":False},
            {"building":"Fractal engine","id":527,"price":155_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[191]["building"],191),"purchased":False},
            {"building":"Fractal engine","id":528,"price":155_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[192]["building"],192),"purchased":False},
            {"building":"Fractal engine","id":529,"price":155_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[193]["building"],193),"purchased":False},
            {"building":"Fractal engine","id":530,"price":155_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[194]["building"],194),"purchased":False},
            {"building":"Fractal engine","id":531,"price":155_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[195]["building"],195),"purchased":False},
            {"building":"Fractal engine","id":532,"price":1_550_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[196]["building"],196),"purchased":False},
            {"building":"Fractal engine","id":676,"price":15_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[197]["building"],197),"purchased":False},
            {"building":"Fractal engine","id":714,"price":155_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[198]["building"],198),"purchased":False},
            {"building":"Javascript console","id":594,"price":710_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[199]["building"],199),"purchased":False},
            {"building":"Javascript console","id":595,"price":3_550_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[200]["building"],200),"purchased":False},
            {"building":"Javascript console","id":596,"price":35_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[201]["building"],201),"purchased":False},
            {"building":"Javascript console","id":597,"price":3_550_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[202]["building"],202),"purchased":False},
            {"building":"Javascript console","id":598,"price":355_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[203]["building"],203),"purchased":False},
            {"building":"Javascript console","id":599,"price":35_500_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[204]["building"],204),"purchased":False},
            {"building":"Javascript console","id":600,"price":35_500_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[205]["building"],205),"purchased":False},
            {"building":"Javascript console","id":601,"price":35_500_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[206]["building"],206),"purchased":False},
            {"building":"Javascript console","id":602,"price":35_500_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[207]["building"],207),"purchased":False},
            {"building":"Javascript console","id":603,"price":35_500_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[208]["building"],208),"purchased":False},
            {"building":"Javascript console","id":604,"price":355_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[209]["building"],209),"purchased":False},
            {"building":"Javascript console","id":677,"price":3_550_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[210]["building"],210),"purchased":False},
            {"building":"Javascript console","id":715,"price":35_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[211]["building"],211),"purchased":False},
            {"building":"Idleverse","id":683,"price":120_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[212]["building"],212),"purchased":False},
            {"building":"Idleverse","id":685,"price":600_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[213]["building"],213),"purchased":False},
            {"building":"Idleverse","id":686,"price":6_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[214]["building"],214),"purchased":False},
            {"building":"Idleverse","id":687,"price":600_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[215]["building"],215),"purchased":False},
            {"building":"Idleverse","id":688,"price":60_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[216]["building"],216),"purchased":False},
            {"building":"Idleverse","id":689,"price":6_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[217]["building"],217),"purchased":False},
            {"building":"Idleverse","id":690,"price":6_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[218]["building"],218),"purchased":False},
            {"building":"Idleverse","id":691,"price":6_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[219]["building"],219),"purchased":False},
            {"building":"Idleverse","id":692,"price":6_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[220]["building"],220),"purchased":False},
            {"building":"Idleverse","id":693,"price":6_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[221]["building"],221),"purchased":False},
            {"building":"Idleverse","id":694,"price":600_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[222]["building"],222),"purchased":False},
            {"building":"Idleverse","id":715,"price":6_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.upgrades[223]["building"],223),"purchased":False},
            #QWOOOOO I DID IT GRANDMA TYPES NOW
            {"building":"Farm","id":57,"price":5000,"score":self.GrandmaTypesMath(self.upgrades[224]["building"],1,224),"purchased":False},
            {"building":"Mine","id":58,"price":600000,"score":self.GrandmaTypesMath(self.upgrades[225]["building"],2,225),"purchased":False},
            {"building":"Factory","id":59,"price":6_500_000,"score":self.GrandmaTypesMath(self.upgrades[226]["building"],3,226),"purchased":False},
            {"building":"Bank","id":250,"price":70_000_000,"score":self.GrandmaTypesMath(self.upgrades[227]["building"],4,227),"purchased":False},
            {"building":"Temple","id":251,"price":1_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[228]["building"],5,228),"purchased":False},
            {"building":"Wizard tower","id":252,"price":16_500_000_000,"score":self.GrandmaTypesMath(self.upgrades[229]["building"],6,229),"purchased":False},
            {"building":"Shipment","id":60,"price":255_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[230]["building"],7,230),"purchased":False},
            {"building":"Alchemy lab","id":61,"price":3_750_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[231]["building"],8,231),"purchased":False},
            {"building":"Portal","id":62,"price":50_000_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[232]["building"],9,232),"purchased":False},
            {"building":"Time machine","id":63,"price":700_000_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[233]["building"],10,333),"purchased":False},
            {"building":"Antimatter condenser","id":103,"price":8_500_000_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[234]["building"],11,234),"purchased":False},
            {"building":"Prism","id":180,"price":105_000_000_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[235]["building"],12,235),"purchased":False},
            {"building":"Chancemaker","id":415,"price":1_300_000_000_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[236]["building"],13,236),"purchased":False},
            {"building":"Fractal engine","id":521,"price":15_500_000_000_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[237]["building"],14,237),"purchased":False},
            {"building":"Javascript console","id":593,"price":3_550_000_000_000_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[238]["building"],15,238),"purchased":False},
            {"building":"Idleverse","id":684,"price":60_000_000_000_000_000_000_000,"score":self.GrandmaTypesMath(self.upgrades[239]["building"],16,239),"purchased":False}
            #Milk upgrades are next but will test now
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

    def getUpgradePrice(self,location): #Gets upgrade prices
        return self.upgrades[location]["price"]

    def x2Upmath(self, Object, location): #The math for calculating efficency of upgrades
        return(((self.getBuildingAmt(Object) * self.getCPS(Object)) *2)/self.getUpgradePrice(location))

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

    def GrandmaTypesMath(self, building, incremetnal, location):
        a = (self.BaseCps["Grandma"] * 2) + (self.BaseCps[building] * (.01 *(math.floor(self.buildingAmt["Grandma"]/ incremetnal))))
        b = a/self.upgrades[location]["price"]
        return b
    def upgrade(self):
        score = 0

        if self.newthing:
            for x in range(len(self.upgradges)):
                if self.upgrades[x]["purchased"] == False:
                    pass
                else:
                    if self.upgrades[x]["score"] >= score:
                        self.bestupgrade = self.upgrades["id"]
                        self.listlocation = x
            self.newthing = False

        if score >= self.score and self.canBuyUpgrade(self.upgrades[self.listlocation][self.bestupgrade]):
            self.buyUpgrade(self.upgrades[self.listlocation][self.bestupgrade])
            self.upgrades[self.listlocation]["purchased"] = True
            self.newthing = True