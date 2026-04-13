import streamlit as st
import requests

# ── CONFIG ─────────────────────────────────────────────────────────────────────
GITHUB_USER  = "tmisbaqcol-maker"
GITHUB_REPO  = "Web-AUCL"
DOCS_FOLDER  = "Docs - Gobierno"
GITHUB_BRANCH = "main"

st.set_page_config(
    page_title="ACUPALC – Plan Estratégico 2026-2030",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── ESTILOS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,600;0,800;1,300&family=DM+Sans:wght@300;400;500&display=swap');

  html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

  h1, h2, h3 { font-family: 'Fraunces', serif !important; }

  .hero-box {
    background: linear-gradient(135deg, #2D5016 0%, #4A7C2F 100%);
    color: #F5F0E8;
    border-radius: 12px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
  }
  .hero-box h1 { color: #F5F0E8 !important; font-size: 2.4rem; margin: 0 0 0.5rem; }
  .hero-box p  { color: rgba(245,240,232,0.8); margin: 0; font-size: 1rem; }
  .hero-tag {
    display: inline-block;
    background: rgba(201,162,39,0.25);
    border: 1px solid rgba(201,162,39,0.5);
    color: #C9A227;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 3px;
    margin-bottom: 1rem;
  }

  .metric-card {
    background: #F5F0E8;
    border-left: 4px solid #4A7C2F;
    border-radius: 0 8px 8px 0;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
  }
  .metric-card h4 { color: #2D5016; margin: 0 0 6px; font-size: 0.9rem; }
  .metric-card p  { color: #4A4A3A; margin: 0; font-size: 0.85rem; line-height: 1.5; }

  .eje-card {
    background: white;
    border: 1px solid rgba(0,0,0,0.07);
    border-radius: 10px;
    padding: 1.25rem;
    height: 100%;
  }
  .eje-num {
    display: inline-block;
    width: 32px; height: 32px;
    border-radius: 50%;
    text-align: center;
    line-height: 32px;
    font-weight: 700;
    font-size: 15px;
    color: white;
    margin-bottom: 0.75rem;
  }
  .e1 { background: #2D5016; }
  .e2 { background: #A0522D; }
  .e3 { background: #C9A227; color: #1A1A14 !important; }
  .e4 { background: #3A7D6B; }

  .dofa-f { background:#EAF3DE; border:1px solid #97C459; border-radius:8px; padding:1rem; }
  .dofa-o { background:#FAEEDA; border:1px solid #EF9F27; border-radius:8px; padding:1rem; }
  .dofa-d { background:#FAECE7; border:1px solid #F0997B; border-radius:8px; padding:1rem; }
  .dofa-a { background:#FCEBEB; border:1px solid #F09595; border-radius:8px; padding:1rem; }

  .doc-card {
    background: white;
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 8px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 12px;
    transition: border-color 0.2s;
  }
  .doc-icon { font-size: 24px; flex-shrink: 0; }
  .doc-info h4 { margin: 0 0 3px; font-size: 14px; color: #1A1A14; }
  .doc-info p  { margin: 0; font-size: 12px; color: #4A4A3A; }
  .doc-badge {
    display: inline-block;
    background: rgba(45,80,22,0.1);
    color: #2D5016;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 3px;
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .mapa-step {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
    color: #F5F0E8;
  }

  section { margin-bottom: 3rem; }
  .stTabs [data-baseweb="tab"] { font-family: 'DM Sans', sans-serif; }
</style>
""", unsafe_allow_html=True)


# ── SIDEBAR ──────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌱 ACUPALC")
    st.markdown("**Plan Estratégico 2026–2030**")
    st.markdown("---")
    st.markdown("""
    **Navegación**
    - [Identidad](#identidad-organizacional)
    - [Diagnóstico DOFA](#diagn-stico-dofa)
    - [Ejes Estratégicos](#ejes-estrat-gicos)
    - [Plan 2026](#plan-de-acci-n-2026)
    - [Documentos](#documentos-de-gobierno)
    - [Financiero](#plan-financiero)
    """)
    st.markdown("---")
    st.caption("Palmar de Candelaria, Colombia")
    st.caption("Asociación Corregimental de Usuarios Campesinos")


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-box">
  <div class="hero-tag">Horizonte estratégico 2026–2030</div>
  <h1>ACUPALC</h1>
  <p>Asociación Corregimental de Usuarios Campesinos de Palmar de Candelaria</p>
  <p style="margin-top:8px; color:rgba(245,240,232,0.6); font-size:14px;">
    Fortaleciendo el campo · Construyendo comunidad · Sembrando futuro sostenible
  </p>
</div>
""", unsafe_allow_html=True)


# ── TABS ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏛️ Identidad", "📊 DOFA", "🎯 Ejes Estratégicos",
    "📅 Plan 2026", "📁 Documentos", "💰 Financiero"
])


# ── TAB 1: IDENTIDAD ──────────────────────────────────────────────────────────
with tab1:
    st.markdown("## Identidad Organizacional")
    st.markdown("""
    ACUPALC es una organización campesina **sin ánimo de lucro**, de carácter comunitario,
    orientada al fortalecimiento social, productivo y económico de los pequeños productores
    del corregimiento de Palmar de Candelaria.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="metric-card">
          <h4>Misión</h4>
          <p>Representar, fortalecer y acompañar a los campesinos asociados mediante la gestión de proyectos productivos, sociales y ambientales, promoviendo el desarrollo sostenible, la seguridad alimentaria y el bienestar integral de las familias rurales del corregimiento.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
          <h4>Visión 2030</h4>
          <p>Ser una organización campesina sólida, autosostenible y reconocida a nivel municipal y departamental por su liderazgo en producción agropecuaria sostenible, gestión de recursos y defensa de los derechos del campesinado.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### Valores Institucionales")
    vals = ["Solidaridad", "Transparencia", "Participación democrática",
            "Equidad", "Responsabilidad ambiental", "Compromiso comunitario"]
    cols = st.columns(3)
    for i, v in enumerate(vals):
        with cols[i % 3]:
            st.success(v)


# ── TAB 2: DOFA ──────────────────────────────────────────────────────────────
with tab2:
    st.markdown("## Diagnóstico Estratégico — Matriz DOFA")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="dofa-f">
          <strong style="color:#3B6D11">💪 Fortalezas</strong>
          <ul style="margin:8px 0 0; color:#27500A; font-size:14px;">
            <li>Experiencia agrícola tradicional</li>
            <li>Sentido de pertenencia comunitario</li>
            <li>Base social organizada</li>
            <li>Conocimiento del territorio</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="dofa-o">
          <strong style="color:#854F0B">🚀 Oportunidades</strong>
          <ul style="margin:8px 0 0; color:#633806; font-size:14px;">
            <li>Acceso a programas del Estado (Min. Agricultura, UMATA)</li>
            <li>Convocatorias de cooperación internacional</li>
            <li>Mercados campesinos y compras públicas locales</li>
            <li>Programas de transición agroecológica</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <div class="dofa-d">
          <strong style="color:#993C1D">⚠️ Debilidades</strong>
          <ul style="margin:8px 0 0; color:#712B13; font-size:14px;">
            <li>Limitaciones en gestión administrativa</li>
            <li>Bajo acceso a financiamiento</li>
            <li>Falta de infraestructura productiva</li>
            <li>Escasa tecnificación</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="dofa-a">
          <strong style="color:#A32D2D">🔴 Amenazas</strong>
          <ul style="margin:8px 0 0; color:#791F1F; font-size:14px;">
            <li>Cambio climático</li>
            <li>Intermediación comercial</li>
            <li>Variabilidad de precios</li>
            <li>Conflictos por uso del suelo</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)


# ── TAB 3: EJES ──────────────────────────────────────────────────────────────
with tab3:
    st.markdown("## Ejes Estratégicos 2026–2030")

    ejes = [
        {
            "num": "1", "clase": "e1",
            "titulo": "Fortalecimiento Organizacional",
            "objetivo": "Consolidar la estructura administrativa, jurídica y financiera de ACUPALC.",
            "estrategias": [
                "Actualización de estatutos",
                "Capacitación en liderazgo y gestión",
                "Implementación de manuales administrativos",
                "Creación de comité de control interno",
            ],
            "indicadores": [
                "N° de capacitaciones realizadas",
                "Estados financieros actualizados",
                "Incremento de asociados activos",
            ],
        },
        {
            "num": "2", "clase": "e2",
            "titulo": "Desarrollo Productivo y Comercial",
            "objetivo": "Mejorar la productividad y el acceso a mercados.",
            "estrategias": [
                "Proyectos agropecuarios sostenibles",
                "Alianzas con mercados locales",
                "Creación de marca colectiva campesina",
                "Participación en ferias y ruedas de negocio",
            ],
            "indicadores": [
                "Incremento del volumen de producción",
                "Nuevos canales comerciales",
                "Aumento de ingresos por asociado",
            ],
        },
        {
            "num": "3", "clase": "e3",
            "titulo": "Gestión de Proyectos y Recursos",
            "objetivo": "Gestionar recursos públicos y privados para el desarrollo rural.",
            "estrategias": [
                "Elaboración de banco de proyectos",
                "Postulación a convocatorias",
                "Alianzas con alcaldía, gobernación y ONG",
                "Formación en formulación MGA",
            ],
            "indicadores": [
                "N° de proyectos presentados",
                "Proyectos aprobados",
                "Recursos gestionados anualmente",
            ],
        },
        {
            "num": "4", "clase": "e4",
            "titulo": "Sostenibilidad Ambiental",
            "objetivo": "Promover prácticas agrícolas sostenibles y responsables.",
            "estrategias": [
                "Capacitación en agroecología",
                "Conservación de fuentes hídricas",
                "Sistemas silvopastoriles",
                "Uso eficiente del agua",
            ],
            "indicadores": [
                "Hectáreas bajo manejo sostenible",
                "Productores capacitados",
                "Reducción en uso de agroquímicos",
            ],
        },
    ]

    col1, col2 = st.columns(2)
    for i, eje in enumerate(ejes):
        col = col1 if i % 2 == 0 else col2
        with col:
            with st.expander(f"Eje {eje['num']}: {eje['titulo']}", expanded=True):
                st.caption(f"*{eje['objetivo']}*")
                st.markdown("**Estrategias:**")
                for e in eje["estrategias"]:
                    st.markdown(f"→ {e}")
                st.markdown("**Indicadores:**")
                for ind in eje["indicadores"]:
                    st.markdown(f"📌 {ind}")


# ── TAB 4: PLAN 2026 ──────────────────────────────────────────────────────────
with tab4:
    st.markdown("## Plan de Acción 2026")

    import pandas as pd
    plan = pd.DataFrame([
        {
            "Actividad": "Actualización estatutaria",
            "Responsable": "Junta Directiva",
            "Plazo": "6 meses",
            "Indicador": "Estatutos aprobados",
            "Fuente de Recursos": "Recursos propios",
        },
        {
            "Actividad": "Proyecto productivo piloto",
            "Responsable": "Comité Productivo",
            "Plazo": "1 año",
            "Indicador": "Proyecto implementado",
            "Fuente de Recursos": "Convocatoria pública",
        },
        {
            "Actividad": "Capacitación en formulación de proyectos",
            "Responsable": "Presidencia",
            "Plazo": "3 meses",
            "Indicador": "20 asociados capacitados",
            "Fuente de Recursos": "Alcaldía",
        },
    ])

    st.dataframe(plan, use_container_width=True, hide_index=True)

    st.markdown("### Mapa Estratégico")
    st.markdown("**Ruta de impacto prevista:**")
    steps = [
        ("🏛️", "Fortalecimiento organizacional"),
        ("📋", "Mejor gestión de proyectos"),
        ("🌱", "Mayor productividad"),
        ("💰", "Mejores ingresos"),
        ("🤝", "Bienestar campesino sostenible"),
    ]
    cols = st.columns(len(steps) * 2 - 1)
    for i, (icon, label) in enumerate(steps):
        with cols[i * 2]:
            st.markdown(
                f"<div style='background:#2D5016;border-radius:8px;padding:12px;text-align:center;'>"
                f"<div style='font-size:22px'>{icon}</div>"
                f"<p style='color:#F5F0E8;font-size:12px;margin:6px 0 0;line-height:1.3'>{label}</p>"
                f"</div>",
                unsafe_allow_html=True,
            )
        if i < len(steps) - 1:
            with cols[i * 2 + 1]:
                st.markdown(
                    "<div style='text-align:center;font-size:22px;padding-top:16px;color:#8BB86A'>→</div>",
                    unsafe_allow_html=True,
                )

    st.markdown("### Seguimiento y Evaluación")
    scols = st.columns(4)
    seg_items = [
        ("📅", "Evaluación semestral", "Revisión de indicadores cada 6 meses"),
        ("📝", "Informe anual", "Reporte consolidado de gestión"),
        ("🏟️", "Asamblea general", "Rendición de cuentas a asociados"),
        ("📈", "Indicadores financieros", "Métricas sociales y económicas"),
    ]
    for i, (icon, titulo, desc) in enumerate(seg_items):
        with scols[i]:
            st.metric(label=f"{icon} {titulo}", value="", delta=desc)


# ── TAB 5: DOCUMENTOS ────────────────────────────────────────────────────────
with tab5:
    st.markdown("## Documentos de Gobierno")

    st.markdown("""
    <div style="background:#EAF3DE; border:1px solid #97C459; border-radius:8px; padding:1rem 1.25rem; margin-bottom:1.5rem; font-size:14px; color:#27500A;">
      <strong>NIT:</strong> 900857355-2 &nbsp;·&nbsp;
      <strong>Representante Legal:</strong> Alicia Esther Polo Julio &nbsp;·&nbsp;
      <strong>Domicilio:</strong> Luruaco, Atlántico
    </div>
    """, unsafe_allow_html=True)

    DOCS_REALES = [
        {
            "icon": "🏛️",
            "titulo": "Certificado UMATA – Alcaldía de Luruaco",
            "desc": "Certifica la inscripción como pequeño productor agropecuario del municipio de Luruaco. Firmado por Enois Junior Molina Mesino, Secretario de UMATA. Expedido: mayo de 2023.",
            "badge": "Certificado oficial",
            "archivo": "Documento_de_Alcaldia.jpeg",
        },
        {
            "icon": "📋",
            "titulo": "Formulario de Caracterización ANT",
            "desc": "N° FCAO-00007214. Registro ante la Agencia Nacional de Tierras. Domicilio: Luruaco, Atlántico. Tel: 3137852447. Correo: polojulioalicia@gmail.com",
            "badge": "ANT – Agencia Nacional de Tierras",
            "archivo": "Formulario_de_Caracterización.jpeg",
        },
        {
            "icon": "🤝",
            "titulo": "Registro fotográfico – Reunión de asociados",
            "desc": "Evidencia de asamblea comunitaria con miembros activos de ACUPALC en el corregimiento de Palmar de Candelaria.",
            "badge": "Registro comunitario",
            "archivo": "Integrantes.jpeg",
        },
        {
            "icon": "📊",
            "titulo": "RUT – Registro Único Tributario (DIAN)",
            "desc": "Formulario 001 · NIT: 900857355-2 · Razón social: ASOCIACION CORREGIMENTAL DE USUARIOS CAMPESINOS DE PALMAR DE CANDELARIA MUNICIPIO DE LURUACO ATLANTICO. Actualizado: 03/11/2022.",
            "badge": "DIAN – Tributario",
            "archivo": "RUT_-_DIAN.jpeg",
        },
    ]

    BASE_URL = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/tree/{GITHUB_BRANCH}/{requests.utils.quote(DOCS_FOLDER)}"

    for doc in DOCS_REALES:
        col_info, col_btn = st.columns([5, 1])
        with col_info:
            st.markdown(
                f"<div class='doc-card'>"
                f"  <div class='doc-icon'>{doc['icon']}</div>"
                f"  <div class='doc-info'>"
                f"    <h4>{doc['titulo']}</h4>"
                f"    <p>{doc['desc']}</p>"
                f"    <span class='doc-badge'>{doc['badge']}</span>"
                f"  </div>"
                f"</div>",
                unsafe_allow_html=True,
            )
        with col_btn:
            link = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{requests.utils.quote(DOCS_FOLDER)}/{requests.utils.quote(doc['archivo'])}"
            st.markdown(
                f"<a href='{link}' target='_blank' style='"
                f"display:inline-block;margin-top:10px;background:#2D5016;"
                f"color:white;padding:8px 16px;border-radius:4px;"
                f"text-decoration:none;font-size:13px;'>Ver →</a>",
                unsafe_allow_html=True,
            )

    st.markdown(f"[📂 Ver carpeta completa en GitHub]({BASE_URL})")


# ── TAB 6: FINANCIERO ────────────────────────────────────────────────────────
with tab6:
    st.markdown("## Plan Financiero Básico")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Fuentes de Ingresos")
        ingresos = [
            "Cuotas de afiliación de asociados",
            "Ingresos por proyectos productivos",
            "Convenios institucionales (alcaldía, gobernación)",
            "Donaciones y cooperación internacional",
        ]
        for item in ingresos:
            st.markdown(f"✅ {item}")

    with col2:
        st.markdown("### Control y Transparencia")
        control = [
            "Libro contable actualizado permanentemente",
            "Revisor fiscal o comité de vigilancia",
            "Presupuesto anual aprobado por Asamblea",
            "Informe semestral de ejecución",
        ]
        for item in control:
            st.markdown(f"✅ {item}")

    st.markdown("---")
    st.markdown("### Socialización del Plan")
    st.info("""
    Para que la planeación estratégica tenga impacto real:
    1. Socializar el documento con **todos los asociados**
    2. Ajustarlo **participativamente**
    3. Convertirlo en un **Plan Operativo Anual (POA)**
    4. Hacer **seguimiento periódico** con indicadores medibles
    """)


# ── FOOTER ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#888; font-size:13px; padding:1rem 0;">
  <strong>ACUPALC</strong> — Asociación Corregimental de Usuarios Campesinos de Palmar de Candelaria<br>
  Plan Estratégico 2026–2030 · Palmar de Candelaria, Colombia
</div>
""", unsafe_allow_html=True)
