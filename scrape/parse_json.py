import json
# Read the JSON file
try:
    with open('/Users/anseungwon/dev/Python/scrape/res.json') as file:
        data = json.load(file)
except json.JSONDecodeError:
    print("Decoding JSON has failed")
except FileNotFoundError:
    print("File not found")

# Access the content array
content = data['article']['content']

# Iterate over the content array
for item in content:
    if item['type'] == 'heading':
        print(f"\033[37m{item['text']}\033[0m\n")
    elif item['type'] == 'paragraph':
        print(f"{item['text']}\n")
