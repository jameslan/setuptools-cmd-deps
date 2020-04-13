from setuptools import setup, Command


class CmdA(Command):
    user_options = ['a']

    def initialize_options(self):
        print('initialize cmdA')

    def finalize_options(self):
        print('finalize cmdA')

    def run(self):
        print('In cmdA')


def main():
    setup(
        name='setuptools-cmd-deps',
        version='0.0.1',
        description='setuptools plugin to configure the dependency among commands',
        long_description=open('README.md').read(),
        url='https://github.com/jameslan/setuptools-cmd-deps',
        python_requires='>=3.5',
        py_modules=['setuptools_cmd_deps'],
        cmdclass={
            'prebuild': CmdA,
        },
        cmd_deps={
            'build_py': ['prebuild'],
            'build': ['prebuild'],
        },
    )


if __name__ == '__main__':
    main()
