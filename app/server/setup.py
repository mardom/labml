import setuptools

with open("../readme.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='labml_app',
    version='0.0.0',
    author="Varuna Jayasiri, Nipun, Aditya",
    author_email="vpjayasiri@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lab-ml/app",
    project_urls={
        'Documentation': 'https://lab-ml.com/'
    },
    install_requires=['labml>=0.4.87',
                      'gunicorn',
                      'numpy',
                      'labml-db',
                      'fastapi',
                      'uvicorn',
                      'aiofiles',
                      ],
    packages=['labml_app'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='machine learning',
)