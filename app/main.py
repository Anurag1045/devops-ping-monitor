import json
import requests


def main():
    with open("app/servers.json", "r") as file:
        data = json.load(file)

    print("DevOps Ping Monitor Started\n")

    for server in data["servers"]:
        try:
            response = requests.get(f"https://{server}", timeout=5)
            print(f"{server}: UP ({response.status_code})")
        except Exception:
            print(f"{server}: DOWN")


if __name__ == "__main__":
    main()
