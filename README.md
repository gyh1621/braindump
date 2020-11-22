[![Netlify Status](https://api.netlify.com/api/v1/badges/e24f724b-59b4-4530-bd35-cd1817f38122/deploy-status)](https://app.netlify.com/sites/gyh-braindump/deploys)

# Braindump

Host org notes online.

## Requirements

- Emacs
- [Ninja](https://ninja-build.org/ "Ninja")
- [ox-hugo][ox-hugo] (waitting for it to be merged)
- [cortex][cortex] (modified from [original one][cortex-origin])

Ninja spawns many Emacs instances in batch mode
running `ox-hugo`, parallelizing the job of exporting the Org files.

## Convert Org to Markdown

`build.py` will convert all Org files in the same level `org` dir into Markdown.
During this process, file content will change (remain same file modification time, for ninja cache),
so it's better to just copy Org dir here.

```
# steps of build.py
1. find org files
2. ignore excluded files
3. convert timestamp content in files to a tag (e.g. "Time-stamp <2020-01-01 01:00:00 user>" -> "- last modified :: 2020-01-01 01:00:00")
4. write file list into build.ninja
4. call ninja
```

To convert all Org files into Markdown, run:

```bash
python3 ./build.py
```

### Exclude / Include List
Create files `excludelist` or `includelist`
and put patterns into them, one per line.
`build.py` will use relative file paths to match the patterns (e.g. org/test.org).

## Hugo Part

Once the Markdown files are generated, we can use Hugo to generate the website.

Install [hugo][hugo]. E.g., on a Mac with Homebrew:

    $ brew install hugo

Make sure the submodule containing the Hugo theme is installed:

    $ git submodule init
    $ git submodule update

Now run hugo to generate the files (find them in `/public`):

    $ hugo

Or run the following to get an immediately browsable website on localhost:

    $ hugo serve

[hugo]: https://gohugo.io/
[ox-hugo]: https://github.com/jethrokuan/ox-hugo/tree/feat/org-hugo-base-dir
[cortex]: https://github.com/gyh1621/cortex
[cortex-origin]: https://github.com/jethrokuan/cortex
[org]: https://github.com/jethrokuan/braindump/tree/master/org
