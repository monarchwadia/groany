from setuptools import setup

setup(
    name='groany',
    version='1.0.0',
    author='Monarch Wadia',
    author_email='monarchwadia@gmail.com',
    description='Dad jokes in your terminal.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/judoscale/python-assignment-monarch',
    entry_points={
        'console_scripts': [
            'groany = groany.scripts.cli:exec',
        ],
    },
    install_requires=[
      "requests"
    ],
    python_requires='>=3.9',
    extras_require={
      'dev': [
          "pytest==7.2.0",
          "mock==4.0.3",
          'pyright==1.1.281',
          "pypandoc==1.10",
          "build"
      ]
    }
)