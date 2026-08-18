import getpass
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException


def parse_ip_int_brief(raw_output):
    parsed = []
    lines = raw_output.splitlines()

    for line in lines:
        if not line.strip() or line.startswith("Interface"):
            continue

        parts = line.split()

        interface = parts[0]
        ip_addr = parts[1]
        protocol = parts[-1]
        status = " ".join(parts[4:-1])

        issue = False
        if status != "up" or protocol != "up":
            issue = True

        parsed.append({
            "interface": interface,
            "ip_address": ip_addr,
            "status": status,
            "protocol": protocol,
            "issue": issue
        })

    return parsed


def main():
    host = input("Target IP/Hostname: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    device = {
        "device_type": "cisco_ios",
        "host": host,
        "username": username,
        "password": password,
    }

    try:
        print(f"Connecting to {host}...")
        net_connect = ConnectHandler(**device)

        int_output = net_connect.send_command("show ip interface brief")
        cpu_output = net_connect.send_command("show processes cpu sorted | exclude 0.00")

        net_connect.disconnect()

        # Parse output using native string split
        interfaces = parse_ip_int_brief(int_output)

        print("\n" + "=" * 50)
        print(f"HEALTH CHECK SUMMARY - {host}")
        print("=" * 50)

        # Flag down interfaces
        alerts = 0
        for item in interfaces:
            if item["issue"]:
                alerts += 1
                print(f"[ALERT] {item['interface']:<20} | IP: {item['ip_address']:<15} | Status: {item['status']} / {item['protocol']}")
            else:
                print(f"[OK]    {item['interface']:<20} | IP: {item['ip_address']:<15} | Status: {item['status']} / {item['protocol']}")

        print("-" * 50)
        print(f"Total interface alerts: {alerts}")

        # Extract CPU 5-minute average
        cpu_lines = cpu_output.splitlines()
        if cpu_lines:
            print(f"CPU Summary: {cpu_lines[0]}")
        print("=" * 50 + "\n")

    except NetmikoTimeoutException:
        print(f"Error: Connection to {host} timed out.")
    except NetmikoAuthenticationException:
        print(f"Error: Authentication failed for {username}.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
