from setuptools import setup

setup(
    name='groany',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'groany = groany.scripts.cli:exec',
        ],
    },
    install_requires=[
      "requests==2.28.1",
      'importlib-metadata; python_version == "3.8"',
    ],
    extras_require={
      'dev': [
          "pytest==7.2.0",
          "mock==4.0.3",
          'pyright==1.1.281'
      ]
    }
)