# Linumerator

### Introduction
This program can be used to enumerate Linux systems. The program can check for sudo permissions, checks for SUID abuse, checks for cronjobs, lists the processes and generates a report in a text file.

### Usage
To use the program, simply run the following command:

`python3 linux_enumeration.py`

The program will then scan the system and generate a report in the reports directory.

### Output
The report will contain the following information:

- A list of all users with sudo permissions
- A list of all SUID files
- A list of all cronjobs
- A list of all running processes
### Requirements
The program requires the following Python modules:

`subprocess`

`os`

`time`
### Installation
To install the program, simply clone the repository and install the required Python modules:

`git clone https://github.com/dhruva-ds16/Linumerator.git`

`pip3 install -r requirements.txt`
### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
The program is licensed under the MIT License.

I hope this helps!
