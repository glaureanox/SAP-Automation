import ih03_structure_list as sl
import ih03_infos as i
# import ib02_inventory as inv

def main():
    sl.read_workon_info_inventory()
    i.open_transaction()
    i.insert_inventory()
    i.find_square_and_check()
    i.send_informations()
    
if __name__ == "__main__":
    main()