from distutils.core import setup

files = ['decapp2.py','decrypy.py','decgui2.py','decgui2.ui','README','setup.py']

setup(name = "decrypy",
    version = "2.0",
    description = "A tool to decrypt Yahoo chat archives",
    author = "Akhil Wali",
    author_email = "green.transistor@gmail.com",
    url = "http://code.google.com/p/decrypy/",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['.'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'.' : files }    
    )

