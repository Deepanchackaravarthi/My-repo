# create_and_read.py

# Create and write to a file
with open("sample.txt", "w") as file:
    file.write("Hello Deepan!\n")
    file.write("This is a Python file handling example.\n")

print("✅ File created and written successfully.\n")

# Read the file content
with open("sample.txt", "r") as file:
    content = file.read()
    print("📖 File Content:\n", content)
