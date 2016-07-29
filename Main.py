#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from subprocess import call
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from urllib import urlretrieve

#Acciones Preliminares

makedir = """mkdir ~/.local/share/icons""" + " >/dev/null 2>&1" 
bash_script = """ bash -c 'Fuente="${BASH_SOURCE[0]}"
            while [ -h "$Fuente" ]; do
                Directorio="$( cd -P "$( dirname "$Fuente" )" && pwd )"
                declare Fuente="$(readlink "$Fuente")"
                [[ $Fuente != /* ]] && Fuente="$Directorio/$Fuente"
            done
        Directorio="$( cd -P "$( dirname "$Fuente" )" && pwd )"
        
        Raiz="$Directorio"
		
		Registro="${Raiz}/Registro.txt"

		echo '' > "$Registro"

		cat "/usr/bin/aria2c" > /dev/null 2>&1
		
		TempErrorVar="$?"
	
		if [ "$TempErrorVar" = "0" ]; then
            
             get="aria2c"
			 GetMode="-o"
			 NoCheckCert="--check-certificate=false"
			 
         else
            
             get="wget"
             GetMode="-O"
			 NoCheckCert="--no-check-certificate"
            
         fi;
	
		cat "/usr/bin/apt-fast" > /dev/null 2>&1
		
		TempErrorVar="$?"
	
		if [ "$TempErrorVar" = "0" ]; then
            
			 apt="apt-fast"
			 
		else
		
			 apt="apt-get"
            
         fi;
		 
		 dpkg="dpkg"
		 
		 Gettie () {
	
		if [ "$get" = "wget" ] ; then
		
			 get="wget"
             GetMode="-O"
			 NoCheckCert="--no-check-certificate"

			Get () {
	
			( "$get" --append-output="$Registro" "$4" "$1" "${GetMode}" "$2/$3" ) > /dev/null 2>&1
	
			}
	
		elif [ "$get" = "aria2c" ] ; then
		
			 get="aria2c"
			 GetMode="-o"
			 NoCheckCert="--check-certificate=false"

			Get () {
	
			( ( "$get" "$1" "${GetMode}" "$3" -d "$2" $4 ) >> "$Registro" )
	
			}
	
		else

			Error
	
		fi
		
		}
		
		Gettie
		
		cat "$HOME/.local/share/icons/Minecraft.png"  >/dev/null 2>&1
		
		if [ "$?" != "0" ]; then
			
			Get "http://www.rw-designer.com/icon-image/5547-64x64x32.png" "$HOME/.local/share/icons" "Minecraft.png" "$NoCheckCert"		
	
		fi
		
		 '
		 
		 """

os.system(makedir)
os.system(bash_script)

XML = """PUT .GLADE FILE CONTENT HERE"""

def Activate_Switchy(switch, active):
	if myswitch.get_active():
		mytext.set_sensitive(True)
		state = "Encendido"
	else:
		mytext.set_sensitive(False)
		mytext.set_text("")
		state = "Apagado"
	print("El Switch fue", state)
	
builder = Gtk.Builder()
#builder.add_from_string(XML)
#builder.add_from_file("""PUT GLADE FILE LOCATION HERE""")

window = builder.get_object("window1")

myswitch = builder.get_object('Switch_Activable')
mytext = builder.get_object('Entrada_Desactivable')
mytext.set_text("")
mytext.set_sensitive(False)

os_name = subprocess.check_output("echo $(lsb_release -is) $(lsb_release -rs) $(lsb_release -cs)", shell=True).rstrip("""\n""")

os_label = builder.get_object('OS_Label')
os_label.set_text(os_name)

ournewbutton = builder.get_object("button1")
ournewbutton2 = builder.get_object("button2")

builder.get_object('Switch_Activable')

myswitch.set_active(False)
myswitch.connect('notify::active', Activate_Switchy)

window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()
