# setuptools-cmd-deps

![Continuous Integration](https://github.com/jameslan/setuptools-cmd-deps/workflows/Continuous%20Integration/badge.svg)
![pypi](https://img.shields.io/pypi/v/setuptools-cmd-deps)

Configure `setuptools` command dependencies easily.

## Why I need this plugin
Once a custom `setuptools` command is defined and needs to be run before some build-in command,
traditionally, there's no simple way and the solution is to override the build-in command,
to call the new custom command before the command implemented in the super class.

In this way, having an additional class and digging into `setuptools`,
are just to configure the command order or dependency.

This could be simplified by using `setuptools-cmd-deps`:
enable the plugin and add custom configuration.

## Command dependency in the project

If your command is just for the project and it won't be reused,
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

If you are developing a `setuptools` plugin,
and want the command definition to be used by other project and run before some command,
specify the dependency in the `setuptools.cmd_deps` section in your `entry_points`.

### Enable setuptools-cmd-deps for the target

Add `setuptools-cmd-deps` in the `install_requires` option of your `setuptools`,
so that any project uses your package, will automatically uses `setuptools-cmd-deps`.

### Define dependency

Generally speaking, you already have `distutils.commands` in your `entry_points`.

For example, you defined `gernate_py` command in the `entry_points` as follows,

```
distutils.commands =
    generate_py = command:GeneratePy
```

and want it always run before `build_py`.
Simply add `setuptools.cmd_deps` in the `entry_points` as follows,

```
setuptools.cmd_deps =
    build_py_dep = build_py:generate_py
```

Note that the name `build_py_dep` is not used here.
It is just for the TOML syntax.
For the same reason, if there are multiple dependencies for one command,
it should use dot `.` as delimiter,

```
setuptools.cmd_deps =
    command_dep = command:cmd1.cmd2
```

Both `cmd1` and `cmd2` will be run before `command`.

Or you can have multiple rules,

```
setuptools.cmd_deps =
    command_dep1 = command:cmd1
    command_dep2 = command:cmd2
```
