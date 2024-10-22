import time
import pyautogui as pg 


def open_transaction():
    while True:
        try:
            search_transaction = pg.locateOnScreen("./img/first_part/search_transaction.png", confidence=0.8)
            
            center = pg.center(search_transaction)
            
            pg.click(center)
            pg.write("ih03")
            pg.press('enter')
            
            return
            
        except Exception as e:
            print(f"Não foi possível abrir a transação.: {e}")
            
def delete_text():
    while True:
        try:
            equip_area = pg.locateOnScreen("./img/third_part/equip_area.png", confidence=0.8)
            
            x = equip_area.left + equip_area.width
            y = equip_area.top + equip_area.height // 2

            pg.moveTo(x=x, y=y)
            pg.click()
            pg.hotkey('ctrl', 'a')
            pg.press('delete')
            
            return
            
        except Exception as e:
            print(f"Não foi possível apagar os dados.: {e}")    
            
def insert_inventory(): # inserir o inventario
    while True:
        try:
            inventory_text_area = pg.locateOnScreen("./img/first_part/inventory/insert_inventory.png", confidence=0.8)
            
            center = pg.center(inventory_text_area)
            
            pg.click(center)
            pg.hotkey('ctrl', 'v')
            pg.press('enter')
            
            return
            
        except Exception as e:
            print(f"Não foi possível inserir o inventário.: {e}")
            
            
def find_square_and_check(): # preencher a checklist
    while True:
        try:
            time.sleep(1)
            checklist_screen = pg.locateOnScreen("./img/first_part/explosion.png", confidence=0.8)
            
            if checklist_screen: 
                checklist_square = pg.locateAllOnScreen("./img/first_part/square_checklist.png", region=checklist_screen, confidence=0.8)
                for box in checklist_square:
                    cntr_sqr = pg.center(box)
                    pg.click(cntr_sqr)
                    time.sleep(0.2)
            return
        
        except Exception as e:
            print(f"Não foi possível preencher a checklist.: {e}")
            

def send_informations(): # enviar as informacoes preenchidas
    while True:
        try:
            clock = pg.locateOnScreen("./img/first_part/send_btn.png", confidence=0.8)
            
            if clock:
                center = pg.center(clock)
                pg.click(center)
            return
        
        except Exception as e:
            print(f"Não foi possível enviar os dados.: {e}")
        

# open_transaction() 
# insert_inventory()   
# find_square_and_check()
# send_informations()
delete_text()