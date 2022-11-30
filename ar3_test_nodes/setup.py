from glob import glob

from setuptools import setup

package_name = "ar3_test_nodes"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name, glob("launch/*.launch.py")),
        ("share/" + package_name + "/configs", glob("configs/*.*")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    author="Emanuel Buholzer",
    author_email="emanuel0xb@gmail.com",
    maintainer="Emanuel Buholzer",
    maintainer_email="emanuel0xb@gmail.com",
    keywords=["ROS"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    description="Getting the ar3 to move",
    long_description="""Getting the ar3 to move""",
    license="Apache License, Version 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "publisher_joint_trajectory_controller = \
                ar3_test_nodes.publisher_joint_trajectory_controller:main",
        ],
    },
)
