// Backend API URL - change this to your server URL
const API_URL = "http://localhost:8000/api/submit-pin";

// Create context menu on installation
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "pinsense-add",
    title: "Add to PinSense",
    contexts: ["image"],
    targetUrlPatterns: ["https://pinterest.com/*", "https://www.pinterest.com/*"]
  });
});

// Handle context menu click
chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "pinsense-add") {
    const imageUrl = info.srcUrl;
    
    // Send image to PinSense backend
    fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        image_url: imageUrl
      })
    })
    .then(response => response.json())
    .then(data => {
      // Show success notification
      chrome.notifications.create({
        type: "basic",
        iconUrl: "images/icon128.png",
        title: "PinSense",
        message: "Pin added successfully!",
        priority: 2
      });
      console.log("Pin added:", data);
    })
    .catch(error => {
      // Show error notification
      chrome.notifications.create({
        type: "basic",
        iconUrl: "images/icon128.png",
        title: "PinSense Error",
        message: "Failed to add pin. Make sure the server is running.",
        priority: 2
      });
      console.error("Error adding pin:", error);
    });
  }
});
