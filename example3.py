# Import Application class from pywinauto module for GUI automation.
from pywinauto.application import Application
# Import the time module for adding delays in the script.
import time

# Start Notepad++ application using UI Automation backend.
# This line launches Notepad++ located at the specified path.
app = Application(backend="uia").start(r"C:\Program Files\Notepad++\notepad++.exe")

# Connect to a running instance of Notepad++ with the title 'new 1 - Notepad++'.
# Timeout is set to 30 seconds, allowing the script some time to find the window.
app.connect(title="new 1 - Notepad++", timeout=30)

# Pause the execution for 2 seconds to ensure the application is fully loaded.
# This delay helps to avoid any race conditions between app start-up and script execution.
time.sleep(2)

# Access the Notepad++ window with the title 'new 1 - Notepad++'.
prg = app.window(title="new 1 - Notepad++")

# Print identifiers for controls within the Notepad++ window.
# This is useful for identifying various UI elements for interaction.
prg.print_control_identifiers()

# Send a string of text to the 'Panel0' control of the Notepad++ window.
# 'with_spaces=True' ensures that spaces in the string are processed correctly.
prg.Panel0.type_keys("This is my first application", with_spaces=True)
