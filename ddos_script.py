
import requests

def run_ddos():
    ip_address = input("Enter IP address to look up: ")
    ip_lookup(ip_address)

def ip_lookup(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'fail':
            print(f"Could not retrieve information for IP {ip_address}")
        else:
            print(f"IP: {ip_address}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ISP: {data['isp']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
    else:
        print("Failed to retrieve data")
        