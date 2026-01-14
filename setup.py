"""
Modified 2026-01-14 for charge_learning package integration
Changes:
- Hardcoded version to '0.2.0+19.gfa5b8b0' (commented out versioneer.get_version())
- Added python_requires='<3.14'
Original source: https://github.com/ICAMS/TensorPotential
"""
from setuptools import setup

import versioneer


setup(
    name='tensorpotential',
    #version=versioneer.get_version(),
    version='0.2.0+19.gfa5b8b0',
    cmdclass=versioneer.get_cmdclass(),
    packages=['tensorpotential', 'tensorpotential.utils', 'tensorpotential.potentials', 'tensorpotential.functions'],
    package_dir={'': 'src'},
    url='',
    license='',
    author='Anton Bochkarev',
    author_email='',
    description='',
    python_requires='<3.14',
    install_requires=
    [
    'scipy',
    'tensorflow>=2.20.0',
    'numpy>=2.1.0',
    'pandas>=2.3.0',
    'ase'
    ]
)

