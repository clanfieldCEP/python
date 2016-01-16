# http://www.stuffaboutcode.com/p/minecraft-api-reference.html
# https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/worksheet/
# run this on the rpi that is currently running MC - ssh/shellinabox etc, they run with 'python lay_tnt.py'
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("WARN: TNT block has been added at your feet!")
tnt = 46
x, y, z = mc.player.getPos()
mc.setBlock(x, y, z, tnt, 1)
