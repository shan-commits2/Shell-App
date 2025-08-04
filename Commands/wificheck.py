import subprocess
import os

def main(args):
    print("Running network check using `ipconfig` or `ifconfig`...")

    try:
        if os.name == 'nt':
            result = subprocess.check_output("ipconfig", shell=True, text=True)
        else:
            result = subprocess.check_output("ifconfig", shell=True, text=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print("Error running network check:", e.output)
