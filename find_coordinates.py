import pyautogui
import time

def get_mouse_position():
    print("Move your mouse to the top-left corner of the message area and press Enter...")
    input()
    x1, y1 = pyautogui.position()
    print(f"Top-left coordinates: ({x1}, {y1})")
    
    print("Now move your mouse to the bottom-right corner of the message area and press Enter...")
    input()
    x2, y2 = pyautogui.position()
    print(f"Bottom-right coordinates: ({x2}, {y2})")
    
    print("\nUse these coordinates in your fishing_bot.py:")
    print(f"self.message_region = {{")
    print(f"    'left': {x1},")
    print(f"    'top': {y1},")
    print(f"    'width': {x2 - x1},")
    print(f"    'height': {y2 - y1}")
    print(f"}}")

if __name__ == "__main__":
    print("This script will help you find the correct coordinates for the message region.")
    print("Make sure Minecraft is running and you can see the fishing messages.")
    time.sleep(2)
    get_mouse_position() 