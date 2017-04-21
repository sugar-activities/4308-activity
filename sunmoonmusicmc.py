# SUN-MOON MUSIC MC - Sonic Environments for Children (2009)
# Art Hunkins (www.arthunkins.com)
#  Multiple Controller version; requires Csound 5.10 or greater
#   
#    SunMoonMusicMC is licensed under the Creative Commons Attribution-Share
#    Alike 3.0 Unported License. To view a copy of this license, visit
#    http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to
#    Creative Commons, 171 Second Street, Suite 300, San Francisco,
#    California, 94105, USA.
#
#    It is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#    Notes:
#
#    Both "Brother Sun Music" and "Sister Moon Music" require one or more
#    MIDI controllers with 8-9 knobs (the 9th controller is only used
#    with the Pan option). The 8 knobs/sliders must have *contiguous*
#    controller #'s, or all be continuous controller 7 on channels 1-8(9).
#    Also, all MIDI devices must be sending on the same channel. (On
#    multiple devices, the various controller #'s may be distributed
#    among the devices in many different ways.)
#
#    The first 7 controllers in "Sister Moon" vary volume for the 7 tones
#    (or tone pairs), while #8 is a MASTER volume control. The same is true
#    for "Brother Sun" except that there are only 6 tones; controller 7
#    varies overall pitch slightly. 
#
#    Important: The MIDI controller(s) must be attached AFTER boot, and
#    BEFORE the version is selected. It is assumed that the controller is
#    a USB device. The inexpensive Korg nanoKontrol is one appropriate
#    controller choice; it can nicely handle either 8- or 9-slider
#    renditions. Choose Scene 4 on the Korg, and Channel "0" in the
#    performance window. Preset all controllers to zero prior to start;
#    then, when using Pan, change controller 9 to its opening position
#    following start.
#
#    If you get audio glitching, open Sugar's Control Panel, and turn off
#    Extreme power management (under Power) or Wireless radio (under
#    Network). Stereo headphones (an inexpensive set will work fine) or
#    external amplifier/speaker system are highly recommended. The audio
#    level will sound higher for "Brother Sun" than for "Sister Moon."
#
#    The font display of this activity can be resized in csndsugui.py,
#    using any text editor. Further instructions are found toward the
#    beginning of csndsugui.py.
#
#    SunMoonMusicMC (Multiple Controller) requires Csound5.10 or later,
#    and Python2.6.
#
# version 2:  GUI tweaks

import csndsugui
from sugar.activity import activity
import gtk
import os

class SunMoonMusicMC(activity.Activity):

 def __init__(self, handle):
  
   activity.Activity.__init__(self, handle)

   red = (0xDDDD, 0, 0)
   brown = (0x6600, 0, 0)
   green = (0, 0x5500, 0)

   win = csndsugui.CsoundGUI(self)
   width = gtk.gdk.screen_width()
   height = gtk.gdk.screen_height()
   if os.path.exists("/etc/olpc-release"):
     adjust = 78
   else:
     adjust = 57
   screen = win.box()
   screen.set_size_request(width, height - adjust)
   scrolled = gtk.ScrolledWindow()
   scrolled.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
   screen.pack_start(scrolled)
   all = gtk.VBox()
   all.show()
   scrolled.add_with_viewport(all)
   scrolled.show()

   win.text("\t  <big><big><b><u>BROTHER SUN &amp; SISTER MOON MUSIC</u> -\t  \n\
\t   Sonic Environments for Children (2010)</b></big>\t\n\
Art Hunkins (www.arthunkins.com)  /  <b>M</b>ultiple <b>C</b>ontroller \
version</big>", all)
   win.text("from <u>The Canticle of the Sun</u> by Francis of Assisi:\n\
<i>\tBe praised, my Lord, through all your creatures,\n\
\t\tespecially through my lord Brother Sun, who brings the day;\n\
\t\tand you give light through him. \
And he is beautiful and radiant in all his splendor!\n\
\t\tOf you, Most High, he bears the likeness.\n\
\tBe praised, my Lord, through Sister Moon and the stars;\n\
\t\tin the heavens you have made them, precious and beautiful.</i>", all, green)

   win.text("\
1+ MIDI controllers with 8-9 knobs/sliders are required; \
the ninth control is only used to vary pan position.\n\
Plug in MIDI controller(s) AFTER boot &amp; BEFORE selecting Sun/Moon; \
zero all controls before start.\n\
Move Pan into position AFTER start. \
Channel '0' = controller 7 on chan 1-8(9); \
all devices set to SAME CHANNEL.", all, brown)
   nbox = win.box(False, all)
   win.text("", nbox)
   but1 = win.cbbutton(nbox, self.version1, " BROTHER SUN Music ")
   but1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0x7700, 0))
   but1.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0, 0x7700, 0))
   but2 = win.cbbutton(nbox, self.version2, " SISTER MOON Music ")
   but2.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0x7700, 0))
   but2.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0, 0x7700, 0))
   bbox = win.box(False, all)
   self.bb = bbox
   self.w = win
   self.r = red
   self.g = green
   self.br = brown
   self.ver = 0

 def playcsd(self, widget):
   if self.p == False:
     self.p = True
     self.w.play()
     self.but.child.set_label("STOP !")
     self.but.child.set_use_markup(True)
     self.but.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0xFFFF, 0, 0))
     self.but.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0xFFFF, 0, 0))
   else:
     self.p = False
     self.w.recompile()
     self.w.channels_reinit()
     self.but.child.set_label("START !")
     self.but.child.set_use_markup(True)
     self.but.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0x7700, 0))
     self.but.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0, 0x7700, 0))

 def version1(self, widget):
   if self.ver != 0:
     self.box1.destroy()
     self.box2.destroy()
   self.ver = 1
   self.box1 = self.w.box(True, self.bb)
   self.w.text("", self.box1)
   self.box2 = self.w.box(True, self.bb)
   self.f = self.w.framebox(" <b>Brother Sun Music</b> ", False, self.box2, self.r)
   self.b1 = self.w.box(True, self.f)
   self.b2 = self.w.box(True, self.f)
   self.b3 = self.w.box(True, self.f)
   self.b4 = self.w.box(True, self.f)
   self.b5 = self.w.box(True, self.f)
   self.w.reset()
   self.w.csd("SunMusicMC.csd")
   self.w.spin(0, 0, 16, 1, 1, self.b1, 0, "Chan", " Channel # ")
   self.w.spin(20, 0, 120, 1, 1, self.b2, 0, "Cont", " 1st Controller # ")
   self.w.button(self.b3, "Mult", ">1 MIDI device ?")
   self.w.button(self.b3, "Pan", "Pan Control ?")
   self.w.spin(7, 0, 127, 1, 1, self.b4, 0, "PCont", "Pan Controller #") 
   self.p = False
   self.w.text("<i>Select options first </i>", self.b5, self.g)
   self.but = self.w.cbbutton(self.b5, self.playcsd, "START !")
   self.but.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0x7700, 0))
   self.but.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0, 0x7700, 0))

 def version2(self, widget):
   if self.ver != 0:
     self.box1.destroy()
     self.box2.destroy()
   self.ver = 2
   self.box1 = self.w.box(True, self.bb)
   self.w.text("\t\t\t\t\t", self.box1)
   self.box2 = self.w.box(True, self.bb)
   self.f = self.w.framebox(" <b>Sister Moon Music</b> ", False, self.box2, self.r)
   self.b1 = self.w.box(True, self.f)
   self.b2 = self.w.box(True, self.f)
   self.b3 = self.w.box(True, self.f)
   self.b4 = self.w.box(True, self.f)
   self.b5 = self.w.box(True, self.f)
   self.w.reset()
   self.w.csd("MoonMusicMC.csd")
   self.w.spin(0, 0, 16, 1, 1, self.b1, 0, "Chan", " Channel # ")
   self.w.spin(20, 0, 120, 1, 1, self.b2, 0, "Cont", " 1st Controller # ")
   self.w.button(self.b3, "Mult", ">1 MIDI device ?")
   self.w.button(self.b3, "Pan", "Pan Control ?")
   self.w.spin(7, 0, 127, 1, 1, self.b4, 0, "PCont", "Pan Controller #") 
   self.p = False
   self.w.text("<i>Select options first </i>", self.b5, self.g)
   self.but = self.w.cbbutton(self.b5, self.playcsd, "START !")
   self.but.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0x7700, 0))
   self.but.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.Color(0, 0x7700, 0))

