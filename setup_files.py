import os

def create_directory_structure():
    # Define the structure
    structure = {
        'static': {
            'css': {
                'components': [
                    'about.css',
                    'hero.css',
                    'header.css',
                    'footer.css',
                    'services.css',
                    'templates.css'
                ],
                'files': ['style.css']
            },
            'js': {
                'components': [
                    'darkMode.js',
                    'templateSlider.js',
                    'mobileMenu.js'
                ],
                'files': ['main.js']
            }
        },
        'templates': {
            'components': [
                'header.html',
                'hero.html',
                'about.html',
                'services.html',
                'templates.html',
                'footer.html'
            ],
            'files': ['base.html']
        }
    }

    # Create directories and files
    for main_dir, contents in structure.items():
        if main_dir == 'static':
            # Handle static directory structure
            for sub_dir, sub_contents in contents.items():
                # Create component directory
                comp_path = os.path.join(main_dir, sub_dir, 'components')
                os.makedirs(comp_path, exist_ok=True)
                
                # Create component files
                for file in sub_contents['components']:
                    file_path = os.path.join(comp_path, file)
                    if not os.path.exists(file_path):
                        with open(file_path, 'w') as f:
                            if file.endswith('.css'):
                                f.write('/* Component styles */\n')
                            elif file.endswith('.js'):
                                f.write('// Component JavaScript\n')
                
                # Create main files
                for file in sub_contents['files']:
                    file_path = os.path.join(main_dir, sub_dir, file)
                    if not os.path.exists(file_path):
                        with open(file_path, 'w') as f:
                            if file.endswith('.css'):
                                f.write('/* Main styles */\n')
                            elif file.endswith('.js'):
                                f.write('// Main JavaScript\n')
        
        elif main_dir == 'templates':
            # Create templates directory and components subdirectory
            comp_path = os.path.join(main_dir, 'components')
            os.makedirs(comp_path, exist_ok=True)
            
            # Create component template files
            for file in contents['components']:
                file_path = os.path.join(comp_path, file)
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        component_name = file.replace('.html', '').title()
                        f.write(f'''<!-- {component_name} Component -->
                                
        <section class="{file.replace('.html', '')}">
            <div class="container">
                <h2>{component_name} Section</h2>
                <!-- Content goes here -->
            </div>
        </section>
        ''')
                    
                    # Create base template
                    base_path = os.path.join(main_dir, 'base.html')
                    if not os.path.exists(base_path):
                        with open(base_path, 'w') as f:
                            f.write('''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>MALF - Create Without Limits</title>
            
            <!-- CSS Files -->
            <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
        </head>
        <body>
            {% include 'components/header.html' %}
            {% include 'components/hero.html' %}
            {% include 'components/about.html' %}
            {% include 'components/services.html' %}
            {% include 'components/templates.html' %}
            {% include 'components/footer.html' %}
            {% include 'components/chat-bubble.html' %}

            <!-- JavaScript Files -->
            <script src="{{ url_for('static', filename='js/main.js') }}"></script>
            <script src="{{ url_for('static', filename='js/components/darkMode.js') }}"></script>
            <script src="{{ url_for('static', filename='js/components/templateSlider.js') }}"></script>
            <script src="{{ url_for('static', filename='js/components/mobileMenu.js') }}"></script>
            <script src="{{ url_for('static', filename='js/components/chat.js') }}"></script>
        </body>
        </html>
        ''')

        # Create initial content for CSS and JS files
        css_content = {
        'header.css': '''.header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 5%;
            background-color: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .logo {
            font-weight: 800;
            font-size: 28px;
            color: #3899ec;
        }

        .nav-menu {
            display: flex;
            gap: 20px;
        }

        .nav-item {
            text-decoration: none;
            color: #333;
            font-weight: 500;
        }''',
        
        'style.css': '''/* Import component styles */
        @import 'components/header.css';
        @import 'components/hero.css';
        @import 'components/about.css';
        @import 'components/services.css';
        @import 'components/templates.css';
        @import 'components/footer.css';
        @import 'components/chat.css';

        /* Global styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            line-height: 1.6;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .btn {
            padding: 12px 24px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .btn-primary {
            background-color: #3899ec;
            color: white;
        }

        .btn-secondary {
            background-color: #f5f5f5;
            color: #333;
        }'''
            }

    # Write initial content to CSS files
    for filename, content in css_content.items():
        if filename == 'header.css':
            file_path = os.path.join('static', 'css', 'components', filename)
        else:
            file_path = os.path.join('static', 'css', filename)
        
        with open(file_path, 'w') as f:
            f.write(content)

    print("Directory structure created successfully!")

if __name__ == '__main__':
    create_directory_structure()