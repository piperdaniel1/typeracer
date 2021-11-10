import keyboard
import time

prompt = input("enter type prompt here: ")
target_wpm = 100

print("press s to start...")
while(keyboard.is_pressed('s') == False):
    pass

for char in prompt:
    keyboard.write(char)
    time.sleep(1/target_wpm)
