from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='jupyter_disqus',
    version='0.1',
    description='Add disqus to your jupyter notebook',
    long_description=readme,
    author='Costa Huang',
    author_email='costa.huang@outlook.com',
    install_requires=['IPython', 'htmlmin==0.1.12'],
    packages=['jupyter_disqus', 'jupyter_disqus.tests'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
    url="https://github.com/vwxyzjn/jupyter_disqus"
)
