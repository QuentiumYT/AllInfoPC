import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 2
__filename__ = "AllInfoPC"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:urllib.request.urlretrieve("http://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("http://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("http://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("http://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

import socket, platform, psutil, wmi, ctypes

os_info = wmi.WMI().Win32_OperatingSystem()[0]
proc_info = wmi.WMI().Win32_Processor()[0]
gpu_info = wmi.WMI().Win32_VideoController()[0]
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576
bits_str = str(ctypes.sizeof(ctypes.c_voidp))
bits_int = int(bits_str)
bits = bits_int * 8

def start_getinfos():
    file = open("InfosPC.txt", "w", encoding="utf-8")
    file.write("Information sur toutes les caractéristiques de votre PC :" + "\n"+ "\n")
    file.write("Informations sur Windows :" + "\n")
    file.write("" + "\n")
    file.write("Name : " + socket.gethostname() + "\n")
    file.write("FQDN : " + socket.getfqdn() + "\n")
    file.write("System Platform : " + sys.platform + "\n")
    file.write("Machine : " + platform.machine() + "\n")
    file.write("Node : " + platform.node() + "\n")
    file.write("Platform : " + platform.platform() + "\n")
    file.write("System OS : " + platform.system() + "\n")
    file.write("System bits : " + str(bits) + "\n")
    file.write("Release : " + platform.release() + "\n")
    file.write("Version : " + platform.version() + "\n")
    file.write("Number of CPUs : " + str(psutil.cpu_count()) + "\n")
    file.write("Number of Physical CPUs : " + str(psutil.cpu_count(logical=False)) + "\n")
    file.write("Version : " + platform.python_version() + "\n")
    file.write("Compiler : " + platform.python_compiler() + "\n")
    file.write("Build version : " + platform.python_build()[0] + "\n")
    file.write("Build date : " + platform.python_build()[1] + "\n")
    file.write("\n")
    file.write("Informations sur le PC :" + "\n")
    file.write("\n")
    file.write("CPU : " + str(proc_info.Name) + "\n")
    file.write("RAM : " + str(system_ram) + " GB" + "\n")
    file.write("Graphics Card : " + str(gpu_info.Name) + "\n")
    file.write("Pocessor : " + platform.processor() + "\n")
    file.write("Memory total : " + str(psutil.virtual_memory()[0]) + "\n")
    file.write("Memory available : " + str(psutil.virtual_memory()[1]) + "\n")
    file.write("Memory used : " + str(psutil.virtual_memory()[3]) + "\n")
    file.write("Memory percent : " + str(psutil.virtual_memory()[2]) + "\n")
    file.write("Memory free : " + str(psutil.virtual_memory()[4]) + "\n")
    file.close()
    allinfopc.destroy()

allinfopc = Tk()
width = 750
height = 500
allinfopc.update_idletasks()
x = (allinfopc.winfo_screenwidth() - width) // 2
y = (allinfopc.winfo_screenheight() - height) // 2
allinfopc.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
allinfopc.resizable(width=False, height=False)
allinfopc.configure(bg = "lightgray")
if os.path.exists(__iconpath__):
    allinfopc.iconbitmap(__iconpath__)
allinfopc.title(__filename__)
Label(allinfopc, text="Bienvenue dans le programme AllInfoPC !", font="impact 30", fg="red", bg="lightgray").pack(pady=80)
Button(allinfopc, text="Récupérer les infos", command=start_getinfos, relief=GROOVE, width=25, font="impact 20", fg="black").pack(pady=50)
allinfopc.mainloop()
