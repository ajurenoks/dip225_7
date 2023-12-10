# Import the pyautogui module.
# PyAutoGUI is a Python module for automating keyboard and mouse movements.
import pyautogui

# Iterate over all the windows currently open on the system.
# pyautogui.getAllWindows() fetches a list of Window objects, each representing an open window.
for x in pyautogui.getAllWindows():
    # Print the title of each window.
    # The title property of a Window object gives the title of the window as seen on the top bar.
    print(x.title)
