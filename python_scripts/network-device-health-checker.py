from netmiko import ConnectHandler

cisco_device = {"device_type": "cisco_ios",
                "username": "ciscosw",
                "password": "password123",
                "host": "10.0.0.0"
}

net_connect = ConnectHandler(**cisco_device)

output = net_connect.send_command("show version")

print(output)

version_line = "Cisco IOS Software, C3560 Software (C3560-IPSERVICESK9-M), Version 12.2(55)SE10, RELEASE SOFTWARE (fc1)"

clean_data = version_line.split(",")

for parts in clean_data:
    if "Version" in parts:
        version = parts.split("Version ")
        answer = version[1]
print(answer)

