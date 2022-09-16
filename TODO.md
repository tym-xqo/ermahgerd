# TODO

- [x] organize into project and name files appropriately
- [ ] `setup.py` with console script
- [x]`argparse` for input file
- [ ] document yaml format and usage
- [x] add `pygraphviz` and generate svg ~~(maybe other formats?)~~ from script
- [ ] reverse engineer from DDL to YAML
- [ ] forward engineer DDL from YAML
- [ ] unit tests
- [ ] browser app: paste yaml in one pane, get diagram in other pane
- [ ] handle PKs that are also FKs
- [ ] incorporate rank adjustments
- [ ] figure out why gaps in splines in svg output (maybe a graphviz bug? seems related to multiple arrow shapes on ortho splines specifically, but that' all I know)
- [ ] allow output as raw `dot` file, and maybe png or others in addition to svg
