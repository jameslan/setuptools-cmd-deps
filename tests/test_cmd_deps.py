from subprocess import check_output
from os.path import dirname


project_dir = dirname(dirname(__file__))


def run_setup(code, command):
    # run in project dir so that the entry_points settings
    # in setup.cfg could take effect
    return check_output(
        ['python', '-c', code, command],
        cwd=project_dir,
    ).decode()


def test_implicit_dep():
    out = run_setup('__import__("setuptools").setup()', 'build_py')
    assert 'running decl_cmd1' in out
    assert 'running decl_cmd2' in out
    assert 'running fixture_custom_cmd' in out


def test_setup_keyword():
    out = run_setup(
        '__import__("setuptools").setup(cmd_deps={"alias":["build_py"]})',
        'alias',
    )
    assert 'running build_py' in out
    assert 'running decl_cmd1' in out
    assert 'running decl_cmd2' in out
    assert 'running fixture_custom_cmd' in out
