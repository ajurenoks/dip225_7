# Import the Application class from pywinauto module
from pywinauto.application import Application

# Start an application with UI Automation backend and run 'calc.exe'
app = Application(backend="uia").start(r"calc.exe")

# Connect to an already running calculator application with the title 'Kalkulators'
# Wait for a maximum of 10 seconds to establish this connection
app.connect(title="Kalkulators", timeout=10)

# Access the main window of the calculator with the title 'Kalkulators'
prg = app.window(title="Kalkulators")

# Print the identifiers for all the controls in the calculator window
# This helps in understanding what controls are available for interaction
prg.print_control_identifiers()

# Simulate a click on the button with identifier 'Button25'
prg.Button25.click()

# Simulate clicks on buttons with identifiers 'Button26' and 'Button27'
prg.Button26.click()
prg.Button27.click()

# Send the keys '1234' to a control with identifier 'Static2'
prg.Static2.type_keys("1234")

# Retrieve the text currently displayed in the 'Static2' control
a = prg.Static2.window_text()

# Print the retrieved text to the console
print(a)
