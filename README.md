# Base — Controle De Treinos

Esta é a aplicação-base da avaliação de reposição.

Ela já possui CRUD de treinos com SQLite. O arquivo `auth.py` também já foi iniciado com Blueprint, mas a autenticação com `session` ainda precisa ser implementada.

## Executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:5000`.

## Arquivos Principais

- `app.py`: rotas Flask.
- `auth.py`: módulo de autenticação já iniciado, ainda sem rotas cadastradas.
- `database.py`: funções de banco de dados.
- `templates/`: páginas HTML.

## Observação

Não substitua a aplicação por outro projeto. A tarefa é adaptar esta base para autenticação com `session`, completando o módulo `auth.py` e mantendo as rotas de treinos em `app.py`.

# Justificativa

## 1. Por que as rotas de autenticação foram movidas para auth.py?
Para aplicar o Blueprint 'auth_bp', fazendo com que as rotas fiquem marcadas com @auth_bp ao invés de @app, isso faz com que as rotas de autenticação e treinos fiquem separadas, ajudando na separação e na fluidez.

## 2. Como a aplicação identifica o usuário logado usando session?
Por meio da linha if 'usuario_id' not in session, ela verifica se tem um usuário logado e, se não, redireciona para o login, ela utiliza o session['usuario_id] para identificar o usuário, que foi definida no login.

## 3. Como o código impede que um usuário acesse treinos de outro usuário?
Por meio da verificação 'WHERE usuario_id = ?' no banco, que passa o id do usuário que cadastrou o treino para mostrar somente eles, e também 'if treino['usuario_id'] != session['usuario_id']:' que faz com que um usuário não possa apagar, editar ou concluir treinos de outros usuários, já que verifica se o usuário logado é o mesmo que cadastrou o treino, se não, retorna o erro 404.