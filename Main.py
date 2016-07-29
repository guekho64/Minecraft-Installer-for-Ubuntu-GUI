#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

## First Version Ever ##

import os
import subprocess
import gi
from gi.repository import Gtk

XML = """HERE GOES THE .GLADE FILE"""

def button_1clicked(self, button):
	from subprocess import call
			
	Damn = 1
			
	print (Damn)
			
	output = subprocess.check_output("echo $(cat 'Some Example Dir')", shell=True)
			
	#call(["bash", "-c", '  foo=Hi ; export foo '])
			
	#hy = os.environ['foo']
			
	print (output)
				
def button_2clicked(self, button):
	from subprocess import call
			
	Damn2 = 2
			
	print (Damn2)
			
	#call(["bash", "-c", '  O=8 ; echo "$H" '])
				
def Activate_Switchy(switch, active):
	from subprocess import call
			
	Damn2 = 2
			
	print (Damn2)
			
	#call(["bash", "-c", '  O=8 ; echo "$H" '])
			
			
			
builder = Gtk.Builder()
builder.add_from_string(XML)

window = builder.get_object("window1")

switch = builder.get_object('Switch_Activable')

ournewbutton = builder.get_object("button1")
ournewbutton2 = builder.get_object("button2")

builder.get_object('Switch_Activable')

switch.set_active(False)
switch.connect('notify::active', Activate_Switchy)

ournewbutton.set_label("Hello, World!")
ournewbutton2.set_label("Nope!")

window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()
