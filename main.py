import os
import sys

def create_flask_project_structure(project_name):
    # Estrutura de diretórios do projeto
    directories = [
        project_name,
        os.path.join(project_name, 'static'),
        os.path.join(project_name, 'templates'),
        os.path.join(project_name, 'instance'),
        os.path.join(project_name, 'tests'),
    ]

    # Cria os diretórios
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Cria os arquivos principais
    with open(os.path.join(project_name, 'app.py'), 'w') as f:
        f.write('# app.py\n# Seu código Flask vai aqui.\n')

    with open(os.path.join(project_name, 'requirements.txt'), 'w') as f:
        f.write('# requirements.txt\n# Adicione as dependências do seu projeto aqui.\n')

    # Mensagem de sucesso
    print(f'Projeto {project_name} criado com sucesso!')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python create_flask_project.py nome_do_projeto')
    else:
        create_flask_project_structure(sys.argv[1])
