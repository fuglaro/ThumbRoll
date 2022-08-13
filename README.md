
# ThumbRoll

Example application for creating and loading 2 bit grayscale videos onto a Thumby.

This uses Timendus' grayscale library (https://github.com/Timendus/thumby-grayscale), which is aiming to be included in the Thumby standard API. At time of writing, a compatible thumbyGrayscale.py library file can be obtained from the dropInReady branch. This isn't fully supported on the code.thumby.us Code Editor and Emulator, but you can launch your own server with the grayscale fork (https://github.com/fuglaro/TinyCircuits-Thumby-Code-Editor) which we hope to push upstream. Otherwise you can load it direct to your Thumby device, or just use the Fast Execute feature on code.thumby.us.

Note that the Thumby doesn't have a large amount of device storage, so don't expect to be playing a whole movie with this.

## Preparation

* Install the following:
  * ffpmeg (https://ffmpeg.org/)
  * Python3 (https://www.python.org/)
  * Pillow Python library, also known as PIL (https://pypi.org/project/Pillow/)
* Clone or Download this git respository.

## Creating Your Own Grayscale Video

The aim of this is to take the video you would like to play on the Thumby, and convert it to the right resolution, drop it to the desired frame rate, and reduce it to 4 color grayscale, while utilising dithering to retain quality, and then finally, converting to a format compatible with the ShadedSprite class from thumbyGrayscale. There are many ways to achieve this, but here we use ffmpeg to do the video transcoding, and an included Python script utilising PIL to convert to the ShadedSprite format.

This is a three step process.

1. Find a video to use, then place it into your clone of this git repository and name it `input.gif` or something similar. You should be able to put any video into this location.
```bash
cp myvideo.gif input.gif
```
2. Transcode the video into a 2 bit grayscale gif with the desired frame rate and resolution. The frame rate should be equal to or lower than the source video. Update `input.gif` to the name of your source video, and update `30` to your desired frame rate, and update the resolution (scale), if you don't want a full screen video:
```bash
ffmpeg -i input.gif -i palette.png -lavfi "fps=30,scale=72:40,paletteuse" processed.gif
```
3. We should now have a 2 bit grayscale video (`processed.gif`) in the same folder. This can be viewed in a video player, or by dragging into your browser. The next step is to convert this into a format compatible with the ShadedSprite class. We will be making 2 **bin** files, one with the black and white layer, and one with the grayscale shading. We will use the createShadedSprite.py script to do this. This should leave two files in the same folder: `vid.BIT.bin` and `vid.SHD.bin`):
```bash
python3 createShadedSprite.py
```

## Loading Your Grayscale Video to the Thumby

Now that you have your two `bin` files making up a grayscale video with the correct colors and format, you and play it on the Thumby by using the example MicroPython code in `ThumbRoll.py`.

First, if it doesn't already exist, load the thumbyGrayscale library:

* `thumbyGrayscale.py` (see above for where to find this) -> `/lib/thumbyGrayscale.py`

Then create a `/Games/ThumbRoll` folder on your Thumby and load the following files into it:

* ThumbRoll.py
* vid.BIT.bin
* vid.SHD.bin

If you have used a different Frame Rate or Resolution was in this example, you will have to adjust these parameters in the ThumbRoll.py file.

You should now be able to launch the ThumbRoll game on the Thumby, and the video will play.
