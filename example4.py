# Import the Application class from pywinauto for GUI automation.
from pywinauto.application import Application
# Import the time module for adding delays in the script.
import time

# Start the Zoom application using the UI Automation backend.
# This line launches Zoom from its installation directory.
app = Application(backend="uia").start(r"C:\Users\user\AppData\Roaming\Zoom\bin\Zoom.exe")

# Connect to the Zoom application window with the title 'Zoom'.
# Timeout is set to 30 seconds to allow time for the application to open and be detected.
app.connect(title="Zoom", timeout=30)

# Wait for 2 seconds to ensure the Zoom application window is ready.
time.sleep(2)

# Access the main Zoom window.
prg = app.window(title="Zoom")

# Additional delay to ensure stability in automation.
time.sleep(1)

# Uncomment the following line to print identifiers for controls in the Zoom window.
# This can be used to identify buttons and fields for interaction.
# prg.print_control_identifiers()

# Click on the button with the identifier 'Button11' in the Zoom window.
# This is the button 'Join a Meeting'.
prg.Button11.click()

# Connect to the 'Join Meeting' window that appears after clicking 'Join a Meeting'.
# The timeout is set to 5 seconds.
app2 = Application(backend="uia").connect(title="Join Meeting", timeout=5)

# Uncomment to print control identifiers for the 'Join Meeting' window.
# This is useful to identify fields where meeting ID and name are entered.
# app2.JoinMeeting.print_control_identifiers()

# Type '1234' into the 'Edit2' field in the 'Join Meeting' window.
# This could represent a placeholder meeting ID.
app2.JoinMeeting.Edit2.type_keys("1234")

# Use a loop to send 20 backspace keystrokes to the 'Edit2' field.
# This clears out the previously entered meeting ID.
for i in range(0, 20):
    app2.JoinMeeting.Edit2.type_keys("{BACKSPACE}")

# Enter 'Aleksejs Jurenoks' into the 'Edit3' field, which might be the name field.
# 'with_spaces=True' ensures that spaces are correctly included.
app2.JoinMeeting.Edit3.type_keys("Aleksejs Jurenoks", with_spaces=True)
