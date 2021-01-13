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
Where `[dir]` is the directory to recursively fix. Right after unarchiving your takeout you can use `"Takeout/Google Photos"` for example.

## Why this matters

### ExifTool

The awesome [ExifTool](https://exiftool.org) project can be used to automatically import the json data as exif data into the relevant media files, but only if the json and media files are named perfectly consistently.

For sake of interest, here is the command that does the exif fix:

```sh
exiftool -r -d %s -tagsfromfile "%d/%F.json" "-GPSAltitude<GeoDataAltitude" "-GPSLatitude<GeoDataLatitude" "-GPSLatitudeRef<GeoDataLatitude" "-GPSLongitude<GeoDataLongitude" "-GPSLongitudeRef<GeoDataLongitude" "-Keywords<Tags" "-Subject<Tags" "-Caption-Abstract<Description" "-ImageDescription<Description" "-DateTimeOriginal<PhotoTakenTimeTimestamp" -ext '*' -overwrite_original --ext json [dir]
```

The `%d/%F.json` part specifies that the companion json files will be named exactly the same as the related media files (with a lowercase extension) and `.json` appended to the end.

### Chevereto

[Chevereto](https://chevereto.com/) is an open-source photo hosting app that has native support for [importing Google Photos Takeout](https://v3-docs.chevereto.com/features/bulk-content-importer.html#importing-from-google-photos) images and parsing the related json files, but obviously only if they are named consistently.

## Posterity

Because Google often changes its API's on a whim, I fully expect this script and the related `exiftool` command not to work at some point in the future. But as of January 2021 it works, so Takeout your photos and use it while you can!

