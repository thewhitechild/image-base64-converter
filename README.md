## Converting an image to base64

```
py imagetobase64.py your-picture.jpg
```

## Converting a base64 text file to an image

The file format of the image generated is JPEG.

```
py base64toimage.py your-base64-file.txt
```

### To specify the file format
Simply include the file extension as part of the script arguments, as demonstrated in the example below.

```
py base64toimage.py your-base64-file.txt png
```