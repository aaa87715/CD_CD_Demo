from asyncio import sleep

import requests

def demo():
    response = requests.get("https://httpbin.org/get")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    if response.status_code == 200:
        return "Success"
    else:
        return "Failure"

def main():
    while True:
        sleep(3)
        print("Hello, World!")
        response = requests.get("https://httpbin.org/get")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")

if __name__ == "__main__":
    main()