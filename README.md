![image alt](https://github.com/InfoSec-HA/InfoSec-HA-Lab-V1/blob/main/attacker.png?raw=true)
## InfoSec-HA-lab version 1

Are you tired of the long and painful process of setting up penetration testing environments manually? 
Welcome to InfoSec-HA-Lab, a powerful and community-driven project designed to make your life easier. With just one click, you can install and deploy a complete web application security lab—no errors, no complexities, and no wasted time, inshallah.


## 🛡️ What is InfoSec-HA-Lab?

InfoSec-HA-Lab (High-Availability Cybersecurity Lab) is a pre configured, containerized platform that bundles popular vulnerable web applications and training environments. Its mission is to democratize access to cybersecurity education by eliminating installation headaches.

This is how it looks:

![image alt](https://github.com/InfoSec-HA/InfoSec-HA-Lab-V1/blob/main/InfoSec_HA.png?raw=true)

# What’s Included in InfoSec-HA-Lab V1?

1. bWAPP
2. xvwa
3. dvwa
4. mutillidae
5. hackademic
6. sqli-labs
7. xss-lab
 
# 🚀 Coming Soon in Version 2

We're already working on the next upgrade—InfoSec-HA-Lab V2—which will include even more powerful labs to extend your learning experience:

7. rapid7 hackazon
8. WebGoat
9. owasp juice shop
10. WackoPicko
11. Damn Vulnerable NodeJS Application

# 🌍 Why InfoSec-HA-Lab Matters

In a world where cybersecurity threats are evolving rapidly, hands-on practice is no longer optional—it’s essential. InfoSec-HA-Lab eliminates setup barriers and allows you to focus on what truly matters: learning, experimenting, and mastering web application security.

Whether you're preparing for certifications, hunting bugs, or simply exploring new attack vectors, InfoSec-HA-Lab is your ideal companion.

# Server Installation 

You can download Ubuntu server 2018 64 and it's the best one with php7.2 7.3 platform:
[Download Ubuntu Server 64]
```
https://old-releases.ubuntu.com/releases/18.04.5/ubuntu-18.04.5-live-server-amd64.iso
```

Please note that PHP version 7.2 is require.

------------------------------
Run Script :

```
sudo apt-get install git

sudo git clone https://github.com/InfoSec-HA/InfoSec-HA-Lab-V1.git

cd InfoSec-HA-Lab-V1

sudo chmod +x setup.sh

sudo ./setup.sh


```

------------------------------

Login details

for xvwa :
```php
admin:admin
xvwa:xvwa
user:vulnerable
```
for Mutillidae :
```php
admin:admin
pass:adminpass
```
for bWAPP :
```php
admin:bee
pass:bug
```
for dvwa :
```php
admin:admin
pass:password
```


## Contact: X ##
[InfoSec-HA-Lab](https://twitter.com/InfoSec-HA)
