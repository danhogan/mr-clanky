import json

def login(session, headers):
    with open('config.json') as config_file:
        config = json.load(config_file)

    username = config['username']
    password = config['password']

    login_data = {
        "msgs": [
            {
                "method": "login",
                "data": {
                    "u": username,
                    "p": password,
                    "t": "03AFcWeA6gnBtgiB7uyNRHfHANdEEGNSBmRM-NqQw0E5PVYGA1HBrULrlSXgV_r3hQqJRa99XTM7yOmaGWlocyV4KVM_OQFGN69AAlEAZgbfeq2IiF76RvNRxXwAS_OsO4Nguf2w0Li29R_VesGnuKEzUIWiy-Rgaxo-nn4l0HkqVB05N7O5685pbvAKaLMMeVBvpVId-UwNSY4NKtOeyCdUzUFTEzy5C-c1DIXwXD6WyqgfIpgd3tmTR0CcT_dyMihqge81UhMPSzLlAEfz7A5vXTVkp8OVIyA2Nz7rDrYKZIIjFWyy2oZPfM6RtDe6k7sbzQgcL972jJplVSz1j2XwFJI3cv7dBOFgJRX4FnjWK04cdJfXDSiUMQNrzJZ7KOvaRGFRPn1yVRmMQEWwAZmEchrADH6_YNLVXsfQHjt620nkRsgtW5jjRQWdjus8JWZEygNwM4BBN3GOzZUm_rqdd1ARkLet-wBFJvKje9qdkQu9__U07HTSTHdAstUezXx8BI1TZ2Pl5mhhqPzI3xCnMChDk27zwrbwZn20ox3PwvdW1An6_ZTTDmMGz0mEdTHONVYsUhI8ptTikYjMvO0PW5wmAjNndj0ueSPNP5noOsxemitQu2zZ2rUZu6xnRofNPow3Xuo2RdqI6Ni6tMW7uXM_39l3tYaJplbY8b1K4EARuB9S4tQjc",
                    "v": 3
                }
            }
        ],
        "uiv": 3,
        "refUrl": "https://www.fantrax.com/home",
        "dt": 0,
        "at": 0,
        "av": "3.0",
        "tz": "America/New_York",
        "v": "163.0.0"
    }

    login_response = session.post('https://www.fantrax.com/fxpa/req', headers=headers, json=login_data)

    if login_response.status_code == 200:
        print("Login successful")
    else:
        print("Login failed")
        print(login_response.text)
        exit()