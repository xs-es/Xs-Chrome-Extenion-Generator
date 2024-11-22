# Chrome Extension Template Generator

## Description
The Chrome Extension Template Generator is a Python script that automatically creates the essential files and folder structure needed to start developing a Chrome extension. This tool simplifies the setup process, allowing developers to focus on building their extensions without worrying about the initial configuration.

## Features
- Generates a complete folder structure for a Chrome extension.
- Creates essential files including:
  - `manifest.json`: The metadata file for the extension.
  - `background.js`: The background script for handling background tasks.
  - `popup.html`: The HTML file for the extension's popup interface.
  - `popup.js`: The JavaScript file for the popup functionality.
  - `styles.css`: The CSS file for styling the popup.
  - An `icons` folder for extension icons.
  
## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/xs-es/Xs-Chrome-Extenion-Generator.git
   cd /v1.0/Xs-Chrome-Extenion-Generator
   ```

2. Run the Python script to create the extension structure:
   ```bash
   python create_chrome_extension.py
   ```

### Loading the Extension in Chrome
1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable "Developer mode" in the top right corner.
3. Click on "Load unpacked" and select the folder created by the script.

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
- This project was created to streamline the development process for Chrome extensions and help developers get started quickly.
