# 🤖 Vagas Bot Sentinela

Este é um bot em Python projetado para monitorar vagas de emprego (LinkedIn, Indeed, Glassdoor) em tempo real e enviar alertas instantâneos para o seu Telegram. 

O foco do projeto é a **velocidade**: ser o primeiro a saber de vagas de Estágio e Júnior para aumentar as chances de contratação.

## 🚀 Funcionalidades

- **Monitoramento Multi-Site:** Busca vagas no LinkedIn, Indeed e Glassdoor simultaneamente.
- **Filtros Inteligentes:** Busca por múltiplos termos (ex: "Estágio", "Júnior") em múltiplas localizações (ex: "Belém", "Remoto").
- **Alertas Instantâneos:** Envia notificação no Telegram com Nome da Vaga, Empresa, Local e Link para aplicação.
- **Proteção Anti-Ban:** Possui delays aleatórios para evitar bloqueios por excesso de requisições.

---

## 🛠️ Pré-requisitos

- Python 3.10 ou superior.
- Uma conta no Telegram.

---

## 📦 Instalação

1. **Clone este repositório** (ou baixe os arquivos):
   ```bash
   git clone [https://github.com/SEU_USUARIO/vagas-bot.git](https://github.com/SEU_USUARIO/vagas-bot.git)
   cd vagas-bot

```

2. **Crie um ambiente virtual (Opcional, mas recomendado):**
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

```


3. **Instale as dependências:**
⚠️ **Atenção:** A biblioteca correta é `python-jobspy`, não instale apenas `jobspy`.
```bash
pip install python-jobspy pandas requests python-dotenv

```



---

## ⚙️ Configuração

Antes de rodar, você precisa configurar as chaves de acesso.

### 1. Criando o Bot no Telegram

1. Abra o Telegram e pesquise por **@BotFather**.
2. Envie o comando `/newbot`.
3. Dê um nome e um user para o bot.
4. O BotFather vai te dar um **TOKEN** (ex: `123456:ABC-DEF...`). Copie-o.

### 2. Descobrindo seu Chat ID

1. Inicie uma conversa com o seu novo bot (clique em **Começar** ou envie `/start`).
2. Pesquise por **@userinfobot** no Telegram e clique em iniciar.
3. Ele vai te responder com o seu `Id` (um número, ex: `1234567890`). Copie-o.

### 3. Configurando o arquivo `.env`

1. Na pasta do projeto, crie um arquivo chamado `.env` (sem nome antes do ponto).
2. Cole o conteúdo abaixo e substitua pelos seus dados:

```ini
TELEGRAM_TOKEN=Cole_Seu_Token_Aqui
CHAT_ID=Cole_Seu_ID_Aqui

```

> **Nota de Segurança:** O arquivo `.env` está listado no `.gitignore` para não ser enviado ao GitHub, mantendo suas senhas seguras.

---

## ▶️ Como Rodar

Basta executar o arquivo principal:

```bash
python main.py

```

O bot começará a varrer os sites e enviará mensagens no Telegram assim que encontrar novas vagas.

---

## 🎨 Personalização

Para mudar o que o bot busca, edite as listas no início do arquivo `main.py`:

```python
# Adicione ou remova locais
locais = ["São Paulo, SP", "Remote", "Belém, PA"]

# Adicione ou remova termos de busca
termos = [
    "Estágio em Desenvolvimento",
    "Python Junior",
    "Suporte Técnico"
]

```

---

## ❓ Solução de Problemas Comuns

**Erro: `ModuleNotFoundError: No module named 'jobspy'**`
Isso acontece se você instalar a biblioteca errada. Certifique-se de rodar:
`pip uninstall jobspy` e depois `pip install python-jobspy`.

**Erro: `401 Unauthorized**`
Seu Token do Telegram está errado ou incompleto no arquivo `.env`. Verifique se não há espaços em branco.

**Erro: `400 Bad Request**`
Você provavelmente esqueceu de clicar em "Começar" (`/start`) na conversa com o seu bot no Telegram. Ele não pode mandar mensagem sem sua permissão inicial.

---

## 📝 Licença

Este projeto é para fins educacionais e pessoais. Respeite os termos de serviço das plataformas de emprego e evite fazer requisições excessivas (spam).

```