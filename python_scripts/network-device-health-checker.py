from netmiko import ConnectHandler

device = {"device_type": "cisco_ios",
          "host": "Your_Ip",
          "username": "your_user",
          "password": "your_password"


}

connection = ConnectHandler(**device)
