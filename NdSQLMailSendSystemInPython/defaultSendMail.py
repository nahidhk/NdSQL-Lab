import requests

url = "https://mailr.ndsql.top/index.php"

data = {
    "to": "nahidtdx@gmail.com",
    "username": "DefaultUsername",
    "subject": "This is a Subject!( Only Test )",
    "message": "This is default Message. only test use this Message!"
}

try:
    response = requests.post(url, data=data, timeout=10)

    print("HTTP:", response.status_code)
    print("RAW:", response.text)

    result = response.json()
    print("Server Message:", result["message"])

except Exception as e:
    print("Error sending mail:", e)