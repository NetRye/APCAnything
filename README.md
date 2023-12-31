# Network Device Configuration Script with SSH (APC UPS Management)

This Python script automates the management of APC UPS devices, or any network device that supports SSH connections. It utilizes SSH connections and the `wexpect` library to interact with the devices and execute customizable commands either hardcoded or within the excel file.

## Prerequisites

Before running this script, make sure you have the following:

1. Python: Ensure that Python is installed on your system. You can download Python from the official Python website (https://www.python.org) and follow the installation instructions.

2. Example Excel File: An example Excel file named "devices.xlsx" is included in the repository to help you understand the required format. You can find it in the same location where you found this script. You can use this file as a template and modify it according to your devices and configuration needs.

## Usage

1. Check Dependencies: The script checks for the required dependencies specified in the `dependencies` list. If any dependencies are missing or have an incorrect version, the script automatically installs the correct version using `pip`.

2. Import Libraries: The script imports the necessary libraries, including `wexpect`, `getpass`, `pandas`, and `tkinter.filedialog`.

3. Select Excel File: The script prompts you to select the Excel file that contains the device information and configuration commands. A file dialog window will appear, allowing you to browse and select the desired file.

4. Read Excel Data: The script uses the `pandas` library to read the selected Excel sheet into a DataFrame, making it easier to manipulate and access the data.

5. User Authentication: Enter your password when prompted by the script. This password will be used to authenticate the SSH connections to the network devices.

6. Execute Commands: The script loops through each row in the Excel file. It establishes an SSH connection to the device, handles any authentication or prompt requirements, and sends the specified commands. The output of each command is logged to a separate log file.

7. Handle Exceptions: The script includes error handling to manage potential exceptions, such as timeouts or incorrect prompts when connecting to devices. Any encountered errors will be displayed in the terminal.

## Output

The script generates log files for each device in the format "{hostname}.log" in the same directory as the script. Each log file contains the output of the executed commands for the respective device.

Additionally, the script displays the output and error messages in the terminal in real-time, allowing you to monitor the progress and identify any issues.

Review the log files and terminal messages to ensure that the commands were executed successfully and to address any errors that may have occurred.

## Disclaimer

This script is provided as-is and without any warranty. It is your responsibility to review and test the script before using it in a production environment. The author assumes no liability for any damages or issues arising from the use of this script.

Please use this script responsibly and ensure that you have appropriate permissions and authorization to access and manage the devices.

## Example Excel File

To help you get started, an example Excel file named "devices.xlsx" is included in the repository. It demonstrates the required format for the Excel file, with the "Hostnames" column containing the device hostnames and the "Commands" column containing the management commands for the devices.

Feel free to modify this example file or create your own Excel file following the same format to suit your devices and configuration requirements.

## Conclusion

This network device management script automates the process of managing APC UPS devices or any network device that supports SSH connections. It provides a convenient way to execute commands on multiple devices simultaneously. The script also handles dependencies by checking and installing the required modules automatically.

Feel free to customize the script according to your specific needs and extend its functionality to manage other types of network devices.
