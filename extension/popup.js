// Load saved settings
document.addEventListener("DOMContentLoaded", () => {
  chrome.storage.sync.get(["apiUrl"], (result) => {
    if (result.apiUrl) {
      document.getElementById("apiUrl").value = result.apiUrl;
    } else {
      document.getElementById("apiUrl").value = "http://localhost:8000";
    }
  });
});

// Save settings
document.getElementById("save").addEventListener("click", () => {
  const apiUrl = document.getElementById("apiUrl").value;
  
  chrome.storage.sync.set({ apiUrl }, () => {
    // Show feedback
    const button = document.getElementById("save");
    button.textContent = "✓ Saved!";
    button.style.background = "#28a745";
    
    setTimeout(() => {
      button.textContent = "Save Settings";
      button.style.background = "#e60023";
    }, 2000);
  });
});
