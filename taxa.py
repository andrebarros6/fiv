import math
import streamlit as st

st.title("Calculadora de Número Mínimo de Óvulos para Sucesso na FIV")

st.markdown("""
Esta aplicação calcula o número mínimo de óvulos necessários para atingir uma probabilidade desejada de nascimento de um bebé, dado um cenário conservador de taxa de sucesso por óvulo.

**Fórmula usada:**
\( n \geq \frac{\log(1 - P)}{\log(1 - p)} \)

Onde:
- \( p \): taxa de sucesso por óvulo (ex: 0.20)
- \( P \): probabilidade desejada de pelo menos 1 nascimento (ex: 0.95)
""")

# Inputs
success_rate = st.number_input("Taxa de sucesso por óvulo (entre 0.01 e 1.0):", min_value=0.01, max_value=1.0, value=0.20, step=0.01)
desired_prob = st.number_input("Probabilidade desejada de ter pelo menos um bebé (entre 0.50 e 0.999):", min_value=0.50, max_value=0.999, value=0.95, step=0.01)

# Cálculo
if success_rate >= 1.0:
    st.warning("A taxa de sucesso por óvulo não pode ser 100% para este cálculo.")
elif desired_prob >= 1.0:
    st.warning("A probabilidade desejada precisa ser inferior a 100%.")
else:
    try:
        n = math.ceil(math.log(1 - desired_prob) / math.log(1 - success_rate))
        st.success(f"\n✅ Seriam necessários **pelo menos {n} óvulos** para atingir uma chance de {int(desired_prob*100)}% de ter um bebé, assumindo uma taxa de sucesso de {int(success_rate*100)}% por óvulo.")
    except ValueError:
        st.error("Verifique se os valores estão entre 0 e 1 (não inclusivo).")
        