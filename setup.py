from distutils.core import setup
setup(
  name = 'topsis_101703129',         
  packages = ['topsis_101703129'],   
  version = '0.7',
  license='MIT',
  description = 'This package allows you to implement topsis approach in python',
  author = 'Ayush Garg',                  
  author_email = '987ayush@gmail.com',      
  url = 'https://github.com/ayush7garg/topsis_101703129', 
  download_url = 'https://github.com/ayush7garg/topsis_101703129/archive/v_01.tar.gz',  
  keywords = ['TOPSIS'],   
  install_requires=[
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)