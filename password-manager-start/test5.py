import json

with open("password_list_json.json", mode="r") as file:
    rzecz = json.load(file)
    print(f'Website: YOYOYOY \nUsername: {(rzecz["YOYOYOY"]["username"])} \nPassword: {(rzecz["YOYOYOY"]["password"])}')
