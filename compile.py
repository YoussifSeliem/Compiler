import scanner
import Cparser
import subprocess

# Replace 'your_command_here' with the actual command you want to run
command = 'python .\scanner.py tst.c tst.txt'

# Run the command
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check the result
if result.returncode == 0:
    print("Command executed successfully")
    print("Output:")
    print(result.stdout)
else:
    print("Error executing command")
    print("Error message:")
    print(result.stderr)
