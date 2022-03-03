import mysql.connector as mysqlpyth

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor
    
    bdd = mysqlpyth.connect(user='root', password='root', host='localhost', port="8081", database='breizhibus2')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()

def lire_bus():
    global cursor

    connexion()
   
    query = "SELECT * FROM bus"

    cursor.execute(query)
    liste_bus = []

    for enregistrement in cursor :
        bus = {}
        bus['id_bus'] = enregistrement[0]
        bus['numero'] = enregistrement[1]
        bus['immatriculation'] = enregistrement[2]
        bus['nombre_place'] = enregistrement[3]
        bus['id_ligne'] = enregistrement[4]
        liste_bus.append(bus)

    deconnexion()
    return liste_bus



def lire_arret_ligne(ligne):
    global cursor

    connexion()
   
    query = 'SELECT nom_arret, adresse FROM arrets natural join arrets_lignes natural join lignes where nom_lig="'+ligne+'";'

    cursor.execute(query)
    liste_ar_ad = []

    for enregistrement in cursor :
        bus = {}
        bus['nom_arret'] = enregistrement[0]
        bus['adresse'] = enregistrement[1]
        liste_ar_ad.append(bus)

    deconnexion()
    return liste_ar_ad

def ajout_bus(numero, immatriculation, nombre_place, ligne):
    global cursor
    global bdd

    connexion()
   
    query = 'INSERT INTO bus(numero, immatriculation, nombre_place, id_ligne) VALUES ("'+ numero +'","'+ immatriculation +'", "'+ nombre_place +'", (SELECT id_ligne FROM lignes WHERE nom_lig = "'+ ligne +'"));'

    cursor.execute(query)
    bdd.commit()

    deconnexion()

def test(nom, mdp): 
    global cursor 
    
    connexion()
    
    query = 'SELECT nom, mdp FROM admins WHERE nom="'+nom+'" AND mdp="'+mdp+'";'
    cursor.execute(query) 
    
    test = cursor.fetchall()
    
    deconnexion()
    
    return len(test)

def lire_bus():
    global cursor

    connexion()
   
    query = 'SELECT numero, immatriculation, nombre_place, nom_lig FROM bus natural join lignes;'

    cursor.execute(query)
    liste_bus = []

    for enregistrement in cursor :
        bus = {}
        bus['numero'] = enregistrement[0]
        bus['immatriculation'] = enregistrement[1]
        bus['nombre_place'] = enregistrement[2]
        bus['ligne'] = enregistrement[3]
        liste_bus.append(bus)
    print(len(liste_bus))


    deconnexion()
    return liste_bus

def modif_bus(immatriculation, nombre_place, ligne, numero):
    global cursor
    global bdd

    connexion()
   
    query = 'UPDATE bus SET immatriculation="'+immatriculation+'", nombre_place="'+nombre_place+'", id_ligne=(SELECT id_ligne FROM lignes WHERE nom_lig="'+ligne+'") WHERE numero="'+ numero +'";'

    cursor.execute(query)
    bdd.commit()

    deconnexion()

def supprimer_bus(numero):
    global cursor
    global bdd

    connexion()
   
    query = 'DELETE FROM bus WHERE numero="'+numero+'";'

    cursor.execute(query)
    bdd.commit()

    deconnexion()