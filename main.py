
import bot as c
import timer as t
timer = t.CodeTimer() 
clicker = c.Clicker()  # Clicker object
print(clicker.x2Upmath("Grandma", clicker.x2UpgradeIds[0]))
def main():
    timer.codeBegining()
    clicker.getUpgrade()
    clicker.clickCookie()
    clicker.ChooseBuilding()
    timer.codeEnd()
    print(f"Code exectued in {timer.getCodeTime():1.2f}")


# Idk what it does but its important
if __name__ == '__main__':
    while True:
        main()