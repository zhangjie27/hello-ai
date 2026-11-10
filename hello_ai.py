import json

CONFIG_FILE = "config.json"

try:
    with open(CONFIG_FILE, encoding="utf-8") as f:
        data = json.load(f)
    print(f"模型：{data['model']}")
    print(f"温度：{data['temperature']}")
except FileNotFoundError:
    print("找不到 config.json，请检查是否在这个目录里")