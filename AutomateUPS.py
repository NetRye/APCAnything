
import sys
import subprocess

def check_dependency(module_name, version=None):
    try:
        module = __import__(module_name)
        if version and module.__version__ != version:
            raise ModuleNotFoundError
    except ModuleNotFoundError:
        print(f"{module_name} module is not installed or is an incorrect version. Installing correct version now it now...")
        package = f"{module_name}=={version}" if version else module_name
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{module_name} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {module_name}: {e}")
            sys.exit(1)

# Specify your dependencies as a list. Each tuple contains the module name and its pinned version (or None if you don't want to pin the version).
dependencies = [
    ("wexpect", "4.0.0"),
    ("getpass", None),
    ("pandas", None),
    ("tkinter.filedialog", None)
]

for dependency, version in dependencies:
    check_dependency(dependency, version)

# Everything above is meant to install the correct modules below automatically without the need to pip install modules like pandas or getpass...
import wexpect
import getpass
import pandas as pd
from tkinter.filedialog import askopenfilename

# Replace with the path to your Excel file
#excel_file_path = r"C:\Users\xyzuser\Documents\PythonStuff\UPS\upscommandstest.xlsx"
excel_file_path = askopenfilename(title="Select Excel file", filetypes=[("Excel files", "*.xlsx")])

# Read the data from the Excel file into a pandas DataFrame
data = pd.read_excel(excel_file_path)
password = getpass.getpass()  # Get the password once before the loop


# Loop through each row of the data
for index, row in data.iterrows():
    # Get the hostname and commands for the current row
    hostname = row["Hostnames"]
    commands = row["Commands"].split(";")
    print(f"commands for {hostname}: {commands}")

    # Create a string with the ssh command and options
    ssh_command = f"ssh username@{hostname}"

    # Spawn a child process with the ssh command
    log_file = open(f"{hostname}.log", "w")
    child = wexpect.spawn(ssh_command)
    child.logfile_send = None  # Do not log the sent commands

    # Wait for the prompt to appear and send a command
    print(f"Checking for Fingerprint on {hostname}")
    try:
        child.expect("yes", timeout=3)
        print(f"Fingerprint not found...Adding Fingerprint Now from {hostname}")
        child.sendline("yes")
        child.expect("password:")
        print(f"Added Fingerprint on {hostname}")
        child.sendline(password)
        #print("child.before:", child.before)
        #print("child.after:", child.after)
    except wexpect.ExceptionPexpect:
        print(f"Timed out waiting for 'fingerprint' prompt on {hostname}")
        child.expect("password:")
        child.sendline(password)
        #print("child.before:", child.before)
        #print("child.after:", child.after)
        print(f"Password Sent to {hostname}")

    child.expect_exact("apc>")
    print("child.before:", child.before + "\n")
    print("child.after:", child.after + "\n")
    log_file.write("Output of UPS Welcome Screen " + child.before + "\n") 
    log_file.write("Output of excel command: " + child.after + "\n")
        
    for command in commands:
        child.sendline(command + '\r\n')
        try:
            child.expect_exact("apc>", timeout=3)
            log_file.write(child.before)
            log_file.write(child.after)
            print("child.before:", child.before + "\n")
        except wexpect.ExceptionPexpect:
            print(f"ERROR: Timed out waiting for 'apc>' prompt on {hostname} after sending command")
            print("child.before:", child.before + "\n")
            break  # exit the loop if the prompt is not found after sending a command
        
    
   #Format for standard commands
    child.expect_exact("apc>")
    child.sendline("system")
    child.expect_exact("apc>")
    log_file.write("child before 1" + child.before + "\n")
    child.sendline("upsabout")
    print("child.before:", child.before)
    child.expect_exact("apc>")
    print("child.before output for upsabout = ", child.before)
    log_file.write("child output for upsabout " + child.before + "\n")
    child.sendline("detstatus -all")
    child.expect_exact("apc>")
    print("child.before:detstatus", child.before)
    log_file.write("Output of detstatus " + child.before + "\n")
    child.sendline("about")
    child.expect_exact("apc>")
    print("child.before:about output ", child.before + "\n")
    log_file.write("Output of about " + child.before + "\n")
    print("end of loop")



    print(f"Finished running commands. Closing log file.")
    child.close()  
    log_file.close()