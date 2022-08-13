#!/usr/bin/python3

from PIL import Image, ImageSequence

buf = bytearray()
shd = bytearray()

# Fill the bitmap and shader buffers from the gif
with Image.open("processed.gif") as im:
    w = im.width
    h = im.height
    fs = 0
    for f in ImageSequence.Iterator(im):
        f = f.convert('RGB')
        fs += 1
        for ys in range(0, h, 8):
            for x in range(w):
                bbw = 0
                bgs = 0
                for y in range((h if h < ys+8 else ys+8)-1, ys-1, -1):
                    p = f.getpixel((x,y))[0]
                    cbw = 0 if p < 128 else 1
                    cgs = 1 if 64 <= p < 192 else 0
                    bbw <<= 1
                    bbw |= cbw
                    bgs <<= 1
                    bgs |= cgs
                buf.append(bbw)
                shd.append(bgs)
desc = f"{w}x{h}x{fs}"
print("Video Properties:", desc)

# Write the bytes to files:
with open(f"vid.BIT.bin", "wb") as fo:
    fo.write(bytes(buf))
with open(f"vid.SHD.bin", "wb") as fo:
    fo.write(bytes(shd))
print("Created:\n\tvid.BIT.bin\n\tvid.SHD.bin")
