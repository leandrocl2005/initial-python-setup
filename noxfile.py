# coding=utf-8

"""Nox configuration File."""


import nox


@nox.session(python="3.8")
def tests(session):
    """Test's Session."""
    session.install('pytest', 'pytest-cov')
    session.run('pytest', '--cov', 'src')


# noxfile.py
@nox.session(python="3.8")
def lint(session):
    """Lint's Session."""
    session.install(
        "flake8",
        "flake8-docstrings"
    )
    session.run('flake8', 'src', 'noxfile.py')


@nox.session(python="3.8")
def mypy(session):
    """Typing Session."""
    session.install("mypy")
    session.run("mypy", 'src', 'noxfile.py')
