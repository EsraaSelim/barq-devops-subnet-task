import pandas as pd
import ipaddress

IPs = pd.read_excel('ip_data.xlsx')

#print(f'xlsx data: {IPs}')

def get_Network(ip, mask):
    return ipaddress.IPv4Network(f"{ip}/{mask}", strict=False).network_address

def get_Broadcast(ip, mask):
    return ipaddress.IPv4Network(f"{ip}/{mask}", strict=False).broadcast_address

def get_prefix(mask):
    return ipaddress.IPv4Network(f'0.0.0.0/{mask}').prefixlen

def get_Hosts(cidr):
    net = ipaddress.IPv4Network(cidr, strict=False)
    if net.prefixlen == 32:
        return 1
    elif net.prefixlen == 31:
        return 2
    else:
        return (2 ** (32 - net.prefixlen)) - 2
    


IPs["Network Address"] = IPs.apply(lambda row: get_Network(row["IP Address"],row["Subnet Mask"]), axis=1)

IPs["Broadcast Address"] = IPs.apply(lambda row: get_Broadcast(row["IP Address"],row["Subnet Mask"]), axis=1)

IPs["prefix"] = IPs["Subnet Mask"].apply(get_prefix)

IPs["CIDR Notation"] = IPs["Network Address"].astype(str) + "/" + IPs["prefix"].astype(str)

IPs["Usable Hosts"] = IPs["CIDR Notation"].apply(get_Hosts)

#print (IPs)

subnet_summary = IPs.groupby("CIDR Notation").agg({
    "Network Address":"first",
    "Broadcast Address":"first",
    "Usable Hosts":"first",
    "IP Address":"count"
    }).rename(columns={"IP Address": "Number of IPs found"}).reset_index()

#print(subnet_summary)
subnet_summary.to_csv("subnet_report.csv", index=False)

print ("subnet summary saved as: subnet_report.csv")


