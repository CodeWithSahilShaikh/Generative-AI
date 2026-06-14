# Python Environment & Package Commands

### 1. Check Active Python
Find out which Python your terminal is currently using:
```bash
python -c "import sys; print(sys.executable)"
# OR (Windows)
where python
```

### 2. Check Active PIP
Verify exactly where PIP will install packages:
```bash
python -m pip -V
```

### 3. Check if Package is Installed
See if a package exists in the current environment (and its location):
```bash
python -m pip show <package_name> 
```

### 4. Safest Way to Install Packages
Ensure packages are installed into your *active* environment (not globally):
```bash
python -m pip install <package_name>
```
