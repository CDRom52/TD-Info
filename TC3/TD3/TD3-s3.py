import http.server
import socketserver
from urllib.parse import urlparse, parse_qs, unquote
import json

# numéro du port TCP utilisé par le serveur
port_serveur = 8080

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    """Classe dérivée pour traiter les requêtes entrantes du serveur"""

    # sous-répertoire racine des documents statiques
    static_dir = 'client'

    def __init__(self, *args, **kwargs):
        """Surcharge du constructeur pour imposer 'client' comme sous répertoire racine"""
        super().__init__(*args, directory=self.static_dir, **kwargs)

    def do_GET(self):
        """Traiter les requêtes GET (surcharge la méthode héritée)"""
        self.init_params()

        # prénom et nom dans le chemin d'accès
        if self.path_info[0] == "coucou":
            self.send_coucou()

        # prénom et nom dans la chaîne de requête
        elif self.path_info[0] == "toctoc":
            self.send_toctoc()

        # requête générique
        elif self.path_info[0] == "service":
            self.send_service()   

        # sinon : comportement par défaut
        else:
            super().do_GET()


    def do_POST(self):
        """Traiter les requêtes POST"""
        self.init_params()

        # prénom et nom dans le corps de la requête
        if self.path_info[0] == "toctoc":
            self.send_toctoc()
          
        # requête générique
        elif self.path_info[0] == "service":
            self.send_service()   

        else:
            self.send_error(405)


    def send_coucou(self):
        """Générer une réponse en JSON contenant le nom et prénom passés dans le chemin d'accès"""
        # On extrait les valeurs
        prenom = self.path_info[1] if len(self.path_info) > 1 else ""
        nom = self.path_info[2] if len(self.path_info) > 2 else ""

        # On crée une structure de données propre (Dictionnaire)
        data = {
            "message": f"Bonjour {prenom} {nom}",
            "prenom": prenom,
            "nom": nom,
            "provenance": "path_info"
        }
        
        # On sérialise en chaîne JSON
        body = json.dumps(data, ensure_ascii=False)
        headers = [('Content-Type', 'application/json;charset=utf-8')]
        self.send(body, headers)


    def send_toctoc(self):
        """Générer une réponse en JSON contenant le nom et prénom passés dans les paramètres"""
        # Récupération sécurisée (parse_qs renvoie des listes)
        prenom = self.params.get('Prenom', [''])[0]
        nom = self.params.get('Nom', [''])[0]

        data = {
            "message": f"Bonjour {prenom} {nom}",
            "prenom": prenom,
            "nom": nom,
            "provenance": "params"
        }
        
        body = json.dumps(data, ensure_ascii=False)
        headers = [('Content-Type', 'application/json;charset=utf-8')]
        self.send(body, headers)


    def send_service(self):
        """Générer une réponse en JSON retournant les détails techniques de la requête"""
        data = {
            "path_info": self.path_info,
            "query_string": self.query_string,
            "body_brut": self.body,
            "params_analyses": self.params
        }

        body = json.dumps(data, ensure_ascii=False)
        headers = [('Content-Type', 'application/json;charset=utf-8')]
        self.send(body, headers)     


    def send(self, body, headers=[]):
        """Envoyer la réponse au client avec le corps et les en-têtes fournis"""
        # on encode la chaine de caractères à envoyer
        encoded = bytes(body, 'UTF-8')

        # on envoie la ligne de statut
        self.send_response(200)

        # on envoie les lignes d'entête et la ligne vide
        [self.send_header(*t) for t in headers]
        self.send_header('Content-Length', int(len(encoded)))
        self.end_headers()

        # on envoie le corps de la réponse
        self.wfile.write(encoded)
        

    def init_params(self):
        """Analyse la requête pour initialiser nos paramètres"""
        # analyse de l'adresse
        info = urlparse(self.path)
        self.path_info = [unquote(v) for v in info.path.split('/')[1:]]
        self.query_string = info.query
        
        # récupération des paramètres dans la query string
        self.params = parse_qs(info.query)

        # récupération du corps et des paramètres (2 encodages traités)
        length = self.headers.get('Content-Length')
        ctype = self.headers.get('Content-Type')
        if length:
          self.body = str(self.rfile.read(int(length)),'utf-8')
          if ctype == 'application/x-www-form-urlencoded' : 
            self.params = parse_qs(self.body)
          elif ctype == 'application/json' :
            self.params = json.loads(self.body)
        else:
          self.body = ''
       
        # traces
        print('info_path =',self.path_info)
        print('body =',length,ctype,self.body)
        print('params =', self.params)


# Programme principal
if __name__ == '__main__' :
    # instanciation et lancement du serveur
    httpd = socketserver.TCPServer(("", port_serveur), RequestHandler)
    print(f"Serveur actif sur le port {port_serveur}...")
    httpd.serve_forever()