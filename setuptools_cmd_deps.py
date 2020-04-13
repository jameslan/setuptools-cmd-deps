from pkg_resources import iter_entry_points


def gen_proxy(cmd_class, deps):
    def run(self):
        for dep in deps:
            self.run_command(dep)
        cmd_class.run(self)

    return type('Proxy_' + cmd_class.__name__, (cmd_class, ), {'run': run})


def setup_proxies(dist, dep_spec):
    for cmd, deps in dep_spec.items():
        cmd_class = dist.get_command_class(cmd)

        dist.cmdclass[cmd] = gen_proxy(cmd_class, deps)


def collect_deps(dep_spec):
    for spec in iter_entry_points('setuptools.cmd_deps'):
        dep_spec.setdefault(spec.module_name, []).extend(spec.attrs)
    return dep_spec


def cmd_deps(dist, keyword, value):
    pass


def finalize_cmd_deps(dist):
    setup_proxies(dist, collect_deps(getattr(dist, 'cmd_deps') or {}))
