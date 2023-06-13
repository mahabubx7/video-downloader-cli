# video-downloader-cli

A custom python script as a CLI for yt-dlp made easy

### It used `yt-dlp` under the hood.

## Guides

Follow the given instructions to use this script & be happy 🙂

#### Pre-Requirements

- Python (3.7 or later)
- Pip

#### Install dependencies

Now install the one and only dependency as python package

```sh
$ pip install yt-dlp
```

#### How to use

Go to the script folder or grab the `download.py` file location.
Then execute this...

```sh
$ python download.py <your_target_url>
```

> Note: if you are in the same directory while executing this, it's okay. But if you are not then try `python <path_to_download_py_script> <your_target_url>`.

_There are some options_

- `--playlist`: It will help yt-dlp to understand the url is a playlist.
- `--indexing`: It will help to indexing playlist videos by renaming them.
- `--dir=<path>`: You can specify your target location to save.
- `--quality=<resolution_number>`: To get specific resolution videos i.e. 1080

Enjoy 🥳 (@mahabubx7)
