# Python-CIDR-Calculator
🐍 Python CIDR Calculator

🔢 Step-by-Step CIDR Calculation
1. Convert the CIDR Prefix to a Subnet Mask
/8 = 255.0.0.0

/16 = 255.255.0.0

/24 = 255.255.255.0

General rule: The prefix length tells how many bits in the subnet mask are set to 1.

Example:

/26 = 255.255.255.192 (because 26 ones in binary = 11111111.11111111.11111111.11000000)

2. Calculate Number of Hosts
Formula: 2^(32 - prefix_length) - 2

Example /24: 2^(32 - 24) - 2 = 254 usable hosts

3. Determine Network and Broadcast Address
For 192.168.1.0/26:

Subnet mask: 255.255.255.192

Block size: 256 - 192 = 64

Subnets: 192.168.1.0, 192.168.1.64, 192.168.1.128, 192.168.1.192

Network: 192.168.1.0

Broadcast: 192.168.1.63

Usable range: 192.168.1.1 – 192.168.1.62

📋 CIDR Table (Common Prefixes)
CIDR	Subnet Mask	Hosts	Block Size
/30	255.255.255.252	2	4
/29	255.255.255.248	6	8
/28	255.255.255.240	14	16
/27	255.255.255.224	30	32
/26	255.255.255.192	62	64
/25	255.255.255.128	126	128
/24	255.255.255.0	254	256
/16	255.255.0.0	65,534	65,536
