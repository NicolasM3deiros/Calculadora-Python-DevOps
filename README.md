# 🧮 Calculadora Python com CI/CD e Alertas no Discord

Este projeto é uma aplicação de Calculadora com interface gráfica (GUI) desenvolvida em Python. O grande diferencial deste repositório é a implementação de uma esteira completa de **Integração e Entrega Contínua (CI/CD)** utilizando GitHub Actions, com execução de testes automatizados em ambiente virtualizado e notificações em tempo real via Discord.

## 📋 Sobre o Projeto

O objetivo principal deste projeto foi unir o desenvolvimento de software tradicional com práticas modernas de **DevOps**. A cada novo *commit* ou *Pull Request*, a infraestrutura do GitHub Actions é acionada para construir o ambiente, instalar dependências e validar o código.

### ✨ Funcionalidades:
* **Interface Gráfica (GUI):** Design moderno e responsivo para operações matemáticas.
* **Testes Unitários:** Suite de testes automatizados cobrindo as operações básicas (Soma, Subtração, Multiplicação e Divisão).
* **Pipeline de CI/CD:** Automação completa do fluxo de trabalho.
* **Alertas no Discord:** Notificações dinâmicas enviadas para um servidor através de Webhooks, informando o autor do commit, a branch e o status dos testes.

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** [Python 3.10+](https://www.python.org/)
* **Interface Gráfica:** `CustomTkinter` / `Tkinter`
* **Testes:** Módulo `unittest` (nativo)
* **Automação (CI/CD):** [GitHub Actions](https://github.com/features/actions)
* **Ambiente Virtual de Teste:** `xvfb` (X Virtual Framebuffer para rodar GUIs em servidores Linux)
* **Integração:** Webhooks do Discord via `curl` e Bash Scripting

## ⚙️ Como a Esteira (Pipeline) Funciona

O fluxo de trabalho está definido em `.github/workflows/pipeline.yml` e segue estas etapas:
1. **Checkout:** O código é baixado na máquina virtual do GitHub.
2. **Setup:** Configuração do ambiente Python e instalação da biblioteca `customtkinter`.
3. **Instalação do xvfb:** Instalação do monitor virtual necessário para rodar testes de interface gráfica em servidores sem monitor físico.
4. **Execução de Testes:** O comando `xvfb-run` dispara o `unittest`.
5. **Notificação:** Um script avalia se o evento foi um *Push* ou *Pull Request* e envia a mensagem personalizada para o canal do Discord.

## 🚀 Como executar o projeto localmente

Para rodar esta calculadora na sua máquina, siga os passos abaixo:

1. Clone o repositório:
    git clone https://github.com/NicolasM3deiros/NOME_DO_REPOSITORIO.git

2. Acesse a pasta do projeto:
    cd NOME_DO_REPOSITORIO

3. Instale a biblioteca de interface gráfica:
    pip install customtkinter

4. Execute a aplicação:
    python Calculadora.py

5. Para rodar os testes unitários manualmente:
    python -m unittest test_calculadora.py

---
Desenvolvido por **Nicolas Alcides Laranjeira Medeiros** 🎓
