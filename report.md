# Analysis Questions:

## 1. Which subnet has the most hosts?
If we consider subnets with the most amount of usable hosts then the answer would be any subnet with a subnet mask of 255.255.252.0 or prefix/22. Each has of these subnets has 1022 usable hosts:
1. 10.15.4.0/22
2. 10.2.0.0/22
3. 10.20.4.0/22
4. 10.3.0.0/22
5. 172.16.48.0/22
6. 172.16.60.0/22
7. 192.168.100.0/22
8. 192.168.20.0/22

If we consider how much of each subnet is actually used in the "ip_data.xlsx", then all of the subnets are equal as each subnet exactly has 1IP address used.

## 2. Are there overlapping subnets? If yes, which ones?
No overlapping subnets found. Each subnet has a unique IP address space, ranges from network address to broadcast address, that does not intersect with that of any other subnet.

## 3. What is the smallest and largest subnet in terms of address space?
The smallest subnet has 254 usable hosts:
1. 10.0.3.0/24
2. 10.4.3.0/24
3. 10.50.2.0/24
4. 172.16.20.0/24
5. 172.16.40.0/24
6. 192.168.1.0/24
7. 192.168.2.0/24
8. 192.168.3.0/24
9. 192.168.4.0/24

The largest subnet has 1022 usable hosts:
1. 10.15.4.0/22
2. 10.2.0.0/22
3. 10.20.4.0/22
4. 10.3.0.0/22
5. 172.16.48.0/22
6. 172.16.60.0/22
7. 192.168.100.0/22
8. 192.168.20.0/22

## 4. Suggest a subnetting strategy that could reduce wasted IPs in this network.
From the input IP addresses, each subnet has only 1 IP address used, yet the IP allocation for all is either /24 (254 usable hosts), /23 (510usable hosts), or /22 (1022 usbale hosts). The best strategy for this network is Variable-Length Subnet Mask (VLSM). VSLM strategy assigns IPaddress to a subnet based on the network's actual needs. It maximizes efficiency and reduces wasted IPs by assigning the smallest subnet thatexactly fits the IPs needed. So for subnetworks were only 1 IP is used, a subnet mask of /30 would be more suitable as it only provides 1 usable IP address along with a network and broadcast addresses.
