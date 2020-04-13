from setuptools import setup


def main():
    setup(
        name='setuptools-cmd-deps',
        version='0.1.0',
        long_description=open('README.md').read(),
        url='https://github.com/jameslan/setuptools-cmd-deps',
        py_modules=['setuptools_cmd_deps'],
    )


if __name__ == '__main__':
    main()
