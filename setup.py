from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-16") as f:
    requirements = f.read().splitlines()

setup(
    name='leetcode_daily',
    entry_points={
        'console_scripts': [
            'leetcode-daily = leetcode_daily.main:main',
        ]
    },
    version='1.0.0',
    author='happydave1',
    packages=find_packages(),
    install_requires=requirements,
)