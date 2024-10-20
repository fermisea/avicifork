from setuptools import setup, find_packages

setup(
    name="avici",
    version="1.0.5",
    description="Amortized Inference for Causal Structure Learning",
    author="Lars Lorch",
    author_email="lars.lorch@inf.ethz.ch",
    url="https://github.com/larslorch/avici",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10.0",
    packages=find_packages(),
    package_data={
        "avici": [
            "assets/*.tsv",
            "config/examples/*.yaml",
            "config/train/*.yaml",
            "synthetic/sergio/*.yaml",
        ],
    },
    install_requires=[
        "jax==0.4.34",
        "jaxlib==0.4.34",
        "tensorflow",
        "imageio",
        "matplotlib",
        "numpy",
        "pandas",
        "igraph",
        "scikit-learn",
        "tqdm",
        "dm-haiku>=0.0.8",
        "psutil",
        "optax",
        "pyarrow",
        "tensorflow-datasets~=4.3.0",
        "deepdiff",
        "huggingface-hub",
    ],
)
