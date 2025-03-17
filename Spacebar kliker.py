import keyboard
import time

def spacebar_clicker():
    print("Press the spacebar as fast as you can!")
    print("Press Space to start, and ESC to quit.")
    
    keyboard.wait("space")  # Wait for user to start
    print("Go!")
    
    start_time = time.time()
    clicks = 1  # Start with 1 click since space is pressed to start
    last_pressed = False  # Track if space was already pressed
    
    while True:
        if keyboard.is_pressed("space"):
            if not last_pressed:  # Only count if space wasn't already held
                clicks += 1
                last_pressed = True
        else:
            last_pressed = False  # Reset when space is released
        
        elapsed_time = time.time() - start_time
        if elapsed_time >= 2:
            print(f"HPS: {clicks / 2}")
            clicks = 0
            start_time = time.time()
        
        if keyboard.is_pressed("esc"):
            print("Exiting...")
            break

if __name__ == "__main__":
    spacebar_clicker()
