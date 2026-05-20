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

        # IMPORTANT : On vérifie si le premier élément du chemin est "toctoc"
        # Exemple d'URL : /toctoc/Jean/Dupont -> path_info = ['toctoc', 'Jean', 'Dupont']
        if len(self.path_info) > 0 and self.path_info[0] == "toctoc":
            self.send_toctoc_path()

        # Ancien système "coucou" (au cas où)
        elif len(self.path_info) > 0 and self.path_info[0] == "coucou":
            self.send_coucou()

        # Requête générique
        elif len(self.path_info) > 0 and self.path_info[0] == "service":
            self.send_service()   

        # Sinon : comportement par défaut (fichiers statiques comme TD3-s4.html)
        else:
            super().do_GET()


    def do_POST(self):
        """Traiter les requêtes POST"""
        self.init_params()

        if len(self.path_info) > 0 and self.path_info[0] == "toctoc":
            # Si on fait du POST, les données sont dans le body, on garde l'ancien comportement ou erreur
            self.send_error(405, "Utilisez GET pour le format d'URL /toctoc/prenom/nom")
          
        elif len(self.path_info) > 0 and self.path_info[0] == "service":
            self.send_service()   

        else:
            self.send_error(405)


    def send_coucou(self):
        """Générer une réponse en JSON contenant le nom et prénom passés dans le chemin d'accès"""
        prenom = self.path_info[1] if len(self.path_info) > 1 else ""
        nom = self.path_info[2] if len(self.path_info) > 2 else ""

        data = {
            "message": f"Bonjour {prenom} {nom}",
            "prenom": prenom,
            "nom": nom,
            "provenance": "path_info_coucou"
        }
        self.envoyer_json(data)


    def send_toctoc_path(self):
        """Nouvelle méthode : extrait le prénom et le nom directement depuis le chemin de l'URL"""
        # Dans /toctoc/Jean/Dupont :
        # self.path_info[0] vaut 'toctoc'
        # self.path_info[1] vaut 'Jean' (Prenom)
        # self.path_info[2] vaut 'Dupont' (Nom)
        prenom = self.path_info[1] if len(self.path_info) > 1 else ""
        nom = self.path_info[2] if len(self.path_info) > 2 else ""

        data = {
            "message": f"Bonjour {prenom} {nom}",
            "prenom": prenom,
            "nom": nom,
            "provenance": "path_info_toctoc"
        }
        self.envoyer_json(data)


    def send_service(self):
        """Générer une réponse en JSON retournant les détails techniques de la requête"""
        data = {
            "path_info": self.path_info,
            "query_string": self.query_string,
            "body_brut": self.body,
            "params_analyses": self.params
        }
        self.envoyer_json(data)     


    def envoyer_json(self, data):
        """Méthode utilitaire pour factoriser l'envoi de JSON"""
        body = json.dumps(data, ensure_ascii=False)
        headers = [('Content-Type', 'application/json;charset=utf-8')]
        self.send(body, headers)


    def send(self, body, headers=[]):
        """Envoyer la réponse au client avec le corps et les en-têtes fournis"""
        encoded = bytes(body, 'UTF-8')
        self.send_response(200)
        [self.send_header(*t) for t in headers]
        self.send_header('Content-Length', int(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
        

    def init_params(self):
        """Analyse la requête pour initialiser nos paramètres"""
        info = urlparse(self.path)
        # Découpe le chemin (ex: "/toctoc/Jean/Dupont" devient ['toctoc', 'Jean', 'Dupont'])
        self.path_info = [unquote(v) for v in info.path.split('/') if v != '']
        self.query_string = info.query
        self.params = parse_qs(info.query)

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
       
        # traces dans la console de VS Code
        print('info_path =', self.path_info)
        print('params =', self.params)


if __name__ == '__main__' :
    httpd = socketserver.TCPServer(("", port_serveur), RequestHandler)
    print(f"Serveur TD3-s4 actif sur le port {port_serveur}...")
    httpd.serve_forever()