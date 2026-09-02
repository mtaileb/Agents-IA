Ce dépôt contient le code des exemples d'agents. Le code démontre comment créer et exécuter un agent d'IA en utilisant les outils et les API compatibles avec le standard OpenAI.

## Instructions d'installation de l'environnement Python + Claude Desktop

### 1. Cloner le dépôt

Pour commencer, clonez ce dépôt sur votre machine locale :

    git clone https://github.com/cxbxmxcx/AI-Agent-Workflows.git
    cd AI-Agent-Workflows

### 2. Créer votre environnement

Ce projet nécessite **Python 3.11+**. Créez et activez un environnement virtuel Python :

#### Sous macOS/Linux :

    python3 -m venv venv
    source venv/bin/activate

#### Sous Windows :

    python -m venv venv
    venv\Scripts\activate

Si vous préférez utiliser un environnement Python externe, assurez-vous de définir le chemin Python dans VS Code :

  1. Ouvrez la Palette de commandes (`Ctrl+Maj+P` ou `Cmd+Maj+P` sur macOS).
  2. Recherchez "Python : Sélectionner l'interpréteur".
  3. Choisissez l'interpréteur Python pour votre environnement.

### 3. Installer les dépendances

#### Méthode A : Utilisation du débogage de VS Code

Si vous avez VS Code, vous pouvez simplement lancer le débogage (appuyez sur `F5`) pour exécuter les exemples. Les dépendances requises seront installées automatiquement dans le cadre du processus de débogage.

#### Méthode B : Installation manuelle

Alternativement, vous pouvez installer manuellement les dépendances en utilisant uv et pip :

    pip install uv && uv pip install -r requirements.txt

### 4. Configurer l'environnement

Créez un fichier `.env` à la racine du répertoire pour stocker votre clé API OpenAI. Utilisez le fichier `.env.example` fourni comme modèle :

#### Exemple de fichier `.env` :

    OPENAI_API_KEY=votre_clé_api_openai_ici

Remplacez `votre_clé_api_openai_ici` par votre véritable clé API OpenAI. Vous pouvez obtenir une clé API depuis la page des clés API d'OpenAI.

### 5. Exécuter le code

Pour exécuter le code d'exemple, naviguez vers le fichier Python. Par exemple :

    python3 01_first_agent.py

Cela exécutera l'agent et affichera la sortie dans le terminal.

## Remarques

  * Assurez-vous d'utiliser l'interpréteur Python correct qui correspond à votre environnement.
  * Le fichier `.env` ne doit pas être partagé ou committé dans le contrôle de version pour garder votre clé API sécurisée.

## Installation de Claude Desktop

### Prérequis : Installation de Node.js

Claude Desktop nécessite Node.js pour fonctionner. Sur Linux et WSL (Windows Subsystem for Linux), la méthode recommandée est **nvm** (Node Version Manager), qui permet de gérer plusieurs versions de Node.js sans privilèges administrateur.

#### Installation de nvm

Exécutez la commande suivante pour installer nvm :

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
**💡 Astuce importante** : Si vous rencontrez l'erreur `Failed to clone nvm repo` ou un avertissement concernant `REMOTE REPO IDENTIFICATION HAS CHANGED`, cela est probablement dû à une variable d'environnement `NVM_INSTALL_GITHUB_REPO` mal configurée. Pour résoudre ce problème, exécutez :
```bash
unset NVM_INSTALL_GITHUB_REPO
```
Puis relancez la commande d'installation ci-dessus.

Si le problème persiste, vous pouvez forcer l'installation par script (sans Git) avec :
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | METHOD=script bash
```

Ensuite :
```bash
nvm install --lts
nvm use --lts
```

### Vérification de votre installation de Node et npx

Une fois Node installé, il est utile de prendre un moment pour confirmer que tout est bien dans votre PATH et pour développer un modèle mental de la façon dont npx gère les paquets qu'il exécute. Les sous-sections suivantes couvrent la vérification des versions et une brève visite du cache de npx.

#### B.2.1 Vérification des versions installées

Ouvrez une nouvelle fenêtre de terminal et exécutez les trois commandes suivantes :

```bash
node --version
npm --version
npx --version
```

Chaque commande devrait afficher un numéro de version. `node --version` devrait indiquer v20 ou une version ultérieure, et `npm --version` ainsi que `npx --version` devraient chacun afficher un numéro proche de 10. Si l'une des trois commandes renvoie une erreur `Command Not Found`, la mise à jour du PATH par l'installateur n'a pas pris effet. Fermez et rouvrez votre terminal (ou votre session shell entière) et réessayez.

#### B.2.2 Comment npx trouve et met en cache les paquets

Lorsque vous exécutez un paquet avec npx, il fait approximativement ce qui suit :

1. Il recherche le paquet dans votre dossier `node_modules` local. S'il y trouve l'exécutable, il exécute cette copie.
2. Si le paquet n'est pas installé localement, il recherche dans le cache global npm à `~/.npm/_npx` (ou l'équivalent sur Windows). Si la version demandée est déjà dans le cache, il exécute la copie en cache.
3. Si le paquet n'est pas non plus dans le cache, npx le télécharge depuis le registre npm, le place dans le cache, et l'exécute.

La conséquence pratique est que la première exécution d'un serveur MCP avec npx est nettement plus lente que les exécutions suivantes car elle passe du temps à télécharger le paquet. À partir de la seconde exécution, npx lance simplement la copie en cache.

**ASTUCE :** L'option `-y` (abordée dans la section suivante) indique à npx de sauter l'invite interactive *"Need to install the following packages, ok?"*. Les clients MCP qui lancent un serveur MCP en tant que sous-processus n'ont aucun moyen de répondre à cette invite, donc incluez toujours `-y` lors de la configuration d'un client.

---

### B.3 Exécution d'un serveur MCP avec npx

Avec Node installé et vérifié, vous êtes prêt à exécuter un serveur MCP. Les sous-sections suivantes décomposent la commande npx en ses parties, puis détaillent un exemple concret utilisant le serveur MCP officiel pour le système de fichiers, et montrent enfin comment connecter ce serveur à un client MCP.

#### B.3.1 Anatomie de la commande npx

Une commande typique pour lancer un serveur MCP avec npx comporte quatre parties :

```
npx -y <nom-du-paquet> [arguments-du-serveur...]
```

- **npx** — Le lanceur fourni avec Node.js.
- **-y** — Raccourci pour `--yes`. Accepte automatiquement l'invite d'installation, ce qui est requis lorsqu'un client MCP lance le serveur en tant que sous-processus.
- **`<nom-du-paquet>`** — Le paquet npm qui fournit le serveur MCP, par exemple, `@modelcontextprotocol/server-filesystem`.
- **`[arguments-du-serveur...]`** — Tous les arguments que le serveur MCP accepte lui-même. Ils sont transmis au processus du serveur. Le serveur de système de fichiers, par exemple, prend un ou plusieurs chemins de répertoire que le client MCP est autorisé à lire et écrire.

#### B.3.2 Exécution du serveur MCP de système de fichiers

Pour un exemple concret, le serveur MCP officiel pour le système de fichiers se trouve sur npm sous le nom `@modelcontextprotocol/server-filesystem`. Pour l'exécuter sur un seul répertoire, ouvrez un terminal et exécutez :

```bash
npx -y @modelcontextprotocol/server-filesystem /chemin/vers/repertoire/autorise
```

Sur Windows, remplacez le chemin au style Unix par un chemin Windows, par exemple :

```bash
npx -y @modelcontextprotocol/server-filesystem C:\Users\vous\Documents
```

La première exécution télécharge le paquet et peut prendre quelques secondes ; les exécutions suivantes démarrent presque instantanément. Une fois le serveur en cours d'exécution, il communique avec son client via l'entrée et la sortie standard en utilisant le protocole MCP. L'exécuter directement dans un terminal est principalement utile comme test de bon fonctionnement : le serveur affichera une bannière de démarrage puis attendra des messages MCP sur stdin. Appuyez sur `Ctrl-C` pour l'arrêter.

Les clients MCP lancent leurs serveurs en tant que sous-processus, ce qui signifie que vous n'exécutez normalement pas vous-même la commande npx — vous la décrivez au client dans un fichier de configuration. L'emplacement exact de ce fichier dépend du client. Claude Desktop, par exemple, lit un fichier de configuration JSON dans votre profil utilisateur. L'entrée pour le serveur de système de fichiers ressemble à ceci :

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/chemin/vers/repertoire/autorise"
      ]
    }
  }
}
```

Notez que le champ `command` est simplement `npx` et que le nom du paquet apparaît comme l'une des entrées `args`, avec `-y` listé en premier pour supprimer l'invite d'installation. Ce même modèle fonctionne pour tout serveur MCP publié sur npm : modifiez le nom du paquet et les arguments finaux pour correspondre au serveur que vous souhaitez exécuter.

---

### B.4 Dépannage et maintien de Node en bonne santé

La plupart des problèmes avec les serveurs MCP lancés via npx se classent dans quelques catégories. Les sous-sections suivantes couvrent les problèmes les plus probables, comment vider le cache de npx lorsqu'une copie obsolète cause des problèmes, et comment maintenir Node à jour.

#### B.4.1 Problèmes courants

Voici les problèmes que vous êtes le plus susceptible de rencontrer :

- **"npx: command not found"** — Votre shell ne voit pas les binaires Node. Fermez et rouvrez votre terminal pour que le PATH mis à jour soit pris en compte. Sur macOS et Linux, confirmez que `nvm use --lts` a été exécuté dans le shell actuel, ou ajoutez-le à votre fichier de démarrage du shell.
- **Erreurs EACCES ou de permission lors de l'installation** — Vous avez installé Node avec `sudo`, et le cache appartient désormais à root. La solution la plus propre est de supprimer l'installation système et de passer à nvm, qui installe Node dans votre répertoire personnel.
- **Le client MCP signale que le serveur s'est arrêté immédiatement** — Exécutez la même commande npx directement dans un terminal. Le message d'erreur du serveur apparaîtra là-bas mais est normalement avalé par le client.
- **Le client MCP se bloque au démarrage** — Vous avez presque certainement oublié l'option `-y`, et npx attend une invite de confirmation d'installation à laquelle le client ne peut pas répondre.

#### B.4.2 Vider le cache de npx

Si vous soupçonnez que npx exécute une copie obsolète d'un serveur MCP, par exemple après qu'un paquet a publié un correctif que vous souhaitez récupérer, videz le cache et laissez-le retélécharger lors de la prochaine exécution :

```bash
npm cache clean --force
```

Pour épingler une version spécifique lors de la prochaine exécution, ajoutez plutôt `@<version>` au nom du paquet, par exemple, `npx -y @modelcontextprotocol/server-filesystem@latest`. Cela force npx à résoudre la version demandée auprès du registre avant de l'exécuter.

#### B.4.3 Mise à jour de Node

Node publie une nouvelle version LTS environ une fois par an. Pour rester sur la LTS actuelle, mettez à jour périodiquement en utilisant le même outil que celui utilisé pour installer Node :

- **Sur Windows avec l'installateur officiel** : téléchargez le dernier .msi LTS depuis https://nodejs.org et exécutez-le. L'installateur met à niveau l'installation existante sur place.
- **Avec Homebrew sur macOS** : exécutez `brew upgrade node`.
- **Avec nvm sur Linux, macOS ou WSL** : exécutez `nvm install --lts` suivi de `nvm alias default lts/*` pour faire de la nouvelle version la version par défaut pour les futurs shells.

Après la mise à niveau, relancez les trois vérifications de version de la section B.2.1 pour confirmer que les nouvelles versions sont sur votre PATH.
