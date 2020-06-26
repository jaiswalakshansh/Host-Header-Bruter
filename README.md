# Host-Header-Bruter


Overview
--------
The repo is a short tool for bruteforcing host-header values and observing any response change in requests
The basic idea id to see response change in the a particular  that may occur due to variation in hosts header values the payloads in header.txt is combined from 

```
User-Agent:Bots,devices,BlindXss
Host:Host validation bypass
X-Forwarded-For:Different ips for internal redirecterrors stack trace
X-forwarded-Host:Different ips for internal redirecterrors stack trace
Referer:Different ips for internal redirecterrors stack trace
Origin:Origin Bypass 
Location:Redirections
X-Forwarded-Port:Check if port forwarding is allowed explicit outside

```


Installation & Usage
------------

```
git clone https://github.com/jaiswalakshansh/Host-Header-Bruter.git
cd Host-Header-Bruter
python hosthdbrute.py -u https://google.com/ -he header.txt
```

Currently the output is saved in /output with file names as 1,2 3.... and for differentiate among them we can use
```
cd output
vim -d *.txt
```

TODO:
-------------
```
[ ] Add cookie based requests
[ ] Add automatic difference output
[ ] Add Multiple combination of headers 
```