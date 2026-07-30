import json
import requests
import time


def main():
    print("DevOps Ping Monitor Started\n")

    while True:
        with open("app/servers.json", "r") as file:
            data = json.load(file)

        for server in data["servers"]:
            try:
                response = requests.get(f"https://{server}", timeout=5)
                print(f"{server}: UP ({response.status_code})")
            except Exception:
                print(f"{server}: DOWN")

        time.sleep(10)


if __name__ == "__main__":
    main()
