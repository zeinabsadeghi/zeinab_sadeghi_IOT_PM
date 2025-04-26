"""

In The Name of GOD


Created on Sat Jan 25 17:34:06 2025

@author: Ali Pilehvar Meibody



============FINAL PROJECT==============
Objective: Designing and developing IOT Management GUI panel for smart house 


Tasks:
    
    TASK1:
        
    too ghesmate REAL -->khate 473
    az class Device estefade kon
    va yek device_type jadid bezar masalan --> water 
    
    
    
    
    TASK2 :
        

        ADMIN PANELE NAHAEE
        BARAYE HAME fnction ha --> print (logg bnvisid)
        
        f'self.name baste shode'
        self.name
        slef.topic
        self.group
        
        
        tabe haye baghimonde va nesfe ra takmil konid
        
        
        
    Task3:
        
        yek doone tabe b ekhtiare khodetoon besazid (ide bezarid)
        
    
 
  
Github source:
    https://github.com/Fanavarico/Python140307
    
    
    
    
"""




'''


Aim(hadaf) ---> panel besazi --> dastoor bedi --> Things


ELEMENT --> identify (tashkhis bedi hameye ajza ha)


1-Panel (ino design) --> core (haste)



Ensan ----> GUI (tasvir) -----> CORE (to minevisi) ---> Things (lamp, door, fan ,..)


Things --->  lamp, door, fan , temperature sensor, humidity (rotoobat) , doorbinm sensore roshanaee , sensor harekat ,..


Category (dast ebandi):
    
    Device --> man mikham taghir bdm mesle lamp , door, fan 
    Sensor--> temp , humidity , doorbin 



device , sensor---> class --> thing object 

2 category --> 2 class

class --> device --> devise number1 ,nooor , roshankon= True
class --> sensor


az python --> device (lamp) dastoor bedam?


communication approaches
rah haye ertebati




class device --> address bdm behesh , port , kodom noghtas, hamechisho behesh begam
man imitonam behesh dastoor bedam -> on , offg kon


ghadam --> connect
ghadame 2 --> dastro bdm --> on , off




class DEVICE

a=device()
b=debvice()
c=devbice()

a.turn_on()
b.turn_one()




ADMIN_PANEL() -->class

create_multiple_devices(20,dar)
turn_on_all



functions inside admin_panel ---> GUI() dokmash

GUI ()------------



'''


#yek class misazam bename Device 
#k badan biam  hey bsoorate zir
#a=Device()
#hey object besazam

#Obejct--> lamp , dare ,....

#a=Device(..........)
#moshakhast ro bayad tooye init

a='home/group'

'''
khoneee


group------
living room
kitchen
parking
wc
....



device_type
lamp
fan
door



device name

'''
a='home/living_room/lamp/lamp3'



#topic-->masitr path
#C:/user/alpha/desktop/folder..

#topic='home/group/device_type/device_nam'




#mqtt_broker='localhost',port=1883

class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
       
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        #self.topic_list[0] --> Home 
        #***agar man bekham ke in ro gostaresh bedam inja mitonam noe khone hgaram ham baham avaz konam (future)
        
        
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]

        self.port=port







a=Device('home/living_room/lamp/lamp1')


b=Device('home/kitchen/door/frontdoor')


a.name     #'lamp1'
a.device_type #'lamp'
a.group #'living_room'
    


a.name
b.name


b.group

a.group



b.name #456
b.device_type



'''
import Adafruiy_DHT


class Sensor:
    def __init__(self,name,group,unit,pin):
        self.name=name
        self.group=group
        self.pin=pin #sensor pin
        self.unit=unit #C , ....
        self.current_value=None
        
    def read_sensor(self):
        humidity,temperature=Adafruiy_DHT.read_retry(Adafruiy_DHT.DHT22,self.pin)
        
        if self.unit=='C':
            self.current_value=temperature
        elif self.unit=='%':
            self.current_value=humidity
            
        return self.current_value

#themo
#damasanje man roo --> 300

a=Sensor('damasanje4','living_room','C',300)

#hamroghe mikhay bhsh dastresi peyd akoni
a.read_sensor()

'''


import numpy as np


class Sensor:
    def __init__(self,topic,pin=100):
        self.topic=topic
        self.topic_list=self.topic.split('/')

        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.pin=pin #sensor pin

    def read_sensor(self):
        
        if self.device_type=='thermo':
        
            a=np.random.uniform(22,27)
            self.curren_value=a
            return self.curren_value
        
        elif self.device_type=='light':
            
            a=np.random.uniform(0,100)
            self.curren_value=a
            return self.curren_value
            
        
            
        
a=Sensor('home/living_room/thermo/t10') #inja pin ro bnvisi dar donyaye vaghei
a.name
a.group

a.device_type

#dar yaande harj abkham in sensore t10 ro bbinm dama chande

a.read_sensor()




#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================
#===============================================



class Sensor:
    def __init__(self,topic,pin=100):
        self.topic=topic
        self.topic_list=self.topic.split('/')

        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.pin=pin #sensor pin

    def read_sensor(self):
        
        if self.device_type=='thermo':
        
            a=np.random.uniform(22,27)
            self.curren_value=a
            return self.curren_value
        
        elif self.device_type=='light':
            
            a=np.random.uniform(0,100)
            self.curren_value=a
            return self.curren_value
            
        

#device_type = Lamp , Fan , Door

#MQTT --> COMMUNICATION beyne device ha hast 
#dastoor beham midan

#Gpio
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO  # For controlling GPIO pins

'''

electronic --> mqtt gpio

mqtt
gpio




'''


#mqtt --> home/living_room/lamp/lamp232

class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
       
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        #self.topic_list[0] --> Home 
        #***agar man bekham ke in ro gostaresh bedam inja mitonam noe khone hgaram ham baham avaz konam (future)
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]

        self.port=port
        self.mqtt_broker=mqtt_broker
        
        self.connect_mqtt()
        

        self.setup_gpio()
        
        
        
    def connect_mqtt(self):
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        

        
    def setup_gpio(self):
        
        #Light ba signal
        #doors --> motor
        #fans --> motor 
        
        #PIN -->
          
        if self.device_tye=='lights':
            GPIO.setup(17,GPIO.OUT)

        elif self.device_type=='doors': 
            GPIO.setup(27,GPIO.OUT)
            
        elif self.device_type=='fans':
            GPIO.setup(22,GPIO.OUT)
            
            
        
            
        
        
        
    def turn_on(self):
        self.send_command('TURN_ON') #ramzie k toye MQTT
        
        
    def turn_off(self):
        self.send_command('TURN_OFF')
        
        
        
    def send_command(self,command):
        '''send a command via MQTT'''
        #baraye devciam self.topic--> home/lkiving_room/lamp/lamp10
        
        #commandi k migm -->moteghayer
        
        #@turn on 
        #turn of
        
        self.mqtt_client.publish(self.topic,command)
        print(f'command {command} send to topic {self.topic}')
        
        
        
        
        
        
a1=Device('home/living_room/lamp/lamp25w')

a1.name



#========TAKMILI==========

A1=Device('home/living_room/lamps/lamp22')

A1.turn_on()

'''

DEVICE-->KETABKHOONE

MESAL--> 

5 TABE


gpio

setup()  devcie
turn on --> ino bzni

agar light --> ino bzn 

ono bzn

yehafte



'''

#=====================REAL====================

class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):

        self.topic=topic
        
        self.topic_list=self.topic.split('/')        
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.port=port
        self.mqtt_broker=mqtt_broker 
        self.status='off'
        self.speed=0
        


        self.connect_mqtt()
        self.setup_gpio()

        
    def connect_mqtt(self):
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        
        
    def setup_gpio(self):
        if self.device_type=='lights':
            GPIO.setup(17,GPIO.OUT)
            print(f'{self.name} connected to GPIO')

        elif self.device_type=='doors': 
            GPIO.setup(27,GPIO.OUT)
            print(f'{self.name} connected to GPIO')

            
        elif self.device_type=='fans':
            GPIO.setup(22,GPIO.OUT)
            print(f'{self.name} connected to GPIO')

            if self.speed>0:
                GPIO.setup(18, GPIO.OUT)  # For fan speed, if using PWM
                #self.pwm = GPIO.PWM(18, 100)  # PWM frequency 100Hz
                #self.pwm.start(0)
        elif self.device_type=='water':
            GPIO.setup(23,GPIO.OUT)
            print(f'{self.name} connected to GPIO')




                
            

    def turn_on(self):
        self.status='on'
        print(f'{self.name} is turn on')

        self.send_command('TURN_ON') #ramzie k toye MQTT
        if self.device_type=='lights':
            GPIO.output(17, GPIO.HIGH)
            
        elif self.device_type=='doors':
            GPIO.output(27, GPIO.HIGH)
            
        elif self.device_type=='fans':
            GPIO.output(22, GPIO.HIGH)

         elif self.device_type=='water':
            GPIO.setup(23,GPIO.HIGH)
            

            
            
    def set_speed(self,speed):
        
        if self.status=='off':
            print(f'{self.name} currently is off')
            return None
        
        else:
            self.speed=speed
            self.send_command(f'SET_SPEED:{speed}')
    


    def turn_off(self):
        self.status='off'
        
        self.send_command('TURN_OFF')
        if self.device_type=='lights':
            GPIO.output(17, GPIO.LOW)
            
        elif self.device_type=='doors':
            GPIO.output(27, GPIO.LOW)
            
        elif self.device_type=='fans':
            GPIO.output(22, GPIO.LOW)

         elif self.device_type=='water':
            GPIO.setup(23,GPIO.LOW)
            

            
        
    def get_status(self):
        return self.status
        
    
    def send_command(self,command):
        '''send a command via MQTT'''

        self.mqtt_client.publish(self.topic,command)
        print(f'command {command} send to topic {self.topic}')
        
        
        
#========BAD AZ TASK1 =================================

#---deviuce aslit---------


class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):

        self.topic=topic
        
        self.topic_list=self.topic.split('/')        
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.port=port
        self.mqtt_broker=mqtt_broker 
        self.status='off'
        self.speed=0

        #self.connect_mqtt()
        #self.setup_gpio()

        
    def connect_mqtt(self):
        
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        print(f'{self.name} connected to mqtt')
        
        
    def setup_gpio(self):
        if self.device_tye=='lights':
            GPIO.setup(17,GPIO.OUT)
            print(f'{self.name} connected to gpio')

        elif self.device_type=='doors': 
            GPIO.setup(27,GPIO.OUT)
            print(f'{self.name} connected to gpio')
            
        elif self.device_type=='fans':
            GPIO.setup(22,GPIO.OUT)
            if self.speed>0:
                GPIO.setup(18, GPIO.OUT)  # For fan speed, if using PWM
                #self.pwm = GPIO.PWM(18, 100)  # PWM frequency 100Hz
                #self.pwm.start(0)
                print(f'{self.name} connected to gpio')

        elif self.device_type=='water':
            GPIO.setup(23,GPIO,OUT)
            print(f'{self.name} connected to gpio')
                
                
                
            

    def turn_on(self):
        self.status='on'
        print(f'{self.name} is turned on')
        #self.send_command('TURN_ON') #ramzie k toye MQTT
        if self.device_type=='lights':
            GPIO.output(17,GPIO.HIGH)
            
            #GPIO.output(17, GPIO.HIGH)
            
        elif self.device_type=='doors':
            GPIO.output(27,GPIO.HIGH)
            
            #GPIO.output(27, GPIO.HIGH)
            
        elif self.device_type=='fans':
            GPIO.output(22,GPIO.HIGH)
        
            #GPIO.output(22, GPIO.HIGH)
        
        elif self.device_type=='water':
            GPIO.output(23,GPIO.HIGH)
            
            
    def set_speed(self,speed):
        
        if self.status=='off':
            print(f'{self.name} currently is off')
            return None
        
        else:
            self.speed=speed
            #self.send_command(f'SET_SPEED:{speed}')
    


    def turn_off(self):
        self.status='off'
        print(f'{self.name} is turned off')
        #self.send_command('TURN_OFF')
        if self.device_type=='lights':
            GPIO.output(17, GPIO.LOW)
            
            
        elif self.device_type=='doors':
            GPIO.output(27, GPIO.LOW)
            
            
        elif self.device_type=='fans':
            GPIO.output(22, GPIO.LOW)
            

        elif self.device_type=='water':
            GPIO.output(23,GPIO.LOW)
            
        
    def get_status(self):
        return self.status
        
    
    def send_command(self,command):
        '''send a command via MQTT'''
        self.mqtt_client.publish(self.topic,command)
        print(f'command {command} send to topic {self.topic}')
        
        
    
a1=Device('home/living_room/lamps/lamp45')

a1.name

a1.group

a1.turn_on()

a1.get_status()


a1.turn_off()


a1.get_status()

a1=Device('home/living_room/lamps/lamps1')
a2=Device('home/living_room/lamps/rew')
a3=Device('home/living_room/lamps/lamtsrsp45')
a4=Device('home/living_room/lamps/lamp45')
a5=Device('home/living_room/lamps/lamp45')
a6=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')
a1=Device('home/living_room/lamps/lamp45')


#========================================




#self.groups={'living_rooms' = [devicew1,device2,device3,devcie5,,device5]}
class AdminPanel:

    def __init__(self):
        self.groups={}
        
    def creat_group(self,group_name):
        ''' give me the name for one section of your house'''
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created')
            #logg mimone
        else:
            print('yout group name is duplicated name')
            
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            
           
        else:
            print(f'Group {group_name} does not exist')
        
        
    #dota function ro neveshtam ta inja bvrsm
    
    
    def creat_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            
            
        else:
            print(f'Group {group_name} does not exist')

        

    
    
a1=AdminPanel()         
        
a1.groups        
# {}

#hamon aval bayad groop hato besazi-->jahaye khoanto

a1.creat_group('living_room')
 
a1.groups
{'living_room': []}



a1.creat_group('parking')

a1.groups
#{'living_room': [], 'parking': []}



#badi
#device misazam va mriizam dakhelesh

#to ag ghablan mikahsti ye lamp bsazi 
#a1=Device('home/living_room/.......')

a1.creat_device('living_room','lamps','lamp1')
a1.groups

'''
{'living_room': [<__main__.Device at 0x11f65e780>], 'parking': []}


'''

mygroups=a1.groups
mydevices=mygroups['living_room']

mydevice=mydevices[0]

mydevice.name


class AdminPanel:

    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        ''' give me the name for one section of your house'''
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created')
            #logg mimone
        else:
            print('yout group name is duplicated name')
            
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            
           
        else:
            print(f'Group {group_name} does not exist')
        
        
    #dota function ro neveshtam ta inja bvrsm
    
    
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            
            
        else:
            print(f'Group {group_name} does not exist')
            
            
    def create_multiple_devices(self,group_name,device_type,number_of_devices):
        if group_name in self.groups:
            for i in range(1,number_of_devices+1):
                
                device_name=f"{device_type}{i}"
                
                topic=f'home/{group_name}/{device_type}/{device_name.lower()}'
            
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
            
            
        else:
            print(f'Group {group_name} does not exist')
            



a1=AdminPanel()

a1.create_group('living_room')

a1.create_multiple_devices('living_room','lamps',40)

mygroups=a1.groups['living_room']

mygroups[1].name #lamps2'

mygroups[1].turn_on()



#==========================================================

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

    
    

            
            
