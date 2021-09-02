
import bot as c
import timer as t
timer = t.CodeTimer() 
clicker = c.Clicker()  # Clicker object
#clicker.giveCookies(10000)
def main():
    clicker.ChooseBuilding()
    clicker.upgrade()
    clicker.clickCookie()
    clicker.ShimmerLogic()




# Idk what it does but its important
if __name__ == '__main__':
    while True:
        main()