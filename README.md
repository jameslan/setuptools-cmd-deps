# setuptools-cmd-deps
Configure `setuptools` command dependencies easily.

Once a custom `setuptools` command is defined and needs to be run before some build-in command,
the solution is to override the build-in command to ensure the new custom command is called.

For example, if a custom command `genreate_py` is implemented in class `GeneratePy`
and needs to be run before `build_py`,
You need to create you own command class `MyBuildPy` and call both `generate_py` and build-in `build_py`.
Then call `setup` as follows,

```python
setuptools.setup(
    cmdclass={
        'generate_py': GenereatePy,
        'build_py': MyBuildPy,
    },
)
```

It can be simplified by using `setuptools-cmd-deps`.

## Command dependency in the project
If the command is just for the project and it won't be shared,
you could use new setup keyword `cmd_deps` to define the dependencies.

### Enable setuptools-cmd-deps
- If your `setup.py` will run only after all depending packages are installed,
add `setuptools-cmd-deps` in your dependency list,
such as `requirements.txt`, or `Pipfile`.

- If your `setup.py` supports running out of venv,
you may not want these packages to be installed in the system.
Then add `setuptools-cmd-deps` in the `setup_requires` option of your `setuptools`.

### Define dependency

```python
setuptools.setup(
    cmdclass={'generate_py': GenereatePy},
    cmd_deps={'build_py': ['generate_py']},
)
```

## Command dependency to be shared
If you want command definition to be used by other project and run before some command,
specify the dependency in the `setuptools.cmd_deps` section in your `entry_points`.

### Enable setuptools-cmd-deps for the target
Add `setuptools-cmd-deps` in the `install_requires` option of your `setuptools`,
so that any project uses your package, will automatically uses `setuptools-cmd-deps`.

### Define dependency
Generally speaking, you already have `distutils.commands` in your `entry_points`.

For example, you defined `gernate_py` command as follows,

```
distutils.commands =
    generate_py = command:GeneratePy
```

and want it always run before `build_py`, then add `setuptools.cmd_deps` as follows,

```
setuptools.cmd_deps =
    build_py_dep = build_py:generate_py
```

Note that the name `build_py_dep` is not used here.
It is just for the syntax.
For the same reason, if there are multiple dependencies for one command,
it should use dot `.` as delimiter,

```
setuptools.cmd_deps =
    command_dep = command:cmd1.cmd2
```

or you can have multiple rules,

```
setuptools.cmd_deps =
    command_dep1 = command:cmd1
    command_dep2 = command:cmd2
```
