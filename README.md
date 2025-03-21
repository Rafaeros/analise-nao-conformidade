<hr>

### Dashboard de Análise de Não Conformidades💻
  Este projeto implementa um dashboard interativo de análise de não conformidades utilizando o Streamlit, Pandas e Plotly. A partir de um arquivo Excel contendo dados de não conformidades, o dashboard permite gerar gráficos de barras mostrando a quantidade de não conformidades por tipo e por cliente em um período específico.

### Funcionalidades📚
* Upload de arquivo Excel contendo dados de não conformidades.
* Gráfico de barras com a quantidade de não conformidades por tipo.
* Gráfico de barras com a quantidade de não conformidades por cliente.
* Filtro de dados com base em um intervalo de datas selecionado pelo usuário.

### Tecnologias Utilizadas💻
* Streamlit: Para criar o dashboard interativo.
* Pandas: Para manipulação e análise de dados.
* Plotly: Para criação dos gráficos interativos.

<hr>

### Instalação🛠
* Antes de rodar o projeto, instale as dependências necessárias. Utilize o comando abaixo para instalar os pacotes:

Windows:
```bash
python -m venv venv
venv/Scripts/activate
pip install -r pyproject.toml
```
Linux:
```bash
python -m venv venv
source venv/bin/activate
pip install -r pyproject.toml
```

### Como Usar 📃
1. Faça o upload de um arquivo Excel contendo os dados de não conformidades na interface.

2. O arquivo deve ter a coluna DATA NÃO CONFORMIDADE, NÃO CONFORMIDADE, CLIENTE, QTD NÃO CONFORME e OPERAÇÃO.
Selecione o intervalo de datas desejado para a análise.

3. Clique no botão "Gerar Gráficos" para visualizar os gráficos interativos:

* O primeiro gráfico mostrará a quantidade de não conformidades por tipo.
* O segundo gráfico mostrará a quantidade de não conformidades por cliente.
* O terceiro gráfico mostrará a quantidade de não conformidade por linha de produção.

### Rodando o Projeto👨‍💻
Para executar o dashboard, basta rodar o seguinte comando na raiz do projeto:

```bash
    streamlit run dashboard.py
```

Isso abrirá a aplicação no navegador, onde você pode interagir com os gráficos.

### Contribuição📚
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias para o projeto, fique à vontade para abrir uma issue ou submeter um pull request.

### Licença📃
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

<hr>