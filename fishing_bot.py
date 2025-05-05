import time
import pyautogui
import pytesseract
from PIL import Image
import mss
import mss.tools

class FishingBot:
    def __init__(self):
        # Initialize screen capture
        self.sct = mss.mss()
        # Set up the region to capture (bottom right corner where messages appear)
        # You'll need to adjust these coordinates based on your screen
        self.message_region = {
            'left': -1367,
            'top': 248,
            'width': 301,
            'height': 197
        }
        self.last_text = ""  # Keep track of last detected text
        self.last_fish_time = 0  # Track when we last caught a fish
        self.last_cast_time = 0  # Track when we last cast the rod
        
    def capture_screen(self):
        """Capture the screen region where messages appear"""
        screenshot = self.sct.grab(self.message_region)
        return Image.frombytes('RGB', screenshot.size, screenshot.rgb)
    
    def detect_fish(self, image):
        """Detect if the 'fishing bobber splashes' message is present"""
        # Convert image to text using OCR
        text = pytesseract.image_to_string(image)
        text = text.strip().lower()
        
        # DEBUG: show detected text when it changes
        # if text != self.last_text and text:
        #     print(f"Detected text: {text}")
        #     self.last_text = text
        
        # Check for the fishing message and ensure enough time has passed
        current_time = time.time()
        if "fishing bobber splashes" in text and (current_time - self.last_fish_time) >= 3:
            self.last_fish_time = current_time
            return True
        return False
    
    def fish(self):
        """Main fishing loop"""
        print("Fishing bot started. Press Ctrl+C to stop.")
        self.last_cast_time = time.time()  # Initialize cast time
        recast_count = 0  # Counter for consecutive recasts

        try:
            while True:
                current_time = time.time()
                
                # Check if we need to recast (45 second failsafe)
                if current_time - self.last_cast_time >= 45:
                    print("No fish detected for 45 seconds, recasting...")
                    pyautogui.rightClick()  # Reel in or out
                    self.last_cast_time = current_time
                    recast_count += 1  # Increment the recast counter
                    
                    # Check if we've recast 5 times in a row
                    if recast_count >= 5:
                        print("Recast limit reached. Shutting down the bot.")
                        break  # Exit the loop to stop the bot
                    
                    continue
                
                # Reset the recast counter if fish is detected
                screen = self.capture_screen()
                if self.detect_fish(screen):
                    print("🎣 Fish detected! Reeling in...")
                    pyautogui.rightClick()  # Right click to reel in
                    time.sleep(1)  # Wait for animation
                    pyautogui.rightClick()  # Right click again to start fishing
                    self.last_cast_time = current_time  # Update cast time
                    recast_count = 0  # Reset the recast counter
                time.sleep(0.5)  # Small delay to prevent high CPU usage
                
        except KeyboardInterrupt:
            print("\nFishing bot stopped.")

if __name__ == "__main__":
    # Give user time to switch to Minecraft window
    print("Starting in 5 seconds... Switch to Minecraft window!")
    time.sleep(5)
    
    bot = FishingBot()
    bot.fish() 