# Virtual environments (venv) and requirements.txt

## 1. What it is and why you need it
A virtual environment is a folder with its own Python and its own installed packages,
separate from the Python of your system. Each project gets its own, so the packages of
one project never clash with the ones of another.

## 2. Create, activate and deactivate (Git Bash on Windows)
    python -m venv .venv              # creates the environment 
    source .venv/Scripts/activate     # activates it: "(.venv)" appears in the prompt
    deactivate                        # leaves it

Other terminals use another activation command (cmd: `.venv\Scripts\activate.bat`,
PowerShell: `.venv\Scripts\Activate.ps1`).

## 3. Check which Python you are using
    which python                      # must end in .venv/Scripts/python
    python -m pip --version           # the path must be inside .venv
If either path points outside .venv, the environment is not active.

## 4. Installing packages with pip
Always call pip as `python -m pip`, so it is the pip of the active Python.

    python -m pip list                # packages installed right now
    python -m pip install requests    # installs a package 
    python -m pip show requests       # version, location and what it needs
    python -m pip uninstall requests  # removes it
    python -m pip install package==1.2.3   # a specific version

A new environment only has pip. Install requests again after uninstalling it

## 5. requirements.txt: the list of what the project needs
    python -m pip freeze > requirements.txt

`freeze` lists every installed package with its exact version, including the packages
that your packages need. That is why it has more lines than the ones you installed.
To install everything from that file:

    python -m pip install -r requirements.txt

Rules:
- Commit `requirements.txt`. Never commit `.venv/`.
- Run `freeze` again every time you install or remove a package.

## 6. The real test: rebuild the project from scratch
It proves that someone who clones your repository can run your code.
Run it from `python/`, with the test environment outside the repository:

    python -m venv ~/venv_test
    source ~/venv_test/Scripts/activate
    python -m pip list                              # almost empty
    python -m pip install -r requirements.txt       # rebuilds everything
    python -m pip list                              # now it matches your project
    python -c "import requests; print(requests.__version__)"
    deactivate
    source .venv/Scripts/activate                   # back to your project
    rm -r ~/venv_test                               # removes the test environment

## 7. Mistakes to avoid
- Installing packages with the environment off: they go to the system Python.
  Check the "(.venv)" in the prompt first.
- Installing a package and forgetting to update requirements.txt.
- Committing `.venv/`.
- Moving or renaming the project folder: an environment keeps absolute paths inside,
  so it breaks. Delete it and create it again, then run `pip install -r requirements.txt`.
- Using `pip` instead of `python -m pip`: it can belong to a different Python.