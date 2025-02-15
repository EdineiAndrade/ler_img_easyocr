# Emissão Automática de Seguros

Este projeto automatiza a emissão de seguros para uma lista de clientes, utilizando **Selenium** para automação web e **Flet** para a interface gráfica. Ele permite importar uma lista de clientes de um arquivo Excel, iniciar a emissão de seguros e exibir o status de cada cliente em uma tabela.

---

## Funcionalidades

* **Importar Lista de Clientes** :
* Carrega os dados dos clientes de um arquivo Excel.
* **Iniciar Emissão de Seguros** :
* Automatiza a emissão de seguros para todos os clientes da lista.
* **Tabela de Status** :
* Exibe o nome do cliente e o status da emissão ("Emitido" ou "Erro").
* Atualiza o status em tempo real.
* Design com borda laranja transparente.

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

* Python 3.8 ou superior.
* Bibliotecas listadas no arquivo `requirements.txt`.

---

## Como Configurar

1. Clone o repositório:
   bash

   Copy

   ```
   git clone https://github.com/seu-usuario/emissao_seguros.git
   cd emissao_seguros
   ```
2. Instale as dependências:
   bash

   Copy

   ```
   pip install -r requirements.txt
   ```
3. Coloque o arquivo `clientes.xlsx` na pasta `/data`. O arquivo deve conter as seguintes colunas:

   * `Nome`
   * `Endereço`
   * `Idade`
   * `Escolaridade`
   * `Telefone`
   * `Email`

---

## Como Executar

1. Execute o script principal:
   bash

   Copy

   ```
   python src/main.py
   ```
2. Na interface gráfica:

   * Clique em **Importar Lista** para carregar o arquivo Excel.
   * Clique em **Iniciar Emissão** para começar o processo de emissão de seguros.
   * Acompanhe o status de cada cliente na tabela.

---

## Estrutura do Projeto

Copy

```
/emissao_seguros
│
├── /data
│   └── clientes.xlsx               # Arquivo Excel com os dados dos clientes
│
├── /src
│   ├── __init__.py                 # Arquivo vazio para tornar a pasta um módulo Python
│   ├── main.py                     # Script principal com a interface Flet
│   ├── selenium_automation.py      # Funções de automação com Selenium
│   └── utils.py                    # Funções utilitárias (leitura de Excel, logs, etc.)
│
├── requirements.txt                # Lista de dependências do projeto
└── README.md                       # Documentação do projeto
```

---

## Tecnologias Utilizadas

* **Python** : Linguagem de programação principal.
* **Selenium** : Automação de navegadores para emissão de seguros.
* **Flet** : Biblioteca para criar a interface gráfica.
* **Pandas** : Leitura e manipulação de dados do Excel.

---

## Contribuição

Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](https://chat.deepseek.com/a/chat/s/LICENSE) para mais detalhes.

---

## Contato

Se você tiver alguma dúvida ou sugestão, entre em contato:

* **Nome** : Seu Nome
* **Email** : [seu-email@example.com](mailto:seu-email@example.com)
* **GitHub** : [seu-usuario](https://github.com/seu-usuario)

---

## Capturas de Tela

![Interface Gráfica](https://chat.deepseek.com/a/chat/s/screenshots/interface.png)
*Interface gráfica do projeto.*
