from mcpi.minecraft import Minecraft
from mcpi import block
import time


class tntboom:
    
    def tntblock(self):
        mc = Minecraft.create("192.168.1.13")
        x,y,z=mc.entity.getPos() 
        tnt = 46
        mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)

    def tntblock2(self,wh):
        mc = Minecraft.create("192.168.1.13")
        x,y,z=mc.entity.getPos() 
        tnt = 46
        mc.setBlocks(x+1, y+1, z+1, x+wh, y+wh, z+wh, tnt, 1)

    def gname(self):
        mc = Minecraft.create("192.168.1.13")
        entityIds=mc.getPlayerEntityIds()
        for entityId in entityIds:
            print entityId
         
wf=tntboom()
wf.gname()
wf.tntblock2(50)


#.getPlayerEntityIds()
