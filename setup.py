from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    description="Math_quiz",
    author="Selina Werner",
    author_email="aniles162@gmail,com",
    url="https://github.com/aniles162/dsss_homework_2.git",
    packages=find_packages(include=['math_quiz', 'math_quiz.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
