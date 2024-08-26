# Projeto Demonstração de IA na Saúde - Backend

Olá!!
Primeiramente gostaria que soubesse que é uma satisfação
ter você por aqui. Este é o repositório do backend do nosso projeto de apresentação
das possibilidades que a IA pode trazer para a área da saúde.

## 🤩 Menções Honrosas

1. Para o treinamento dos modelos usamos a arquitetura YoloV8
2. Para realizar as anotações usamos o site Roboflow
3. Nosso backend foi construído usando Python/Fastapi

## ☑️ Andamento do Projeto

- Em Produção

O deploy desta API foi realizando usando google cloud e está disponível
através do endereço abaixo

```
Temporariamente Indisponível...
```

## 📜 Swagger

Através do link abaixo você pode acessar a documentação da nossa API

```
Temporariamente Indisponível...
```

## ☄️ Versão Atual

- 0.1.0

## 🕹️ Funcionalidades

Para realizar boas detecção você deve enviar imagens que se assemelhem as
que estão como exemplos. Considere o zoom, formato e proporção entre
altura e largura antes de submeter as imagens a qualquer rota.

### 📌 Detecção de Leucócitos em Scan

Esta detecção é realizada em imagens escanedas de lâminas
de esfregaço de sangue periférico. As seguintes células são
identificadas:

1. Neutrófilos
2. Eosinófilos
3. Monócitos
4. Basófilos
5. Linfócitos

Rota:

```
/hematological-slides/scanned-leukocytes/predict
```

Imagem de Exemplo:
[[click para ver a imagem]](images%2Fscanned.jpg)

### 📌 Detecção de Leucócitos em Ocular

Esta detecção é realizada em imagens, de esfregaço de sangue periférico,
obtidas usando a ocular de um microscópio ótico.As seguintes células são
identificadas:

1. Neutrófilos
2. Eosinófilos
3. Monócitos
4. Basófilos
5. Linfócitos

Rota:

```
/hematological-slides/microscope-leukocytes/predict
```

Imagem de Exemplo:
[[click para ver a imagem]](images%2Focular.jpg)

### 📌 Detecção de Soro ou Plasma em Tubos

Esta detecção é realizda em tubos para amostras laboratoriais e busca
por soro ou plasma.

1. Soro/Plasma

Rota:

```
/blood-serum/predict
```

Imagem de Exemplo:
[[click para ver a imagem]](images%2Fserum.jpg)

### 📌 Detecção de Ki67 em células

Esta detecção busca por células positivas para Ki67 em imagens de lâminas
histopatológicas obtidas através da ocular de um microscópio. Os seguintes
itens são identificados:

1. Nulo
2. Ki67

Rota:

```
/ki67/predict
```

Imagem de Exemplo:
[[click para ver a imagem]](images%2Fki67.jpg)

### 📌 Detecção de Possíveis Melanomas

Esta detecção é realizada em imagens de pele que se deseje avaliar
pintas ou sinais suspeito de serem melanomas.

1. Suspeito
2. Normal

Rota:

```
/melanoma/predict
```

Imagem de Exemplo:
[[click para ver a imagem]](images%2Fmela.jpg)

### 📌 Detecção de Espermatozoides

Esta detecção é realiza em imagens de espermatozoides obtidas através
da ocular de um microscópio com contraste de fases. Nesta detecção
não serão retornados os nomes referentes aos objetos, mas sim um índice
como exemplificado abaixo:

1. 0 - Espermatozoide Normais
2. 2 e 3 - Inadequados

Rota:

```
/sperm/predict
```

Imagem de Exemplo:
[[click para ver a imagem]](images%2Fsperm.jpg)

## 🚀 Clonando Projeto

Nesta seção, explicaremos como você pode realizar o download e
rodar o projeto em sua máquina.

### 📋 Pré-requisitos

Antes de iniciar, verifique se você atende aos seguintes pré-requisitos:

- Python 3.11.2 ou superior
- Poetry
- Git
- Postgres
- Docker e Docker Compose

### 🔧 Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. Clonando o Repositório:

```bash
git clone https://github.com/lspraciano/projectBiomedicIADemonstrationsBackend.git
```

2. No diretório raiz do projeto, instale as dependências com o comando:

```bash
cd projectBiomedicIADemonstrationsBackend
poetry install --no-root
```

3. No diretório "configuration", crie um arquivo chamado ".secrets.toml" com as
   variáveis de ambiente sensíveis necessárias. Veja o exemplo abaixo:

```
[production]
DB_URL = "postgresql+asyncpg://USER_NAME:PASSWORD@HOST:PORT/PROD_DB_NAME" 

[development]
DB_URL = "postgresql+asyncpg://USER_NAME:PASSWORD@HOST:PORT/DEV_DB_NAME" 

[testing]
DB_URL = "postgresql+asyncpg://USER_NAME:PASSWORD@HOST:PORT/TEST_DB_NAME"
```

obs: Troque os valores de USER_NAME, PASSWORD, HOST,PORT e PROD_DB_NAME, por
valores referentes aos bancos de dados que deseje.

4. No mesmo diretório "configuration", você encontrará o arquivo "settings.toml"
   que contém configurações não sensíveis. Certifique-se de que este arquivo
   esteja configurado corretamente. Abaixo temo o significado das variáveis contidas
   nele.

```
[default] -> Os valores contidos nessa chave, serão atribuido como padrão.
[production] -> Os valores contidos nessa chave, serão atribuido em modo de produção.
[development] -> Os valores contidos nessa chave, serão atribuido em modo de devesenvolvimento.
[testing] -> Os valores contidos nessa chave, serão atribuido em modo de teste.

API_URL = "foo" -> Prefixo da API.
SERVER_RELOAD = 0 -> reinício automático da aplicação. 0 é Não, 1 é Sim.
```

5. Defina a variável de ambiente "BIOIADEMON_APP_RUNNING_MODE" para o modo
   de execução desejado. Por exemplo:

No Windows:

```bash
setx BIOIADEMON_APP_RUNNING_MODE "development"
```

No Linux:

```bash
export BIOIADEMON_APP_RUNNING_MODE=development
```

Observação: Pode ser necessário reiniciar o terminal para que a variável
de ambiente seja reconhecida.

6. Ative o ambiente virtual com o comando:

```bash
poetry shell
```

7. Atualize o banco de dados para a versão mais recente usando o comando:

```bash
alembic upgrade head
```

8. Inicie a aplicação com o comando:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

9. Você pode acessar a documentação das rotas da API usando o seguinte endereço:

```
http://127.0.0.1:8000/api/v1/docs
```

ou
clique [aqui](http://127.0.0.1:8000/api/v1/docs) para abrir o endereço diretamente no navegador

## 🔥 Testes

Para executar os testes, utilize um dos seguintes comandos:

```bash
python -m run_tests
```

## ⚡ Rodando em Container

Siga os passos abaixo para configurar iniciar corretamente a aplicação em um
container

```bash
docker-compose up --build
```

Após a execução deste comando, você pode verificar se o serviço está funcionando
corretamente acessando o endereço:

```
http://127.0.0.1/api/v1
```

ou
clique [aqui](http://127.0.0.1/api/v1) para abrir o endereço diretamente no navegador