# fiv
 This is a simple [Streamlit](https://streamlit.io/) app to estimate the **minimum number of frozen eggs** needed to achieve a desired probability of having at least one baby via IVF, based on a given success rate per egg.

# 🎯 Calculadora de Sucesso com Óvulos Congelados (FIV)

Esta é uma aplicação simples em [Streamlit](https://streamlit.io/) que estima o **número mínimo de óvulos** necessários para atingir uma probabilidade desejada de nascimento de um bebé através de FIV (fertilização in vitro), com base numa taxa de sucesso por óvulo.

## 🧮 O que a app faz

Com base nos seguintes dados introduzidos pelo utilizador:
- **Taxa de sucesso por óvulo** (ex: 20%)
- **Probabilidade desejada de nascimento** (ex: 95%)

A aplicação calcula:
- O **número mínimo de óvulos** necessários para atingir essa probabilidade, assumindo que cada óvulo tem uma chance independente de sucesso.

## 🚀 Como executar localmente

1. Clona este repositório:
   ```bash
   git clone https://github.com/teuusuario/taxa.git
   cd taxa

2. Instala as dependências:
   ```bash
   pip install streamlit

3. Executa a aplicação:
   ```bash
   streamlit run taxa.py

4. A app será aberta automaticamente no navegador: http://localhost:8501

## 📁 Ficheiros incluídos
calculadora_ovulos.py – script principal da aplicação em Streamlit

README.md – este ficheiro

research.md - ficheiro com alguma pesquisa onde indica quais as taxas de sucesso conseguidas em estudos controlados. As taxas descritas devem ser utilizadas para os cálculos na aplicação.

## 📊 Fórmula utilizada
A fórmula usada é:

n ≥ log(1 - P) / log(1 - p)

Onde:

p = taxa de sucesso por óvulo

P = probabilidade desejada de ter pelo menos um bebé

Nota: Verifica as percentagens de acordo com os estudos realizados no documento research.md

## ⚠️ Aviso
Esta calculadora é uma ferramenta estatística simplificada e não substitui aconselhamento médico. As taxas reais de sucesso variam consoante a clínica, idade da mulher e outros fatores clínicos. 



Feita com ❤️ para apoiar decisões informadas no planeamento da fertilidade.

Disclaimer: aplicação feita com o suporte do ChatGPT. 
