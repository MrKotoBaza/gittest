import requests

response = requests.get("https://google.com")

print(response.status_code)

if response:
    with open("a8.txt", "w") as f:
        
        for i in response.text:
            f.write(i)

    #print(response.json())
    print(response.headers["content-type"])
    print(response.headers.keys())

else:
    print(response.status_code)
