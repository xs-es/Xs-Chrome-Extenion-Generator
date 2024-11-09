import os

# Define the structure of the Chrome extension
extension_structure = {
    "my_chrome_extension": {
        "manifest.json": '''{
    "manifest_version": 3,
    "name": "My Chrome Extension",
    "version": "1.0",
    "description": "A simple Chrome extension.",
    "action": {
        "default_popup": "popup.html",
        "default_icon": "icons/icon.png"
    },
    "background": {
        "service_worker": "background.js"
    },
    "icons": {
        "48": "icons/icon.png"
    }
}''',
        "background.js": '''// Background script
console.log("Background script running");''',
        "popup.html": '''<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Hello, Chrome Extension!</h1>
    <script src="popup.js"></script>
</body>
</html>''',
        "popup.js": '''// Popup script
console.log("Popup script running");''',
        "styles.css": '''/* Styles for the popup */
body {
    font-family: Arial, sans-serif;
}''',
        "icons": {
            "icon.png": ''
        }
    }
}

# Function to create the directory structure
def create_extension_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_extension_structure(path, content)
        else:
            with open(path, 'w') as file:
                file.write(content)

# Create the extension
create_extension_structure(os.getcwd(), extension_structure)
print("Chrome extension structure created successfully.")
