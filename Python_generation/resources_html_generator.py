import os

def create_html_resources(system_resources_list = None, user_resources_list = None):
    if system_resources_list is None:
        system_resources_list = []

    if user_resources_list is None:
        user_resources_list = []
    
    template_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml" href="Resources/System_assets/LOGO_OFICIAL.svg">
    <title>Vita Wiki - Botica Vitanova</title>
    <link rel="stylesheet" href="Styles/style.css">
    <script src="Scripts/script.js"></script>
</head>
<body>

    <header>
        <button class="menu-toggle" onclick="toggleMenu()"><img src="burger-icon.svg" class="burger-icon"></button>

        <div class="header-container">
            
            <div class="brand-block">
                <img src="Resources/System_assets/LOGO_NOMBRE_OFICIAL.svg" alt="Botica Vitanova" class="logo-vitanova">
                <p class="header-eslogan">¡TU SALUD EN MANOS DE PROFESIONALES!</p>
            </div>

        </div>

        <nav class="navigation">
            <ul class="nav-links">
                <li><a href="index.html">Inicio</a></li>
                <li><a href="vitawiki.html">Vita Wiki</a></li>
                <li><a href="resource.html">Recursos</a></li>
            </ul>
        </nav>
    </header>
    
    <h1 class="resources-title">¡BIENVENIDO A RECURSOS DE VITANOVA!</h1>
    <p class="resources-subtitle">¡Aquí encontrarás los recursos gráficos que usamos a diario en las Boticas VitaNova!</p>

    <main class="resources-container">
        
        <div id="System-resources" class="resource-card-section">
            <div class="container-section-icon">
                <h2>Recursos del sistema!</h2>
            </div>
            <div class="resources-grid">
                {{ system-resources-items }}
            </div>
        </div>

        <div id="User-resources" class="resource-card-section">
            <div class="container-section-icon">
                <h2>Recursos de usuario!</h2>
            </div>
            <div class="resources-grid">
                {{ user-resources-items }}
            </div>
        </div>

    </main>

    <footer>
        <p>© 2026 Botica Vitanova - Nasca, Ica</p>
    </footer>

</body>
</html>'''

    item_template = '''<section class="resource-item">
                    <h3>{{ resource-name }}</h3>
                    <img src="{{ resource-path }}" alt="{{ alt-resource-name }}" class="icon-demostrative">
                </section>'''
    
    system_items = ""
    user_items = ""

    for item in system_resources_list:
        resource_html = item_template

        name_resource = item.get("name")
        path_resource = item.get("path")

        alt_name = name_resource.replace(" ", "_")

        resource_html = resource_html.replace("{{ resource-name }}", name_resource)
        resource_html = resource_html.replace("{{ resource-path }}", path_resource)
        resource_html = resource_html.replace("{{ alt-resource-name }}", alt_name)
        
        system_items += "               " + resource_html.strip() + "\n"

    for item in user_resources_list:
        resource_html = item_template

        name_resource = item.get("name")
        path_resource = item.get("path")

        alt_name = name_resource.replace(" ", "_")

        resource_html = resource_html.replace("{{ resource-name }}", name_resource)
        resource_html = resource_html.replace("{{ resource-path }}", path_resource)
        resource_html = resource_html.replace("{{ alt-resource-name }}", alt_name)

        user_items += "             " + resource_html.strip() + "\n"
    
    template_html = template_html.replace("{{ system-resources-items }}", system_items)
    template_html = template_html.replace("{{ user-resources-items }}", user_items)

    with open("resource.html", "w", encoding="utf-8") as file:
        file.write(template_html)

# 🛠️ RECURSOS DEL SISTEMA: Construyen la interfaz y los botones de la web
system_resources_list = [
    {"name": "Logo con nombre de VitaNova", "path": "Resources/System_assets/LOGO_NOMBRE_OFICIAL.svg"},
    {"name": "Logo oficial de VitaNova", "path": "Resources/System_assets/LOGO_OFICIAL.svg"},
    {"name": "Logo oficial de VitaWiki", "path": "Resources/System_assets/Logo_vitawiki_pre.svg"},
    {"name": "Portada de VitaNova", "path": "Resources/System_assets/Portada_VitaNova.png"},
    {"name": "Icono de objeto en desarrollo", "path": "Resources/System_assets/En_desarrolo_icon.svg"},
    {"name": "Icono de hamburguesa (3 rayas)", "path": "Resources/System_assets/burger-icon.svg"},
    {"name": "Icono de calendario", "path": "Resources/System_assets/Calendario_icon_pre.svg"},
    {"name": "Icono de ubicación", "path": "Resources/System_assets/Ubicacion_icon_pre.svg"}
]

# 👥 RECURSOS DE USUARIO: Ilustran el contenido y los artículos de la Wiki
user_resources_list = [
    {"name": "Icono oficial del POS de VitaNova", "path": "Resources/User_assets/LOGO_OFICIAL_POS.ico"}
]

create_html_resources(system_resources_list, user_resources_list)