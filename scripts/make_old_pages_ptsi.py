import os
chemins = [
        "../../01_IntroductionIS_Analyser",
        "../../03_Etude_Cinematique_Systemes_Solides_Chaine_Energie_Analyser_Modeliser_Resoudre",
        "../../04_Etude_Systemes_Electriques_Analyser_Modeliser_Resoudre_Realiser",
        "../../06_Etude_Statique_Systemes_Solides_Chaine_Energie_Analyser_Modeliser_Resoudre",
        "../../09_Etude_Dynamique_Systemes_Solides_Chaine_Energie_Analyser_Modeliser_Resoudre"
        ]


def make_pdf_list(chemins:[str]):
    """
    Réalisation de la liste de tous les fichier pdf.
    REnvoie une liste de dictionnaires :
    dico = {'fichier':file,'last_modif':modif:....}
    """
    tex_liste=[]
    for path in chemins :
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".pdf"):
                    if verif(root,file) :
                        dico = make_dico_from_pdf_file(root, file)
                        tex_liste.append(dico)


    return tex_liste

def verif(root,file):
    """
    Exclusion de fichiers
    """
    test = []
    for t in test :
        if (t in root) or (t in file) :
            return False
    return True

def make_dico_from_pdf_file(root, file):
    """
    Réalise un dictionnaire à partir d'un fichier tex

    Clés du dico :
     - full_chemin : chemin relatif + nom de fichier.tex par rapport au dossier de ce script
     - last_modif : dernière modification
     - chmein : chemin relatif du dossier
     - fichier : fichier.tex
     % "{'classe':(''),'chapitre':'','type':(''),'titre':'', 'source':' ','comp':(None),'corrige':True}"
    """
    fich = os.path.join(root, file)
    fich = fich.replace("\\","/")
    root = root.replace("\\","/")
    modif = os.path.getmtime(fich)

    dico = {'full_chemin':fich,'last_modif':modif,"chemin":root,"fichier":file}

    lien_pdf = "https://xpessoles-cpge.fr/pdf/old/"+dico['fichier']
    dico['lien_pdf'] = lien_pdf
    dico['source'] = lien_pdf

    dico['depot'] = dico["chemin"][6:].split("/")[0]
    dico['lien_git']="https://github.com/xpessoles/"+dico['depot']+"/tree/main"+dico["chemin"][6+len(dico['depot']):]

    return dico

def write_md(pdf_list) :
    fid = open('old_ptsi.md','r', encoding="utf8")
    fid.write("| Chemin | Fichier |  PDF  | Source | \n")
    fid.write("| :----- | :-----: | :---: | :----: | \n")

    for pdf in pdf_list :
        fid.write("|"+pdf['chemin'][5:]+"|")
        fid.write(pdf['fichier'][5:]+"|")
        fid.write("[:fontawesome-solid-file-pdf:]("+pdf['lien_pdf']+") | ")
        fid.write("[:material-github:]("+pdf["lien_git"]+") | \n")

    fid.close()
PDF_LISTE = make_pdf_list(chemins)
