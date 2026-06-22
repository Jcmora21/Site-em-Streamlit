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

# Caixas de diálogo para "Quantidades, massa e volume"

	@st.dialog("Calcular n-º de partículas")
	def calcular_n_particulas():
		st.subheader("Calcular n-º de partículas")
		st.latex(r"n = \frac{N}{N_A}")
		st.divider()

		N = st.number_input("Nº de partículas (n)", value=6.02e23, format="%.2e", step=1e20)
		if st.button("Calcular", type="primary", use_container_width=True):
			n = N / constantes["Constante de Avogadro"]
			st.success(f"**Resultado:** n = **{n:.4e}** mol")
			st.caption("Quantidade de matéria")

	@st.dialog("Calcular Massa molar")
	def calcular_massa_molar():
		st.subheader("Calcular Massa molar")
		st.latex(r"M = \frac{m}{n}")
		st.divider()

		m = st.number_input("Massa (m)", format="%0f", value=None)
		n = st.number_input("Mol (n)", format="%0f", value=None)
		if st.button("Calcular", type="primary", use_container_width=True):
			if n <= 0:
				st.error("n não pode ser 0 nem negativo!")
			else:
				M = m / n
				st.success(f"***Resultado:** M = **{M:.3f}** g/mol")

	@st.dialog("Calcular volume molar")
	def calcular_volume_molar():
		st.subheader("Calcular volume molar")
		st.latex(r"V_m = \frac{V}{n}")
		st.divider()

		escolha_Vm = st.radio(
			label="É um gás a condições PTN?",
			options=["Sim","Não"],
			horizontal=True)

		if escolha_Vm == "Sim":
			st.success("**Resultado:** Vm = 22.4 dm³/mol")
		if escolha_Vm == "Não":
			V = st.number_input("Volume (V) em dm³", format="%0f", value=None)
			n = st.number_input("Mol (n)", format="%0f", value=None)

			if st.button("Calcular", type="primary", use_container_width=True):
				if n <= 0:
					st.error("n não pode ser 0 nem negativo!")
				else:
					Vm = V / n
					st.success(f"**Resultado:** Vm = **{Vm:.3f}** dm³/mol")

	@st.dialog("Calcular densidade")
	def calcular_densidade():
		st.subheader("Calcular densidade")
		st.latex(r"\rho = \frac{m}{V}")
		st.divider()

		m = st.number_input("Massa (m)", format="%0f", value=None)
		V = st.number_input("Volume (V) em dm³", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if V <= 0:
				st.error("O volume não pode ser 0 nem negativo!")
			else:
				p = m / V
				st.success(f"**Resultado:** ρ = **{p:.3f}** Kg/dm³")

# Caixas de diálogo para Energia

	@st.dialog("Calcular concentração")
	def calcular_concentracao():
		st.subheader("Calcular concentração")
		st.latex(r"c = \frac{n}{V}")
		st.divider()

		n = st.number_input("Mol (n)", format="%0f", value=None)
		V = st.number_input("Volume (V) em dm³", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if V <= 0:
				st.error("O volume não pode ser 0 nem negativo!")
			else:
				c = n / V
				st.success(f"**Resultado:** c = {c:.3f} mol/dm³")

	@st.dialog("Calcular fração molar")
	def calcular_fracao_molar():
		st.subheader("Calcular fração molar")
		st.latex(r"{X_\text{A}} = \frac{n_\text{A}}{n_{\text{total}}}")
		st.divider()

		n_A = st.number_input("Mol do soluto (nA)", format="%0f", value=None)
		n_total = st.number_input("Mol total (ntotal)", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if n_total <= 0:
				st.error("O número total de mols não pode ser 0 nem negativo!")
			else:
				X_A = n_A / n_total
				st.success(f"**Resultado:** Xₐ = {X_A:.3f}")

	@st.dialog("Calcular o pH")
	def calcular_pH():
		st.subheader("Calcular o pH")
		st.latex(r"\text{pH} = -\log_{10}([H_3O^+])")
		st.divider()

		H3O_conc = st.number_input("Concentração de H₃O⁺ ([H₃O⁺]) em mol/dm³", format="%0.00e", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if H3O_conc <= 0:
				st.error("A concentração de H₃O⁺ deve ser maior que 0!")
			else:
				pH = -np.log10(H3O_conc)
				st.success(f"**Resultado:** pH = {pH:.3f}")

# Caixas de diálogo para Energia
	@st.dialog("Calcular energia cinética")
	def calcular_energia_cinetica():
		st.subheader("Calcular energia cinética")
		st.latex(r"E_c = \frac{1}{2} \times  m \times v^2")
		st.divider()

		m = st.number_input("Massa (m) em kg", format="%0f", value=None)
		v = st.number_input("Velocidade (v) em m/s", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			Ec = 0.5 * m * v**2
			st.success(f"**Resultado:** Ec = {Ec:.3f} J")

	@st.dialog("Calcular trabalho da força F")
	def calcular_trabalho_F():
		st.subheader("Calcular trabalho da força F")
		st.latex(r"W_{\vec{F}} = F d \cos(\alpha)")
		st.divider()

		F = st.number_input("Força (F) em N", format="%0f", value=None)
		d = st.number_input("Deslocamento (d) em m", format="%0f", value=None)
		alpha = st.number_input("Ângulo (α) entre a força e o deslocamento em graus", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			alpha_rad = np.radians(alpha)
			W_F = F * d * np.cos(alpha_rad)
			st.success(f"**Resultado:** Wₓ = {W_F:.3f} J")

	@st.dialog("Calcular diferença de potencial")
	def calcular_diferença_potencial():
		st.subheader("Calcular diferença de potencial")
		st.latex(r"U = R \times I")
		st.divider()

		R = st.number_input("Resistência (R) em Ω", format="%0f", value=None)
		I = st.number_input("Corrente (I) em A", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			U = R * I
			st.success(f"**Resultado:** U = {U:.3f} V")
	
	@st.dialog("Calcular energia absorvida/libertada")
	def calcular_energia_absorvida_libertada():
		st.subheader("Calcular energia absorvida/libertada")
		st.latex(r"E = m \times \Delta{h}")
		st.divider()

		m = st.number_input("Massa (m) em kg", format="%0f", value=None)
		delta_h = st.number_input("Variação de altura (Δh) em m", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			E = m * constantes["Aceleração gravítica"] * delta_h
			st.success(f"**Resultado:** E = {E:.3f} J")

	@st.dialog("Calcular energia potencial gravítica")
	def calcular_energia_potencial_gravitica():
		st.subheader("Calcular energia potencial gravítica")
		st.latex(r"E_{pg} = m \times g \times h")
		st.divider()

		m = st.number_input("Massa (m) em kg", format="%0f", value=None)
		h = st.number_input("Altura (h) em m", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			Epg = m * constantes["Aceleração gravítica"] * h
			st.success(f"**Resultado:** Eₚg = {Epg:.3f} J")

	@st.dialog("Trabalho da força FR pela Ec")
	def calcular_trabalho_FR_Ec():
		st.subheader("Trabalho da força FR pela Ec")
		st.latex(r"W_{\vec{F}_{R}} = \Delta{E_{c}}")
		st.divider()

		Ec_inicial = st.number_input("Energia cinética inicial (Ec₁) em J", format="%0f", value=None)
		Ec_final = st.number_input("Energia cinética final (Ec₂) em J", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			W_FR_Ec = Ec_final - Ec_inicial
			st.success(f"**Resultado:** Wₓ = {W_FR_Ec:.3f} J")

	@st.dialog("Calcular potência elétrica")
	def calcular_potencia_eletrica():
		st.subheader("Calcular potência elétrica")
		st.latex(r"P = U \times I")
		st.divider()

		U = st.number_input("Diferença de potencial (U) em V", format="%0f", value=None)
		I = st.number_input("Corrente (I) em A", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			P = U * I
			st.success(f"**Resultado:** P = {P:.3f} W")

	@st.dialog("Calcular variação da energia interna")
	def calcular_variação_energia_interna():
		st.subheader("Calcular variação da energia interna")
		st.latex(r"\Delta{U}= W+Q")
		st.divider()

		W = st.number_input("Trabalho (W) em J", format="%0f", value=None)
		Q = st.number_input("Calor (Q) em J", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			delta_U = W + Q
			st.success(f"**Resultado:** ΔU = {delta_U:.3f} J")

	@st.dialog("Calcular energia mecânica")
	def calcular_energia_mecanica():
		st.subheader("Calcular energia mecânica")
		st.latex(r"E_{m} = E_{c} + E_{p}")
		st.divider()

		Ec = st.number_input("Energia cinética (Ec) em J", format="%0f", value=None)
		Ep = st.number_input("Energia potencial (Ep) em J", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			Em = Ec + Ep
			st.success(f"**Resultado:** Em = {Em:.3f} J")

	@st.dialog("Calcular trabalho da força FR pela Epg")
	def calcular_trabalho_FR_EPG():
		st.subheader("Calcular trabalho da força FR pela Epg")
		st.latex(r"W_{\vec{F}_{R}} = -\Delta{E_{pg}}")
		st.divider()

		Epg_inicial = st.number_input("Energia potencial gravítica inicial (Epg₁) em J", format="%0f", value=None)
		Epg_final = st.number_input("Energia potencial gravítica final (Epg₂) em J", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			W_FR_Epg = -(Epg_final - Epg_inicial)
			st.success(f"**Resultado:** Wₓ = {W_FR_Epg:.3f} J")

	@st.dialog("Calcular diferença de potencial do gerador")
	def calcular_diferença_potencial_gerador():
		st.subheader("Calcular diferença de potencial do gerador")
		st.latex(r"U = \varepsilon - r \times I")
		st.divider()

		epsilon = st.number_input("Força eletromotriz (ε) em V", format="%0f", value=None)
		r = st.number_input("Resistência interna (r) em Ω", format="%0f", value=None)
		I = st.number_input("Corrente (I) em A", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			U_gerador = epsilon - r * I
			st.success(f"**Resultado:** U = {U_gerador:.3f} V")

	@st.dialog("Calcular energia irradiada")
	def calcular_energia_irradiada():
		st.subheader("Calcular energia irradiada")
		st.latex(r"E_r = \frac{P}{A}")
		st.divider()

		P = st.number_input("Potência (P) em W", format="%0f", value=None)
		A = st.number_input("Área (A) em m²", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if A <= 0:
				st.error("A área não pode ser 0 nem negativa!")
			else:
				E_irradiada = P / A
				st.success(f"**Resultado:** Eᵣ = {E_irradiada:.3f} W/m²")

	@st.dialog("Calcular potência")
	def calcular_potencia():
		st.subheader("Calcular potência")
		st.latex(r"P = \frac{E}{\Delta{t}}")
		st.divider()

		E = st.number_input("Energia (E) em J", format="%0f", value=None)
		delta_t = st.number_input("Variação de tempo (Δt) em s", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if delta_t <= 0:
				st.error("O tempo não pode ser 0 nem negativo!")
			else:
				P = E / delta_t
				st.success(f"**Resultado:** P = {P:.3f} W")

	@st.dialog("Calcular trabalho da força não conservativa")
	def calcular_trabalho_FNC():
		st.subheader("Calcular trabalho da força não conservativa")
		st.latex(r"W_{\vec{F}_{NC}} = \Delta{E_m}")
		st.divider()

		Em_inicial = st.number_input("Energia mecânica inicial (Em₁) em J", format="%0f", value=None)
		Em_final = st.number_input("Energia mecânica final (Em₂) em J", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			W_FNC = Em_final - Em_inicial
			st.success(f"**Resultado:** Wₓ = {W_FNC:.3f} J")

	@st.dialog("Calorimetria")
	def calcular_calorimetria():
		st.subheader("Calorimetria")
		st.latex(r"E = m \times c \times \Delta{T}")
		st.divider()

		m = st.number_input("Massa (m) em kg", format="%0f", value=None)
		c = st.number_input("Capacidade térmica mássica (c) em J/(kg·°C)", format="%0f", value=constantes["Capacidade térmica mássica da água líquida"])
		delta_T = st.number_input("Variação de temperatura (ΔT) em °C", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			E_calorimetria = m * c * delta_T
			st.success(f"**Resultado:** E = {E_calorimetria:.3f} J")

	@st.dialog("Calcular posições")
	def calcular_posições():
		st.subheader("Calcular posições")
		st.latex(r"x = x_{0}+v_{0}t+\frac{1}{2}at^2")
		st.divider()

		x0 = st.number_input("Posição inicial (x₀) em m", format="%0f", value=None)
		v0 = st.number_input("Velocidade inicial (v₀) em m/s", format="%0f", value=None)
		t = st.number_input("Tempo (t) em s", format="%0f", value=None)
		a = st.number_input("Aceleração (a) em m/s²", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			x = x0 + v0 * t + 0.5 * a * t**2
			st.success(f"**Resultado:** x = {x:.3f} m")

	@st.dialog("Calcular frequência angular")
	def calcular_frequência_angular():
		st.subheader("Calcular frequência angular")
		st.latex(r"\omega = \frac{2\pi}{T}")
		st.divider()

		T = st.number_input("Período (T) em s", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if T <= 0:
				st.error("O período não pode ser 0 nem negativo!")
			else:
				omega = 2 * np.pi / T
				st.success(f"**Resultado:** ω = {omega:.3f} rad/s")

	@st.dialog("Calcular força gravítica")
	def calcular_força_gravítica():
		st.subheader("Calcular força gravítica")
		st.latex(r"F_{g} = G \times \frac{m_{1} \times m_{2}}{r^2}")
		st.divider()

		m1 = st.number_input("Massa 1 (m₁) em kg", format="%0f", value=None)
		m2 = st.number_input("Massa 2 (m₂) em kg", format="%0f", value=None)
		r = st.number_input("Distância entre os centros de massa (r) em m", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if r <= 0:
				st.error("A distância não pode ser 0 nem negativa!")
			else:
				Fg = constantes["Constante de gravitação universal"] * (m1 * m2) / r**2
				st.success(f"**Resultado:** Fg = {Fg:.3e} N")

	@st.dialog("Calcular velocidade")
	def calcular_velocidade():
		st.subheader("Calcular velocidade")
		st.latex(r"v = v_{0} + a \times t")
		st.divider()

		v0 = st.number_input("Velocidade inicial (v₀) em m/s", format="%0f", value=None)
		a = st.number_input("Aceleração (a) em m/s²", format="%0f", value=None)
		t = st.number_input("Tempo (t) em s", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			v = v0 + a * t
			st.success(f"**Resultado:** v = {v:.3f} m/s")

	@st.dialog("Calcular força resultante")
	def calcular_força_resultante():
		st.subheader("Calcular força resultante")
		st.latex(r"F_{R} = m \times a")
		st.divider()

		m = st.number_input("Massa (m) em kg", format="%0f", value=None)
		a = st.number_input("Aceleração (a) em m/s²", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			FR = m * a
			st.success(f"**Resultado:** FR = {FR:.3f} N")

	@st.dialog("Calcular aceleração centripeta")
	def calcular_aceleracao_centripeta():
		st.subheader("Calcular aceleração centripeta")
		st.latex(r"a_c = \frac{v^2}{r}")
		st.divider()

		v = st.number_input("Velocidade (v) em m/s", format="%0f", value=None)
		r = st.number_input("Raio (r) em m", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if r <= 0:
				st.error("O raio não pode ser 0 nem negativo!")
			else:
				ac = v**2 / r
				st.success(f"**Resultado:** ac = {ac:.3f} m/s²")

	@st.dialog("Calcular velocidade angular")
	def calcular_velocidade_angular():
		st.subheader("Calcular velocidade angular")
		st.latex(r"\omega = \frac{v}{r}")
		st.divider()

		v = st.number_input("Velocidade (v) em m/s", format="%0f", value=None)
		r = st.number_input("Raio (r) em m", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if r <= 0:
				st.error("O raio não pode ser 0 nem negativo!")
			else:
				omega = v / r
				st.success(f"**Resultado:** ω = {omega:.3f} rad/s")

	@st.dialog("Calcular força centrípeta")
	def calcular_força_centrípeta():
		st.subheader("Calcular força centrípeta")
		st.latex(r"F_{c} = m \times a_{c}")
		st.divider()

		m = st.number_input("Massa (m) em kg", format="%0f", value=None)
		ac = st.number_input("Aceleração centripeta (a_c) em m/s²", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			Fc = m * ac
			st.success(f"**Resultado:** Fc = {Fc:.3f} N")

	@st.dialog("Calcular comprimento de onda")
	def calcular_comprimento_de_onda():
		st.subheader("Calcular comprimento de onda")
		st.latex(r"\lambda = \frac{c}{f}")
		st.divider()

		c = st.number_input("Velocidade da luz (c) em m/s", format="%0f", value=3e8)
		f = st.number_input("Frequência (f) em Hz", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if f <= 0:
				st.error("A frequência não pode ser 0 nem negativa!")
			else:
				lambda_ = c / f
				st.success(f"**Resultado:** λ = {lambda_:.3f} m")

	@st.dialog("Calcular índice de refração absoluto")
	def calcular_indice_refracao_absoluto():
		st.subheader("Calcular índice de refração absoluto")
		st.latex(r"n = \frac{c}{v}")
		st.divider()

		c = st.number_input("Velocidade da luz (c) em m/s", format="%0f", value=3e8)
		v = st.number_input("Velocidade da luz no meio (v) em m/s", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if v <= 0:
				st.error("A velocidade da luz no meio não pode ser 0 nem negativa!")
			else:
				n = c / v
				st.success(f"**Resultado:** n = {n:.3f}")

	@st.dialog("Calcular fluxo magnético")
	def calcular_fluxo_magnetico():
		st.subheader("Calcular fluxo magnético")
		st.latex(r"\Phi = B \times A \times \cos(\theta)")
		st.divider()

		B = st.number_input("Campo magnético (B) em T", format="%0f", value=None)
		A = st.number_input("Área (A) em m²", format="%0f", value=None)
		theta = st.number_input("Ângulo (θ) em graus", format="%0f", value=0)

		if st.button("Calcular", type="primary", use_container_width=True):
			if B is None or A is None:
				st.error("Os valores de B e A não podem ser nulos!")
			else:
				theta_rad = np.radians(theta)
				Phi = B * A * np.cos(theta_rad)
				st.success(f"**Resultado:** Φ = {Phi:.3f} Wb")
	
	@st.dialog("Calcular indução eletromagnética")
	def calcular_inducao_eletromagnetica():
		st.subheader("Calcular indução eletromagnética")
		st.latex(r"\left|{\varepsilon_{i}}\right| = \frac {\Delta\Phi_{m}}{\Delta t}")
		st.divider()

		delta_Phi = st.number_input("Variação do fluxo magnético (ΔΦ) em Wb", format="%0f", value=None)
		delta_t = st.number_input("Variação de tempo (Δt) em s", format="%0f", value=None)

		if st.button("Calcular", type="primary", use_container_width=True):
			if delta_t <= 0:
				st.error("O tempo não pode ser 0 nem negativo!")
			else:
				epsilon = delta_Phi / delta_t
				st.success(f"**Resultado:** ε = {epsilon:.3f} V")

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
				calcular_massa_molar()
			st.latex(r"M = \frac{m}{n}")

		with col3:
			if st.button("Calcular volume molar", use_container_width=True):
				calcular_volume_molar()
			st.latex(r"V_m = \frac{V}{n}")

		with col4:
			if st.button("Calcular densidade", use_container_width=True):
				calcular_densidade()
			st.latex(r"\rho = \frac{m}{V}")

# Fórmulas para Soluções
	elif categoria == "Soluções":
		st.subheader("Fórmulas para Soluções", anchor=False)
		col1, col2, col3 = st.columns(3)

		with col1:
			if st.button("Calcular concentração", use_container_width=True):
				calcular_concentracao()
			st.latex(r"c = \frac{n}{V}")

		with col2:
			if st.button("Calcular fração molar", use_container_width=True):
				calcular_fracao_molar()
			st.latex(r"{X_\text{A}} = \frac{n_\text{A}}{n_{\text{total}}}")

		with col3:
			if st.button("Calcular o pH", use_container_width=True):
				calcular_pH()
			st.latex(r"\text{pH} = -\log_{10}([H_3O^+])")

# Fórmulas para Energia
	elif categoria == "Energia":
		st.subheader("Fórmulas para Energia", anchor=False)
		col1, col2, col3, col4 = st.columns(4)

		with col1:
			if st.button("Calcular energia cinética", use_container_width=True):
				calcular_energia_cinetica()
			st.latex(r"E_c = \frac{1}{2} \times  m \times v^2")

			st.divider()

			if st.button("Calcular trabalho da força F", use_container_width=True):
				calcular_trabalho_F()
			st.latex(r"W_{\vec{F}} = F d \cos(\alpha)")

			st.divider()

			if st.button("Calcular diferença de potencial", use_container_width=True):
				calcular_diferença_potencial()
			st.latex(r"U = R \times I")

			st.divider()

			if st.button("Calcular energia absorvida/libertada", use_container_width=True):
				calcular_energia_absorvida_libertada()
			st.latex(r"E = m \times \Delta{h}")

		with col2:
			if st.button("Calcular energia potencial gravítica", use_container_width=True):
				calcular_energia_potencial_gravitica()
			st.latex(r"E_{pg} = m \times g \times h")

			st.divider()

			if st.button("Calcular trabalho da força FR pela Ec", use_container_width=True):
				calcular_trabalho_FR_Ec()
			st.latex(r"W_{\vec{F}_{R}} = \Delta{E_{c}}")

			st.divider()

			if st.button("Calcular potência elétrica", use_container_width=True):
				calcular_potencia_eletrica()
			st.latex(r"P = U \times I")

			st.divider()

			if st.button("Calcular variação da energia interna", use_container_width=True):
				calcular_variação_energia_interna()
			st.latex(r"\Delta{U}= W+Q")

		with col3:
			if st.button("Calcular energia mecânica", use_container_width=True):
				calcular_energia_mecanica()
			st.latex(r"E_{m} = E_{c} + E_{p}")

			st.divider()

			if st.button("Calcular trabalho da força FR pela Epg", use_container_width=True):
				calcular_trabalho_FR_EPG()
			st.latex(r"W_{\vec{F}_{R}} = -\Delta{E_{pg}}")

			st.divider()

			if st.button("Calcular diferença de potencial do gerador", use_container_width=True):
				calcular_diferença_potencial_gerador()
			st.latex(r"U = \varepsilon - r \times I")

			st.divider()

			if st.button("Calcular energia irradiada", use_container_width=True):
				calcular_energia_irradiada()
			st.latex(r"E_r = \frac{P}{A}")

		with col4:
			if st.button("Calcular potência", use_container_width=True):
				calcular_potencia()
			st.latex(r"P = \frac{E}{\Delta{t}}")

			st.divider()

			if st.button("Calcular trabalho da força não conservativa", use_container_width=True):
				calcular_trabalho_FNC()
			st.latex(r"W_{\vec{F}_{NC}} = \Delta{E_m}")

			st.divider()

			if st.button("Calcular calorimetria", use_container_width=True):
				calcular_calorimetria()
			st.latex(r"E = m \times c \times \Delta{T}")

# Fórmulas para Mecânica
	elif categoria == "Mecânica":
		st.subheader("Fórmulas de Mecânica", anchor=False)
		col1, col2, col3 = st.columns(3)

		with col1:
			if st.button("Calcular posições", use_container_width=True):
				calcular_posições()
			st.latex(r"x = x_{0}+v_{0}t+\frac{1}{2}at^2")

			st.divider()

			if st.button("Calcular frequência angular",use_container_width=True):
				calcular_frequência_angular()
			st.latex(r"\omega = \frac{2\pi}{T}")

			if st.button("Calcular força gravítica", use_container_width=True):
				calcular_força_gravítica()
			st.latex(r"F_{g} = G \times \frac{m_{1} \times m_{2}}{r^2}")

		with col2:
			if st.button("Calcular velocidade", use_container_width=True):
				calcular_velocidade()
			st.latex(r"v = v_{0} + a \times t")

			st.divider()

			if st.button("Calcular força resultante", use_container_width=True):
				calcular_força_resultante()
			st.latex(r"F = m \times a")

		with col3:
			if st.button("Calcular acelerarção centripeta",use_container_width=True):
				calcular_aceleracao_centripeta()
			st.latex(r"a_{c} = \frac{v^2}{r}")

			st.divider()

			if st.button("Calcular velocidade angular", use_container_width=True):
				calcular_velocidade_angular()
			st.latex(r"v = \omega \times r")

# Fórmulas para Ondas e Eletromagnetismo
	elif categoria == "Ondas e Eletromagnetismo":
		st.subheader("Fórmulas para Ondas e Eletromagnetismo", anchor=False)
		col1, col2, col3 = st.columns(3)

		with col1:
			if st.button("Calcular comprimento de onda", use_container_width=True):
				calcular_comprimento_de_onda()
			st.latex(r"\lambda = \frac{v}{f}")

			st.divider()

			if st.button("Calcular índice de refração absoluto", use_container_width=True):
				calcular_indice_refracao_absoluto()
			st.latex(r"n = \frac{c}{v}")

		with col2:
			if st.button("Calcular fluxo magnético",use_container_width=True):
				calcular_fluxo_magnetico()
			st.latex(r"\Phi_{m}=B\times A \times \cos(\alpha)")

			st.divider()

			if st.button("Relação dos índices de refração",use_container_width=True):
				st.subheader("Relação dos índices de refração")
			st.latex(r"n_{1} \sin(\alpha_{1}) = n_{2} \sin(\alpha_{2})")

		with col3:
			if st.button("Calcular indução eletromagnética",use_container_width=True):
				calcular_inducao_eletromagnetica()
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
