import requests

def get_ip_info():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        print("==== My Public IP Information ====")
        print(f"Public IP: {data.get('ip', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"ISP: {data.get('org', 'N/A')}")
        print("==================================")

    except Exception as e:
        print("Error retrieving IP info:", e)

if __name__ == "__main__":
    get_ip_info()
