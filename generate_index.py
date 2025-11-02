import os

# Dossier où sont tes images
image_folder = "docs/images"
# Fichier HTML de sortie
output_file = "docs/index.html"

# Liste toutes les images du dossier
images = [img for img in os.listdir(image_folder) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Commence le HTML
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Iris Beauty</title>
  <link rel="stylesheet" href="style.css">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Poppins', sans-serif; background-color: #fdf6f0; text-align: center; margin:0; padding:0;}
    header { background-color: #e0c3b0; padding:20px 0; }
    header h1 { margin:0; }
    nav a { margin:0 15px; text-decoration:none; color:#5a3825; font-weight:500;}
    main { padding:20px; }
    .collection { display:flex; flex-wrap:wrap; justify-content:center; gap:20px; margin-top:30px; }
    .parfum { width:200px; text-align:center; background:rgba(255,255,255,0.9); padding:15px; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.1);}
    .parfum img { width:100%; border-radius:10px; }
    footer { background-color:#e0c3b0; padding:10px 0; margin-top:30px;}
  </style>
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

# Ajoute chaque image dans une div
for i, img in enumerate(images, 1):
    html_content += f'    <div class="parfum">\n'
    html_content += f'      <img src="images/{img}" alt="Parfum {i}">\n'
    html_content += f'      <p>Parfum {i}</p>\n'
    html_content += f'    </div>\n'

# Termine le HTML
html_content += """
  </div>
</main>

<footer>
  © 2025 Iris Beauty — Tous droits réservés
</footer>

</body>
</html>
"""

# Écrit le fichier
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"{output_file} généré avec {len(images)} images.")
