import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(
	page_title="Calculadora FQ A",
	page_icon="⌬",
	layout="wide"
)

# Cabeçalho
st.title("Calculadora FQ A", anchor=False)
st.subheader("*Atualizado: Fórmulas 2026*", anchor=False)

st.divider()

# Definir as constantes
constantes = { 
    "Capacidade térmica mássica da água líquida": 4.18e3,   # Capacidade térmica mássica da água líquida
    "Constante de Avogadro": 6.02e23,     					# Constante de Avogadro
    "Constante de gravitação universal": 6.67e-11,      	# Constante de gravitação universal
    "Índice de refração do ar": 1.000,      				# Índice de refração do ar
    "Aceleração gravítica": 9.80,          					# Aceleração gravítica
    "Velocidade da luz no vácuo": 3.00e8,    				# Velocidade da luz no vácuo
    "Produto iónico da água": 1.012e-14,    				# Produto iónico da água
    "Volume molar": 22.4         							# Volume molar
}

with st.sidebar:
	st.title("⌬ Calculadora FQ A")
	st.divider()

	st.subheader("Navegação")

	if st.button("Fórmulas", use_container_width=True):
		st.session_state.pagina = "Fórmulas"

	if st.button("Constantes", use_container_width=True):
		st.session_state.pagina = "Constantes"

	st.divider()
	st.caption("Atualizado para 2026")

if "pagina" not in st.session_state:
	st.session_state.pagina = "Fórmulas"

if st.session_state.pagina == "Fórmulas":
# Escolha da categoria
	st.subheader("Escolha a categoria da fórmula:", anchor=False)

	if "formula_ativa" not in st.session_state:
		st.session_state.formula_ativa = None

	categoria = st.radio(
		label="Texto",
		options=["Quantidades, massa e volume", "Soluções", "Energia", "Mecânica", "Ondas e Eletromagnetismo"],
		horizontal=False,
		label_visibility="collapsed"
	)

	st.divider()

# Caixas de diálogo

	@st.dialog("Calcular n-º de partículas")
	def calcular_n_particulas():
		st.subheader("Calcular n-º de partículas")
		st.latex(r"n = \frac{N}{N_A}")
		st.divider()

		N = st.number_input("Nº de partículas (N)", value=6.02e23, format="%.2e", step=1e20)
		if st.button("Calcular", type="primary", use_container_width=True):
			n = N / constantes["Constante de Avogadro"]
			st.success(f"**Resultado:** n = **{n:.4e}** mol")
			st.caption("Quantidade de matéria")

# Fórmulas para Quantidades, massa e volume
	if categoria == "Quantidades, massa e volume":
		st.subheader("Fórmulas para Quantidades, massa e volume", anchor=False)
		col1, col2, col3, col4 = st.columns(4)

		with col1:
			if st.button("Calcular n-º de partículas", use_container_width=True):
				calcular_n_particulas()
			st.latex(r"n = \frac{N}{N_A}")

		with col2:
			if st.button("Calcular Massa molar", use_container_width=True):
				st.session_state.formula_ativa = "massa_molar"
			st.latex(r"M = \frac{m}{n}")

		with col3:
			if st.button("Calcular volume molar", use_container_width=True):
				st.session_state.formula_ativa = "volume_molar"
			st.latex(r"V_m = \frac{V}{n}")

		with col4:
			if st.button("Calcular densidade", use_container_width=True):
				st.session_state.formula_ativa = "densidade"
			st.latex(r"\rho = \frac{m}{V}")

# Fórmulas para Soluções
	elif categoria == "Soluções":
		st.subheader("Fórmulas para Soluções", anchor=False)
		col1, col2, col3 = st.columns(3)

		with col1:
			if st.button("Calcular concentração", use_container_width=True):
				st.session_state.formula_ativa = "concentração"
			st.latex(r"c = \frac{n}{V}")

		with col2:
			if st.button("Calcular fração molar", use_container_width=True):
				st.session_state.formula_ativa = "fracao_molar"
			st.latex(r"{X_\text{A}} = \frac{n_\text{A}}{n_{\text{total}}}")

		with col3:
			if st.button("Calcular o pH", use_container_width=True):
				st.session_state.formula_ativa = "pH"
			st.latex(r"\text{pH} = -\log_{10}([H_3O^+])")

# Fórmulas para Energia
	elif categoria == "Energia":
		st.subheader("Fórmulas para Energia", anchor=False)
		col1, col2, col3, col4 = st.columns(4)

		with col1:
			if st.button("Calcular energia cinética", use_container_width=True):
				st.session_state.formula_ativa = "energia_cinetica"
			st.latex(r"E_c = \frac{1}{2} \times  m \times v^2")

			st.divider()

			if st.button("Calcular trabalho da força F", use_container_width=True):
				st.session_state.formula_ativa = "trabalho_F"
			st.latex(r"W_{\vec{F}} = F d \cos(\alpha)")

			st.divider()

			if st.button("Calcular diferença de potencial", use_container_width=True):
				st.session_state.formula_ativa = "U"
			st.latex(r"U = R \times I")

			st.divider()

			if st.button("Calcular energia absorvida/libertada", use_container_width=True):
				st.session_state.formula_ativa = "energia_absorvida_libertada"
			st.latex(r"E = m \times \Delta{h}")

		with col2:
			if st.button("Calcular energia potencial gravítica", use_container_width=True):
				st.session_state.formula_ativa = "energia_gravitica"
			st.latex(r"E_{pg} = m \times g \times h")

			st.divider()

			if st.button("Calcular trabalho da força FR pela Ec", use_container_width=True):
				st.session_state.formula_ativa = "trabalho_FR_Ec"
			st.latex(r"W_{\vec{F}_{R}} = \Delta{E_{c}}")

			st.divider()

			if st.button("Calcular potência elétrica", use_container_width=True):
				st.session_state.formula_ativa = "potencia_eletrica"
			st.latex(r"P = U \times I")

			st.divider()

			if st.button("Calcular variação da energia interna", use_container_width=True):
				st.session_state.formula_ativa = "variação_energia_interna"
			st.latex(r"\Delta{U}= W+Q")

		with col3:
			if st.button("Calcular energia mecânica", use_container_width=True):
				st.session_state.formula_ativa = "energia_mecanica"
			st.latex(r"E_{m} = E_{c} + E_{p}")

			st.divider()

			if st.button("Calcular trabalho da força FR pela Epg", use_container_width=True):
				st.session_state.formula_ativa = "trabalho_FR_EPG"
			st.latex(r"W_{\vec{F}_{R}} = -\Delta{E_{pg}}")

			st.divider()

			if st.button("Calcular diferença de potencial do gerador", use_container_width=True):
				st.session_state.formula_ativa = "U_gerador"
			st.latex(r"U = \varepsilon - r \times I")

			st.divider()

			if st.button("Calcular energia irradiada", use_container_width=True):
				st.session_state.formula_ativa = "E_irradiada"
			st.latex(r"E_r = \frac{P}{A}")

		with col4:
			if st.button("Calcular potência", use_container_width=True):
				st.session_state.formula_ativa = "potencia"
			st.latex(r"P = \frac{E}{\Delta{t}}")

			st.divider()

			if st.button("Calcular trabalho da força não conservativa", use_container_width=True):
				st.session_state.formula_ativa = "trabalho_FNC"
			st.latex(r"W_{\vec{F}_{NC}} = \Delta{E_m}")

			st.divider()

			if st.button("Calcular calorimetria", use_container_width=True):
				st.session_state.formula_ativa = "calorimetria"
			st.latex(r"E = m \times c \times \Delta{T}")

# Fórmulas para Mecânica
	elif categoria == "Mecânica":
		st.subheader("Fórmulas de Mecânica", anchor=False)
		col1, col2, col3 = st.columns(3)

		with col1:
			if st.button("Calcular posições", use_container_width=True):
				st.session_state.formula_ativa = "posições"
			st.latex(r"x = x_{0}+v_{0}t+\frac{1}{2}at^2")

			st.divider()

			if st.button("Calcular frequência angular",use_container_width=True):
				st.session_state.formula_ativa ="frequência_angular"
			st.latex(r"\omega = \frac{2\pi}{T}")

			if st.button("Calcular força gravítica", use_container_width=True):
				st.session_state.formula_ativa = "força_gravítica"
			st.latex(r"F_{g} = G \times \frac{m_{1} \times m_{2}}{r^2}")

		with col2:
			if st.button("Calcular velocidade", use_container_width=True):
				st.session_state.formula_ativa = "velocidade"
			st.latex(r"v = v_{0} + a \times t")

			st.divider()

			if st.button("Calcular força resultante", use_container_width=True):
				st.session_state.formula_ativa = "Força_resultante"
			st.latex(r"F = m \times a")

		with col3:
			if st.button("Calcular acelerarção centripeta",use_container_width=True):
				st.session_state.formula_ativa ="aceleração_centripeta"
			st.latex(r"a_{c} = \frac{v^2}{r}")

			st.divider()

			if st.button("Calcular velocidade angular", use_container_width=True):
				st.session_state.formula_ativa = "velocidade_angular"
			st.latex(r"v = \omega \times r")

# Fórmulas para Ondas e Eletromagnetismo
	elif categoria == "Ondas e Eletromagnetismo":
		st.subheader("Fórmulas para Ondas e Eletromagnetismo", anchor=False)
		col1, col2, col3 = st.columns(3)

		with col1:
			if st.button("Calcular comprimento de onda", use_container_width=True):
				st.session_state.formula_ativa ="comprimento_onda"
			st.latex(r"\lambda = \frac{v}{f}")

			st.divider()

			if st.button("Calcular índice de refração absoluto", use_container_width=True):
				st.session_state.formula_ativa ="índice_refração"
			st.latex(r"n = \frac{c}{v}")

		with col2:
			if st.button("Calcular fluxo magnético",use_container_width=True):
				st.session_state.formula_ativa ="fluxo_magnético"
			st.latex(r"\Phi_{m}=B\times A \times \cos(\alpha)")

			st.divider()

			st.button("Relação dos índices de refração",use_container_width=True)
			st.latex(r"n_{1} \sin(\alpha_{1}) = n_{2} \sin(\alpha_{2})")

		with col3:
			if st.button("Calcular indução eletromagnética",use_container_width=True):
				st.session_state.formula_ativa ="indução_eletromagnética"
			st.latex(r"\left|{\varepsilon_{i}}\right| = \frac {\Delta\Phi_{m}}{\Delta t}")

	st.divider()

elif st.session_state.pagina == "Constantes":
    st.title("Constantes Físicas e Químicas", anchor=False)
    st.subheader("Valores para o Exame Nacional de FQA 2026", anchor=False)
    st.divider()

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Lista de Constantes", anchor=False)
        for nome, valor in constantes.items():
            nome_formatado = nome.replace("_", " ").title()
            st.metric(label=nome_formatado, value=f"{valor:.3e}")
    
    with col2:
        st.subheader("Download")
        
        # Criar texto formatado para o ficheiro .txt
        texto_constantes = "CONSTANTES FQA 2026\n"
        texto_constantes += "="*40 + "\n\n"
        
        for nome, valor in constantes.items():
            nome_formatado = nome.replace("_", " ").title()
            texto_constantes += f"{nome_formatado:25} = {valor:.3e}\n"
        
        texto_constantes += "\nFonte: (https://iave.pt/wp-content/uploads/2025/11/IP-EX-FQA715-2026.pdf)"

        st.download_button(
            label="Descarregar Constantes (TXT)",
            data=texto_constantes,
            file_name="constantes_fqa_2026.txt",
            mime="text/plain"
        )
