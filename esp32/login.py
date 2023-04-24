import urequests
import json

def login_psu():
    username = "6310110533"
    password = "Fuckyou@29"
    payload = {'username': username,
               'password': password}
    url = "https://cp-xml-40g.psu.ac.th:6082/php/uid.php"
    url2 = "http://172.30.222.54:8088/login/login.php"
    
    response = urequests.post(
                                url=url2,
                                data = str(payload)
                              )
#     res = urequests.get("https://server-dev.psu.ac.th:8444")
#     print(res.content)
    print("-----------------------------------------------------")
    print(response.content.decode())
    print(response.status_code)
login_psu()