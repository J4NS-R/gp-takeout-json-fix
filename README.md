# Google Photos Takeout Pre-Exif Organiser

As we all know Google Photos is utterly pathetic when it comes to Taking out media files.

After you've untarred/unzipped your takeout archives, the following issues are present:

- All media files have incorrect or absent Exif data (this data is in related `.json` files).
- Some media files have no companion json files.
- Media files with long names have cut-off companion json file names, e.g.:
```
Photo:      IMG_123456790.jpg
Companion:  IMG_123456790.j.json
```
- Some `jpg` files and companion files have the `jpeg` extension, e.g.:
```
Photo:      IMG_1234.jpg
Companion:  IMG_1234.jpeg.json
```
- Some media files and companion files have inconsistent extension casing, e.g.:
```
Photo:      IMG_1234.jpg
Companion:  IMG_1234.JPG.json
```

## How to fix this

```sh
python3 fixgptakeout.py [dir]
```
Where `[dir]` is the directory to recursively fix. Right after unarchiving your takeout you can use `"Takeout/Google Photos"`i for example.

## Why this matters

The naming of the companion json files is important because the awesome [ExifTool](https://exiftool.org) project can be used to automatically import the json data as exif data into the relevant media files, but only if the json and media files are named perfectly consistently.

