from setuptools import find_packages, setup

setup(
    name="testypie",
    use_scm_version={
        "local_scheme": "dirty-tag",
        "write_to": "testypie/_version.py",
        "fallback_version": "0.0.0",
    },
    author="Ross Fenning",
    author_email="github@rossfenning.co.uk",
    packages=find_packages("testypie"),
    url="https://github.com/avengerpenguin/testypie",
    description="HTTP proxy that generates and loads from fixtures for testing.",
    license="GPLv3+",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    install_requires=["Flask", "requests", "httplib2", "PyYAML", "clize",],
    setup_requires=["pytest-runner", "setuptools_scm>=3.3.1", "twine"],
    entry_points={"console_scripts": ["testypie = testypie:cli",],},
)
