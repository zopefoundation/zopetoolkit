from setuptools import setup


version = '3.0.dev0'

with open('README.rst') as f:
    README = f.read()

setup(
    name='zopetoolkit',
    version=version,
    description='Set of libraries maintained by the Zope project.',
    author='Zope team',
    author_email='zope-dev@zope.dev',
    license='ZPL',
    long_description_content_type='text/x-rst',
    long_description=README,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
    python_requires='>=3.8',
    install_requires=[],
    entry_points={},
    packages=[],
)
