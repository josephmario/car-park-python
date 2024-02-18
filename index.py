import itertools
import datetime
from datetime import timedelta
import math

type_park = """
Choose:
1. (1) - Park the Vehicle
2. (2) - Exit Parked Vehicle
2. (3) - Admin
"""

type_vehicle = """
Choose:
1. (1) - SMALL 
2. (2) - Medium
3. (3) - Large
3. (4) - Back
"""

slot = """
Choose:
1. (1) - 1st Slot 
2. (2) - 2nd Slot
3. (3) - 3rd Slot
3. (4) - Back
"""

add_slot = """
Choose:
1. (1) - 1st Slot 
2. (2) - 2nd Slot
3. (3) - 3rd Slot
3. (4) - 4th Slot
3. (5) - Back
"""

activate = """
Choose:
1. (1) - Open 
2. (2) - Close
3. (3) - Back
"""

slot_a = []
slot_b = []
slot_c = []
slot_d = []
choose_type_switch = True

class Parking:
    id_obj = itertools.count()
    activate_slot = False
    def __init__(self, num_type):
        self.id = next(Parking.id_obj)
        self.num_type = num_type
        self.start_switch = True
        self.start_switch_slot = True
        self.start_switch_admin = True
        self.slots = self._get_slots(slot_a, slot_b, slot_c, slot_d)
        
        # self.removed_slot = self._remove_slots(slot_a, slot_b, slot_c, slot_d)
    def start(self):
        if(self.num_type == 1):
            self._slot()
        elif(self.num_type == 2):
            self._exit()
        elif(self.num_type == 3):
            self._admin()
            
    def _admin(self):
        try:
            while self.start_switch_admin:
                print(activate)
                active_slot = int(input("Enter the number: "))
                if(active_slot == 1):
                    Parking.activate_slot = True
                elif(active_slot == 2):
                    Parking.activate_slot = False
                main()
                
                if active_slot not in [1, 2, 3]:
                        raise ValueError("Invalid Input")
        except ValueError as e:
                print("An error occurred: {}. Try again.".format(e))
       
    def _slot(self):
        try:
            while self.start_switch_slot:
                print(Parking.activate_slot)
                if(Parking.activate_slot):
                    print(add_slot)
                else:
                    print(slot)
                num_slot = int(input("Enter the number of slot: "))
                if num_slot == 1:
                    if len(slot_a) == 3:
                        print(" Slot A Not Available")
                    else:
                        self._type_vichecle(num_slot)
                elif num_slot == 2:
                    if len(slot_b) == 3:
                        print(" Slot B Not Available")
                    else:
                        self._type_vichecle(num_slot)
                elif num_slot == 3:
                    if len(slot_c) == 3:
                        print(" Slot C Not Available")
                    else:
                        self._type_vichecle(num_slot)
                elif num_slot == 4 and Parking.activate_slot:
                    if len(slot_d) == 4:
                        print(" Slot D Not Available")
                    else:
                        self._type_vichecle(num_slot)
                elif num_slot == 5:
                    main() 
                
                if num_slot not in [1, 2, 3, 4, 5]:
                        raise ValueError("Invalid Slot type specified")
        except ValueError as e:
                print("An error occurred: {}. Try again.".format(e))
            
    def _exit(self):
        print('===================================================================')
        for slot in self.slots:
            datetime = slot['datetime']
            id = slot['id']
            type_vehicle_char = 'Small'
            type_slot = None
            if slot['slot'] == 1:
                type_slot = '1st Slot'
            elif slot['slot'] == 2:
                type_slot = '2nd Slot'
            elif slot['slot'] == 3:
                type_slot = '3rd Slot'
            elif slot['slot'] == 4:
                type_slot = '4th Slot'
                
            if slot['type_vehicle'] == 2:
                type_vehicle_char = 'Medium'

            if slot['type_vehicle'] == 3:
                type_vehicle_char = 'Large'

            print("ID: {}, Type vehicle: {}, slot: {} Date & Time: {}".format(id, type_vehicle_char, type_slot, datetime))
        print('===================================================================')
        num_id = int(input("Enter the number of id: "))
        total_price = 20
        for slot in self.slots:
            if slot['id'] == num_id:
                total_sec = datetime.now() - slot['datetime']
                total_hour = total_sec.seconds // 3600
                total_mins = total_sec.seconds // 60
                total_days = total_sec.seconds // 86400
                
                type_vehicle_price = 20
                if slot['type_vehicle'] == 2:
                    total_price = type_vehicle_price = 60
                if slot['type_vehicle'] == 3:
                    total_price = type_vehicle_price = 100

                if(total_mins <= 60):
                    print("ID: {}, Type vehicle: {}, Total Price: {}".format(id, type_vehicle_char, type_vehicle_price))
                elif(total_hour < 24): 
                    total_price = type_vehicle_price * total_hour
                    print("ID: {}, Type vehicle: {}, Total Price: {}".format(id, type_vehicle_char, total_price))
                elif(total_hour > 24): 
                    print('Overnight Parking Charge 5000 pesos')
                    total_price = type_vehicle_price * total_hour
                    total_price = total_price + 5000
                    print("ID: {}, Type vehicle: {}, Total Price: {}".format(id, type_vehicle_char, total_price))
                else:
                    print('Overnight Parking Charge 5000 pesos')
                    total_price = type_vehicle_price * total_hour
                    price_total_days = total_days * 5000
                    total_price = total_price + price_total_days
                    print("ID: {}, Type vehicle: {}, Total Price: {}".format(id, type_vehicle_char, total_price))
                break;
        payment = int(input("Enter the payment: "))
        if(total_price <= payment):  
            exchange_fare = payment - total_price
            if(exchange_fare > 0):
                print("Here's your exchange fare {}, Thank you Please park us again".format(exchange_fare))
            else:
                print("Thank you Please park us again") 
            removed_element = self._remove_slots(slot_a, slot_b, slot_c, slot_d, num_id)
            
        else:
            print('Insufficient Payment')

    @staticmethod
    def _get_slots(slot_a, slot_b, slot_c, slot_d):
        slots = []
        for a in slot_a:
            slots.append(a)
        for b in slot_b:
            slots.append(b)
        for c in slot_c:
            slots.append(c)
        for d in slot_d:
            slots.append(d)
        return slots
    
    def _remove_slots(self, slot_a, slot_b, slot_c, slot_d, num_id):
        index_to_remove = None
        find_array = None
        for a in slot_a:
            if a['id'] == num_id:
                find_array = slot_a
                index_to_remove = next((index for index, item in enumerate(slot_a) if item["id"] == num_id), None)
                break;
        for b in slot_b:
            if b['id'] == num_id:
                find_array = slot_b
                index_to_remove = next((index for index, item in enumerate(slot_b) if item["id"] == num_id), None)
                break;
        for c in slot_c:
            if c['id'] == num_id:
                find_array = slot_c
                index_to_remove = next((index for index, item in enumerate(slot_c) if item["id"] == num_id), None)
                break;
        for d in slot_d:
            if d['id'] == num_id:
                find_array = slot_d
                index_to_remove = next((index for index, item in enumerate(slot_d) if item["id"] == num_id), None)
                break;
     
        if index_to_remove is not None and find_array is not None:
            removed_element = find_array.pop(index_to_remove)
            print('removed', removed_element)
            return removed_element

    def _type_vichecle(self, num_slot):
        self.start_switch_slot = False
        while self.start_switch:
            
            try:
                print(type_vehicle)

                option = int(input("Enter your choice: "))

                if option == 1:
                    self.start_switch = False
                    self._small(option, num_slot)

                if option == 2:
                    self.start_switch = False
                    self._medium(option, num_slot)
                if option == 3:
                    self.start_switch = False
                    self._large(option, num_slot)
                if option == 4:
                    self.start_switch_slot = True
                    self._slot()
                if option not in [1, 2, 3, 4]:
                    raise ValueError("Invalid vehicle type specified")
                
            except ValueError as e:
                print("An error occurred: {}. Try again.".format(e))
    
    def _small(self, option, num_slot):
        print("20/hour for vehicles parked in SP")
        print("For parking that exceeds 24 hours, every full 24-hour chunk is charged 5,000 pesos regardless of the parking slot + The remainder hours are charged")
        self._display_choice(option, num_slot)
        
        
    def _medium(self, option, num_slot):
        print("60/hour for vehicles parked in MP")
        print("For parking that exceeds 24 hours, every full 24-hour chunk is charged 5,000 pesos regardless of the parking slot + The remainder hours are charged")
        self._display_choice(option, num_slot)

    def _large(self, option, num_slot):
        print("100/hour for vehicles parked in LP")
        print("For parking that exceeds 24 hours, every full 24-hour chunk is charged 5,000 pesos regardless of the parking slot + The remainder hours are charged")
        self._display_choice(option, num_slot)


    def _display_choice(self, option, num_slot):
        _per_hr = "20 Pesos"
        if option == 2:
            _per_hr = "60 Pesos" 
        elif option == 3:
            _per_hr = "100 Pesos"
        
        print(f"""
            1. Slot : {num_slot}
            2. Type Vehicle - {option}
            3. Per Hr Rate - {_per_hr}
        """)
        self._set_logic(option, _per_hr, num_slot)

    def _set_logic(self, option, _per_hr, num_slot):
        slot_payload = ({
            'id': self.id,
            'type_vehicle': option,
            'slot': num_slot,
            'datetime': datetime.datetime.now()
        })
        
        if num_slot == 1:
            slot_a.append(slot_payload)
            print(slot_a)
        elif num_slot == 2:
            slot_b.append(slot_payload)
            print(slot_b)
        elif(num_slot == 3):
            slot_c.append(slot_payload)
            print(slot_c)
        elif(num_slot == 4):
            slot_d.append(slot_payload)
            print(slot_d)
        
        self.start_switch = True
        self.start_switch_slot = True
        main()
def main():
    while choose_type_switch:
        
        try:
            print("##### Welcome to Ayala Corp Car Parking System #####")
            print(type_park)
            num_type = int(input("Enter the number of type: "))
            if num_type not in [1, 2, 3]:
                    raise ValueError("Invalid park type specified")
            
            parking = Parking(num_type)
            parking.start()

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__': 
    main()
