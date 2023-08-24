import os
import subprocess
import time

def list_processes():
    # Get a list of all processes
    processes = psutil.process_iter()

    # Iterate over the processes
    for process in processes:
        # Get the process name
        process_name = process.name()

        # Get the process ID
        process_id = process.pid

        # Print the process name and ID
        print(f"Process name: {process_name}")
        print(f"Process ID: {process_id}")

def list_cronjobs():
    # Get the cronjobs
    cronjobs = subprocess.check_output(["crontab", "-l"])

    # Print the cronjobs
    print(f"Cronjobs:")
    print(cronjobs)

def check_sudo_permissions():
    # Get the sudo permissions
    sudo_permissions = subprocess.check_output(["sudo", "-l"])

    # Print the sudo permissions
    print(f"Sudo permissions:")
    print(sudo_permissions)

def check_suid_abuse():
    # Get a list of all files with SUID or SGID permissions
    suid_files = subprocess.check_output(["find", "/ -perm /4000"])
    sgid_files = subprocess.check_output(["find", "/ -perm /2000"])

    # Print the SUID and SGID files
    print(f"SUID files:")
    print(suid_files)
    print(f"SGID files:")
    print(sgid_files)

def create_report():
    # Create a text file
    report_file = open("report.txt", "w")

    # Write the information to the text file
    report_file.write("Processes:\n")
    list_processes()
    report_file.write("\nCronjobs:\n")
    list_cronjobs()
    report_file.write("\nSudo permissions:\n")
    check_sudo_permissions()
    report_file.write("\nSUID and SGID files:\n")
    check_suid_abuse()

    # Close the text file
    report_file.close()

if __name__ == "__main__":
    # Get the current user
    user = os.getenv("USER")

    # Create the report
    create_report()

    # Print a message
    print("Report created successfully!")
