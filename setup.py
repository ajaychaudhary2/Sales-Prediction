from setuptools import setup, find_packages

setup(
    name="sales-prediction-app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "pandas",
        "scikit-learn",
    ],
    entry_points={
        "console_scripts": [
            "train-model=train_model:train_and_save_model"
        ]
    },
    author="Your Name",
    description="A simple sales prediction web app using Flask and ML",
)
