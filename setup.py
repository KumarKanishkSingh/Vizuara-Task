from setuptools import setup, find_packages

setup(
    name='your-app-name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit==0.88.0',
        'scikit-learn==0.24.2',
        'numpy==1.21.2',
        'pandas==1.3.3',
        'matplotlib==3.4.3',
        'torch==1.9.0',
        'streamlit-drawable-canvas==0.4.0',
        'Pillow==8.3.2',
        'scikit-neuralnetwork==0.7',
    ],
)
