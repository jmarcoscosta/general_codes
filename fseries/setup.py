from distutils.core import setup

setup(
     name='fseries',    # This is the name of your PyPI-package.
     scripts=['fseries'],                  # The name of your scipt, and also the command you'll be using for calling it
     version='0.1.5',                          # Update the version number for new releases
     author= 'Joao Marcos Costa',
     author_email='jmcosta944@gmail.com',
     keywords='fourier series calculus science engineering math',
     install_requires=['numpy','scipy'],
     url = 'https://github.com/jmarcoscosta/general_codes/tree/master/fseries',
     download_url= 'https://github.com/jmarcoscosta/general_codes/blob/master/fseries/dist/python-fourier-series-calculator-0.1.4.tar.gz',
     classifiers = [],
)
