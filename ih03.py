import time
import pyautogui as pg 


def open_transaction():
    while True:
        try:
            search_transaction = pg.locateOnScreen("./img/search_transaction.png", confidence=0.8)
            
            center = pg.center(search_transaction)
            
            pg.click(center)
            pg.write("ih03")
            pg.press('enter')
            
            return
            
        except Exception as e:
            print(f"Não foi possível abrir a transação.: {e}")
            
            
def insert_inventory(): # inserir o inventario
    while True:
        try:
            inventory_text_area = pg.locateOnScreen("./img/inventory/insert_inventory.png", confidence=0.7)
            
            center = pg.center(inventory_text_area)
            
            pg.click(center)
            pg.write("200000024508")
            pg.press('enter')
            
            return
            
        except Exception as e:
            print(f"Não foi possível inserir o inventário.: {e}")
            
            
def find_square_and_check(): # preencher a checklist
    while True:
        try:
            time.sleep(1)
            checklist_screen = pg.locateOnScreen("./img/explosion.png", confidence=0.8)
            
            if checklist_screen: 
                checklist_square = pg.locateAllOnScreen("./img/square_checklist.png", region=checklist_screen, confidence=0.8)
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
            clock = pg.locateOnScreen("./img/send_btn.png", confidence=0.8)
            
            if clock:
                center = pg.center(clock)
                pg.click(center)
            return
        
        except Exception as e:
            print(f"Não foi possível enviar os dados.: {e}")
        

# open_transaction() 
insert_inventory()   
find_square_and_check()
send_informations()