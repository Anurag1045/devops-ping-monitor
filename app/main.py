import json
import requests
import time


def load_servers(path="app/servers.json"):
    with open(path, "r") as file:
        return json.load(file)["servers"]


def check_server(server):
    try:
        response = requests.get(f"https://{server}", timeout=5)
        return f"{server}: UP ({response.status_code})"
    except Exception:
        return f"{server}: DOWN"


def main():
    print("DevOps Ping Monitor Started\n")

    while True:
        for server in load_servers():
            print(check_server(server))

        time.sleep(10)


if __name__ == "__main__":
    main()
