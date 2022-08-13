
from os import stat
from thumbyGrayscale import display, ShadedSprite
display.startGPU()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Set the Frame Rate (ADJUST IF NEEDED)
display.setFPS(30)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Find the video files
for loc in ["/Games/ThumbRoll/", "./", "/"]:
    try:
        stat(loc+"vid.BIT.bin")
        break
    except OSError:
        pass

# Load the video files
vid = ShadedSprite(

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Set the resolution (ADJUST IF NEEDED)
    72, 40,
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    loc+"vid.BIT.bin",
    loc+"vid.SHD.bin", 0, 0)

# Play the video
t = 0
while True:
    vid.setFrame(t)
    display.drawSprite(vid)
    display.update()
    t += 1