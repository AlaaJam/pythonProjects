import pathlib
import setuptools

setuptools.setup(
    name="DataPrepKit",
    version="0.1.0",
    description="Brief description",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://DataPrepKit.xyz",
    author="Alaa Abdelqader",
    author_email="alaanadaja7@gmail.com",
    license="The Unlicense",
    project_urls={
        "Documentation": "https://DataPrepKit.xyz/docs",
        "Source": "https://github.com/AlaaJam/pythonProjects.git",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
    python_requires=">=3.10, <3.12",
    install_requires=["requests", "pandas >=2.0","numpy","scikit-learn"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={"console_scripts":["DataPrepKit = DataPrepKit.cli:main"]},
)
