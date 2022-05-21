print("Bienvenue au Calculaeur (Calculateur santé/sans T)")
#######################################################################################
# PARTIE 1 : QUESTIONNAIRE
#######################################################################################
# Rappel des questions à poser:
#   Pour chaque jour
#       Avez-vous déjeuné ce matin? (o/n)
#       Quelle fraction de votre alimentation a consisté de fruits et légumes?
#       Combien de minutes d'activité physique avez-vous effectué?
#       Souhaitez-vous ajouter un jour? (o/n)
#######################################################################################
ajout_jour = ("o")
numero_jour = int(0)
dejeune = tuple()
fruit_legume = tuple()
activite_physique = tuple()
sante = 0

while ajout_jour == "o" :
    numero_jour = numero_jour + 1
    print("jour", numero_jour)

    dejeune = dejeune + (str(input("Avez vous dejeuné ce matin? (o/n):", )),)
    fruit_legume = fruit_legume + (float(input("Quelle fraction de votre alimentation a consisté de fruits et légumes?:", )),)
    activite_physique = activite_physique + (int(input("Combien de minutes d'activité physique avez-vous effectué?:", )),)
    ajout_jour = input("Souhaitez-vous ajouter un jour? (o/n):", )

#######################################################################################
# PARTIE 2 : CALCUL #

#######################################################################################
# Rappel des phrases à (possiblement) afficher:
#   Vous ne mangez pas équilibré tous les jours! Visez 50% de légumes. ( si 1 journé utilisateur a mange -0.2 ou + 0.8)
#   Vous ne faites pas suffisamment de sport! Visez 30 minutes par jour en moyenne. (moyenne activite physique <= 30)
#   Attention! Vous ne devez pas faire du sport sur un estomac vide! (si il as pas mangé mais as fait du sport pendant 1 jour)
#######################################################################################

print("Calcul des conseils en cours...\n")

#CALCUL MANGER ÉQUILIBRÉ
nombre_dans_seq = 0
somme_legume = 0

while nombre_dans_seq != numero_jour :
    pourcentage_legume = fruit_legume[nombre_dans_seq]
    if pourcentage_legume < 0.2 or pourcentage_legume > 0.8:
        print("Vous ne mangez pas equilibré tous les jours! Visez 50% de légumes.")
        nombre_dans_seq = numero_jour
    else: nombre_dans_seq = nombre_dans_seq + 1

if pourcentage_legume > 0.2 or pourcentage_legume < 0.8:
    sante = sante + 1

#CALCUL MOYENNE ACTIVITÉ PHYSIQUE

nombre_dans_seq = 0
somme_physique = 0
while nombre_dans_seq != numero_jour :
    temps_activite = activite_physique[nombre_dans_seq]
    somme_physique = temps_activite + somme_physique
    nombre_dans_seq = nombre_dans_seq + 1

    moyenne_physique = somme_physique / numero_jour

if moyenne_physique <= 30:
    print("Vous ne faites pas suffisamment de sport! Visez 30 minutes par jour en moyenne.")
else: sante = sante + 1

#CALCUL SI SPORT SANS MANGER

nombre_dans_seq = 0
while nombre_dans_seq != numero_jour :
    temps_activite = activite_physique[nombre_dans_seq]
    dejeune_ce_jour = dejeune[nombre_dans_seq]
    if dejeune_ce_jour == "n" and temps_activite > 0:
        print("Attention! Vous ne devez pas faire du sport sur un estomac vide!")
        nombre_dans_seq = numero_jour
    else : nombre_dans_seq = nombre_dans_seq + 1
if dejeune_ce_jour == "o" and temps_activite > 0 :
    sante = sante + 1
print("Fin du calcul!\n")

if sante == 3:
    print("Vous mangez et bougez très bien! Continuez sur cette belle lancée.")

print("Passez une belle journée!")
