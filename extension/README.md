# PinSense Browser Extension

This is a Chrome/Chromium browser extension that allows you to add Pinterest pins to PinSense with a single right-click.

## Installation

### For Chrome:
1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode" (toggle in the top-right corner)
3. Click "Load unpacked"
4. Navigate to this `extension/` folder and select it
5. The extension will appear in your Chrome toolbar

### For Firefox:
1. Open Firefox and go to `about:debugging`
2. Click "This Firefox" in the left sidebar
3. Click "Load Temporary Add-on"
4. Select the `manifest.json` file in this folder

## Usage

1. **Start your PinSense backend server**:
   ```bash
   cd backend/
   uvicorn app.main:app --reload
   ```

2. **Right-click any image on Pinterest** and select "Add to PinSense"

3. You'll see a notification confirming the pin was added

4. **(Optional) Configure the backend URL**:
   - Click the PinSense extension icon in your toolbar
   - Enter your backend server URL (default: `http://localhost:8000`)
   - Click "Save Settings"

## How It Works

- The extension adds a context menu item "Add to PinSense" for all images on Pinterest
- When clicked, it sends the image URL to your backend API endpoint: `POST /api/submit-pin`
- Your backend downloads the image and generates an embedding
- Success/error notifications appear in your browser

## Files

- `manifest.json` - Extension configuration
- `background.js` - Context menu handler and API communication
- `popup.html` - Extension popup UI
- `popup.js` - Settings management

## Notes

- Make sure your backend server is running before using the extension
- The extension stores the backend URL in Chrome's sync storage
- You can modify the `API_URL` in `background.js` if needed
