# 💊 NeoLuminis | Sistema de Controle de Estoque

Uma aplicação web robusta e intuitiva desenvolvida em Django para o gerenciamento de inventário de medicamentos em drogarias e farmácias. Este sistema permite o controle absoluto sobre entradas, saídas, precificação e categorização de produtos, garantindo uma gestão de estoque segura e eficiente.

---

## 🚀 Principais Funcionalidades

* **Autenticação de Usuários:** Sistema de login seguro com controle de acesso restrito (apenas funcionários autorizados acessam o estoque).
* **Gestão de Medicamentos (CRUD):** Cadastro, edição, visualização e exclusão de remédios com suporte a upload de fotos das embalagens.
* **Baixa Rápida de Estoque (PDV Simulada):** Botão prático na interface principal para descontar uma unidade do inventário com um único clique, agilizando o atendimento no balcão.
* **Busca Dinâmica Avançada:** Filtro em tempo real por nome ou princípio ativo do medicamento, resistente a erros de digitação (letras maiúsculas/minúsculas).
* **Indicadores de Status:** Alertas visuais automáticos informando se o estoque está normal, baixo ou esgotado.
* **Segurança e Tratamento de Erros:** Página de Erro 404 personalizada e proteção de dados sensíveis utilizando variáveis de ambiente.
* **Painel Administrativo Nativo:** Integração completa com o Django Admin para gerenciamento avançado de dados e permissões.

---

## 📂 Estrutura de Diretórios

```text
Farmacia-django/
├── core/                   # Configurações globais do projeto Django (settings.py, urls.py)
├── website/                # Aplicativo principal contendo a lógica de negócios
│   ├── migrations/         # Histórico de alterações do banco de dados
│   ├── admin.py            # Registro de modelos no painel administrativo
│   ├── models.py           # Estrutura do banco de dados (Tabela Medicamento)
│   ├── views.py            # Funções de processamento (Lógica das telas e baixa de estoque)
│   └── urls.py             # Rotas específicas do aplicativo
├── templates/              # Páginas HTML globais e de erro
│   └── 404.html            # Tela customizada de página não encontrada
├── media/                  # Diretório de armazenamento de uploads (fotos dos medicamentos)
├── venv/                   # Ambiente virtual isolado do Python (não versionado)
├── .env                    # Variáveis de ambiente e credenciais secretas (não versionado)
├── .gitignore              # Lista de arquivos bloqueados no repositório
├── db.sqlite3              # Banco de dados relacional local
├── manage.py               # Utilitário de linha de comando do Django
└── requirements.txt        # Lista de dependências e bibliotecas do projeto

```

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Framework Web:** Django 6.x
* **Banco de Dados:** SQLite (nativo para desenvolvimento)
* **Frontend:** HTML5 e CSS3 puro (Variáveis CSS, Flexbox)
* **Segurança:** Python-Decouple (Gestão de variáveis de ambiente)
* **Processamento de Imagens:** Pillow

---

## 📋 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:

* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

---

## ⚙️ Instruções de Instalação

Siga o passo a passo abaixo para rodar o projeto localmente.

### 1. Clonar o repositório

```bash
git clone https://github.com/Yohendev/Farmacia-django.git
cd farmacia-django

```

### 2. Criar e Ativar o Ambiente Virtual (venv)

O ambiente virtual isola os pacotes deste projeto para não causar conflitos com outros sistemas no seu computador.

**No Windows (PowerShell / CMD):**

```powershell
python -m venv venv
venv\Scripts\activate

```

**No Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Instalar as Dependências

Com o ambiente ativado, instale as bibliotecas exigidas pelo sistema:

```bash
pip install -r requirements.txt

```

---

## 🔐 Variáveis de Ambiente

Para a segurança do projeto, as senhas e chaves não ficam no código. Crie um arquivo chamado exatamente **`.env`** na raiz do projeto (na mesma pasta do `manage.py`) e insira as seguintes variáveis:

```env
SECRET_KEY=a_chave_aqui
DEBUG=True

```

---

## ▶️ Como Executar o Projeto

**1. Preparar o Banco de Dados**
Aplique as migrações para criar as tabelas necessárias:

```bash
python manage.py migrate

```

**2. Criar um Superusuário (Administrador)**
Crie uma conta para acessar o painel de controle nativo:

```bash
python manage.py createsuperuser

```

*(Siga os passos no terminal para informar nome de usuário, e-mail e senha).*

**3. Iniciar o Servidor**

```bash
python manage.py runserver

```

A aplicação estará disponível em seu navegador no endereço: **`http://127.0.0.1:8000/`**

---
