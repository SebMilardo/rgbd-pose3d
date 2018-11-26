import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rgbdpose3d",
    version="0.0.1",
    author="Sebastiano Milardo",
    author_email="milardo@mit.edu",
    description="3D Human Pose Estimation in RGBD Images for Robotic Task Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SebMilardo/rgbd-pose3d",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)