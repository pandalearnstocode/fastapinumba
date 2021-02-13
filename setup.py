from setuptools import setup, find_packages

setup(
    name='fastapinumba',
    version='0.0.1',
    url='https://github.com/pandalearnstocode/fastapinumba.git',
    author='Aritra Biswas',
    author_email='pandalearnstocode@gmail.com',
    description='Stress testing concurrency of REST APIs using numeric computing stack',
    packages=find_packages(),    
    install_requires=['numpy', 'numba'],
)