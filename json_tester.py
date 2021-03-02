import json

print("File name: ")
filename = input()

with open(filename, "r", encoding = "utf-8") as f:
	output = json.load(f)
print(output)