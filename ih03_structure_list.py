import time
import pyautogui as pg 

def read_workon_info_inventory():
    while True:
        try:
            inventory = pg.locateOnScreen("./img/sec_part/inventory.png", confidence=0.8)
            
            x = inventory.left + inventory.width
            y = inventory.top + inventory.height // 2

            pg.moveTo(x=x, y=y)
            pg.click(clicks=2, interval=0.20)
            pg.hotkey('ctrl', 'c')
        
        except Exception as e:
            print(f"Something deu errado: {e}")

def found_inventory_and_click():
    raise NotImplementedError()    

read_workon_info_inventory()