from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='simplebmi',
    version='1.0.1',
    description='A very basic BMI calculator',
    Long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Praveen Yadav',
    author_email='praveen885127@gmail.com',
    License='MIT',
    classifiers=classifiers,
    keywords='BMI',
    packages=find_packages(),
    install_requires=['']
)