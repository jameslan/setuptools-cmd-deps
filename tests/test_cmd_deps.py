from subprocess import check_output
from os.path import dirname


project_dir = dirname(dirname(__file__))


def test_implicit_dep():
    out = check_output(
        ['python', '-c', '__import__("setuptools").setup()', 'build_py'],
        cwd=project_dir,
    ).decode()
    assert 'running decl_cmd1' in out
    assert 'running decl_cmd2' in out
    assert 'running fixture_custom_cmd' in out


def test_setup_keyword():
    out = check_output(
        [
            'python',
            '-c',
            '__import__("setuptools").setup(cmd_deps={"alias":["build_py"]})',
            'alias',
        ],
        cwd=project_dir,
    ).decode()
    assert 'running build_py' in out
    assert 'running decl_cmd1' in out
    assert 'running decl_cmd2' in out
    assert 'running fixture_custom_cmd' in out
