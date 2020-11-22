[![Netlify Status](https://api.netlify.com/api/v1/badges/e24f724b-59b4-4530-bd35-cd1817f38122/deploy-status)](https://app.netlify.com/sites/gyh-braindump/deploys)

# Braindump

This braindump is generated via [ox-hugo][ox-hugo] and uses the
[cortex][cortex] theme.

The org files used to generate the markdown files are also hosted here
for posterity. They can be found in [the org folder][org].

## Installation instructions

I use the [Ninja](https://ninja-build.org/ "Ninja") build tool to convert my Org
files into Markdown locally. This is so that only changed Org files get
reprocessed into Markdown files. Ninja spawns many Emacs instances in batch mode
running `ox-hugo`, parallelizing the job of exporting the Org files.

To convert all Org files into Markdown, run:

```bash
python3 ./build.py
```

`build.py` will convert all Org files in the same level `org` dir into Markdown.
During this process, file content will change (remain same file modification time, for ninja cache),
so it's better to just copy Org dir here:
```
# steps of build.py
1. ignore some files
2. convert timestamp content in filtered files to a tag (e.g. "Time-stamp <2020-01-01 01:00:00 user>" -> - last modified :: 2020-01-01 01:00:00)
3. write file list into build.ninja
4. call ninja
```

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
[ox-hugo]: https://github.com/kaushalmodi/ox-hugo
[cortex]: https://github.com/jethrokuan/cortex
[org]: https://github.com/jethrokuan/braindump/tree/master/org
