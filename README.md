# My Chrome Extension

## Description
My Chrome Extension is a simple Chrome extension that demonstrates the basic structure and functionality of a Chrome extension. It includes a popup that displays a greeting message and a background script that runs in the background.

## Features
- Popup interface with a greeting message.
- Background script for handling background tasks.
- Basic styling using CSS.
- Placeholder for an extension icon.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/my_chrome_extension.git
   cd my_chrome_extension
   ```

2. Run the Python script to create the extension structure:
   ```bash
   python create_chrome_extension.py
   ```

### Loading the Extension in Chrome
1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable "Developer mode" in the top right corner.
3. Click on "Load unpacked" and select the `my_chrome_extension` folder created by the script.

### Usage
- Click on the extension icon in the Chrome toolbar to open the popup.

## Creating an Executable (EXE)
To create an executable file for the Python script, you can use `PyInstaller`. Follow these steps:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Navigate to the directory containing your Python script:
   ```bash
   cd path/to/your/script
   ```

3. Create the executable:
   ```bash
   pyinstaller --onefile create_chrome_extension.py
   ```

4. After the process completes, find the executable in the `dist` folder.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by the need for a simple Chrome extension template.
