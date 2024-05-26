import requests
import json
import time
from colorama import Fore, Style

# Class text color
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'

# Fungsi untuk mendapatkan kode OTP
def get_otp(nomor):
    url = "https://xclite.netlify.app/api/users/otp"

    payload = {
        "msisdn": f"{nomor}"
    }
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en,en-US;q=0.9,id;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://xclite.netlify.app',
        'priority': 'u=1, i',
        'referer': 'https://xclite.netlify.app/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print(Fore.GREEN + f"[+] {response.status_code} Kode OTP Berhasil dikirim"  + Style.RESET_ALL)
        return response.json(), response.status_code
    else:
        return response.json(), response.status_code

# Fungsi login/untuk autentikasi kode OTP
def auth_otp(kode_auth, kode_otp):
    url = "https://xclite.netlify.app/api/users/login"

    payload = {
        "data": "{\"authId\":\"% s\",\"stage\":\"OTP\",\"callbacks\": [{\"type\":\"MetadataCallback\",\"output\":[{\"name\":\"data\",\"value\":{\"stage\":\"OTP\"}}],\"_id\":0},{\"type\":\"PasswordCallback\",\"output\":[{\"name\":\"prompt\",\"value\":\"One Time Password\"}],\"input\":[{\"name\":\"IDToken2\",\"value\":\"% s\"}],\"_id\":1},{\"type\":\"TextOutputCallback\",\"output\":[{\"name\":\"message\",\"value\":\"{\\\"code\\\":\\\"000\\\",\\\"data\\\":{\\\"max_validation_attempt_suspend_duration\\\":\\\"900\\\",\\\"max_validation_attempt\\\":5,\\\"sent_to\\\":\\\"SMS\\\",\\\"next_resend_allowed_at\\\":\\\"1716645680\\\"},\\\"status\\\":\\\"SUCCESS\\\"}\"},{\"name\":\"messageType\",\"value\":\"0\"}],\"_id\":2},{\"type\":\"ConfirmationCallback\",\"output\":[{\"name\":\"prompt\",\"value\":\"\"},{\"name\":\"messageType\",\"value\":0},{\"name\":\"options\",\"value\":[\"Submit OTP\",\"Request OTP\"]},{\"name\":\"optionType\",\"value\":-1},{\"name\":\"defaultOption\",\"value\":0}],\"input\":[{\"name\":\"IDToken4\",\"value\":0}],\"_id\":3}]}" % (kode_auth, kode_otp)
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://xclite.netlify.app',
        'priority': 'u=1, i',
        'referer': 'https://xclite.netlify.app/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
    }
    
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print(Fore.YELLOW + f"[\] Sedang Autentikasi OTP ..."  + Style.RESET_ALL)
        return response.json(), response.status_code
    else:
        return response.json(), response.status_code

# Fungsi untuk dor xcl
def dor_xcl(token):
    url = "https://xclite.netlify.app/api/users/buy"

    payload = {
        "idToken": f"{token}"
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en,en-US;q=0.9,id;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://xclite.netlify.app',
        'priority': 'u=1, i',
        'referer': 'https://xclite.netlify.app/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print(Fore.GREEN + f"[+] {response.status_code} Registrasi Paket XCL Berhasil"  + Style.RESET_ALL)
        return response.json(), response.status_code
    elif response.status_code == 400:
        print(Fore.RED + "[!] Saldo/pulsa tidak cukup! Gunakan Pulsa 9000"  + Style.RESET_ALL)
    else:
        print(Fore.RED + f"[!] {response.status_code} Error"  + Style.RESET_ALL)
        return response.json(), response.status_code

def main():
    print("     ┎ ╴ ╴ ╴ ╴ ╴ ╴ ╴ ╴  ╴ ╴ ╴ ╴ ╴ ╴ ╴ ╴ ╴ ╴ ┓        ")
    print("     ┃     TEMBAK XL XCL M (LIMIT 80GB)     ┃        ")
    print("     ┗ ╴ ╴ ╴ ╴ ╴ ╴ ╴ ╴  ╴ ╴ ╴ ╴ ╴ ╴ ╴ ╴ ╴ ╴ ┚        ")
    # Input number xl dengan awalan 62xxxx
    nomor = int(input("[>] Masukkan nomor anda (diawali dengan 62): "))
    while True:
        # Dapat JSON dari fungsi get_otp (berisi authId, dll)
        otp_responses, otp_response_code = get_otp(nomor)
        # print(otp_responses)

        # Input kode OTP untuk login
        # Dapat JSON berisi tokenID
        if otp_response_code == 200:
            kode_otp = input("[>] Silakan masukkan Kode OTP anda: ")
            token_responses = auth_otp(otp_responses['message']['authId'], kode_otp)

            # Tembak dorrrrr
            if 'tokenId' in token_responses[0]['message']:
                print(Fore.GREEN + "[+] Autentikasi OTP berhasil, sedang memulai ..." + Style.RESET_ALL)
                dor_xcl(token_responses[0]['message']['tokenId'])
                break
            else:
                t = 60
                while t: 
                    mins, secs = divmod(t, 60) 
                    timer = '{:02d}:{:02d}'.format(mins, secs) 
                    print(Fore.RED + "[!] Kode OTP tidak dikenali, will send OTP and try again sir! (wait 1 minute) "  + Style.RESET_ALL + timer, end="\r")
                    time.sleep(1) 
                    t -= 1
                print("")
        else:
            print(Fore.RED + f"[!] {otp_response_code} - {otp_responses['message']}"  + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()