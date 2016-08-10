#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import subprocess
from subprocess import call
import threading
from multiprocessing import Process

# Variables

# Scripts Internos (Bash)
	
makedir = """ bash -c '

# Variables

	Local_Icons_Dir="$HOME/.local/share/icons"
	
# Script

mkdir -p "$Local_Icons_Dir" > /dev/null 2>&1

' """

install_gi = """ bash -c '

# Variables

	# Proceso(s)
	
		Fuente="${BASH_SOURCE[0]}"
		while [ -h "$Fuente" ]; do
		Directorio="$( cd -P "$( dirname "$Fuente" )" && pwd )"
		declare Fuente="$(readlink "$Fuente")"
		[[ $Fuente != /* ]] && Fuente="$Directorio/$Fuente"
		done
	
	# Directorios
			
		Directorio="$( cd -P "$( dirname "$Fuente" )" && pwd )"
        
		Raiz="$Directorio"
		
		Registro="${Raiz}/Registro.log"
		
	# Programas
	
		App_AptFast="/usr/sbin/apt-fast"
		
	# Imagenes Stock
	
		ErrorImage="list-remove"
		
	# Dialogos
	
		AlgoSalioMal="Algo estuvo mal"
		
		ErrorCodigo="Error código $?"
		
# Funciones
		
	# Función: Notificación "Algo anda mal"
    
        KO () {
        
        ( notify-send "$AlgoSalioMal" "$ErrorCodigo" --icon="$ErrorImage" ) > /dev/null 2>&1
        
        }
		
	# Funcion: Error
	
		trap Error INT

        Error () {
       
        ( rm -R "${HOME}/.guekho64/minecraft/.secret" )
        
        KO
		
        exit
		
		}
		
	# Funcion: Decide
	
		Decide () {
		
		cat "$App_AptFast" > /dev/null 2>&1
		
			if [ "$?" = "0" ]; then
            
				apt="apt-fast"
			 
			else
		
				apt="apt-get"
            
			fi;
		
		}
        
# Script
		
		Decide
		
		pkexec "$apt" install python-gi -y
		
' """

bash_script = """ bash -c '

# Variables

	# Proceso(s)
	
		Fuente="${BASH_SOURCE[0]}"
		while [ -h "$Fuente" ]; do
		Directorio="$( cd -P "$( dirname "$Fuente" )" && pwd )"
		declare Fuente="$(readlink "$Fuente")"
		[[ $Fuente != /* ]] && Fuente="$Directorio/$Fuente"
		done
	
	# Directorios
			
		Directorio="$( cd -P "$( dirname "$Fuente" )" && pwd )"
        
		Raiz="$Directorio"
		
		Registro="${Raiz}/Registro.log"
		
	# Programas
	
		App_Aria2="/usr/bin/aria2c"
		
		App_AptFast="/usr/sbin/apt-fast"
		
		dpkg="dpkg"
		
	# Archivos
	
		Minecraft_Icon_Location="$HOME/.local/share/icons/Minecraft.png"
		
		Minecraft_64x64_Internet_Location="http://www.rw-designer.com/icon-image/5547-64x64x32.png"
		
		Local_Icons_Directory="$HOME/.local/share/icons"

		Minecraft_Icon_Name="Minecraft.png"
		
	# Imagenes Stock
	
		ErrorImage="list-remove"
		
	# Dialogos
	
		AlgoSalioMal="Algo estuvo mal"
		
		ErrorCodigo="Error código $?"
		
# Funciones
		
	# Función: Notificación "Algo anda mal"
    
        KO () {
        
        ( notify-send "$AlgoSalioMal" "$ErrorCodigo" --icon="$ErrorImage" ) > /dev/null 2>&1
        
        }
		
	# Funcion: Error
	
		trap Error INT

        Error () {
        
        ( rm -R "${HOME}/.guekho64/minecraft/.secret" | tee -a "$Registro" ) > /dev/null 2>&1
        
        KO
		
        exit
        
        }
				
	# Funcion: Gettie
			
		Gettie () {
		
			cat "$App_Aria2" > /dev/null 2>&1
		
			if [ "$?" = "0" ]; then
            
				get="aria2c"
				GetMode="-o"
				NoCheckCert="--check-certificate=false"
			 
			else
            
				get="wget"
				GetMode="-O"
				NoCheckCert="--no-check-certificate"
            
			fi;
	
			cat "$App_AptFast" > /dev/null 2>&1
		
			if [ "$?" = "0" ]; then
            
				apt="apt-fast"
			 
			else
		
				apt="apt-get"
            
			fi;

			if [ "$get" = "wget" ] ; then
				
				Get () {
	
					( "$get" "$4" "$1" "${GetMode}" "$2/$3" ) > /dev/null 2>&1
							
				}
	
			elif [ "$get" = "aria2c" ] ; then
		
				Get () {
	
					( ( "$get" "$1" "${GetMode}" "$3" -d "$2" $4 ) )
	
				}
	
			else

				Error
	
			fi
					
			}
				
# Script
		
		Gettie
		
		cat "$Minecraft_Icon_Location"  > /dev/null 2>&1
		
		if [ "$?" != "0" ]; then
			
			Get "$Minecraft_64x64_Internet_Location" "$Local_Icons_Directory" "$Minecraft_Icon_Name" "$NoCheckCert"		
	
		fi

' """

get_dist=""" bash -c '  

echo "$(lsb_release -is) $(lsb_release -rs) $(lsb_release -cs)"

' """

get_prog_file_location=""" bash -c '  

echo "$HOME"/.guekho64/minecraft/.secret/

' """

get_log_location=""" bash -c '

# Variables

	# Proceso(s)
	
		Fuente="${BASH_SOURCE[0]}"
		while [ -h "$Fuente" ]; do
		Directorio="$( cd -P "$( dirname "$Fuente" )" && pwd )"
		declare Fuente="$(readlink "$Fuente")"
		[[ $Fuente != /* ]] && Fuente="$Directorio/$Fuente"
		done
	
	# Directorios
			
		Directorio="$( cd -P "$( dirname "$Fuente" )" && pwd )"
        
		Raiz="$Directorio"
		
		Registro="${Raiz}/Registro.log"
		
# Funciones

	# Funcion: Limpiar Registro
	
        ClearRegistryFile () {
		
		rm "$Registro" > /dev/null 2>&1
				
		}
		
# Script

	ClearRegistryFile

	echo "$Registro"

' """

bash_main_script_final = """
		
		
		
		"""
		
# Python

# Variables

# Variable del archivo .glade
		
XML = """



"""

log_created_no_passwd = """Debe introducir su contraseña para continuar

Se ha generado el archivo de registro"""

log_created_wrong_passwd = """La contraseña es incorrecta

Se ha generado el archivo de registro"""

# Checar algunos parámetros

if os.geteuid() is 0:
	os.system(""" echo "No ejecute este programa como ROOT, solo introdúzca su contraseña cuando el programa se la pida" > ./Error.txt """)
	sys.exit(1)

try:
	subprocess.check_output(""" echo -e "GET google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1 """, shell=True)
except:
	os.system(""" echo "No estás conectado a internet. Conéctate e inténtalo de nuevo" > ./Error.txt """)
	sys.exit(2)
	
# Procesos Preliminares

os_name = subprocess.check_output(get_dist, shell=True).rstrip("""\n""")
made_dir = subprocess.check_output(makedir, shell=True).rstrip("""\n""")
downloaded_icon = subprocess.check_output(bash_script, shell=True).rstrip("""\n""")
log_location = subprocess.check_output(get_log_location, shell=True).rstrip("""\n""")
prog_file_location = subprocess.check_output(get_prog_file_location, shell=True).rstrip("""\n""")

os.environ["Temp_Registry_Buffer"] = downloaded_icon
os.environ["RegistroActual"] = log_location
os.environ["XMLGlade"] = XML
os.environ["ProgressFileLocation"] = prog_file_location

# Mini Bash Script

dump_registry_to_a_file=""" bash -c '  

echo "$Temp_Registry_Buffer" > "$RegistroActual"

' """

# Proceso Intermedio

#os.system(dump_registry_to_a_file)

# Dependencias

try:
	import gi
	gi.require_version('Gtk', '3.0')
	from gi.repository import Gtk, GdkPixbuf
except:
	os.system(install_gi)
pass
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

# Misceláneos
		
version = "0.2"
nombre = "Instalador de Minecraft"
minecraft_icon = subprocess.check_output("ls ~/.local/share/icons/Minecraft.png", shell=True).rstrip("""\n""")
iconie_file = open(minecraft_icon, 'rb')
iconie = iconie_file.read()
loader = GdkPixbuf.PixbufLoader.new_with_type('png')
loader.write(iconie)
Miny = loader.get_pixbuf()
loader.close()
		
# Constructor(es)

builder = Gtk.Builder()
#builder.add_from_string(XML)
builder.add_from_file("""./Sin guardar 2.glade""")
			
# Ventanas
		
window = builder.get_object("VentanaPrincipal")
ventana_acerca_de = builder.get_object("AcercaDe")
ventatana_no_passwd = builder.get_object("NoPasswd")
ventatana_wrong_passwd = builder.get_object("WrongPasswd")
			
# Barra(s) de Progreso
		
barra_de_progreso = builder.get_object("Barra_De_Progreso")
			
# Switches
		
myswitch = builder.get_object('Switch_Offline')
switch_premium = builder.get_object('Switch_Premium')
			
# Entrada(s) de Texto
		
mytext = builder.get_object('Entrada_Desactivable')
PasswdEntry = builder.get_object('Contraseña')
			
# Etiquetas
		
os_label = builder.get_object('Etiqueta_Sistema_Operativo')
etiqueta_ventana_no_passwd = builder.get_object('Etiqueta_No_Passwd')
etiqueta_ventana_wrong_passwd = builder.get_object('Etiqueta_WrongPasswd')
			
# Botones
		
boton1 = builder.get_object("Boton_1")
boton2 = builder.get_object("Boton_2")
boton_wrong = builder.get_object("Boton_Cerrar_WrongPasswd")
boton_none = builder.get_object("Boton_Cerrar_NoPasswd")
boton_opcional = builder.get_object("Boton_Activable_Opcional")
boton_acerca_de = builder.get_object("Boton_Del_Menu_1")
			
# Casillas
		
casilla1 = builder.get_object("Casilla1")
casilla2 = builder.get_object("Casilla2")
casilla3 = builder.get_object("Casilla3")
casilla4 = builder.get_object("Casilla4")
casilla5 = builder.get_object("Casilla5")
casilla6 = builder.get_object("Casilla6")
casilla7 = builder.get_object("Casilla7")
casilla8 = builder.get_object("Casilla8")
casilla9 = builder.get_object("Casilla9")
casilla10 = builder.get_object("Casilla10")
casilla11 = builder.get_object("Casilla11")
casilla12 = builder.get_object("Casilla12")
			
# Botones Radiales

boton_radial_1 = builder.get_object("Boton_Radial_1")
boton_radial_2 = builder.get_object("Boton_Radial_2")
boton_radial_3 = builder.get_object("Boton_Radial_3")
boton_radial_4 = builder.get_object("Boton_Radial_4")
boton_radial_5 = builder.get_object("Boton_Radial_5")
boton_radial_6 = builder.get_object("Boton_Radial_6")
			
# Contenedores
		
contenedor_opciones = builder.get_object("Contenedor_Opciones")
			
# Funciones

# Python
	
def Activate_Switchy(switch, active):
	if myswitch.get_active():
		mytext.set_sensitive(True)
		state = "Encendido"
	else:
			mytext.set_sensitive(False)
			mytext.set_text("")
			state = "Apagado"
		
def EsconderAbout(ventana_acerca_de):
	ventana_acerca_de.hide()
	return True

def Esconder(window, event):
	window.hide()
	return True

def EsconderNone(event):
	ventatana_no_passwd.hide()
	return True

def EsconderWrong(event):
	ventatana_wrong_passwd.hide()
	return True
	
def ClickAbout(widget, event):
	ventana_acerca_de.connect("delete_event", Esconder)
	ventana_acerca_de.connect('response', Esconder)
	ventana_acerca_de.run()
	
def Install(button):
	boton2.set_sensitive(False)
	if casilla9.get_active():
		os.system(dump_registry_to_a_file)
		etiqueta_ventana_no_passwd.set_text(log_created_no_passwd)
		etiqueta_ventana_wrong_passwd.set_text(log_created_wrong_passwd)
	Passwd = PasswdEntry.get_text().rstrip()
	print Passwd
	if Passwd == "":
		ventatana_no_passwd.connect("delete_event", Esconder)
		ventatana_no_passwd.set_position(Gtk.WindowPosition.CENTER)
		ventatana_no_passwd.show_all()
		boton_none.connect("clicked", EsconderNone)
		boton2.set_sensitive(True)
	else:
		os.environ["Passwd"] = Passwd
		try:
			Bash_Passwd = subprocess.check_output(""" autosudo () {  echo "$Passwd" | sudo -S "$@" ; } ; autosudo echo "Hola" > /dev/null 2>&1 """, shell=True).rstrip("""\n""")
		except:
			ventatana_wrong_passwd.connect("delete_event", EsconderWrong)
			ventatana_wrong_passwd.set_position(Gtk.WindowPosition.CENTER)
			boton_wrong.connect("clicked", EsconderWrong)
			ventatana_wrong_passwd.show_all()
			boton2.set_sensitive(True)
		else:
			
			os.system(""" bash -c '
	
				autosudo () {  echo "$Password" | sudo -S "$@" ; }
				
				mkdir -p "$ProgressFileLocation"
				
				autosudo chmod 777 "$ProgressFileLocation"
				
				echo "0.00" > "$ProgressFileLocation/Progress.txt"	
				
				' """)
			
			def Ok():
	
				try:
		
					ProgressFile = os.environ["ProgressFileLocation"] + "/Progress.txt"
					file = open(ProgressFile)
					txt = file.read()
		
					number = float(txt)
						
					barra_de_progreso.set_fraction(number)
		
				except ValueError:
		
					pass
	
				if number != 1.00:
					threading.Timer(0.01, Ok).start()
		
				
			def P1():
				
				os.system(""" for i in $(seq 0.01 0.01 1.00); do sleep 0.01;echo "$i" > "$ProgressFileLocation/Progress.txt" ; done """)				
			
			p1 = Process(target=Ok)
			p2 = Process(target=P1)

			p1.run()
			p2.start()
						
			boton2.set_sensitive(False)
			print ("Fin")
	
def Quick_Installation(button):
		if boton_opcional.get_active():
			contenedor_opciones.set_sensitive(False)
			casilla1.set_active(True)
			casilla2.set_active(False)
			casilla3.set_active(False)
			casilla4.set_active(False)
			casilla5.set_active(False)
			casilla6.set_active(False)
			casilla7.set_active(False)
			casilla8.set_active(False)
			casilla9.set_active(False)
			casilla10.set_active(False)
			casilla11.set_active(False)
			casilla12.set_active(False)
			boton_radial_1.set_active(False)
			boton_radial_2.set_active(True)
			boton_radial_3.set_active(False)
			boton_radial_4.set_active(True)
			boton_radial_5.set_active(False)
			boton_radial_6.set_active(False)
		else:
			contenedor_opciones.set_sensitive(True)
				
# Ejecutables

# Python
		
ventana_acerca_de.set_version(version)
mytext.set_text("")
mytext.set_sensitive(False)
os_label.set_text(os_name)
casilla1.set_active(True)
casilla2.set_active(False)
casilla3.set_active(False)
casilla4.set_active(False)
casilla5.set_active(False)
casilla6.set_active(False)
casilla7.set_active(False)
casilla8.set_active(False)
casilla9.set_active(False)
casilla10.set_active(False)
casilla11.set_active(False)
casilla12.set_active(False)
boton_radial_1.set_active(False)
boton_radial_2.set_active(True)
boton_radial_3.set_active(False)
boton_radial_4.set_active(True)
boton_radial_5.set_active(False)
boton_radial_6.set_active(False)
boton2.connect("clicked", Install)
boton1.connect("clicked", Gtk.main_quit )
boton_opcional.connect("clicked", Quick_Installation)
boton_opcional.set_active(True)
contenedor_opciones.set_sensitive(False)
boton_acerca_de.connect("activate", ClickAbout, "Aplicación")
switch_premium.set_active(True)
myswitch.set_active(False)
myswitch.connect('notify::active', Activate_Switchy)
ventana_acerca_de.set_position(Gtk.WindowPosition.CENTER)
ventana_acerca_de.set_title(nombre)
ventana_acerca_de.set_icon_from_file(minecraft_icon)
ventana_acerca_de.set_default_icon_list([Miny])
ventana_acerca_de.set_logo_icon_name(None)
window.set_icon_from_file(minecraft_icon)
window.set_position(Gtk.WindowPosition.CENTER)
window.set_title(nombre)
ventatana_no_passwd.set_title(nombre)
ventatana_wrong_passwd.set_title(nombre)
window.connect("delete-event", Gtk.main_quit)
window.show_all()

if __name__ == '__main__':
	import signal
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	Gtk.main()
		
# Cambiar fuentes de texto en Glade para hacerlo más compatible con Debian 8 (Y más elegante, se ve horrible)		CHECK!!!
# Cambiar Iconos para hacerlos más compatibles con Debian 8 + Ubuntu 12 
# Extraño issue en Ubuntu 12 con icono de (About dialog)
# Añadir diálogos de pregunta cuando se elige la opción de "Pregúntame" en caso de detectar algún error y corregirlo inmediatamente (Hacer ventanitas, ponerles su función y añadirlas , jiji)
# Implementar las funcionalidades del Instalador Original en este Nuevo (Léerse todo el puto código)
