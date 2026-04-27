# 🧮 Calculadora Python com CI/CD e Alertas no Discord

Este projeto é uma aplicação de Calculadora com interface gráfica desenvolvida em Python. O grande diferencial deste repositório é a implementação de uma esteira completa de **Integração e Entrega Contínua (CI/CD)** utilizando GitHub Actions, com testes automatizados e integração em tempo real com um bot do Discord.

## 📋 Sobre o Projeto

O objetivo principal foi unir o desenvolvimento de software tradicional com práticas modernas de **DevOps**. A cada novo commit ou Pull Request, a nuvem do GitHub constrói o ambiente, roda os testes unitários da calculadora em um monitor virtual e notifica a equipe no Discord sobre o status da operação.

### ✨ Funcionalidades:
* Interface Gráfica (GUI) moderna para cálculos matemáticos.
* Testes Unitários automatizados cobrindo as quatro operações básicas.
* Pipeline de CI/CD configurado no GitHub Actions.
* Alertas dinâmicos enviados para um servidor do Discord via Webhook.

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.10
* **Interface Gráfica:** CustomTkinter / Tkinter
* **Testes:** Módulo `unittest` nativo do Python
* **Automação (CI/CD):** GitHub Actions
* **Ambiente Virtual de Teste:** `xvfb` (X Virtual Framebuffer para testes de GUI no Linux)
* **Integração:** Webhooks do Discord (via cURL e Bash Scripting)

## ⚙️ Como a Esteira (Pipeline) Funciona

O arquivo `.github/workflows/pipeline.yml` escuta eventos no repositório e executa os seguintes passos:
1. Faz o checkout do código.
2. Instala o Python 3.10 e as dependências (incluindo o monitor virtual `xvfb`).
3. Roda a suíte de testes unitários do arquivo `test_calculadora.py`.
4. Avalia o evento gerador (Push, PR Aberto ou Merge) e o status do teste.
5. Dispara uma notificação personalizada para o canal do Discord informando o resultado.

## 🚀 Como executar o projeto localmente

Para rodar esta calculadora na sua máquina, você precisará ter o Python instalado.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/NicolasM3deiros/SEU_REPOSITORIO.git](https://github.com/NicolasM3deiros/SEU_REPOSITORIO.git)
