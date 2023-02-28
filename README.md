# Preliminaries: Python & VS Code

## Install Python

### Windows / macOS

Download from python.org and install it locally. Make sure you add the python 
executable (and other imporant executables, like pip) to the system path, by 
checking the appropriate box located right in the installation main dialog.

You can now access the Python interpreter by typing `python` at the terminal.

If you're using the WSL, then you'll probably want to install it as you would 
in a Ubuntu based Linux distro. And if you're using the WSL, you're probably
savy enough to know what to do. In this case, the python 

You can now access the Python interpreter by typing `python3` at the terminal.

### macOS

Proceed as in Windows. Or, if you installed Homebrew, install Python from 
there with:

    $ brew install python@3.10   # or whichever version is the one you want

You can now access the Python interpreter by typing `python3` at the terminal.

### Linux

On Linux, you probably shouldn't use the system wide python. Search for 
instructions for your distribution (though the following might work: 
[Install Latest Python on Linux Mint 21](https://linuxhint.com/install-latest-python-on-linux-mint-21 "Install Python on Mint 21") ).

On a Ubuntu based distro, usually you add the dead snakes PPA repository to 
APT and then do:

    $ [sudo] apt update
    $ [sudo] apt install python3.10   # or whichever version is the one you want
    OR
    $ [sudo] apt install python3.10-full   # to install all libraries in the
                                           # the standard library

You can now access the Python interpreter by typing `python3` at the terminal.

## Install VS Code

Just follow the instructions given by Microsoft. On macOS, you may as well
install VS Code via a package manager like Homebrew. If you're using a Ubuntu based Linux, 
usually you obtain a `.deb` file and then install it `dpkg -i`.

After installing VS Code, then install the standard Python extensions from 
inside VS Code.

Get yourself aquainted with VS Code by going through the Walkthroughs that you
find on the "Get Started" page (displayed when you first start VS 
Code). Read the tutorials on the VS Code main site. Among other topics, 
learn about:

- Common menu options
- Creating and using Workspaces
- Icons on the left bar
- Extensions
- Common shortcuts like Shift+Ctrl+P, Ctrl+P, Ctrl+B, etc.

**NOTE**: Use Cmd instead of Ctrl on macOS.

# Configure Worspace in VS Code

Create a workspace inside VS Code and make sure the folder where you saved 
the '.code-workspace' file is added to the workspace. A best practice is
to store the file in a `.vscode` folder, and the add the parent folder 
to the workspace (this will be the project root `/` folder).

## Create project layout directories

Under the project's root directory, create the following directories:

    client      : all client-side front-end code (html, css, js)
    server      : all server-side back-end code (python)

## Create a virtual environment for Python

Open a command line (or the VS Code integrated terminal). On Unix, under the 
root folder, issue the following command:

    $ python3 -m venv .venv

This will create a virtual environment for Python inside the `.venv` directory.
VS Code will automatically detect this directory and will use the python 
interpreter inside that directory. 

If you want the `.venv` directory to be installed under `/server`, then 
issue instead:

    $ python3 -m venv ./server/.venv

**NOTE 1**: On Windows use `python` instead of `python3`. Alternatively, you 
may want to use `$ py -3 -m venv .venv` (or `$ py -3 -m venv .\server\.venv).

** NOTE 2**: Please read 
[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

## Activating the Virtual Environment.

Whenever you open the terminal, you need to activate it with:

    $ source .venv/bin/activate

In Windows do:

    C:\> .venv\Scripts\activate.bat      -> cmd
    C:\> .venv\Scripts\Activate.ps1j      -> PowerShell

When a virtual environment is activated, you then access Python with `python`
**both** in Unix and in Windows. The same applies to commands like `pip` (use 
`pip` instead of `pip3`).

# Install FastAPI and dependencies

First, open a terminal and activate the virtual environment.

## Standard dependencies

    pip install fastapi
    pip install "uvicorn[standard]"   # asynchronous web server (implements ASGI)
    pip install jinja2 python-multipart sqlalchemy sqlmodel

## Extra dependencies

    pip install ptpython
    pip install docopt

To be defined.
