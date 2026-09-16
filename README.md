# TaskVault — API de Gerenciamento de Tarefas com JWT

API REST para gerenciamento de tarefas pessoais, com autenticação via JWT. Cada usuário se cadastra, faz login e passa a gerenciar suas próprias tarefas (criar, editar, deletar e buscar) de forma isolada e segura.

---

## 📋 Funcionalidades

| # | Funcionalidade | Descrição |
|---|---|---|
| 1 | Cadastro de usuário | Cadastro via e-mail e senha |
| 2 | Login | Autenticação e geração de token JWT |
| 3 | Criar tarefa | Usuário autenticado cria uma nova tarefa |
| 4 | Atualizar tarefa | Edita título e/ou descrição de uma tarefa existente |
| 5 | Deletar tarefa | Remove uma tarefa do usuário |
| 6 | Buscar tarefa | Consulta tarefa(s) do usuário logado |

## 🔒 Validações e Segurança

- Validação de formato de e-mail e senha no cadastro
- Senha do usuário é criptografada (hash) antes de ser salva no banco
- Após o login, é gerado um **token JWT**, que deve ser enviado nas próximas requisições para acessar as rotas protegidas

## 🛠️ Tecnologias utilizadas

- **Python**
- **Flask** — framework web
- **SQLite3** — banco de dados

---

## ▶️ Como rodar o projeto

### 1. Instale um cliente para testar as rotas

Escolha um dos programas abaixo para enviar as requisições à API:

- [Bruno](https://www.usebruno.com/)
- [Postman](https://www.postman.com/)
- [Insomnia](https://insomnia.rest/)

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Rode o servidor

```bash
flask run
```

Se o comando acima não funcionar, use:

```bash
python app.py
```

No Linux:

```bash
python3 app.py
```

---

## 🧪 Testando as rotas

### 1) Cadastro de usuário

Corpo da requisição:

```json
{
  "email": "test@dominio.com",
  "senha": "123456789"
}
```

### 2) Login

Use o **mesmo e-mail e senha** cadastrados. A resposta trará o token JWT gerado.

Corpo da requisição:

```json
{
  "email": "test@dominio.com",
  "senha": "123456789"
}
```

Resposta esperada (exemplo):

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

> 💡 A partir daqui, envie esse token no header `Authorization` das próximas requisições (rotas protegidas).

### 3) Criar tarefa

Corpo da requisição:

```json
{
  "titulo": "python123",
  "descricao": "python123"
}
```

> A `descricao` é opcional e pode ser enviada vazia.
