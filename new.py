'''

APM:

Salam daryfat shod moafagh bashid

'''




#----------------------nemoneye akahri
class admin_panel():
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'group {group_name} is created')
            
        else:
            print('your name is dublicated')
        
        
    def add_device_to_group(self,group_name,device):
        
        if group_name in self.groups:
            self.groups[group_name].append(device)
            

        else:
            print('your group is not created')
            
            
            #d1=Device('home/group/device_type/name')
            
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            #F'DEVICE IS CREATE'
           print(f'device {device.name} is created')
            
        else:
            print('your group is not created')
            
            
            
    def create_multiple_devices(self,group_name,device_type,number_of_devcies):
        
        if group_name in self.groups:
            
            for i in range(1,number_of_devcies+1):
                #number=10 -> 1,2,3,4,5,6,7,8,9,10 -->i
                
                device_name=f'{device_type}{i}'
                
                topic=f'home/{group_name}/{device_type}/{device_name}'
                
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
                print(f'device {new_device.name} created')

            
        else:
            print('your group is not created')
            
            
            
    def get_devices_in_groups(self,group_name):
        if group_name in self.groups:
            return self.groups[group_name] #listi az device
            
            
        else:
            print('your group is not created')
            return []
            
            
            #tamame device haye yek grooh ro roshan koen
    def turn_on_all_in_groups(self,group_name):
        
        devices=self.get_devices_in_groups(group_name)
        #list 
        #{'living_room'}:[d1,d2,d3,df34,....]
        #devices=[d1,d2,d3,df34,....]
        
        for device in devices:
            #DEVICE() class
            #in class --> .location .name .group .device__type
            #.turn_on turn_off
            device.turn_on()
            print(f'{device.name} in group {group_name} is turned ON')
            
            
            
    def turn_off_all_in_groups(self,group_name):
        '''
        yek group name begire mesle living_room
        tamame device haro khamosh kone
        
        
        '''
        device= self.get_devices_in_groups(group_name)
        for device in devices:
            device.turn_off()
            print(f'{device.name} in group {group_name} is turned OFF')
            

    
    

    def turn_on_all_devices(self):
        '''
        tamam device haro roshan kone
        **na fghht vase ye goroh
        '''            
        for group_name, device in self.group.items():
            for device in devices:
                device.turn_on
                print(f'{device.name} in group {group_name} is turn ON')
    
    def turn_off_all_devices(self):
        '''
        tamam device haro khamoosh kone
        **na fghht vase ye goroh
        '''            
        for group_name, device in self.group.items():
            for device in devices:
                device.turn_off
                print(f'{device.name} in group {group_name} is turn OFF')
    
    def get_status_in_group(self,gorup_name):
        
        '''
        
        group_name bdi
        bege device ha done done roshanan ya kahmoosh
        
        print kone
        device {esme} --> on
        devcie {} --> off
        
        
        '''
    
        device=self.get_devices_in_groups(gorup_name)
        for device in devices:
            status=device.get_status()
            print(f'device {device.name} --> {status}')
    
    
    def get_status_in_device_type(self,device_type):
        
        '''
        device_type-->masalan lamp
        
        name , too kodom goroh on off
        
        lamp2 in living_room is off
        lamp3 in wc is on
        
        '''
        for group_name,devices in self.groups.items():
            for device in devices:
                if device.device_type==device_type:
                    status=device.get_status()
                print(f'{device.name} in {group_name} is {status}')
        
    #Sensor --> a1=Sensor(...)
    #def create_device
    
    def create_sensor(self,group_name,sensor_type,name):
        if group_name in self.groups:
            topic=f'home/{group_name}/{sensor_type}/{name}'
            new_sensor=sensor(topic)
            self.groups[group_name].append(new_sensor)
            print(f'sensor {new_sensor.name} is created in group')
        else:
            print('your group is nat created')
    
    def add_sensor_in_group(self,group_name,sensor):
        #yek group name bede va to sensor ro tooye oon list ezaf koni
        
        #add_devcie_in_group
        
        if group_name in self.groups:
            self.groups[group_name].append(sensor)
            print(f'sensor {sensor.name} added to group {group_name}')

        else:
            print('your group is not added')
    
    
    def get_data_from_sensor_in_group(self,group_name):
        if group_name in self.groups:
            for device in self.groups[group_name]:
                if isinstance(device,sensor):
                    data=device.get_data()
                    print(f'{device.name} --> {data}')

        else:
            print("your group don't have data")
        
        '''
        
        lkiving__room --> tamame sensor haro mire behet 
        datasho pas mide
        '''
        
    def summarize_group_activity(self, group_name):
    """
    اطلاعات خلاصه‌ی یک گروه:
    - تعداد کل دستگاه‌ها و تعداد روشن‌ها
    - تعداد سنسورها و میانگین داده‌ها
    """
    if group_name not in self.groups:
        print("Group does not exist.")
        return
    
    devices = self.groups[group_name]
    device_count = 0
    device_on_count = 0
    sensor_count = 0
    sensor_data_list = []

    for item in devices:
        if isinstance(item, Device):
            device_count += 1
            if item.get_status().lower() == 'on':
                device_on_count += 1
        elif isinstance(item, Sensor):
            sensor_count += 1
            try:
                data = float(item.get_data())
                sensor_data_list.append(data)
            except:
                continue # Ignore sensors with non-numeric data

    print(f"\nSummary for group '{group_name}':")
    print(f"Devices: {device_count} total, {device_on_count} ON")
    print(f"Sensors: {sensor_count} total")
    if sensor_data_list:
        avg_data = sum(sensor_data_list) / len(sensor_data_list)
        print(f"Average Sensor Data: {avg_data:.2f}")
    else:
        print("No numeric sensor data available.")

    
    

            
            
