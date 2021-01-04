from setuptools import setup

package_name = 'smach_napp'

setup(
    name=package_name,
    version='0.8.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Chih-Chieh.Chang',
    maintainer_email='chih-chieh.chang@adlinktech.com',
    description='This is a Neuron App of FSM based on SMACH',
    license='BSD',
    entry_points={
        'console_scripts': [
            'smach_nav2_client = smach_napp.smach_nav2_client:main'
        ],
    },
)
