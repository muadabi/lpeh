# lpeh

## 01 - Introduction

## 02 - Writting a MAC Address Changer - Python Basics

**What is a MAC Address and how to change it**

MAC Address
- Media Access Control
  - Permanent
  - Physical
  - Unique
- Assigned by manufacturer.

Why change the MAC address?
1. Increase anonymity.
2. Impersonate other devices.
3. Bypass filters.

```bash
# find the current MAC address of your network interface (e.g., eth0) using the command:
andi@dmz-lts:~$ ip link show eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether bc:24:11:97:e3:3d brd ff:ff:ff:ff:ff:ff
    altname enp0s18

# change the current MAC address using the command:
andi@dmz-lts:~$ sudo ip link set eth0 address 00:11:22:33:44:55

```


**Using Python modules and executing system commands**

Using a module to execute system commands

- the subprocess module contains a number of functions.
- these functions allow us to execute system commands.
- commands depend on the OS which executes the script.

Syntax:
```python
import subprocess

subprocess.run(['ls', '-l'])

```

[Subprocess official documentation](https://docs.python.org/3/library/subprocess.html)


**Implementing a very basic MAC changer**

```python

#!/usr/bin/env python3
import subprocess

subprocess.run(['sudo', 'ip', 'link', 'set', 'eth0', 'address', '00:11:22:33:44:55'])
subprocess.run(['ip', 'link', 'show', 'eth0'])

```

**Variables and strings**

Variables 

- a variable is a location in memory that contains a certain value.
- similar to maths, its a name that is used to store information.

```python
# ex:
x = 1
y = x + x
print(y)

```

```python

#!/usr/bin/env python3
import subprocess

interface = 'eth0'
mac_address = '00:11:22:33:44:55'

print(f'[+] changing MAC address for {interface}, to {mac_address}')
subprocess.run(['ip', 'link', 'show', interface])
subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'address', mac_address])
subprocess.run(['ip', 'link', 'show', interface])

```

[Strings](https://www.tutorialspoint.com/python/python_strings.htm)
[Variables](https://www.tutorialspoint.com/python/python_variables.htm)


**Using variables in MAC changer**

**Getting input from the user**

Handling user input

- easiest way of getting user input is through keyboard.
- there are a number of ways to achive that.
- input() function prompts the user to enter value.

```python
# Ex:
age = input("What is your age?")

```

```python
#!/usr/bin/env python3
import subprocess

interface = input('interface name > ')
mac_address = input('new MAC address > ')

print(f'[+] changing MAC address for {interface}, to {mac_address}')
subprocess.run(['ip', 'link', 'show', interface])
subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'address', mac_address])
subprocess.run(['ip', 'link', 'show', interface])

```

[More info about python build in functions](https://docs.python.org/3/library/functions.html#raw_input)


**Handling user input**

**Handlling command-line arguments**

[Optparse documentation page](https://docs.python.org/3/library/optparse.html)


**Initialising variables based on command-line arguments**

**Python functions**

FUNCTIONS

- set of instructions to carry out a task.
- can take input, and return result.
- make the code clearer, reusable, and more abstract.
- input() function prompts the user to enter a value.

**Returning values from functions**

**Decision making in Python**

DECISION MAKING

- execute code ONLY if a condition is true.

```python
if condition:
    # code to execute when condition is true
else:
    # code to execute when condition is false

# rest of code

---
if condition1:
    # code to execute when codition1 is true
elif condition2:
    # code to execute when condition2 is true AND condition1 is false
else:
    # code to execute when ALL conditions are FALSE

# rest of code

---
if condition1:
    # code to execute when condition1 is true

if condition2:
    # code to execute when condition2 is true

# rest of code
```

[More info on Decision Making](https://www.tutorialspoint.com/python/python_decision_making.htm)


**Using conditional statements in MAC changer**


## 03 - MAC Changer - Algorithm Design

**Introduction to Algorithms**

SIMPLE ALGORITHM

Goal -> check if MAC address was changed.

Steps:
1. execute and read ifconfig.
2. read the MAC addrress from output.
3. check if MAC in ifconfig is what the user requested.
4. print appropriate message.


**Reading output returned by system commands**

[subprocess.check_output](https://docs.python.org/3/library/subprocess.html)

**Introduction to regular expressions (Regex)**

[Python - Regular Expressions](https://www.tutorialspoint.com/python/python_reg_expressions.htm)
[Pythex](https://pythex.org/)

REGULAR EXPRESSIONS

- search for specific patterns within a string.
- uses rules to match pattern.

[re](https://docs.python.org/3/library/re.html)

**Extracting a substring using Regex**

**Refactoring and Housekeeping**

**Implementing the validation algorithm**


## 04 - Programming a Network Scanner

**Introduction and teaser**

NETWORK SCANNER
- discover all devices on the network.
- display their IP address.
- display their MAC address.

```bash
netdiscover -r 10.0.2.1/24

```

**Installing windows as a virtual machine**

**Introduction to ARP**

[Scapy documentation](https://scapy.readthedocs.io/en/latest/)
[Scapy librar](https://scapy.readthedocs.io/en/latest/usage.html#arp-ping)

```bash

arp 

```

**Designing an algorithm to discover clients on the same network**

ALGORITHM

Goal -> discover clients on network.

Steps:
1. create arp request directed to broadcast MAC asking for IP.
2. send packet and receive response.
3. parse the response.
4. print results.

**Using Scapy to create an ARP request**

Goal -> discover clients on network.

Steps:
1. create arp request directed to broadcast MAC asking for IP.
Two main parts:
    -> use ARP to ask who has target IP.
    -> set destination MAC to broadcast MAC.

**Combining frames to broadcast packets**

**Sending and receiving packets**

[more info about the sr function](https://scapy.readthedocs.io/en/latest/usage.html#send-and-receive-packets-sr)

Steps:
2. send packet and receive response.

**Introduction lists in Python**

[More info about python lists](https://www.tutorialspoint.com/python/python_lists.htm)

LISTS
- list of values/elements, all can be stored in one variable.

Ex:
```python
lucky_numbers_list = [3, 7, 8, 17, 24]

# elements can be accessed using their index
print(lucky_numbers_list[0]) # prints 3
print(lucky_numbers_list[1]) # prints 7
print(lucky_numbers_list[2]) # prints 8

```

**Iterating over lists and analysing packet**

**Using escape characters to improve program output**

[Python escape characters](https://docs.python.org/2.0/ref/strings.html)

**Introduction to dictionaries in Python**

[More info about dictionaries](https://www.tutorialspoint.com/python/python_dictionary.htm)

DICTIONARIES
- similar to lists but use key instead of index.

Ex:
```python
target_client = {"mac:" "00:11:22:33:44:55", "ip": "10.0.2.1", "os": "windows"}

#python will interpret this as
#key    mac                 ip          os
#value  00:11:22:33:44:55   10.0.2.1    windows

#elements can be accessed using thier key
print(target_client["mac"]) #prints 00:11:22:33:44:55
print(target_client["ip"]) #prints 10.0.2.1
print(target_client["os"]) #prints windows
```

**Improve the program using a list of dictionaries**

LIST OF DICTIONARIES

**Iterating over nested data structures**

**Testing network scanner with python 3**

[argparse](https://docs.python.org/3.3/library/argparse.html)


## Writing an ARP Spoffer

**What is ARP spoofing**

Why ARP spoofing is possible:
1. clients accept responses even if they did not send a request.
2. client trust response without any form of verification.

**Intercepting data in a network using arpspoof**

```bash
#kali linux
arpspoof -i eth0 -t 10.0.3.10 10.0.3.250
arpspoof -i eth0 -t 10.0.3.250 10.0.3.10

echo 1 > /proc/sys/net/ipv4/ip_forward
```
 
 **Creating an ARP response**

 **Sending ARP responses**

 **Extracting MAC address from response**

 **Introduction to loops in Python**

 [More on Python loops](https://www.tutorialspoint.com/python/python_loops.htm)

 **Dynamic Printing**

 **Exception handling in Python**

 [More on Exceptions Handling](https://www.tutorialspoint.com/python/python_exceptions.htm)

 **Implementing a restore function**

 ## Writing an packet sniffer

 **Introduction and teaser**

 PACKET_SNIFFER
 - capture data flowing through an interface.
 - filter this data.
 - display intersesting information such as:
    - login info (username & passwords).
    - visited websites.
    - images.
    - etc.

**Sniffing packets using scapy**

**Extracting data from a specific layer**

**Analysing sniffed packet & extracting fields from layers**

**Analysing fields & extracting passwords**

**Extracting URLs**

**capturing passwords from any computer connected to the same network**

**Strings & bytes in Python 3**

## 07 - Writting a DNS Spoofer

**Intercepting Packets - creating a proxy**

**Converting packets to Scapy packets**

**Introduction to DNS spoofing**

**Filtering DNS responses**

**Amalysing & creating a custom DNS response**

**Modify packets on the fly**

**Redicrect DNS respnoses**

## Writting a file incerceptor

**Introduction & teaser**
