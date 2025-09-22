# api_caller.py (Corrected Version)
import requests
import json
import pyotp
import hashlib
import base64 # <-- Required for Base32 encoding

# ==========================================================
# TODO: FILL IN YOUR DETAILS HERE
# ==========================================================
# CORRECT
GIST_URL = "https://gist.github.com/DCchoudhury15/9e2f0f1a9c51a6a738060c84d98804cc"
CONTACT_EMAIL = "divyanshuchoudhury51@gmail.com"
# ==========================================================


def main():
    """
    Main function to generate TOTP and send the API request.
    """
    print("🚀 Starting the API submission process...")

    # 1. Create the raw secret key string
    raw_secret = CONTACT_EMAIL + "HENNGECHALLENGE004"

    # 2. Convert the raw secret to Base32, which pyotp expects
    base32_secret = base64.b32encode(raw_secret.encode('utf-8'))

    # 3. Generate the Time-based One-Time Password (TOTP)
    try:
        totp = pyotp.TOTP(
            s=base32_secret, # Use the correctly encoded secret
            digits=10,
            digest=hashlib.sha512,
            interval=30
        )
        otp_password = totp.now()
        print(f"✅ Generated TOTP: {otp_password}")
    except Exception as e:
        print(f"❌ Error generating TOTP: {e}")
        return

    # 4. Prepare the HTTP request components
    url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "github_url": GIST_URL,
        "contact_email": CONTACT_EMAIL,
        "solution_language": "python" 
    }

    # 5. Send the POST request with Basic Authentication
    print("📡 Sending POST request to the server...")
    try:
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(payload),
            auth=(CONTACT_EMAIL, otp_password)
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during the request: {e}")
        return

    # 6. Display the server's response
    print("\n--- Server Response ---")
    print(f"Status Code: {response.status_code}")
    print("Response Body:")
    print(response.text)
    print("-----------------------")

    if response.status_code == 200:
        print("\n🎉 Congratulations! Mission 3 is successful!")
    else:
        print("\n❗️ Something went wrong. Check the status code and response body for clues.")

if __name__ == "__main__":
    if "YOUR_GIST_URL_HERE" in GIST_URL or "YOUR_EMAIL_HERE" in CONTACT_EMAIL:
        print("🛑 Error: Please update the GIST_URL and CONTACT_EMAIL variables in the script before running.")
    else:
        main()