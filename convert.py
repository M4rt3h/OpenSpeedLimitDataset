from pathlib import Path
from PIL import Image

def traiter_dossier_securise(chemin_dossier):
    dossier = Path(chemin_dossier)
    
    if not dossier.is_dir():
        print(f"Erreur : '{chemin_dossier}' n'est pas un dossier valide.")
        return

    extensions_a_convertir = {'.jpg', '.jpeg', '.ppm'}
    prefixe_temp = "tmp_sec_"
    
    fichiers = [f for f in dossier.iterdir() if f.is_file() and not f.name.startswith(prefixe_temp)]
    fichiers.sort()

    compteur = 0

    # Étape 1 : Conversion et renommage avec un préfixe temporaire
    for fichier in fichiers:
        extension = fichier.suffix.lower()
        nouvelle_extension = '.png' if extension in extensions_a_convertir else extension
        chemin_sortie_temp = dossier / f"{prefixe_temp}{compteur}{nouvelle_extension}"

        try:
            if extension in extensions_a_convertir:
                with Image.open(fichier) as img:
                    img.save(chemin_sortie_temp, format="PNG")
                fichier.unlink()
            else:
                fichier.rename(chemin_sortie_temp)
            
            compteur += 1
            
        except Exception as e:
            print(f"Erreur sur {fichier.name} : {e}")

    # Étape 2 : Suppression du préfixe temporaire pour obtenir les noms définitifs
    for fichier_temp in dossier.glob(f"{prefixe_temp}*"):
        nom_final = fichier_temp.name.replace(prefixe_temp, "", 1)
        chemin_final = dossier / nom_final
        fichier_temp.rename(chemin_final)

    print(f"\nTerminé. {compteur} fichier(s) traité(s) sans conflit.")

if __name__ == "__main__":
    dossier_images = "./1" 
    
    traiter_dossier_securise(dossier_images)
