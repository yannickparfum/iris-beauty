import os

# Dossier où sont tes images
images_folder = "docs/images"

# Fichier HTML à générer
output_file = "docs/index.html"

# Liste les fichiers images
images = [img for img in os.listdir(images_folder) if img.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

# Commence le HTML
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Iris Beauty</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Iris Beauty</h1>
    <nav>
      <a href="#">Accueil</a>
      <a href="#">Collection</a>
      <a href="#">Contact</a>
    </nav>
  </header>

  <main>
    <h2>Bienvenue dans l’univers d’Iris Beauty</h2>
    <p>Découvrez nos fragrances uniques, inspirées par la nature et la beauté du monde.</p>

    <div class="collection">
"""

# Ajoute chaque image automatiquement
for img in images:
    html_content += f'      <div class="parfum">\n'
    html_content += f'        <img src="images/{img}" alt="{img}">\n'
    html_content += f'        <p>{img}</p>\n'
    html_content += f'      </div>\n'

# Termine le HTML
html_content += """    </div>
  </main>

  <footer>
    © 2025 Iris Beauty — Tous droits réservés
  </footer>
</body>
</html>
"""

# Écrit dans le fichier index.html
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"index.html généré avec {len(images)} images !")
