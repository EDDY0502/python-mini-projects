import time
import sys
print("\n" * 50)  # Clear the console screen
lyrics = [
    "Hum tere pyaar mein saara aalam",
    "Kho baithhe hain, kho baithhe",
    "Tum kahate ho ke aise",
    "Pyaar ko bhool jaao, bhool jaao",
    "Hum tere pyaar mein saara aalam",
    "Kho baithhe hain, kho baithhe",
    "Tum kahate ho ke aise",
    "Pyaar ko bhool jaao, bhool jaao",
    "Hum tere pyaar mein saara aalam"
]

base_timings = [
    3.3,
    2.4,
    2.1,
    3.0,
    3.3,
    2.4,
    2.1,
    3.0,
    4.5
]

speed = 1.4  # slower or faster (higher = slower)

typing_speed = 0.06  # lower = faster typing, higher = slower typing

for i in range(len(lyrics)):
    line = lyrics[i]                  # current line
    for ch in line:                   # print character by character
        sys.stdout.write(ch)          # show each character
        sys.stdout.flush()            # force print immediately
        time.sleep(typing_speed)      # delay between characters
    
    print()                           # move to next line after finishing text
    time.sleep(base_timings[i] * speed - len(line) * typing_speed)
