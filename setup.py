from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    install_requires=[
        "anyio==3.5.0; python_full_version >= '3.6.2'",
        "fastapi==0.75.0",
        "greenlet==2.0.0a1; python_version >= '3' and platform_machine == 'aarch64' or (platform_machine == 'ppc64le' or (platform_machine == 'x86_64' or (platform_machine == 'amd64' or (platform_machine == 'AMD64' or (platform_machine == 'win32' or platform_machine == 'WIN32')))))",
        "idna==3.3; python_version >= '3.5'",
        "loguru==0.6.0",
        "psycopg2-binary==2.9.3",
        "pydantic==1.9.0; python_full_version >= '3.6.1'",
        "sniffio==1.2.0; python_version >= '3.5'",
        "sqlalchemy==1.4.32; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
        "sqlalchemy2-stubs==0.0.2a21; python_version >= '3.6'",
        "sqlmodel==0.0.6",
        "starlette==0.17.1; python_version >= '3.6'",
        "typing-extensions==4.1.1; python_version >= '3.6'",
    ],
    name="commonlib",
    version="0.1.0",
    author="Luciano Perezzini",
    author_email="lperezzini@dcc.fceia.unr.edu.ar",
    description="Common utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/perezzini/da_common",
    packages=["commonlib"],
    python_requires=">=3.9",
    dependency_links=[],
)
