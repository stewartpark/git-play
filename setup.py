from distutils.core import setup

setup(
    name="git-play",
    version="0.1dev",
    author="Ju-yeong Park",
    author_email="interruptz@gmail.com",
    scripts=["bin/git-play"],
    url="http://interruptz.github.com/git-play",
    license="LICENSE",
    description="Git-play is a command line tool for deploying an application server easily from remote git repository.",
    long_description = open("README").read(),
    install_requires=[
        'PyYAML==3.10',
        'GitPython==0.3.2.RC1'      
    ]
)
