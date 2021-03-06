import os
import setuptools


install_requirements = [
    "future",
    "h5py",
    "keras==2.2.0",
    "numpy",
    "pillow",
    "pytest",
    "scipy",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest"
]


def readme():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base_dir, 'README.md')) as f:
        return f.read()


def setup():
    setuptools.setup(
        name="innvestigate",
        version="1.0.2",
        description=("A toolbox to innvestigate neural networks decisions."),
        long_description=readme(),
        classifiers=[
            "License :: OSI Approved :: ",
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Science/Research",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
        url="https://github.com/albermax/innvestigate",
        author="Maxmilian Alber, Sebastian Lapuschkin, Miriam Haegele, Kristof Schuett, Philipp Seegerer, Pieter-Jan Kindermans",
        author_email="workDoTalberDoTmaximilian@gmail.com",
        license="MIT",
        packages=setuptools.find_packages(),
        install_requires=install_requirements,
        setup_requires=setup_requirements,
        tests_require=test_requirements,
        include_package_data=True,
        zip_safe=False,
    )
    pass


if __name__ == "__main__":
    setup()
