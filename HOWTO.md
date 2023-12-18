# How to maintain the ZTK versions page

The [ZTK version configuration page](./README.md) and the linked
version and requirements files are built from a special branch of
the [ZTK GitHub repository](https://github.com/zopefoundation/zopetoolkit).

```bash
  $ git clone -b gh-pages git@github.com:zopefoundation/zopetoolkit
  $ cd zopetoolkit
  $ ./build_indexes.sh
  $ git add README.md releases/
  $ git commit -m "Add new ZTK releases."
  $ git push origin gh-pages
```

The end result is available at https://zopefoundation.github.io/zopetoolkit/.

