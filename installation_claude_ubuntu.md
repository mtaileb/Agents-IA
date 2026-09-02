# Comment installer Claude Desktop sur Ubuntu 24.04.4 LTS

L'application officielle **Claude Desktop** est disponible nativement en version bêta pour Linux (Ubuntu/Debian). Pour l'installer proprement sur **Ubuntu 24.04.4 LTS**, il est fortement recommandé d'utiliser le dépôt APT officiel d'Anthropic afin de bénéficier des mises à jour automatiques via votre gestionnaire de paquets système.

---

## 📋 Prérequis et Installation

Ouvrez votre terminal (`Ctrl` + `Alt` + `T`) et exécutez les commandes suivantes pas à pas :

### 1. Installer Curl
Assurez-vous que l'outil de téléchargement `curl` est bien installé sur votre système :
```bash
sudo apt update && sudo apt install -y curl
```

### 2. Ajouter la clé de signature GPG d'Anthropic
Cette clé permet à votre système de vérifier l'authenticité et la sécurité des paquets fournis par Anthropic :
```bash
sudo curl -fsSLo /usr/share/keyrings/claude-desktop-archive-keyring.asc https://downloads.claude.ai/claude-desktop/key.asc
```

### 3. Ajouter le dépôt APT officiel
Ajoutez l'adresse des serveurs de téléchargement d'Anthropic à vos sources de logiciels :
```bash
echo "deb [signed-by=/usr/share/keyrings/claude-desktop-archive-keyring.asc] https://downloads.claude.ai/claude-desktop/apt/stable stable main" | sudo tee /etc/apt/sources.list.d/claude-desktop.list
```

### 4. Mettre à jour les sources et installer l'application
Mettez à jour la liste de vos logiciels et installez Claude Desktop :
```bash
sudo apt update && sudo apt install -y claude-desktop
```

---

## 🚀 Lancement de l'application

Une fois l'installation terminée, vous pouvez ouvrir l'application de deux manières :

* **Interface graphique :** Appuyez sur la touche `Super` (ou `Windows`), recherchez **Claude** dans votre menu d'applications, puis cliquez sur l'icône.
* **Terminal :** Lancez directement le processus avec la commande suivante :
  ```bash
  claude-desktop
  ```

---

## 🛠️ Désinstallation

Si vous souhaitez supprimer proprement l'application ainsi que son dépôt de votre système, utilisez les commandes suivantes :

```bash
# Supprimer l'application
sudo apt remove --purge -y claude-desktop

# Supprimer le fichier de dépôt APT
sudo rm /etc/apt/sources.list.d/claude-desktop.list

# Supprimer la clé GPG
sudo rm /usr/share/keyrings/claude-desktop-archive-keyring.asc

# Mettre à jour le système
sudo apt update
```
