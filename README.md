# ermahgerd

Structured-text-to-ER-model-diagram generator, inspired by [BurntSushi/erd](TK). Model details are specified in a simple [YAML](https://yaml.org) format, and output as SVG. Where `erd` and similar tools tend to use quite terse specification file formats, the design of `ermahgerd` favors spelling out model details somewhat more explicitly -- hopefully without introducing too much verbosity. It also prefers YAML over a non-standard text format specific to the tool.

See `example.erd.yml` for a sample of the format.

To install, clone this repository, then:

```sh
$ cd ermahgerd
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install .
```

This will install the console script `ermahgerd` in a virtual environment. Pass this command the name of your YAML file, for example:

```sh
$ ermahgerd example.erd.yml
```

Output diagram written to `ermahgerd_output.svg` in your working directory
