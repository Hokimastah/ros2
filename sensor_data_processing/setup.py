from setuptools import find_packages, setup

package_name = 'sensor_data_processing'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/sensor_data_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='ROS2 project with real-time sensor data processing',
    license='MIT',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'publisher_node = sensor_data_processing.publisher_node:main',
            'subscriber_node = sensor_data_processing.subscriber_node:main',
        ],
    },
)
