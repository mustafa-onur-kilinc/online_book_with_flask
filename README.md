# 100 Days of Python - Day 70 (Git, GitHub and Version Control)

This repository displays one sentence long book chapters in pure HTML webpages.

Flask framework is used to write Python code for creating the website and 
Jinja templates are used to create more dynamic HTML pages.

The home page is a simple "List of Content" style page.

## How to Download this Repository

1. Open a terminal (if available, you may use the terminal in your IDE)
2. On this webpage, click the green button with "<> Code" written on it
3. For HTTP and SSH options, run `git clone <repo>` command in terminal

## How to Create Python Virtual Environment

1. After the repository is downloaded, open a terminal
2. Use `cd <repo_directory>` command to go to the repository
3. Create the virtual environment using the `venv` library

To create the virtual environment on Unix/macOS, enter the command below: 
```bash 
python3 -m venv <folder of virtual environment>
```

For Windows, enter this command instead:
```bash
py -m venv <folder of virtual environment>
```

Usually, `.venv` is used for folder name.

## How to Activate Virtual Environment

To activate the virtual environment on Unix/macOS, enter the command below:

```bash
source <folder of virtual environment>/bin/activate
```

For Windows, enter this command instead:
```bash
<folder of virtual environment>\Scripts\activate
```

## Downloading Required Libraries and Frameworks

1. Open a terminal
2. Use `cd <repo_directory>` command to go to the repository
3. Run the command `pip3 install -r requirements_3_14.txt` to download required libraries and frameworks

## Creating a requirements.txt File

1. Open a terminal
2. Make sure your Python virtual environment is activated in the terminal
3. Run this command in the terminal: `pip3 freeze > [requirement file name].txt`

**Note:** Make sure you are in the .venv environment before running
the command in the third step.
Otherwise, you may end up adding unnecessary libraries to the requirements file.

## Resources Used

I used this resource to learn how to automatically generate
a requirements.txt file:

damnever 2015, "Automatically create file 'requirements.txt'",
Stack Exchange, Inc., accessed 30 May 2026, <https://stackoverflow.com/a/33468993>

I used this resource to learn how to separate changes to smaller parts for more
atomic Git commits:

mac et. al. 2022, "Commit only part of a file's changes in Git", 
Stack Exchange, Inc., accessed 30 May 2026, <https://stackoverflow.com/a/1085191>

I used these resources to learn how to create and activate virtual environments:

Soviut 2015, "Creating a virtualenv with preinstalled packages as in requirements.txt",
Stack Exchange, Inc., accessed 31 May 2026, <https://stackoverflow.com/a/41799834>

Create and Use Virtual Environments 2025, PyPA, accessed 31 May 2026,
<https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments>

Syed AHMAD 2023, "Setting up a virtual environment and requirements.txt file for your data science project", 
Medium, Inc., accessed 31 May 2026,
<https://medium.com/@syedhaseebahmad97/setting-up-a-virtual-environment-and-requirements-txt-file-for-your-data-science-project-f5e0b33a4a92>

Resources used to write the codes can be located in comment blocks at the beginning
of files.