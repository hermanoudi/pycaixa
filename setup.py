from setuptools import find_packages, setup


setup(
    name="mouracx",
    version="0.0.1",
    description="Sistema de Fluxo de Caixa",
    author="Hermano Flávio de Moura",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "moura = mouracx.__main__:main"
        ]
    }
)


