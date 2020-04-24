from setuptools import setup


def main():
    setup(
        name='setuptools-cmd-deps',
        long_description=open('README.md').read(),
        url='https://github.com/jameslan/setuptools-cmd-deps',
        py_modules=['setuptools_cmd_deps'],
        setup_requires=['setuptools_scm'],
        use_scm_version=True,
    )


if __name__ == '__main__':
    main()
