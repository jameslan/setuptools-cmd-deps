from setuptools import setup


setup(
    name='fixture_custom_cmd',
    py_modules=['cmd_dep_fixture_custom_cmd'],
    entry_points={
        'distutils.commands': [
            'fixture_custom_cmd = cmd_dep_fixture_custom_cmd:custom_cmd',
        ],
        'setuptools.cmd_deps': [
            'build_py = build_py:fixture_custom_cmd',
        ]
    },
)
