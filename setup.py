from setuptools import setup

setup(
    name='groany',
    version='0.0.3',
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
      "requests==2.28.1",
      'importlib-metadata; python_version == "3.11"',
    ],
    extras_require={
      'dev': [
          "pytest==7.2.0",
          "mock==4.0.3",
          'pyright==1.1.281',
          "pypandoc==1.10",
      ]
    },
    python_requires='>=3.11',
)