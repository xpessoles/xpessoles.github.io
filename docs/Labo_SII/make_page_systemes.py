import os
liste_dico_syst = [
    {
    'num'           :'01',
    'systeme'       :'bgr-300',
    'nom'           :'BGR-300',
    'equip'         :'DIDASTEL',
    'site_equip'    :'http://www.didastel.fr/',
    'description'   :"Boule gyrostabilisée 2 étages",
    'logo'          :"../img/bgr-300.png",
    'page'          :"bgr-300",
    'flag'          :True
    },
    {
    'num'           :'02',
    'systeme'       :'bras-beta',
    'nom'           :'Bras BETA',
    'equip'         :'S2IDIDAC',
    'site_equip'    :'https://s2ididac.com/',
    'description'   :"Le Bras BETA reproduit un système de cotrôle de tubes de géérateur de vapeur.",
    'logo'          :"../img/bras-beta.png",
    'page'          :"bras-beta",
    'flag'          :True
    },
    {
    'num'           :'03',
    'systeme'       :'cheville-nao',
    'nom'           :'Cheville NAO',
    'equip'         :'ERM',
    'site_equip'    :'https://www.erm-automatismes.com/',
    'description'   :"Cheville didactisée du robot NAO",
    'logo'          :"../img/cheville-nao.png",
    'page'          :"cheville-nao",
    'flag'          :True
    },
    {
    'num'           :'04',
    'systeme'       :'comax',
    'nom'           :'CoMAX',
    'equip'         :'DIDASTEL',
    'site_equip'    :'http://www.didastel.fr/',
    'description'   :"Le robot collaboratif CoMAX est un système permettant d'assister le maniemnent des charges lourdes.",
    'logo'          :"../img/comax.png",
    'page'          :"comax",
    'flag'          :True
    },
    {
    'num'           :'05',
    'systeme'       :'controlx',
    'nom'           :'ControlX',
    'equip'         :'DMS',
    'site_equip'    :'https://www.dmseducation.eu/',
    'description'   :"Le ControlX est un axe industriel asservi.",
    'logo'          :"../img/controlx.png",
    'page'          :"controlx",
    'flag'          :True
    },
    {
    'num'           :'06',
    'systeme'       :'cordeuse',
    'nom'           :'Cordeuse',
    'equip'         :'DMS',
    'site_equip'    :'https://www.dmseducation.eu/',
    'description'   :"Cordeuse de raquette didactisée.",
    'logo'          :"../img/cordeuse.png",
    'page'          :"cordeuse",
    'flag'          :True
    },
    {
    'num'           :'07',
    'systeme'       :'dae',
    'nom'           :'Direction Assistée Electrique',
    'equip'         :'DMS',
    'site_equip'    :'https://www.dmseducation.eu/',
    'description'   :"La DAE est un système instrumentée issue d'une TWINGO",
    'logo'          :"../img/dae.png",
    'page'          :"dae",
    'flag'          :True
    },
    {
    'num'           :'08',
    'systeme'       :'d2c',
    'nom'           :'D2C',
    'equip'         :'DMS',
    'site_equip'    :'https://www.dmseducation.eu/',
    'description'   :"Le Drone Didactique Commandé permet d'anlyser le tangage d'un drone",
    'logo'          :"../img/d2c.png",
    'page'          :"d2c",
    'flag'          :True
    },
    {
    'num'           :'09',
    'systeme'       :'ericc',
    'nom'           :'Ericc 3',
    'equip'         :'',
    'site_equip'    :'',
    'description'   :"Le robot Ericc 3 est un robot industriel 6 axes.",
    'logo'          :"../img/ericc.png",
    'page'          :"ericc",
    'flag'          :True
    },
    {
    'num'           :'10',
    'systeme'       :'evolap',
    'nom'           :'Evolap',
    'equip'         :'DMS',
    'site_equip'    :'https://www.dmseducation.eu/',
    'description'   :"L'evolap s'inspire du fonctionnement d'un robot endoscopique.",
    'logo'          :"../img/evolap.png",
    'page'          :"evolap",
    'flag'          :True
    },
    {
    'num'           :'11',
    'systeme'       :'maxpid',
    'nom'           :'MaxPID',
    'equip'         :'DIDASTEL',
    'site_equip'    :'http://www.didastel.fr/',
    'description'   :"Les MaxPID et MaxPID-E sont la partie opérative de robots.",
    'logo'          :"../img/maxpid.png",
    'page'          :"maxpid",
    'flag'          :True
    },
    {
    'num'           :'12',
    'systeme'       :'moteurcc',
    'nom'           :'Moteur à courant continu',
    'equip'         :'3sigma',
    'site_equip'    :'https://3sigma.fr/Accueil.html',
    'description'   :"Platine équipée d'un moteur à courant continu permettant d'analyser son fonctionnement.",
    'logo'          :"../img/moteurcc.png",
    'page'          :"moteurcc",
    'flag'          :True
    },
    {
    'num'           :'13',
    'systeme'       :'moby-crea',
    'nom'           :'Moby Crea',
    'equip'         :'CREA',
    'site_equip'    :'https://crea-technologie.com/fr/',
    'description'   :"Système permettant d'aider au bercement des bébés.",
    'logo'          :"../img/moby-crea.png",
    'page'          :"moby-crea",
    'flag'          :True
    },
    {
    'num'           :'14',
    'systeme'       :'pilote-auto',
    'nom'           :'Pilote Automatique de Voilier',
    'equip'         :'CREA',
    'site_equip'    :'https://crea-technologie.com/fr/',
    'description'   :"Bloc hydraulique permettant d'asservir la position du safran d'un voilier.",
    'logo'          :"../img/pilote-auto.png",
    'page'          :"pilote-auto",
    'flag'          :True
    },
    {
    'num'           :'15',
    'systeme'       :'portail',
    'nom'           :'Portail ABB',
    'equip'         :'',
    'site_equip'    :'',
    'description'   :"Fermeture automatique d'un portail.",
    'logo'          :"../img/portail.png",
    'page'          :"portail",
    'flag'          :True
    },
    {
    'num'           :'16',
    'systeme'       :'rc4',
    'nom'           :'Robot à câbles RC4',
    'equip'         :'DIDASTEL',
    'site_equip'    :'http://www.didastel.fr/',
    'description'   :"Robot à câbles plan",
    'logo'          :"../img/rc4.png",
    'page'          :"rc4",
    'flag'          :True
    },
    {
    'num'           :'17',
    'systeme'       :'robot-delta',
    'nom'           :'Robot Delta 2D',
    'equip'         :'3sigma',
    'site_equip'    :'https://3sigma.fr/Accueil.html',
    'description'   :"Robot delta2D plan",
    'logo'          :"../img/robot-delta.png",
    'page'          :"robot-delta",
    'flag'          :True
    },
    {
    'num'           :'18',
    'systeme'       :'robot-haptique',
    'nom'           :'Robot Haptique',
    'equip'         :'',
    'site_equip'    :'',
    'description'   :"Robot à retour de forces.",
    'logo'          :"../img/robot-haptique.png",
    'page'          :"robot-haptique",
    'flag'          :True
    },
    {
    'num'           :'19',
    'systeme'       :'sympact',
    'nom'           :'Barrière Symapct',
    'equip'         :'DIDASTEL',
    'site_equip'    :'http://www.didastel.fr/',
    'description'   :"Barrière automatisée.",
    'logo'          :"../img/sympact.png",
    'page'          :"sympact",
    'flag'          :True
    },
    {
    'num'           :'20',
    'systeme'       :'toit-206',
    'nom'           :'Toit de 206 cc',
    'equip'         :'DMS',
    'site_equip'    :'https://www.dmseducation.eu/',
    'description'   :"Toit automatisé de 206 CC piloté par un groupe hydraulique.",
    'logo'          :"../img/toit-206.png",
    'page'          :"toit-206",
    'flag'          :True
    },
    {
    'num'           :'21',
    'systeme'       :'tourelle',
    'nom'           :'Tourelle 2 axes',
    'equip'         :'S2IDIDAC',
    'site_equip'    :'https://s2ididac.com/',
    'description'   :"Tourelle 2 axes pour faire des vidéos avec des téléphones portables.",
    'logo'          :"../img/tourelle.png",
    'page'          :"tourelle",
    'flag'          :True
    },
    {
    'num'           :'22',
    'systeme'       :'i3d',
    'nom'           :'Imprimante 3D',
    'equip'         :'DIDASTEL',
    'site_equip'    :'http://www.didastel.fr/',
    'description'   :"Imprimante 3D didactisée",
    'logo'          :"../img/i3d.png",
    'page'          :"i3d",
    'flag'          :True
    },
    {
    'num'           :'23',
    'systeme'       :'plateforme',
    'nom'           :'Plateforme 6 axes',
    'equip'         :'',
    'site_equip'    :'',
    'description'   :"Plateforme Stewart 6 axes, vérins électriques",
    'logo'          :"../img/plateforme.png",
    'page'          :"plateforme",
    'flag'          :True
    },
    {
    'num'           :'2',
    'systeme'       :'',
    'nom'           :'',
    'equip'         :'',
    'site_equip'    :'',
    'description'   :"",
    'logo'          :"../img/.png",
    'page'          :"",
    'flag'          :False
    },
    {
    'num'           :'90',
    'systeme'       :'arduino',
    'nom'           :'Arduino',
    'equip'         :'Arduino',
    'site_equip'    :'https://www.arduino.cc/',
    'description'   :"Pilotage de cartes Arduino",
    'logo'          :"../img/arduino.png",
    'page'          :"arduino",
    'flag'          :True
    },
    {
    'num'           :'91',
    'systeme'       :'sw',
    'nom'           :'Solidworks',
    'equip'         :'Dassault Systèmes',
    'site_equip'    :'https://www.3ds.com/fr/',
    'description'   :"Modélisation géométrique et cinématique avec SolidWors et Méca 3D.",
    'logo'          :"../img/sw.svg",
    'page'          :"sw",
    'flag'          :True
    },
    {
    'num'           :'92',
    'systeme'       :'matlab',
    'nom'           :'Matlab Simulink',
    'equip'         :'Mathworks',
    'site_equip'    :'https://fr.mathworks.com/',
    'description'   :"Modélisation des systèmes avec Matlab et Simulink.",
    'logo'          :"../img/matlab.svg",
    'page'          :"matlab",
    'flag'          :True
    },
]

dico_code_tp = {
        "01" : "Mise en service",
        "02" : "Chaine Fonctionnelle",
        "03" : "Chaines de solides",
        "04" : "Résolution géométrique et cinématique",
        "05" : "",
        "06" : "Modélisation système",
        "07" : "Modélisation composant",
        "08" : "",
        "09" : "Dimensionnement d'un actionneur",
        "10" : "Analyse de l'effet des correcteurs",
        "11" : "",
        "12" : "Choix et Synthèse des correcteurs",}
def creation_index(liste_sys):
    """
    Creation de la page index.md des systèmes.
    """
    print("Creation du fichier index.md")

    fid = open('index.md',"w",encoding='utf8')
    fid.write('[comment]: <> (Généré automatiquement par make_page_systemes.py, creation_index)\n\n')
    fid.write('<div class="grid cards" markdown> \n')
    fid.write('\n')
    for systeme in liste_sys :
        if systeme['flag']:
            fid.write("-   :octicons-graph-16:{ .lg .middle } __"+systeme['nom']+"__\n \n" )
            fid.write('    --- \n \n')
            fid.write("    "+systeme['description']+ " ["+systeme['equip']+"]("+systeme['site_equip']+")\n")
            fid.write('    !['+systeme['nom']+']('+systeme['logo']+"){ align=left } \n \n")
            fid.write("    [:octicons-arrow-right-24: "+systeme['nom']+"]("+systeme['page']+".md) \n\n")
    fid.write("</div> \n")
    fid.close()

def creation_nav(liste_sys):
    """
    Création du fichier du paragraphe de nav à ajouter dans mkdocs.yml
    """

    fid = open("nav_labo.yml","w",encoding = 'utf8')
    fid.write('- Labo SII: \n')
    fid.write('    - Labo_SII/index.md \n')

    for systeme in liste_sys :
        if systeme['flag']:
            fid.write('    - '+systeme['nom']+' : Labo_SII/'+systeme['systeme']+'.md\n')
    fid.close()

    print("Modifier le fichier mkdocs.yml")


def creation_fichiers_systemes(liste_sys,docx_lst):
    """
    Création de fichiers correspodas aux systèmes
    """
    print("Creation d'un fichier md par système.")

    for systeme in liste_sys :

        docx = get_dico_syst_in_liste_dico_syst(systeme['page'],docx_lst)

        fid = open(systeme['page']+".md","w",encoding = 'utf8')

        ## Titre de la page & Tags
        fid.write('---\n')
        fid.write('title: '+systeme["nom"]+" \n")
        fid.write("tags:\n")
        fid.write('  - '+systeme["page"]+"\n")
        for doc in docx :
            if 'tp' in doc['type']:
                fid.write("  - TP-"+doc["code_tp"]+"\n")
        fid.write('---\n\n')

        fid.write('[comment]: <> (Généré automatiquement par make_page_systemes.py, creation_fichiers_systemes)\n\n')



        ## Documentation
        fid.write("## Documentation \n")
        for doc in docx :
            if 'doc' in doc['type']:
                #print(doc)
                fid.write("- [:fontawesome-solid-file-word:]("+doc['chemin_word']+") [:material-github:]("+doc['chemin_git']+")   Documentation \n\n")


        ## Sujets de TP
        fid.write("## Sujets \n")
        for doc in docx :
            if 'tp' in doc['type']:

                fid.write("- [:fontawesome-solid-file-word:]("+doc['chemin_word']+") [:material-github:]("+doc['chemin_git']+") "+doc["code_tp"]+" : "+dico_code_tp[doc["code_tp"]]+"\n")



        fid.close()




def make_docx_list(chemins:[str]):
    """
    Réalisation de la liste de tous les fichier tex.
    REnvoie une liste de dictionnaires :
    dico = {'fichier':file,'last_modif':modif:....}
    """
    docx_liste=[]
    for path in chemins :
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".docx"):
                    if verif(root,file) :
                        dico = make_dico_from_docx_file(root, file)
                        docx_liste.append(dico)


    return docx_liste

def make_dico_from_docx_file(root, file):
    """
    Réalise un dictionnaire à partir d'un fichier tex

    Clés du dico :
     - full_chemin : chemin relatif + nom de fichier.tex par rapport au dossier de ce script
     - last_modif : dernière modification
     - chemin : chemin relatif du dossier
     - fichier : fichier.docx
    """
    fich = os.path.join(root, file)
    fich = fich.replace("\\","/")
    root = root.replace("\\","/")
    modif = os.path.getmtime(fich)


    dico = {
        'full_chemin':fich,
        'last_modif':modif,
        "chemin":root,
        "fichier":file}
    dico['num_systeme'] = file[0:2]
    dico['systeme'] = get_systeme_in_liste_dico_syst(dico['num_systeme'],liste_dico_syst)

    if "TP_Documents_PSI" in fich :
        index = fich.index("TP_Documents_PSI")+len("TP_Documents_PSI/")
        dico['blob']  = fich[index:]
        dico['depot'] = 'TP_Documents_PSI'
        c = root.split("/")
        dico['chemin_git'] = 'https://github.com/xpessoles/TP_Documents_PSI'+"/"+"tree/master/"+c[-1]
        dico['chemin_word'] = 'https://github.com/xpessoles/'+dico['depot']+'/raw/master/'+dico["blob"]
        dico['type'] = "(doc)"

    elif "TP_Sujets" in fich :

        dico['depot'] = 'TP_Sujets'
        index = fich.index("TP_Sujets")+len("TP_Sujets/")
        dico['blob']  = fich[index:]
        dico['type'] = "(tp)"
        dico['code_tp'] = dico['blob'][0:2]
        dico['chemin_word'] = 'https://github.com/xpessoles/'+dico['depot']+'/raw/main/'+dico["blob"]
        c = root.split("/")
        dico['chemin_git'] = 'https://github.com/xpessoles/TP_Sujets'+"/"+"tree/main/"+c[-1]

    return dico



def verif(root,file):
    """
    Exclusion de fichiers
    """
    test = [
    "00_",
    "Colle",
    "old",'TODO',"OLD",
    "99_","98_","TD_Systemes",
    "DocumentsLogicielsSimulation.docx"
    ]
    for t in test :
        if (t in root) or (t in file) :
            return False
    return True

chemins_docx = [
                "../../../TP_Sujets",
                "../../../TP_Documents_PSI",]

def get_systeme_in_liste_dico_syst(num_systeme,liste_dico_syst):
    # Récupere le nim d'un système à partir de son numéro

    for s in liste_dico_syst:
        if s['num'] == num_systeme :
            return s['page']
    return ''

def get_dico_syst_in_liste_dico_syst(systeme,docx_lst):
    # Récupere les fichiers liés à un systeme

    res = []
    for d in docx_lst:
        if d['systeme'] == systeme :
            res.append(d)
    return res

docx_lst=make_docx_list(chemins_docx)


#for d in docx_lst:
#    print( d)
# A DECOMENTER SUIVANT CE QU'ON VEUT


# creation_index(liste_dico_syst)
creation_fichiers_systemes(liste_dico_syst,docx_lst)
# creation_nav(liste_dico_syst)