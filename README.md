
# Thumby Fireplace

Example application for creating and loading 2 bit grayscale videos onto a Thumby.

This uses Timendus' grayscale library (https://github.com/Timendus/thumby-grayscale), which is included here.

Note that the Thumby doesn't have a large amount of device storage, so don't expect to be playing a whole movie with this.


## Creating Your Own Grayscale Video

* Install the following:
  * ffpmeg (https://ffmpeg.org/)
  * Python3 (https://www.python.org/)
  * Pillow Python library, also known as PIL (https://pypi.org/project/Pillow/)

The aim of this is to take the video you would like to play on the Thumby, and convert it to the right resolution, drop it to the desired frame rate, and reduce it to 4 color grayscale, while utilising dithering to retain quality, and then finally, converting to a format compatible with the ShadedSprite class from thumbyGrayscale. There are many ways to achieve this, but here we use ffmpeg to do the video transcoding, and an included Python script utilising PIL to convert to the ShadedSprite format.

This is a three step process.

1. Find a video to use, then place it into your clone of this git repository and name it `input.gif` or something similar. You should be able to put any video into this location.
```bash
cp myvideo.gif input.gif
```
2. Transcode the video into a 2 bit grayscale gif with the desired frame rate and resolution. The frame rate should be equal to or lower than the source video. In the following command, update `30` to your desired frame rate, and update the resolution (scale) if you don't want a full screen video. You may also have to update the input video name if you didn't use `input.gif`:
```bash
ffmpeg -i input.gif -i palette.png -lavfi "fps=30,scale=72:40,paletteuse" processed.gif
```
3. We should now have a 2 bit grayscale video (`processed.gif`) in the same folder. This can be viewed in a video player, or by dragging into your browser. The next step is to convert this into a format compatible with the ShadedSprite class. We will be making 2 **bin** files, one with the black and white layer, and one with the grayscale shading. We will use the createShadedSprite.py script to do this. This should leave two files in the same folder: `vid.BIT.bin` and `vid.SHD.bin`):
```bash
python3 createShadedSprite.py
```
