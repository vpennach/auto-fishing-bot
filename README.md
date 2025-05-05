# Minecraft Auto-Fishing Bot

## Project Overview
This project aims to create an automated fishing bot for Minecraft that uses computer vision to detect when a fish is on the line and automatically reels it in. As a software engineer returning to Minecraft, I wanted to combine my programming skills with my love for the game to automate the more tedious aspects of fishing.

## How To Use Bot

### 1. Enable Visual Sounds in Minecraft
1. Open Minecraft
2. Go to "Options"
3. Click on "Accessibility Settings"
4. Make sure "Show Subtitles" is turned ON
5. This will show text messages for sounds, including the "fishing bobber splashes" message we need

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Find Screen Coordinates
1. Run the coordinate finder script:
```bash
python find_coordinates.py
```
2. When prompted:
   - Move your mouse to the top-left corner of where the subtitles appear
   - Press Enter
   - Move your mouse to the bottom-right corner of where the subtitles appear
   - Press Enter
   - Don't worry about being exact - it's better to make the area  larger than needed
3. The script will output coordinates - copy these numbers
4. Open `fishing_bot.py` and replace the `message_region` coordinates with the numbers you got
   - The bot will still work even if the capture area is bigger than the subtitle area

### 4. Run the Bot
1. Make sure Minecraft is running and you're in a fishing spot
2. Run the bot:
```bash
python fishing_bot.py
```
3. You have 5 seconds to switch back to Minecraft and cast out the first rod
4. The bot will start monitoring for the "fishing bobber splashes" message
5. When a fish is detected, it will automatically:
   - Right-click to reel in
   - Wait 2 seconds
   - Right-click again to cast the line
6. Press Ctrl+C to stop the bot at any time

### Debugging
If you need to see what text the bot is detecting, there's a debug feature in `fishing_bot.py`. Simply uncomment the lines in the `detect_fish` method to enable it. This will print all detected text to the terminal.

## How It Works
The bot will:
1. Capture screenshots of the Minecraft window
2. Use computer vision to detect when a fish is on the line (looking for specific visual cues)
3. Automatically right-click to reel in the fish
4. Repeat the process

## Technical Implementation
The project uses:
- Python for the main programming language
- OpenCV and Tesseract OCR for text detection
- PyAutoGUI for mouse control
- Screen capture libraries to monitor the game window

## Project Goals
- Create a reliable fish detection system
- Implement smooth mouse control
- Make the bot configurable for different Minecraft versions and settings
- Ensure the bot is safe to use and doesn't violate Minecraft's terms of service

## Disclaimer
This project is for educational purposes only. Please ensure you comply with Minecraft's terms of service and use this bot responsibly. This bot is NOT to be used on public servers, you will get caught for cheating. like stated before this is to be used for educational purposes or on your own single player world. 

Fish Responsibly!