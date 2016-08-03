#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import subprocess
from subprocess import call

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
		
		Registro="${Raiz}/Registro.txt"
		
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
        
        ( rm -R "${HOME}/.guekho64/minecraft/.secret" | tee -a "$Registro" ) > /dev/null 2>&1
        
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
		
		pkexec "$apt" install python-gi -y  >> "$Registro"
		
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
		
		Registro="${Raiz}/Registro.txt"
		
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
		
	# Funcion: Limpiar Registro
	
        ClearRegistryFile () {
		
		rm "$Registro" > /dev/null 2>&1
		
		touch "$Registro" > /dev/null 2>&1
		
		}
			
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
	
					( "$get" --append-output="$Registro" "$4" "$1" "${GetMode}" "$2/$3" ) > /dev/null 2>&1
							
				}
	
			elif [ "$get" = "aria2c" ] ; then
		
				Get () {
	
					( ( "$get" "$1" "${GetMode}" "$3" -d "$2" $4 ) >> "$Registro" )
	
				}
	
			else

				Error
	
			fi
					
			}
				
# Script
		
		ClearRegistryFile
		
		Gettie
		
		cat "$Minecraft_Icon_Location"  > /dev/null 2>&1
		
		if [ "$?" != "0" ]; then
			
			Get "$Minecraft_64x64_Internet_Location" "$Local_Icons_Directory" "$Minecraft_Icon_Name" "$NoCheckCert"		
	
		fi

' """
bash_main_script_final = """
		
		
		
		"""
		
os_name = subprocess.check_output("echo $(lsb_release -is) $(lsb_release -rs) $(lsb_release -cs)", shell=True).rstrip("""\n""")
		
# Variable del archivo .glade
		
XML = """  

<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.16.1 -->
<interface domain="es_MX">
  <requires lib="gtk+" version="3.4"/>
  <object class="GtkAboutDialog" id="AcercaDe">
    <property name="can_focus">False</property>
    <property name="halign">center</property>
    <property name="valign">center</property>
    <property name="resizable">False</property>
    <property name="type_hint">dialog</property>
    <property name="has_resize_grip">False</property>
    <property name="program_name">Instalador de Minecraft para Ubuntu</property>
    <property name="copyright" translatable="yes">guekho64©</property>
    <property name="comments" translatable="yes">Este programa te permite instalar Minecraft de forma rápida y sencilla</property>
    <property name="website">https://www.youtube.com/user/guekho64</property>
    <property name="authors">guekho64</property>
    <property name="logo_icon_name">Minecraft</property>
    <property name="license_type">gpl-3-0</property>
    <child internal-child="vbox">
      <object class="GtkBox" id="Caja_Interna_Acerca_De">
        <property name="can_focus">False</property>
        <property name="halign">center</property>
        <property name="valign">center</property>
        <property name="orientation">vertical</property>
        <property name="spacing">2</property>
        <child internal-child="action_area">
          <object class="GtkButtonBox" id="Caja_De_Acciones_Acerca_De">
            <property name="can_focus">False</property>
            <property name="halign">baseline</property>
            <property name="valign">baseline</property>
            <property name="layout_style">end</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="pack_type">end</property>
            <property name="position">0</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkImage" id="Imagen_Boton_Activable_Opcional">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="halign">center</property>
    <property name="valign">center</property>
    <property name="margin_right">4</property>
    <property name="pixel_size">24</property>
    <property name="icon_name">emblem-default</property>
  </object>
  <object class="GtkWindow" id="VentanaPrincipal">
    <property name="can_focus">False</property>
    <property name="resizable">False</property>
    <property name="window_position">center</property>
    <property name="default_width">498</property>
    <property name="default_height">612</property>
    <property name="destroy_with_parent">True</property>
    <property name="urgency_hint">True</property>
    <property name="has_resize_grip">False</property>
    <child>
      <object class="GtkBox" id="Contenedor_Universal">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkMenuBar" id="Barra_De_Menu">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkMenuItem" id="Entrada_Del_Menu_1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Aplicación</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="Item_Del_Menu_1">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkImageMenuItem" id="Boton_Del_Menu_1">
                        <property name="label">gtk-about</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                        <signal name="activate" handler="ClickAbout" swapped="no"/>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkImage" id="Icono">
            <property name="name">3</property>
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="halign">center</property>
            <property name="valign">center</property>
            <property name="margin_top">4</property>
            <property name="margin_bottom">2</property>
            <property name="pixel_size">64</property>
            <property name="icon_name">Minecraft</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="Texto Principal">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">Instalador de Minecraft
para Ubuntu</property>
            <property name="justify">center</property>
            <attributes>
              <attribute name="font-desc" value="Ubuntu 16"/>
              <attribute name="style" value="normal"/>
              <attribute name="weight" value="ultraheavy"/>
            </attributes>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">2</property>
          </packing>
        </child>
        <child>
          <object class="GtkLinkButton" id="Link_Canal">
            <property name="label" translatable="yes">guekho64©</property>
            <property name="use_action_appearance">True</property>
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="receives_default">True</property>
            <property name="no_show_all">True</property>
            <property name="halign">center</property>
            <property name="valign">center</property>
            <property name="uri">https://www.youtube.com/user/guekho64</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">3</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="Etiqueta_Sistema_Operativo">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="halign">center</property>
            <property name="valign">center</property>
            <property name="margin_top">6</property>
            <property name="margin_bottom">6</property>
            <property name="label" translatable="yes">Generic Linux</property>
            <property name="ellipsize">middle</property>
            <attributes>
              <attribute name="font-desc" value="Ubuntu 10"/>
              <attribute name="style" value="italic"/>
              <attribute name="weight" value="book"/>
              <attribute name="variant" value="small-caps"/>
            </attributes>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">4</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="Contraseña">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="halign">center</property>
            <property name="valign">center</property>
            <property name="margin_top">3</property>
            <property name="margin_bottom">6</property>
            <property name="visibility">False</property>
            <property name="primary_icon_stock">gtk-about</property>
            <property name="placeholder_text" translatable="yes">Contraseña</property>
          </object>
          <packing>
            <property name="expand">True</property>
            <property name="fill">True</property>
            <property name="position">5</property>
          </packing>
        </child>
        <child>
          <object class="GtkGrid" id="Selector_De_Launchers">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="halign">center</property>
            <property name="valign">center</property>
            <property name="margin_top">3</property>
            <property name="margin_bottom">9</property>
            <property name="row_homogeneous">True</property>
            <property name="column_homogeneous">True</property>
            <child>
              <object class="GtkLabel" id="Etiqueta_Minecraft_Offline">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <property name="label" translatable="yes">Minecraft Offline</property>
                <property name="justify">center</property>
                <attributes>
                  <attribute name="font-desc" value="Ubuntu 10"/>
                  <attribute name="weight" value="normal"/>
                </attributes>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">1</property>
                <property name="width">1</property>
                <property name="height">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="Etiqueta_Minecraft_Premium">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <property name="label" translatable="yes">Minecraft Premium</property>
                <property name="justify">center</property>
                <attributes>
                  <attribute name="font-desc" value="Ubuntu 10"/>
                  <attribute name="style" value="normal"/>
                  <attribute name="weight" value="normal"/>
                  <attribute name="variant" value="normal"/>
                </attributes>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">0</property>
                <property name="width">1</property>
                <property name="height">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkSwitch" id="Switch_Premium">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">0</property>
                <property name="width">1</property>
                <property name="height">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkSwitch" id="Switch_Offline">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <signal name="activate" handler="Activate_Switchy" swapped="no"/>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">1</property>
                <property name="width">1</property>
                <property name="height">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">6</property>
          </packing>
        </child>
        <child>
          <object class="GtkSeparator" id="Separador_1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="padding">1</property>
            <property name="position">7</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox" id="Caja_Opcional">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="margin_top">6</property>
            <property name="orientation">vertical</property>
            <property name="homogeneous">True</property>
            <child>
              <object class="GtkBox" id="Sub_Caja_Opcional">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="homogeneous">True</property>
                <child>
                  <object class="GtkToggleButton" id="Boton_Activable_Opcional">
                    <property name="label" translatable="yes">Instalación Rápida</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">True</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="image">Imagen_Boton_Activable_Opcional</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">8</property>
          </packing>
        </child>
        <child>
          <object class="GtkNotebook" id="Contenedor_Opciones">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="halign">center</property>
            <property name="valign">center</property>
            <property name="margin_left">24</property>
            <property name="margin_right">24</property>
            <property name="group_name">Opciones</property>
            <child>
              <object class="GtkGrid" id="Rejilla_Opciones">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="margin_left">24</property>
                <property name="margin_right">24</property>
                <property name="margin_bottom">3</property>
                <property name="row_homogeneous">True</property>
                <property name="column_homogeneous">True</property>
                <child>
                  <object class="GtkCheckButton" id="Casilla2">
                    <property name="label" translatable="yes">checkbutton</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="xalign">0</property>
                    <property name="draw_indicator">True</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="top_attach">0</property>
                    <property name="width">1</property>
                    <property name="height">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkCheckButton" id="Casilla1">
                    <property name="label" translatable="yes">Añadir icono al escritorio</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="xalign">0</property>
                    <property name="draw_indicator">True</property>
                  </object>
                  <packing>
                    <property name="left_attach">0</property>
                    <property name="top_attach">0</property>
                    <property name="width">1</property>
                    <property name="height">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkCheckButton" id="Casilla3">
                    <property name="label" translatable="yes">Forzar actualizar "aria2"</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="xalign">0</property>
                    <property name="draw_indicator">True</property>
                  </object>
                  <packing>
                    <property name="left_attach">0</property>
                    <property name="top_attach">1</property>
                    <property name="width">1</property>
                    <property name="height">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkCheckButton" id="Casilla4">
                    <property name="label" translatable="yes">checkbutton</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="xalign">0</property>
                    <property name="draw_indicator">True</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="top_attach">1</property>
                    <property name="width">1</property>
                    <property name="height">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkCheckButton" id="Casilla5">
                    <property name="label" translatable="yes">Forzar Zulu como JVM</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="xalign">0</property>
                    <property name="draw_indicator">True</property>
                  </object>
                  <packing>
                    <property name="left_attach">0</property>
                    <property name="top_attach">2</property>
                    <property name="width">1</property>
                    <property name="height">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkCheckButton" id="Casilla6">
                    <property name="label" translatable="yes">checkbutton</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="xalign">0</property>
                    <property name="draw_indicator">True</property>
                  </object>
                  <packing>
                    <property name="left_attach">1</property>
                    <property name="top_attach">2</property>
                    <property name="width">1</property>
                    <property name="height">1</property>
                  </packing>
                </child>
              </object>
            </child>
            <child type="tab">
              <object class="GtkLabel" id="Opciones">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Opciones</property>
                <attributes>
                  <attribute name="font-desc" value="Ubuntu 10"/>
                  <attribute name="style" value="italic"/>
                  <attribute name="weight" value="normal"/>
                </attributes>
              </object>
              <packing>
                <property name="tab_fill">False</property>
              </packing>
            </child>
            <child>
              <object class="GtkBox" id="Caja_Opciones_Avanzadas">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">baseline</property>
                <property name="valign">baseline</property>
                <property name="margin_left">12</property>
                <property name="margin_right">12</property>
                <property name="margin_top">12</property>
                <property name="margin_bottom">6</property>
                <property name="orientation">vertical</property>
                <property name="homogeneous">True</property>
                <child>
                  <object class="GtkScrolledWindow" id="Ventana_Con_Desplazamiento_Opciones_Avanzadas">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <child>
                      <object class="GtkViewport" id="Vista_Opciones_Avanzadas">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="shadow_type">none</property>
                        <child>
                          <object class="GtkBox" id="Sub-Caja_Opciones_Avanzadas">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="halign">baseline</property>
                            <property name="valign">baseline</property>
                            <property name="margin_right">12</property>
                            <property name="orientation">vertical</property>
                            <property name="spacing">16</property>
                            <property name="homogeneous">True</property>
                            <child>
                              <object class="GtkFrame" id="Marco_Opciones_Avanzadas1">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="label_xalign">0.5</property>
                                <child>
                                  <object class="GtkAlignment" id="Alineamiento_Opciones_Avanzadas1">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="left_padding">12</property>
                                    <child>
                                      <object class="GtkGrid" id="Rejilla_Opciones_Avanzadas1">
                                        <property name="visible">True</property>
                                        <property name="can_focus">False</property>
                                        <property name="row_homogeneous">True</property>
                                        <property name="column_homogeneous">True</property>
                                        <child>
                                          <object class="GtkRadioButton" id="Boton_Radial_1">
                                            <property name="label" translatable="yes">Oracle Java</property>
                                            <property name="visible">True</property>
                                            <property name="can_focus">True</property>
                                            <property name="receives_default">False</property>
                                            <property name="halign">center</property>
                                            <property name="valign">center</property>
                                            <property name="xalign">0</property>
                                            <property name="draw_indicator">True</property>
                                            <property name="group">Boton_Radial_3</property>
                                          </object>
                                          <packing>
                                            <property name="left_attach">0</property>
                                            <property name="top_attach">0</property>
                                            <property name="width">1</property>
                                            <property name="height">1</property>
                                          </packing>
                                        </child>
                                        <child>
                                          <object class="GtkRadioButton" id="Boton_Radial_2">
                                            <property name="label" translatable="yes">OpenJDK</property>
                                            <property name="visible">True</property>
                                            <property name="can_focus">True</property>
                                            <property name="receives_default">False</property>
                                            <property name="halign">center</property>
                                            <property name="valign">center</property>
                                            <property name="xalign">0</property>
                                            <property name="draw_indicator">True</property>
                                            <property name="group">Boton_Radial_1</property>
                                          </object>
                                          <packing>
                                            <property name="left_attach">1</property>
                                            <property name="top_attach">0</property>
                                            <property name="width">1</property>
                                            <property name="height">1</property>
                                          </packing>
                                        </child>
                                        <child>
                                          <object class="GtkRadioButton" id="Boton_Radial_3">
                                            <property name="label" translatable="yes">Zulu </property>
                                            <property name="visible">True</property>
                                            <property name="can_focus">True</property>
                                            <property name="receives_default">False</property>
                                            <property name="halign">center</property>
                                            <property name="valign">center</property>
                                            <property name="xalign">0</property>
                                            <property name="draw_indicator">True</property>
                                            <property name="group">Boton_Radial_2</property>
                                          </object>
                                          <packing>
                                            <property name="left_attach">2</property>
                                            <property name="top_attach">0</property>
                                            <property name="width">1</property>
                                            <property name="height">1</property>
                                          </packing>
                                        </child>
                                      </object>
                                    </child>
                                  </object>
                                </child>
                                <child type="label">
                                  <object class="GtkLabel" id="Etiqueta_Marco_Opciones_Avanzadas1">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">Java Virtual Machine</property>
                                    <attributes>
                                      <attribute name="font-desc" value="Ubuntu Mono 12"/>
                                      <attribute name="style" value="italic"/>
                                      <attribute name="weight" value="thin"/>
                                    </attributes>
                                  </object>
                                </child>
                              </object>
                              <packing>
                                <property name="expand">False</property>
                                <property name="fill">True</property>
                                <property name="position">0</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkFrame" id="Marco_Opciones_Avanzadas2">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="margin_bottom">12</property>
                                <property name="label_xalign">0.5</property>
                                <child>
                                  <object class="GtkAlignment" id="Alineamiento_Opciones_Avanzadas2">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="left_padding">12</property>
                                    <child>
                                      <object class="GtkGrid" id="Rejilla_Opciones_Avanzadas2">
                                        <property name="visible">True</property>
                                        <property name="can_focus">False</property>
                                        <property name="row_homogeneous">True</property>
                                        <property name="column_homogeneous">True</property>
                                        <child>
                                          <object class="GtkRadioButton" id="Boton_Radial_4">
                                            <property name="label" translatable="yes">Oracle Java</property>
                                            <property name="visible">True</property>
                                            <property name="can_focus">True</property>
                                            <property name="receives_default">False</property>
                                            <property name="halign">center</property>
                                            <property name="valign">center</property>
                                            <property name="xalign">0</property>
                                            <property name="draw_indicator">True</property>
                                            <property name="group">Boton_Radial_3</property>
                                          </object>
                                          <packing>
                                            <property name="left_attach">0</property>
                                            <property name="top_attach">0</property>
                                            <property name="width">1</property>
                                            <property name="height">1</property>
                                          </packing>
                                        </child>
                                        <child>
                                          <object class="GtkRadioButton" id="Boton_Radial_5">
                                            <property name="label" translatable="yes">OpenJDK</property>
                                            <property name="visible">True</property>
                                            <property name="can_focus">True</property>
                                            <property name="receives_default">False</property>
                                            <property name="halign">center</property>
                                            <property name="valign">center</property>
                                            <property name="xalign">0</property>
                                            <property name="draw_indicator">True</property>
                                            <property name="group">Boton_Radial_1</property>
                                          </object>
                                          <packing>
                                            <property name="left_attach">1</property>
                                            <property name="top_attach">0</property>
                                            <property name="width">1</property>
                                            <property name="height">1</property>
                                          </packing>
                                        </child>
                                        <child>
                                          <object class="GtkRadioButton" id="Boton_Radial_6">
                                            <property name="label" translatable="yes">Zulu </property>
                                            <property name="visible">True</property>
                                            <property name="can_focus">True</property>
                                            <property name="receives_default">False</property>
                                            <property name="halign">center</property>
                                            <property name="valign">center</property>
                                            <property name="xalign">0</property>
                                            <property name="draw_indicator">True</property>
                                            <property name="group">Boton_Radial_2</property>
                                          </object>
                                          <packing>
                                            <property name="left_attach">2</property>
                                            <property name="top_attach">0</property>
                                            <property name="width">1</property>
                                            <property name="height">1</property>
                                          </packing>
                                        </child>
                                      </object>
                                    </child>
                                  </object>
                                </child>
                                <child type="label">
                                  <object class="GtkLabel" id="Etiqueta_Marco_Opciones_Avanzadas2">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">Java Virtual Machine</property>
                                    <attributes>
                                      <attribute name="font-desc" value="Ubuntu Mono 12"/>
                                      <attribute name="style" value="italic"/>
                                      <attribute name="weight" value="thin"/>
                                    </attributes>
                                  </object>
                                </child>
                              </object>
                              <packing>
                                <property name="expand">False</property>
                                <property name="fill">True</property>
                                <property name="position">1</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkFrame" id="Marco_Opciones_Avanzadas3">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <property name="margin_bottom">12</property>
                                <property name="label_xalign">0.5</property>
                                <child>
                                  <object class="GtkAlignment" id="Alineamiento_Opciones_Avanzadas3">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="left_padding">12</property>
                                    <child>
                                      <object class="GtkGrid" id="Rejilla_Opciones_Avanzadas3">
                                        <property name="visible">True</property>
                                        <property name="can_focus">False</property>
                                        <property name="row_homogeneous">True</property>
                                        <property name="column_homogeneous">True</property>
                                        <child>
                                          <object class="GtkRadioButton" id="Boton_Radial_7">
                                            <property name="label" translatable="yes">Oracle Java</property>
                                            <property name="visible">True</property>
                                            <property name="can_focus">True</property>
                                            <property name="receives_default">False</property>
                                            <property name="halign">center</property>
                                            <property name="valign">center</property>
                                            <property name="xalign">0</property>
                                            <property name="draw_indicator">True</property>
                                            <property name="group">Boton_Radial_3</property>
                                          </object>
                                          <packing>
                                            <property name="left_attach">0</property>
                                            <property name="top_attach">0</property>
                                            <property name="width">1</property>
                                            <property name="height">1</property>
                                          </packing>
                                        </child>
                                        <child>
                                          <object class="GtkRadioButton" id="Boton_Radial_8">
                                            <property name="label" translatable="yes">OpenJDK</property>
                                            <property name="visible">True</property>
                                            <property name="can_focus">True</property>
                                            <property name="receives_default">False</property>
                                            <property name="halign">center</property>
                                            <property name="valign">center</property>
                                            <property name="xalign">0</property>
                                            <property name="draw_indicator">True</property>
                                            <property name="group">Boton_Radial_1</property>
                                          </object>
                                          <packing>
                                            <property name="left_attach">1</property>
                                            <property name="top_attach">0</property>
                                            <property name="width">1</property>
                                            <property name="height">1</property>
                                          </packing>
                                        </child>
                                        <child>
                                          <object class="GtkRadioButton" id="Boton_Radial_9">
                                            <property name="label" translatable="yes">Zulu </property>
                                            <property name="visible">True</property>
                                            <property name="can_focus">True</property>
                                            <property name="receives_default">False</property>
                                            <property name="halign">center</property>
                                            <property name="valign">center</property>
                                            <property name="xalign">0</property>
                                            <property name="draw_indicator">True</property>
                                            <property name="group">Boton_Radial_2</property>
                                          </object>
                                          <packing>
                                            <property name="left_attach">2</property>
                                            <property name="top_attach">0</property>
                                            <property name="width">1</property>
                                            <property name="height">1</property>
                                          </packing>
                                        </child>
                                      </object>
                                    </child>
                                  </object>
                                </child>
                                <child type="label">
                                  <object class="GtkLabel" id="Etiqueta_Marco_Opciones_Avanzadas3">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">Java Virtual Machine</property>
                                    <attributes>
                                      <attribute name="font-desc" value="Ubuntu Mono 12"/>
                                      <attribute name="style" value="italic"/>
                                      <attribute name="weight" value="thin"/>
                                    </attributes>
                                  </object>
                                </child>
                              </object>
                              <packing>
                                <property name="expand">False</property>
                                <property name="fill">True</property>
                                <property name="position">2</property>
                              </packing>
                            </child>
                          </object>
                        </child>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">1</property>
              </packing>
            </child>
            <child type="tab">
              <object class="GtkLabel" id="Opciones_Avanzadas">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Opciones Avanzadas</property>
                <attributes>
                  <attribute name="font-desc" value="&lt;Introducir valor&gt; 10"/>
                  <attribute name="style" value="italic"/>
                  <attribute name="weight" value="normal"/>
                </attributes>
              </object>
              <packing>
                <property name="position">1</property>
                <property name="tab_fill">False</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="padding">7</property>
            <property name="position">9</property>
          </packing>
        </child>
        <child>
          <object class="GtkSeparator" id="Separador_2">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="margin_top">1</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="padding">1</property>
            <property name="position">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="Entrada_Desactivable">
            <property name="visible">True</property>
            <property name="sensitive">False</property>
            <property name="can_focus">True</property>
            <property name="valign">center</property>
            <property name="margin_left">36</property>
            <property name="margin_right">36</property>
            <property name="margin_top">6</property>
            <property name="margin_bottom">8</property>
            <property name="placeholder_text" translatable="yes">Pega la URL del Launcher Offline</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">11</property>
          </packing>
        </child>
        <child>
          <object class="GtkInfoBar" id="Barra_De_Informacon">
            <property name="visible">True</property>
            <property name="app_paintable">True</property>
            <property name="can_focus">False</property>
            <property name="halign">center</property>
            <property name="valign">center</property>
            <property name="margin_left">24</property>
            <property name="margin_right">24</property>
            <property name="margin_top">1</property>
            <property name="margin_bottom">2</property>
            <child internal-child="action_area">
              <object class="GtkButtonBox" id="Zona_De_Informacion">
                <property name="can_focus">False</property>
                <property name="spacing">6</property>
                <property name="layout_style">center</property>
                <child>
                  <object class="GtkLabel" id="Etiqueta_de_Informacion">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <property name="margin_top">3</property>
                    <property name="margin_bottom">3</property>
                    <property name="xalign">0</property>
                    <property name="yalign">0</property>
                    <property name="label" translatable="yes">Se recomienda que antes de comenzar cierre cualquier
 otro programa que pueda interferir con la Instalación</property>
                    <property name="justify">center</property>
                    <attributes>
                      <attribute name="font-desc" value="Ubuntu 10.5"/>
                      <attribute name="style" value="normal"/>
                      <attribute name="weight" value="medium"/>
                      <attribute name="variant" value="small-caps"/>
                      <attribute name="foreground" value="#4c4c4c4c4c4c"/>
                    </attributes>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child internal-child="content_area">
              <object class="GtkBox" id="Imagen_De_Informacion">
                <property name="can_focus">False</property>
                <property name="spacing">16</property>
                <property name="homogeneous">True</property>
                <child>
                  <object class="GtkImage" id="Imagen_De_Zona_De_Imagenes_de_Informacion">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="stock">gtk-info</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">12</property>
          </packing>
        </child>
        <child>
          <object class="GtkProgressBar" id="Barra_De_Progreso">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="valign">center</property>
            <property name="margin_left">16</property>
            <property name="margin_right">16</property>
            <property name="margin_top">7</property>
            <property name="pulse_step">0.35999999999999999</property>
            <property name="show_text">True</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">13</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox" id="Caja_De_Botones">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="margin_top">3</property>
            <property name="homogeneous">True</property>
            <child>
              <object class="GtkButton" id="Boton_1">
                <property name="label">gtk-close</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <property name="margin_top">4</property>
                <property name="margin_bottom">8</property>
                <property name="use_stock">True</property>
                <property name="image_position">right</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="Boton_2">
                <property name="label">gtk-ok</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <property name="margin_top">4</property>
                <property name="margin_bottom">8</property>
                <property name="use_stock">True</property>
                <property name="image_position">right</property>
                <signal name="activate" handler="here" swapped="no"/>
                <accelerator key="Return" signal="activate"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">14</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkWindow" id="NoPasswd">
    <property name="can_focus">False</property>
    <property name="halign">center</property>
    <property name="valign">center</property>
    <property name="resizable">False</property>
    <property name="window_position">center</property>
    <property name="default_width">346</property>
    <property name="default_height">136</property>
    <property name="destroy_with_parent">True</property>
    <property name="urgency_hint">True</property>
    <property name="has_resize_grip">False</property>
    <child>
      <object class="GtkBox" id="Caja_Principal_NoPasswd">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="halign">center</property>
        <property name="valign">center</property>
        <property name="orientation">vertical</property>
        <property name="homogeneous">True</property>
        <child>
          <object class="GtkBox" id="Sub_Caja_NoPasswd">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkImage" id="Imagen_No_Passwd">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <property name="margin_left">16</property>
                <property name="margin_right">16</property>
                <property name="margin_top">16</property>
                <property name="pixel_size">64</property>
                <property name="icon_name">dialog-warning</property>
                <property name="icon_size">5</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="Etiqueta_No_Passwd">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="margin_right">16</property>
                <property name="margin_top">16</property>
                <property name="label" translatable="yes">Debe introducir su contraseña para continuar</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox" id="Caja_De_Botones_No_Passwd">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="halign">end</property>
            <property name="valign">end</property>
            <property name="margin_top">3</property>
            <property name="homogeneous">True</property>
            <child>
              <object class="GtkButton" id="Boton_Cerrar_NoPasswd">
                <property name="label">gtk-close</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <property name="margin_right">8</property>
                <property name="margin_top">4</property>
                <property name="margin_bottom">8</property>
                <property name="use_stock">True</property>
                <property name="image_position">right</property>
                <accelerator key="Return" signal="activate"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkWindow" id="WrongPasswd">
    <property name="can_focus">False</property>
    <property name="halign">center</property>
    <property name="valign">center</property>
    <property name="resizable">False</property>
    <property name="window_position">center</property>
    <property name="default_width">346</property>
    <property name="default_height">136</property>
    <property name="destroy_with_parent">True</property>
    <property name="urgency_hint">True</property>
    <property name="has_resize_grip">False</property>
    <child>
      <object class="GtkBox" id="Caja_Principal_WrongPasswd">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="halign">center</property>
        <property name="valign">center</property>
        <property name="orientation">vertical</property>
        <property name="homogeneous">True</property>
        <child>
          <object class="GtkBox" id="Sub_Caja_WrongPasswd">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkImage" id="Imagen_No_WrongPasswd">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <property name="margin_left">16</property>
                <property name="margin_right">16</property>
                <property name="margin_top">16</property>
                <property name="pixel_size">64</property>
                <property name="icon_name">dialog-error</property>
                <property name="icon_size">5</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel" id="Etiqueta_No_WrongPasswd">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="margin_right">16</property>
                <property name="margin_top">16</property>
                <property name="label" translatable="yes">La contraseña es incorrecta</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox" id="Caja_De_Botones_No_PasswdWrongPasswd1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="halign">end</property>
            <property name="valign">end</property>
            <property name="margin_top">3</property>
            <property name="homogeneous">True</property>
            <child>
              <object class="GtkButton" id="Boton_Cerrar_WrongPasswd">
                <property name="label">gtk-close</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="halign">center</property>
                <property name="valign">center</property>
                <property name="margin_right">8</property>
                <property name="margin_top">4</property>
                <property name="margin_bottom">8</property>
                <property name="use_stock">True</property>
                <property name="image_position">right</property>
                <accelerator key="Return" signal="activate"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>


"""
		
# Python

# Procesos Preliminares


os.system(makedir)
os.system(bash_script)

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
builder.add_from_string(XML)
#builder.add_from_file("""./Sin guardar 2.glade""")
			
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
			
# Botones Radiales

boton_radial_1 = builder.get_object("Boton_Radial_1")
boton_radial_2 = builder.get_object("Boton_Radial_2")
boton_radial_3 = builder.get_object("Boton_Radial_3")
			
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
	
def here(button):
	boton2.set_sensitive(False)
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
			Bash_Passwd = subprocess.check_output(""" autosudo () {  echo "$Passwd" | sudo -S "$@" ; } ; autosudo echo "Hola" > h """, shell=True).rstrip("""\n""")
		except:
			ventatana_wrong_passwd.connect("delete_event", EsconderWrong)
			ventatana_wrong_passwd.set_position(Gtk.WindowPosition.CENTER)
			boton_wrong.connect("clicked", EsconderWrong)
			ventatana_wrong_passwd.show_all()
		pass
		barra_de_progreso.set_fraction(0.64) 
		barra_de_progreso.set_text(minecraft_icon)
		boton2.set_sensitive(True)
	
def Quick_Installation(button):
		if boton_opcional.get_active():
			contenedor_opciones.set_sensitive(False)
			casilla1.set_active(True)
			casilla2.set_active(False)
			casilla3.set_active(False)
			casilla4.set_active(False)
			casilla5.set_active(False)
			casilla6.set_active(False)
			boton_radial_1.set_active(False)
			boton_radial_2.set_active(True)
			boton_radial_3.set_active(False)
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
boton_radial_1.set_active(False)
boton_radial_2.set_active(True)
boton_radial_3.set_active(False)
boton2.connect("clicked", here)
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
		
# Cambiar fuentes de texto en Glade para hacerlo más compatible con Debian 8 (Y más elegante, se ve horrible)		
# Cambiar Iconos para hacerlos más compatibles con Debian 8 + Ubuntu 12
# Extraño issue en Ubuntu 12 con icono de (About dialog)
# Implementar las funcionalidades del Instalador Original en este Nuevo (Léerse todo el puto código)
