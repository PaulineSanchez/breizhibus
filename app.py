from flask import Flask, render_template, request, redirect, url_for 
import bdd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('choix.html')

@app.route('/usager')
def index2():
    return render_template('page-principale-bus.html')

@app.route('/pro', methods=["POST"])
def index3():
    nom = request.values.get('nom')
    mdp = request.values.get('mdp')
    if bdd.test(nom, mdp) == 0:
        return render_template('choix.html')
    else:
        liste_bus = bdd.lire_bus()
        return render_template('bus.html', liste_bus=liste_bus)

@app.route('/bus/ajouter')
def bus_ajout():
    return render_template('page-ajout-bus.html')

@app.route('/bus/modifier')
def bus_modif():
    liste_bus = bdd.lire_bus()
    return render_template('modif_bus.html', liste_bus=liste_bus)

@app.route('/bus/supprimer')
def bus_sup():
    liste_bus = bdd.lire_bus()
    return render_template('supp_bus.html', liste_bus=liste_bus)

@app.route('/affichage', methods=( "GET","POST"))
def aff():
    ligne = request.values.get('choixligne')
    liste_bus = bdd.lire_bus()
    liste_ar_ad = bdd.lire_arret_ligne(ligne)
    return render_template('affichage.html', liste_bus=liste_bus, liste_ar_ad=liste_ar_ad, ligne=ligne)

@app.route('/ajout', methods=["POST"])
def ajout():
    numero = request.values.get("numero")
    immatriculation = request.values.get("immatriculation")
    nombre_place = request.values.get("nombre_place")
    ligne = request.values.get("ligne")
    ajouter = bdd.ajout_bus(numero, immatriculation, nombre_place, ligne)
    liste_bus = bdd.lire_bus()
    return render_template('bus_ajout.html', ajouter=ajouter, liste_bus=liste_bus)

@app.route('/modif', methods=["POST"])
def modif():
    numero = request.values.get("numero")
    immatriculation = request.values.get("immatriculation")
    nombre_place = request.values.get("nombre_place")
    ligne = request.values.get("ligne")
    modifier = bdd.modif_bus(immatriculation, nombre_place, ligne, numero)
    liste_bus = bdd.lire_bus()
    print(len(liste_bus))
    return render_template('bus_ajout.html', modifier=modifier, liste_bus=liste_bus)

@app.route('/supp', methods=["POST"])
def supp():
    numero = request.values.get("numero")
    supprimer = bdd.supprimer_bus(numero)
    liste_bus = bdd.lire_bus()
    return render_template('bus_ajout.html', supprimer=supprimer, liste_bus=liste_bus)


if __name__ == "__main__":
    app.run(debug=True, port=5001)