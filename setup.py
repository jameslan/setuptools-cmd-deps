from setuptools import setup


def main():
    setup(
        name='setuptools-cmd-deps',
        version='0.1.0',
        description='setuptools plugin to configure the dependency among commands',
        long_description=open('README.md').read(),
        url='https://github.com/jameslan/setuptools-cmd-deps',
        python_requires='>=3.5',
        py_modules=['setuptools_cmd_deps'],
    )


if __name__ == '__main__':
    main()
