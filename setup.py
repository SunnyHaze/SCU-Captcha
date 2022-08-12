import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
data_files= ["scu_captcha/model.pt",
             "scu_captcha/preData.pt"
]

setuptools.setup(
    name="scu_captcha",
    version="0.0.5",
    author="Sunnyhaze",
    author_email="mxch1122@126.com",
    keywords=["pip", "scu-captcha"],
    description="SCU captcha recongnition based on Pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    url="https://github.com/SunnyHaze/SCU-Captcha",
    project_urls={
        "Authors's Github": "https://github.com/SunnyHaze",
        "Repo" : "https://github.com/SunnyHaze/SCU-Captcha",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=["requests", "pillow"],
    data_files=data_files,
    include_package_data=True,
    py_modules=["scu_captcha"],
)