# Package Management Using PIP

1. What is PIP?
   - Package Installer for Python
   - For more details on PIP please refer below links
     - [PIP - Python Software Foundation](https://pypi.org/project/pip/)

2. Following are the basic commands used in PIP
   - **pip install -U pip**: Updates pip itself to the latest version.
   - **pip list**: Show all packages installed, with version.
   - **pip list -o**: Show installed packages that are not the newest version available.
   - **pip install <*package_name*>**: This will install a specific package
   - **pip install <*package_name*>*****==version_number***: This will install a specific package and its version
   - **pip freeze > requirements.txt**: It save the list of packages with versions to a requirements.txt file.
   - **pip install -r requirements.txt**: Install all packages in your requirements.txt file.
   - **pip install -U <*package_name*>**: Updates an installed package to the latest version.
   - **pip search <*package_name*>**: To search specific package name
   - **pip show<*package_name*>**: Displays the details of the specific package
   - **pip<*pip_version*>**: To use latest PIP version. (Ex: PIP install wheel)
