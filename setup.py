from setuptools import setup, find_packages
from src import pysatellite

VERSION = pysatellite.__version__


def file_read(path: str) -> str:
    with open(path, encoding='utf8') as f:
        description = f.read()
        return description


setup(
    name="pysatellite",
    download_url=f'https://github.com/pySatellite/pySatellite.github.io/archive/refs/tags/{VERSION}.zip',
    version=VERSION,
    packages=find_packages(exclude=['docs', '.idea', 'tests']),
    description='simulate satellite tracking',
    long_description=file_read('README.md'),
    long_description_content_type='text/markdown',
    author='pySatellite',
    author_email='pySatellite@gmail.com',
    url='https://pySatellite.github.io',
    project_urls={
        "pySatellite documentation": "https://pySatellite.github.io",
        "pySatellite source": "https://github.com/pySatellite/pySatellite.github.io",
    },
    install_requires=[
        "pyfiglet"
    ],
    keywords=['satellite', 'space', 'challenge', 'Environment'],
    python_requires='>=3.6.10',
    package_data={},
    license="GNU",
    license_file='LICENSE',
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)

