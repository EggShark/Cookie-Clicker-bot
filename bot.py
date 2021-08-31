
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
        self.pain = [
            {"building":"Cursor", "id":0,"price":100,"score":self.x2Upmath(self.pain[0]["building"],0)},
            {"building":"Cursor", "id":1, "price":500,"score":self.x2Upmath(self.pain[1]["building"],1)},
            {"building":"Cursor","id":2,"price":10000, "score":self.x2Upmath(self.pain[2]["building"],2)},
            {"building":"Grandma","id":7,"price":1000,"score":self.x2Upmath(self.pain[3]["building"],3)},
            {"building":"Grandma","id":8,"price":5000,"score":self.x2Upmath(self.pain[4]["building"],4)},
            {"building":"Grandma","id":9,"price":50000,"score":self.x2Upmath(self.pain[5]["building"],5)},
            {"building":"Grandma","id":44,"price":5000000,"score":self.x2Upmath(self.pain[6]["building"],6)},
            {"building":"Grandma","id":110,"price":500_000_000,"score":self.x2Upmath(self.pain[7]["building"],7)},
            {"building":"Grandma","id":192,"price":50_000_000_000,"score":self.x2Upmath(self.pain[8]["building"],8)},
            {"building":"Grandma","id":294,"price":50_000_000_000_000,"score":self.x2Upmath(self.pain[9]["building"],9)},
            {"building":"Grandma","id":307,"price":50_000_000_000_000_000,"score":self.x2Upmath(self.pain[10]["building"],10)},
            {"building":"Grandma","id":428,"price":50_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[11]["building"],11)},
            {"building":"Grandma","id":480,"price":50_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[12]["building"],12)},
            {"building":"Grandma","id":506,"price":500_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[13]["building"],13)},
            {"building":"Grandma","id":662,"price":5_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[13]["building"],13)},
            {"building":"Grandma","id":700,"price":50_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[14]["building"],14)},
            {"building":"Farm","id":10,"price":11_000,"score":self.x2Upmath(self.pain[15]["building"],15)},
            {"building":"Farm","id":11,"price":55_000,"score":self.x2Upmath(self.pain[16]["building"],16)},
            {"building":"Farm","id":12,"price":550_000,"score":self.x2Upmath(self.pain[17]["building"],17)},
            {"building":"Farm","id":13,"price":55_000_000,"score":self.x2Upmath(self.pain[18]["building"],18)},
            {"building":"Farm","id":45,"price":5_500_000_000, "score":self.x2Upmath(self.pain[19]["building"],19)},
            {"building":"Farm","id":111,"price":550_000_000_000,"score":self.x2Upmath(self.pain[20]["building"],20)},
            {"building":"Farm","id":193,"price":550_000_000_000_000,"score":self.x2Upmath(self.pain[21]["building"],21)},
            {"building":"Farm","id":295,"price":550_000_000_000_000_000,"score":self.x2Upmath(self.pain[22]["building"],22)},
            {"building":"Farm","id":308,"price":550_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[23]["building"],23)},
            {"building":"Farm","id":429,"price":550_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[24]["building"],24)},
            {"building":"Farm","id":481,"price":550_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[25]["building"],25)},
            {"building":"Farm","id":507,"price":5_500_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[26]["building"],26)},
            {"building":"Farm","id":663,"price":55_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[27]["building"],27)},
            {"building":"Farm","id":701,"price":550_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[28]["building"],28)},
            {"building":"Mine","id":16,"price":120_000,"score":self.x2Upmath(self.pain[29]["building"],29)},
            {"building":"Mine","id":17,"price":600_000,"score":self.x2Upmath(self.pain[30]["building"],30)},
            {"building":"Mine","id":18,"price":6_000_000,"score":self.x2Upmath(self.pain[31]["building"],31)},
            {"building":"Mine","id":47,"price":600_000_000,"score":self.x2Upmath(self.pain[32]["building"],32)},
            {"building":"Mine","id":113,"price":60_000_000_000,"score":self.x2Upmath(self.pain[33]["building"],33)},
            {"building":"Mine","id":195,"price":6_000_000_000_000,"score":self.x2Upmath(self.pain[34]["building"],34)},
            {"building":"Mine","id":296,"price":6_000_000_000_000_000,"score":self.x2Upmath(self.pain[35]["building"],35)},
            {"building":"Mine","id":309,"price":6_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[36]["building"],36)},
            {"building":"Mine","id":430,"price":6_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[37]["building"],37)},
            {"building":"Mine","id":482,"price":6_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[38]["building"],38)},
            {"building":"Mine","id":508,"price":60_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[39]["building"],39)},
            {"building":"Mine","id":664,"price":600_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[40]["building"],40)},
            {"building":"Mine","id":702,"price":6_000_000_000_0000_0000_0000_000_000_000_000_000,"score":self.x2Upmath(self.pain[41]["building"],41)},
            {"building":"Factory","id":13,"price":1_300_000,"score":self.x2Upmath(self.pain[42]["building"],42)},
            {"building":"Factory","id":14,"price":6_500_000,"score":self.x2Upmath(self.pain[43]["building"],43)},
            {"building":"Factory","id":15,"price":65_000_000,"score":self.x2Upmath(self.pain[44]["building"],44)},
            {"building":"Factory","id":46,"price":6_500_000_000,"score":self.x2Upmath(self.pain[45]["building"],45)},
            {"building":"Factory","id":112,"price":650_000_000_000,"score":self.x2Upmath(self.pain[46]["building"],46)},
            {"building":"Factory","id":194,"price":65_000_000_000_000,"score":self.x2Upmath(self.pain[47]["building"],47)},
            {"building":"Factory","id":297,"price":65_000_000_000_000_000,"score":self.x2Upmath(self.pain[48]["building"],47)},
            {"building":"Factory","id":310,"price":65_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[49]["building"],49)},
            {"building":"Factory","id":431,"price":65_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[50]["building"],50)},
            {"building":"Factory","id":483,"price":65_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[51]["building"],51)},
            {"building":"Factory","id":509,"price":650_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[52]["building"],52)},
            {"building":"Factory","id":665,"price":6_500_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[53]["building"],53)},
            {"building":"Factory","id":703,"price":6_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[54]["building"],54)},
            {"building":"Bank","id":232,"price":14_000_000,"score":self.x2Upmath(self.pain[55]["building"],55)},
            {"building":"Bank","id":233,"price":70_000_000,"score":self.x2Upmath(self.pain[56]["building"],56)},
            {"building":"Bank","id":234,"price":700_000_000,"score":self.x2Upmath(self.pain[57]["building"],57)},
            {"building":"Bank","id":235,"price":70_000_000_000,"score":self.x2Upmath(self.pain[58]["building"],58)},
            {"building":"Bank","id":236,"price":7_000_000_000_000,"score":self.x2Upmath(self.pain[59]["building"],59)},
            {"building":"Bank","id":237,"price":700_000_000_000_000,"score":self.x2Upmath(self.pain[60]["building"],60)},
            {"building":"Bank","id":298,"price":700_000_000_000_000_000,"score":self.x2Upmath(self.pain[61]["building"],61)},
            {"building":"Bank","id":311,"price":700_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[62]["building"],62)},
            {"building":"Bank","id":432,"price":700_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[63]["building"],63)},
            {"building":"Bank","id":484,"price":700_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[64]["building"],64)},
            {"building":"Bank","id":510,"price":7_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[65]["building"],65)},
            {"building":"Bank","id":666,"price":70_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[66]["building"],66)},
            {"building":"Bank","id":704,"price":700_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[67]["building"],67)},
            {"building":"Temple","id":238,"price":200_000_000,"score":self.x2Upmath(self.pain[68]["building"],68)},
            {"building":"Temple","id":239,"price":1_000_000_000,"score":self.x2Upmath(self.pain[69]["building"],69)},
            {"building":"Temple","id":240,"price":10_000_000_000,"score":self.x2Upmath(self.pain[70]["building"],70)},
            {"building":"Temple","id":241,"price":1_000_000_000_000,"score":self.x2Upmath(self.pain[71]["building"],71)},
            {"building":"Temple","id":242,"price":100_000_000_000_000,"score":self.x2Upmath(self.pain[72]["building"],72)},
            {"building":"Temple","id":243,"price":10_000_000_000_000_000,"score":self.x2Upmath(self.pain[73]["building"],73)},
            {"building":"Temple","id":299,"price":10_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[74]["building"],74)},
            {"building":"Temple","id":312,"price":10_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[75]["building"],75)},
            {"building":"Temple","id":433,"price":10_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[76]["building"],76)},
            {"building":"Temple","id":485,"price":10_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[77]["building"],77)},
            {"building":"Temple","id":511,"price":100_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[78]["building"],78)},
            {"building":"Temple","id":667,"price":1_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[79]["building"],79)},
            {"building":"Temple","id":705,"price":10_000_000_000_000_000_000_000_000_000_000_000_000_000 ,"score":self.x2Upmath(self.pain[80]["building"],80)},
            {"building":"Wizard tower","id":244,"price":3_300_000_000,"score":self.x2Upmath(self.pain[81]["building"],81)},
            {"building":"Wizard tower","id":245,"price":16_500_000_000,"score":self.x2Upmath(self.pain[82]["building"],82)},
            {"building":"Wizard tower","id":246,"price":165_000_000_000,"score":self.x2Upmath(self.pain[83]["building"],83)},
            {"building":"Wizard tower","id":247,"price":16_500_000_000_000,"score":self.x2Upmath(self.pain[84]["building"],84)},
            {"building":"Wizard tower","id":248,"price":1_650_000_000_000_000,"score":self.x2Upmath(self.pain[85]["building"],85)},
            {"building":"Wizard tower","id":249,"price":165_000_000_000_000_000,"score":self.x2Upmath(self.pain[86]["building"],86)},
            {"building":"Wizard tower","id":300,"price":165_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[87]["building"],87)},
            {"building":"Wizard tower","id":313,"price":165_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[88]["building"],88)},
            {"building":"Wizard tower","id":434,"price":165_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[89]["building"],89)},
            {"building":"Wizard tower","id":486,"price":165_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[90]["building"],90)},
            {"building":"Wizard tower","id":512,"price":1_650_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[91]["building"],91)},
            {"building":"Wizard tower","id":668,"price":16_500_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[92]["building"],92)},
            {"building":"Wizard tower","id":706,"price":165_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[93]["building"],93)},
            {"building":"Shipment","id":19,"price":51_000_000_000,"score":self.x2Upmath(self.pain[94]["building"],94)},
            {"building":"Shipment","id":20,"price":255_000_000_000,"score":self.x2Upmath(self.pain[95]["building"],95)},
            {"building":"Shipment","id":21,"price":2_550_000_000_000,"score":self.x2Upmath(self.pain[96]["building"],96)},
            {"building":"Shipment","id":48,"price":255_000_000_000_000,"score":self.x2Upmath(self.pain[97]["building"],97)},
            {"building":"Shipment","id":114,"price":25_500_000_000_000_000,"score":self.x2Upmath(self.pain[98]["building"],98)},
            {"building":"Shipment","id":196,"price":2_550_000_000_000_000_000,"score":self.x2Upmath(self.pain[99]["building"],99)},
            {"building":"Shipment","id":301,"price":2_550_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[100]["building"],100)},
            {"building":"Shipment","id":314,"price":2_550_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[101]["building"],101)},
            {"building":"Shipment","id":435,"price":2_550_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[102]["building"],102)},
            {"building":"Shipment","id":487,"price":2_550_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[103]["building"],103)},
            {"building":"Shipment","id":513,"price":25_500_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[104]["building"],104)},
            {"building":"Shipment","id":669,"price":255_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[105]["building"],105)},
            {"building":"Shipment","id":707,"price":2_550_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[106]["building"],106)},
            {"building":"Alchemy lab","id":22,"price":750_000_000_000,"score":self.x2Upmath(self.pain[107]["building"],107)},
            {"building":"Alchemy lab","id":23,"price":3_750_000_000_000,"score":self.x2Upmath(self.pain[108]["building"],108)},
            {"building":"Alchemy lab","id":24,"price":37_500_000_000_000,"score":self.x2Upmath(self.pain[109]["building"],109)},
            {"building":"Alchemy lab","id":49,"price":3_750_000_000_000_000,"score":self.x2Upmath(self.pain[110]["building"],110)},
            {"building":"Alchemy lab","id":115,"price":375_000_000_000_000_000,"score":self.x2Upmath(self.pain[111]["building"],111)},
            {"building":"Alchemy lab","id":197,"price":37_500_000_000_000_000_000,"score":self.x2Upmath(self.pain[112]["building"],112)},
            {"building":"Alchemy lab","id":302,"price":37_500_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[113]["building"],113)},
            {"building":"Alchemy lab","id":315,"price":37_500_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[114]["buiilding"],114)},
            {"building":"Alchemy lab","id":436,"price":37_500_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[115]["building"],115)},
            {"building":"Alchemy lab","id":488,"price":37_500_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[116]["building"],116)},
            {"building":"Alchemy lab","id":514,"price":375_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[117]["building"],117)},
            {"building":"Alchemy lab","id":670,"price":3_750_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[118]["building"],118)},
            {"building":"Alchemy lab","id":708,"price":37_500_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[119]["building"],119)},
            {"building":"Portal","id":25,"price":10_000_000_000_000,"score":self.x2Upmath(self.pain[120]["building"],120)},
            {"building":"Portal","id":26,"price":50_000_000_000_000,"score":self.x2Upmath(self.pain[121]["building"],121)},
            {"building":"Portal","id":27,"price":500_000_000_000_000,"score":self.x2Upmath(self.pain[122]["building"],122)},
            {"building":"Portal","id":50,"price":50_000_000_000_000_000,"score":self.x2Upmath(self.pain[123]["building"],123)},
            {"building":"Portal","id":116,"price":5_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[124]["building"],124)},
            {"building":"Portal","id":198,"price":500_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[125]["building"],125)},
            {"building":"Portal","id":303,"price":500_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[126]["building"],126)},
            {"building":"Portal","id":316,"price":500_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[127]["building"],127)},
            {"building":"Portal","id":437,"price":500_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[128]["building"],128)},
            {"building":"Portal","id":489,"price":500_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[129]["building"],129)},
            {"building":"Portal","id":515,"price":5_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[130]["building"],130)},
            {"building":"Portal","id":617,"price":50_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[131]["building"],131)},
            {"building":"Portal","id":709,"price":500_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[132]["building"],132)},
            {"building":"Time machine","id":28,"price":140_000_000_000_000,"score":self.x2Upmath(self.pain[133]["building"],133)},
            {"building":"Time machine","id":29,"price":700_000_000_000_000,"score":self.x2Upmath(self.pain[134]["building"],134)},
            {"building":"Time machine","id":30,"price":7_000_000_000_000_000,"score":self.x2Upmath(self.pain[135]["building"],135)},
            {"building":"Time machine","id":51,"price":700_000_000_000_000_000,"score":self.x2Upmath(self.pain[136]["building"],136)},
            {"building":"Time machine","id":117,"price":70_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[137]["building"],137)},
            {"building":"Time machine","id":199,"price":7_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[138]["building"],138)},
            {"building":"Time machine","id":304,"price":7_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[139]["building"],139)},
            {"building":"Time machine","id":317,"price":7_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[140]["building"],140)},
            {"building":"Time machine","id":438,"price":7_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[141]["building"],141)},
            {"building":"Time machine","id":490,"price":7_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[142]["building"],142)},
            {"building":"Time machine","id":516,"price":70_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[143]["building"],143)},
            {"building":"Time machine","id":672,"price":700_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[144]["building"],144)},
            {"building":"Time machine","id":710,"price":7_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[145]["building"],145)},
            {"building":"Antimatter condenser","id":99,"price":1_700_000_000_000_000,"score":self.x2Upmath(self.pain[146]["building"],146)},
            {"building":"Anitmatter condenser","id":100,"price":8_500_000_000_000_000,"score":self.x2Upmath(self.pain[147]["building"],147)},
            {"building":"Antimatter condenser","id":101,"price":85_000_000_000_000_000,"score":self.x2Upmath(self.pain[148]["building"],148)},
            {"building":"Antimatter condenser","id":102,"price":8_500_000_000_000_000_000,"score":self.x2Upmath(self.pain[149]["building"],149)},
            {"building":"Anitmatter condenser","id":118,"price":850_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[150]["building"],150)},
            {"building":"Antimatter condenser","id":200,"price":85_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[151]["building"],151)},
            {"building":"Antimatter condenser","id":305,"price":85_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[152]["building"],152)},
            {"building":"Antimatter condenser","id":318,"price":85_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[153]["building"],153)},
            {"building":"Antimatter condenser","id":439,"price":85_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[154]["building"],154)},
            {"building":"Antimatter condenser","id":491,"price":85_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[155]["building"],155)},
            {"building":"Antimatter condenser","id":517,"price":850_000_000_000_000_000_000_000_000_000_000_000_000,"price":self.x2Upmath(self.pain[156]["building"],156)},
            {"building":"Antimatter condenser","id":673,"price":8_500_000_000_000_000_000_000_000_000_000_000_000_000_000,"price":self.x2Upmath(self.pain[157]["building"],157)},
            {"building":"Antimatter condenser","id":711,"price":85_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[158]["building"],158)},
            {"building":"Prism","id":175,"price":21_000_000_000_000_000,"score":self.x2Upmath(self.pain[159]["building"],159)},
            {"building":"Prism","id":176,"price":105_000_000_000_000_000,"score":self.x2Upmath(self.pain[160]["building"],160)},
            {"building":"Prism","id":177,"price":1_050_000_000_000_000_000,"score":self.x2Upmath(self.pain[161]["building"],161)},
            {"building":"Prism","id":178,"price":105_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[162]["building"],162)},
            {"building":"Prism","id":179,"price":10_500_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[163]["building"],163)},
            {"building":"Prism","id":201,"price":1_050_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[164]["building"],164)},
            {"building":"Prism","id":306,"price":1_050_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[165]["building"],165)},
            {"building":"Prism","id":319,"price":1_050_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[166]["building"],166)},
            {"building":"Prism","id":440,"price":1_050_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[167]["building"],167)},
            {"building":"Prism","id":492,"price":1_050_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[168]["building"],168)},
            {"building":"Prism","id":518,"price":10_500_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[169]["building"],169)},
            {"building":"Prism","id":674,"price":105_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[170]["building"],170)},
            {"building":"Prism","id":712,"price":1_050_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[171]["building"],171)},
            {"building":"Chancemaker","id":416,"price":260_000_000_000_000_000,"score":self.x2Upmath(self.pain[172]["building"],172)},
            {"building":"Chancemaker","id":417,"price":1_300_000_000_000_000_000,"score":self.x2Upmath(self.pain[173]["building"],173)},
            {"building":"Chancemaker","id":418,"price":13_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[174]["building"],174)},
            {"building":"Chancemaker","id":419,"price":1_300_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[175]["building"],175)},
            {"building":"Chancemaker","id":420,"price":130_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[176]["building"],176)},
            {"building":"Chancemaker","id":421,"price":13_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[177]["building"],177)},
            {"building":"Chancemaker","id":422,"price":13_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[178]["building"],178)},
            {"building":"Chancemaker","id":423,"price":13_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[179]["building"],179)},
            {"building":"Chancemaker","id":441,"price":13_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[180]["building"],180)},
            {"building":"Chancemaker","id":493,"price":13_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[181]["building"],181)},
            {"building":"Chancemaker","id":519,"price":130_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[182]["building"],182)},
            {"building":"Chancemaker","id":675,"price":1_300_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[183]["building"],183)},
            {"building":"Chancemaker","id":713,"price":13_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[184]["building"],184)},
            {"building":"Fractal engine","id":552,"price":3_100_000_000_000_000_000,"score":self.x2Upmath(self.pain[185]["building"],185)},
            {"building":"Fractal engine","id":523,"price":15_500_000_000_000_000_000,"score":self.x2Upmath(self.pain[186]["building"],186)},
            {"building":"Fractal engine","id":524,"price":155_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[187]["building"],187)},
            {"building":"Fractal engine","id":525,"price":15_500_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[188]["building",188])},
            {"building":"Fractal engine","id":526,"price":1_550_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[189]["building"],189)},
            {"building":"Fractal engine","id":527,"price":155_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[190]["building"],190)},
            {"building":"Fractal engine","id":528,"price":155_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[191]["building"],191)},
            {"building":"Fractal engine","id":529,"price":155_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[192]["building"],192)},
            {"building":"Fractal engine","id":530,"price":155_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[193]["building"],193)},
            {"building":"Fractal engine","id":531,"price":155_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[194]["building"],194)},
            {"building":"Fractal engine","id":532,"price":1_550_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[195]["building"],195)},
            {"building":"Fractal engine","id":676,"price":15_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[196]["building"],196)},
            {"building":"Fractal engine","id":714,"price":155_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[197]["building"],197)},
            {"building":"Javascript console","id":594,"price":710_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[198]["building"],198)},
            {"building":"Javascript console","id":595,"price":3_550_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[199]["building"],199)},
            {"building":"Javascript console","id":596,"price":35_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[200]["building"],200)},
            {"building":"Javascript console","id":597,"price":3_550_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[201]["building"],201)},
            {"building":"Javascript console","id":598,"price":355_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[202]["building"],202)},
            {"building":"Javascript console","id":599,"price":35_500_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[203]["building"],203)},
            {"building":"Javascript console","id":600,"price":35_500_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[203]["building"],203)},
            {"building":"Javascript console","id":601,"price":35_500_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[204]["building"],204)},
            {"building":"Javascript console","id":602,"price":35_500_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[205]["building"],205)},
            {"building":"Javascript console","id":603,"price":35_500_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[206]["building"],206)},
            {"building":"Javascript console","id":604,"price":355_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[207]["building"],207)},
            {"building":"Javascript console","id":677,"price":3_550_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[208]["building"],208)},
            {"building":"Javascript console","id":715,"price":35_500_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[209]["building"],209)},
            {"building":"Idleverse","id":683,"price":120_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[210]["building"],210)},
            {"building":"Idleverse","id":685,"price":600_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[211]["building"],211)},
            {"building":"Idleverse","id":686,"price":6_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[212]["building"],212)},
            {"building":"Idleverse","id":687,"price":600_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[213]["building"],213)},
            {"building":"Idleverse","id":688,"price":60_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[214]["building"],241)},
            {"building":"Idleverse","id":689,"price":6_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[215]["building"],215)},
            {"building":"Idleverse","id":690,"price":6_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[216]["building"],216)},
            {"building":"Idleverse","id":691,"price":6_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[217]["building"],217)},
            {"building":"Idleverse","id":692,"price":6_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[218]["building"],218)},
            {"building":"Idleverse","id":693,"price":6_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[219]["building"],219)},
            {"building":"Idleverse","id":694,"price":600_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[220]["building"],220)},
            {"building":"Idleverse","id":715,"price":6_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,"score":self.x2Upmath(self.pain[221]["building"],221)},
            #QWOOOOO I DID IT GRANDMA TYPES NOW
            {"building":"Farm","id":57,"price":5000,"score":self.GrandmaTypesMath(self.pain[222]["building"],1,222)},
            {"building":"Mine","id":58,"price":600000,"score":self.GrandmaTypesMath(self.pain[223]["building"],2,223)},
            {"building":"Factory","id":59,"price":6_500_000,"score":self.GrandmaTypesMath(self.pain[224]["building"],3,224)},
            {"building":"Bank","id":250,"price":70_000_000,"score":self.GrandmaTypesMath(self.pain[225]["building"],4,225)},
            {"building":"Temple","id":251,"price":1_000_000_000,"score":self.GrandmaTypesMath(self.pain[256]["building"],5,226)},
            {"building":"Wizard tower","id":252,"price":16_500_000_000,"score":self.GrandmaTypesMath(self.pain[257]["building"],6,257)},
            {"building":"Shipment","id":60,"price":255_000_000_000,"score":self.GrandmaTypesMath(self.pain[258]["building"],7,258)},
            {"building":"Alchemy lab","id":61,"price":3_750_000_000_000,"score":self.GrandmaTypesMath(self.pain[259]["building"],8,259)},
            {"building":"Portal","id":62,"price":50_000_000_000_000,"score":self.GrandmaTypesMath(self.pain[260]["building"],9,260)},
            {"building":"Time machine","id":63,"price":700_000_000_000_000,"score":self.GrandmaTypesMath(self.pain[261]["building"],10,261)},
            {"building":"Antimatter condenser","id":103,"price":8_500_000_000_000_000,"score":self.GrandmaTypesMath(self.pain[262]["building"],11,262)},
            {"building":"Prism","id":180,"price":105_000_000_000_000_000,"score":self.GrandmaTypesMath(self.pain[263]["building"],12,263)},
            {"building":"Chancemaker","id":415,"price":1_300_000_000_000_000_000,"score":self.GrandmaTypesMath(self.pain[264]["building"],13,263)},
            {"building":"Fractal engine","id":521,"price":15_500_000_000_000_000_000,"score":self.GrandmaTypesMath(self.pain[265]["building"],14,265)},
            {"building":"Javascript console","id":593,"price":3_550_000_000_000_000_000_000,"score":self.GrandmaTypesMath(self.pain[267]["building"],15,267)},
            {"building":"Idleverse","id":684,"price":60_000_000_000_000_000_000_000,"score":self.GrandmaTypesMath(self.pain[268]["building"],16,268)}
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
        return self.pain[location]["price"]

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
        #print("the id of the best upgrade is:", self.UpgradeToBuy, self.upids[self.buildingGroup][self.IdLocation] ,self.upScore, self.score, self.buildingGroup, self.IdLocation)
        if self.upScore > self.score and self.canBuyUpgrade(self.UpgradeToBuy):
            self.buyUpgrade(self.UpgradeToBuy)
            self.BaseCps[self.upids[self.buildingGroup][self.IdLocation]] = self.BaseCps[self.upids[self.buildingGroup][0]] * 2
            self.upids[self.buildingGroup].pop(self.IdLocation)
            self.upIdsPrices[self.buildingGroup].pop(self.IdLocation)
            self.newthing = True
    def GrandmaTypesMath(self, building, incremetnal, location):
        a = (self.BaseCps["Grandma"] * 2) + (self.BaseCps[building] * (.01 *(math.floor(self.buildingAmt["Grandma"]/ incremetnal))))
        b = a/self.pain[location]["price"]
        return b
    def Grandmatypes(self):
        score = 0
        if self.newthing:
            for i in range(len(self.GrandmaTypesInfo)):
                if self.GrandmaTypesMath(self.GrandmaTypesInfo[i]["name"], i + 1, self.GrandmaTypesInfo[i]["price"]) >= score:
                    score = self.GrandmaTypesMath(self.GrandmaTypesInfo[i]["name"], i + 1, self.GrandmaTypesInfo[i]["price"])
                    self.listLocation = i
                    print(score)
            self.newthing = False
        if score >= self.score and score >= self.upScore and self.canBuyUpgrade(self.GrandmaTypesInfo[self.listLocation]["id"]):
            self.buyUpgrade(self.GrandmaTypesInfo[self.listLocation["id"]])
            self.GrandmaTypesInfo.pop(self.listLocation)
            self.newthing = True

