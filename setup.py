from setuptools import setup, find_packages

setup(
    name='dsss_homework_2',  
    version='0.1',           
    packages=find_packages(include=['math_quiz', 'math_quiz.py', 'tests_math_quiz.py', '__init__.py']),  
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',  
        ],
    },
    include_package_data=True,  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
