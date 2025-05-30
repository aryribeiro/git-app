Obs.: caso o app esteja no modo "sleeping" (dormindo) ao entrar, basta clicar no botão que estará disponível e aguardar, para ativar o mesmo. 
![print](https://github.com/user-attachments/assets/ea05b856-39d0-4cce-94ca-f1be40fe1015)

# 🔧 GitApp

Uma aplicação web moderna e profissional desenvolvida em Python/Streamlit para navegar e consultar comandos Git com exemplos práticos.

## 📋 Descrição

O GitApp é uma ferramenta de referência completa que oferece acesso rápido a mais de 150 comandos Git, organizados por nível de importância e com exemplos práticos de uso. A interface limpa e intuitiva permite filtrar comandos por categoria e buscar por termos específicos.

## ✨ Características

- 🎯 **157 comandos Git** organizados por importância
- 🔍 **Sistema de filtros avançado** por categoria e busca textual
- 📊 **Estatísticas em tempo real** dos comandos filtrados
- 💡 **Exemplos práticos** para cada comando
- 🎨 **Interface moderna** com design responsivo
- 📱 **Layout adaptável** para diferentes dispositivos

## 🚀 Funcionalidades

### Filtros Disponíveis
- **🔥 Essenciais (1-10)**: Comandos básicos e fundamentais
- **🚀 Intermediários (11-30)**: Comandos para uso diário
- **⚡ Avançados (31-60)**: Comandos para usuários experientes
- **🔧 Técnicos (61-100)**: Comandos especializados
- **🛠️ Específicos (101-157)**: Comandos para casos especiais

### Interface
- Barra lateral com filtros e estatísticas
- Seletor de comandos com visualização hierárquica
- Exibição detalhada com descrição e exemplos
- Código destacado com syntax highlighting

## 📦 Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd gitapp
   ```

2. **Crie um ambiente virtual** (recomendado)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador**
   ```
   http://localhost:8501
   ```

## 📁 Estrutura do Projeto

```
gitapp/
│
├── app.py              # Aplicação principal
├── comandos.csv        # Base de dados dos comandos Git
├── requirements.txt    # Dependências Python
├── README.md          # Documentação
└── .gitignore         # Arquivos ignorados pelo Git
```

## 🔧 Uso

1. **Filtrar comandos**: Use a barra lateral para selecionar o nível de importância
2. **Buscar comandos**: Digite termos na caixa de busca
3. **Selecionar comando**: Escolha um comando da lista suspensa
4. **Visualizar detalhes**: Veja a descrição e exemplos de uso
5. **Copiar comandos**: Use os exemplos fornecidos diretamente

## 📊 Dados

O arquivo `comandos.csv` contém:
- **comando**: O comando Git
- **descrição**: Explicação do que o comando faz
- **ordem_importância**: Nível de importância (1-157)
- **como_pode_ser_usado**: Exemplos práticos de uso

## 🛠️ Tecnologias

- **Python 3.7+**: Linguagem de programação
- **Streamlit**: Framework para aplicações web
- **Pandas**: Manipulação de dados
- **Pathlib**: Manipulação de caminhos de arquivo

## 🎨 Personalização

Para personalizar a aplicação:

1. **Modificar comandos**: Edite o arquivo `comandos.csv`
2. **Alterar estilo**: Modifique as seções de CSS inline no código
3. **Adicionar funcionalidades**: Estenda a classe `GitCommandsApp`

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Se você encontrar algum problema ou tiver sugestões:

- Abra uma issue no GitHub
- Entre em contato através do email: [seu-email@exemplo.com]

## 🏆 Agradecimentos

- Comunidade Git pela documentação completa
- Equipe Streamlit pelo framework fantástico
- Contribuidores que ajudaram a melhorar a aplicação

---

**Desenvolvido com ❤️ usando Python e Streamlit**
