import ipaddress

def classify_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)

        if isinstance(ip_obj, ipaddress.IPv4Address):
            return "IPv4"
        elif isinstance(ip_obj, ipaddress.IPv6Address):
            return "IPv6"

    except ValueError:
        return "Invalid"


def get_network_info(ip):
    try:
        if "/" not in ip:
            return "No network information available"

        net = ipaddress.ip_network(ip, strict=False)

        return {
            "Network": str(net.network_address),
            "Broadcast": str(net.broadcast_address) if net.version == 4 else "N/A",
            "Total Hosts": net.num_addresses
        }

    except ValueError:
        return "Invalid Network"


if __name__ == "__main__":
    user_input = input("Enter an IP address (with subnet if needed): ")

    print("Type:", classify_ip(user_input))
    print("Details:", get_network_info(user_input))
