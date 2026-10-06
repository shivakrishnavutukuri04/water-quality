import streamlit as st
import numpy as np
import pickle

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="AQUA — Water Quality Intelligence",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------
with open("svm_water_quality_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# ---------------------------------------------------------
# GLOBAL STYLING
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    :root {
        --ink: #07171c;
        --deep: #082a32;
        --ocean: #0b4854;
        --cyan: #6fe5e2;
        --mint: #b7f6e7;
        --foam: #edfdfa;
        --white: #ffffff;
        --muted: #8ca7aa;
        --line: rgba(255,255,255,.12);
        --danger: #ff827d;
        --safe: #72e3bd;
    }

    .stApp {
        background:
            radial-gradient(circle at 78% 5%, rgba(111,229,226,.13), transparent 28%),
            radial-gradient(circle at 15% 28%, rgba(34,130,145,.15), transparent 25%),
            #06181d;
        color: var(--white);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stToolbar"] {
        visibility: hidden;
    }

    .block-container {
        max-width: 1320px;
        padding: 26px 5vw 70px;
    }

    /* ---------- NAV ---------- */
    .nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 58px;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 11px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        letter-spacing: .18em;
        font-size: 14px;
    }

    .brand-mark {
        width: 31px;
        height: 31px;
        border: 1px solid rgba(111,229,226,.55);
        border-radius: 50%;
        display: grid;
        place-items: center;
        color: var(--cyan);
        font-size: 15px;
        box-shadow: 0 0 24px rgba(111,229,226,.12);
    }

    .nav-meta {
        color: #7e9a9e;
        font-size: 11px;
        letter-spacing: .18em;
        text-transform: uppercase;
    }

    /* ---------- HERO ---------- */
    .hero {
        min-height: 520px;
        position: relative;
        overflow: hidden;
        border: 1px solid var(--line);
        border-radius: 34px;
        padding: 74px 7%;
        background:
            radial-gradient(circle at 78% 42%, rgba(111,229,226,.15), transparent 22%),
            linear-gradient(135deg, #09262d 0%, #06191f 58%, #0a343d 100%);
        box-shadow: 0 30px 100px rgba(0,0,0,.28);
    }

    .hero::before {
        content: "";
        position: absolute;
        width: 520px;
        height: 520px;
        right: -120px;
        top: -110px;
        border-radius: 50%;
        background: radial-gradient(
            circle at 35% 30%,
            rgba(255,255,255,.17),
            rgba(111,229,226,.07) 28%,
            transparent 66%
        );
        border: 1px solid rgba(255,255,255,.07);
    }

    .hero-copy {
        position: relative;
        z-index: 2;
        max-width: 700px;
    }

    .eyebrow {
        color: var(--cyan);
        font-size: 11px;
        letter-spacing: .28em;
        text-transform: uppercase;
        font-weight: 700;
        margin-bottom: 23px;
    }

    .hero h1 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(48px, 7vw, 92px);
        line-height: .91;
        letter-spacing: -.055em;
        margin: 0;
        font-weight: 700;
    }

    .hero h1 span {
        color: var(--cyan);
    }

    .hero-sub {
        max-width: 570px;
        color: #9cb6b9;
        font-size: 15px;
        line-height: 1.75;
        margin-top: 28px;
    }

    .hero-stats {
        display: flex;
        gap: 34px;
        margin-top: 38px;
        flex-wrap: wrap;
    }

    .hero-stat {
        border-left: 1px solid rgba(111,229,226,.35);
        padding-left: 14px;
    }

    .hero-stat strong {
        display: block;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 21px;
        color: #fff;
    }

    .hero-stat small {
        color: #718d91;
        font-size: 10px;
        letter-spacing: .13em;
        text-transform: uppercase;
    }

    /* ---------- WATER ORB ---------- */
    .water-orb {
        position: absolute;
        z-index: 1;
        right: 8%;
        top: 88px;
        width: 275px;
        height: 275px;
        border-radius: 50%;
        background:
            radial-gradient(circle at 34% 23%, rgba(255,255,255,.8) 0 2%, transparent 3%),
            radial-gradient(circle at 36% 29%, rgba(255,255,255,.2), transparent 19%),
            radial-gradient(circle at 48% 58%, rgba(111,229,226,.34), transparent 46%),
            linear-gradient(145deg, rgba(190,255,249,.25), rgba(21,105,116,.17));
        border: 1px solid rgba(197,255,250,.28);
        box-shadow:
            inset -25px -25px 60px rgba(0,0,0,.25),
            inset 20px 15px 50px rgba(255,255,255,.08),
            0 0 90px rgba(111,229,226,.10);
        backdrop-filter: blur(3px);
    }

    .water-orb::before,
    .water-orb::after {
        content: "";
        position: absolute;
        border: 1px solid rgba(111,229,226,.17);
        border-radius: 50%;
    }

    .water-orb::before {
        width: 360px;
        height: 360px;
        left: -43px;
        top: -43px;
    }

    .water-orb::after {
        width: 430px;
        height: 430px;
        left: -78px;
        top: -78px;
    }

    /* ---------- PROBLEM ---------- */
    .section {
        padding: 86px 2% 20px;
    }

    .section-label {
        color: var(--cyan);
        font-size: 10px;
        letter-spacing: .25em;
        text-transform: uppercase;
        font-weight: 700;
        margin-bottom: 15px;
    }

    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(30px, 4vw, 52px);
        line-height: 1.02;
        letter-spacing: -.04em;
        max-width: 780px;
        margin: 0;
    }

    .section-title span {
        color: #7f9da1;
    }

    .problem-copy {
        color: #88a2a6;
        max-width: 720px;
        line-height: 1.8;
        margin-top: 20px;
        font-size: 14px;
    }

    .problem-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1px;
        background: var(--line);
        border: 1px solid var(--line);
        margin-top: 46px;
        border-radius: 20px;
        overflow: hidden;
    }

    .problem-card {
        background: rgba(8,35,42,.72);
        padding: 28px;
        min-height: 140px;
    }

    .problem-number {
        font-family: 'Space Grotesk', sans-serif;
        color: var(--cyan);
        font-size: 27px;
        font-weight: 600;
    }

    .problem-card h4 {
        margin: 10px 0 5px;
        font-size: 13px;
        color: #e7f4f2;
    }

    .problem-card p {
        margin: 0;
        color: #708b8f;
        font-size: 11px;
        line-height: 1.6;
    }

    /* ---------- INPUT CONSOLE ---------- */
    .console {
        margin-top: 42px;
        border: 1px solid rgba(255,255,255,.11);
        border-radius: 28px;
        background: rgba(5,24,29,.72);
        overflow: hidden;
        box-shadow: 0 25px 80px rgba(0,0,0,.18);
    }

    .console-top {
        padding: 24px 28px;
        border-bottom: 1px solid var(--line);
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
    }

    .console-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 20px;
        font-weight: 600;
    }

    .console-status {
        color: var(--safe);
        border: 1px solid rgba(114,227,189,.22);
        border-radius: 999px;
        padding: 7px 12px;
        font-size: 9px;
        letter-spacing: .14em;
        text-transform: uppercase;
    }

    .console-body {
        padding: 30px;
    }

    .field-note {
        color: #617c80;
        font-size: 10px;
        letter-spacing: .12em;
        text-transform: uppercase;
        margin-bottom: 16px;
    }

    /* Streamlit widgets */
    [data-testid="stNumberInput"] label {
        color: #9db7ba !important;
        font-size: 11px !important;
        letter-spacing: .03em;
    }

    [data-testid="stNumberInput"] input {
        background: #0b2a31 !important;
        color: #efffff !important;
        border: 1px solid rgba(255,255,255,.09) !important;
        border-radius: 10px !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    [data-testid="stNumberInput"] input:focus {
        border-color: rgba(111,229,226,.55) !important;
        box-shadow: 0 0 0 1px rgba(111,229,226,.15) !important;
    }

    .stButton > button {
        width: 100%;
        min-height: 54px;
        margin-top: 14px;
        border: 1px solid rgba(111,229,226,.42) !important;
        border-radius: 12px !important;
        background: linear-gradient(135deg, #8bf0e7, #5bcfcf) !important;
        color: #062027 !important;
        font-weight: 800 !important;
        letter-spacing: .08em;
        text-transform: uppercase;
        box-shadow: 0 12px 35px rgba(78,214,207,.12);
        transition: .2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 18px 40px rgba(78,214,207,.18);
    }

    /* ---------- RESULT ---------- */
    .result-wrap {
        margin-top: 45px;
    }

    .result-card {
        position: relative;
        overflow: hidden;
        border-radius: 28px;
        border: 1px solid rgba(111,229,226,.18);
        background:
            radial-gradient(circle at 85% 20%, rgba(111,229,226,.14), transparent 26%),
            linear-gradient(135deg, #0b343b, #071f26);
        padding: 45px;
    }

    .result-card.safe {
        border-color: rgba(114,227,189,.25);
    }

    .result-card.unsafe {
        border-color: rgba(255,130,125,.25);
        background:
            radial-gradient(circle at 85% 20%, rgba(255,130,125,.10), transparent 26%),
            linear-gradient(135deg, #351d24, #1d171b);
    }

    .result-kicker {
        color: #789397;
        font-size: 10px;
        letter-spacing: .22em;
        text-transform: uppercase;
    }

    .result-value {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(38px, 5vw, 64px);
        line-height: 1;
        letter-spacing: -.05em;
        margin: 16px 0 14px;
    }

    .result-description {
        color: #9ab3b6;
        max-width: 620px;
        line-height: 1.7;
        font-size: 13px;
    }

    .drop-icon {
        position: absolute;
        right: 9%;
        top: 50%;
        transform: translateY(-50%) rotate(45deg);
        width: 95px;
        height: 95px;
        border-radius: 80% 10% 80% 80%;
        background: linear-gradient(145deg, #b6fff4, #319fa6);
        box-shadow:
            inset -12px -15px 24px rgba(0,40,48,.35),
            0 0 55px rgba(111,229,226,.15);
        opacity: .82;
    }

    .unsafe .drop-icon {
        background: linear-gradient(145deg, #ffb2a7, #a34e58);
        box-shadow: 0 0 55px rgba(255,130,125,.12);
    }

    /* ---------- FLOW ---------- */
    .flow {
        display: grid;
        grid-template-columns: 1fr auto 1fr auto 1fr;
        align-items: center;
        gap: 18px;
        margin-top: 38px;
    }

    .flow-card {
        border: 1px solid var(--line);
        border-radius: 18px;
        background: rgba(9,38,45,.58);
        padding: 25px;
    }

    .flow-index {
        color: var(--cyan);
        font-size: 10px;
        letter-spacing: .15em;
    }

    .flow-card h4 {
        margin: 14px 0 6px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 18px;
    }

    .flow-card p {
        color: #718c90;
        font-size: 11px;
        line-height: 1.6;
        margin: 0;
    }

    .arrow {
        color: #55777c;
        font-size: 20px;
    }

    /* ---------- FOOTER ---------- */
    .footer {
        margin-top: 100px;
        padding-top: 25px;
        border-top: 1px solid var(--line);
        display: flex;
        justify-content: space-between;
        gap: 20px;
        color: #567276;
        font-size: 10px;
        letter-spacing: .12em;
        text-transform: uppercase;
    }

    @media (max-width: 900px) {
        .water-orb {
            width: 190px;
            height: 190px;
            right: -35px;
            top: 155px;
            opacity: .55;
        }

        .problem-grid {
            grid-template-columns: repeat(2, 1fr);
        }

        .flow {
            grid-template-columns: 1fr;
        }

        .arrow {
            display: none;
        }

        .drop-icon {
            opacity: .25;
            right: 5%;
        }
    }

    @media (max-width: 600px) {
        .block-container {
            padding: 20px 18px 50px;
        }

        .hero {
            padding: 48px 28px;
            min-height: 570px;
        }

        .hero h1 {
            font-size: 50px;
        }

        .problem-grid {
            grid-template-columns: 1fr;
        }

        .console-body,
        .result-card {
            padding: 23px;
        }

        .footer {
            flex-direction: column;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------
st.markdown(
    """
    <div class="nav">
        <div class="brand">
            <div class="brand-mark">≈</div>
            AQUA
        </div>
        <div class="nav-meta">WATER QUALITY INTELLIGENCE / ML SYSTEM</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown(
    """
    <section class="hero">
        <div class="water-orb"></div>

        <div class="hero-copy">
            <div class="eyebrow">Water quality prediction · Machine learning</div>

            <h1>
                READ THE<br>
                WATER.<br>
                <span>BEFORE YOU DRINK.</span>
            </h1>

            <div class="hero-sub">
                A machine-learning based screening interface that evaluates
                nine measurable water-quality parameters and predicts whether
                the supplied sample is classified as potable by the trained SVM model.
            </div>

            <div class="hero-stats">
                <div class="hero-stat">
                    <strong>09</strong>
                    <small>Water parameters</small>
                </div>
                <div class="hero-stat">
                    <strong>SVM</strong>
                    <small>Classification model</small>
                </div>
                <div class="hero-stat">
                    <strong>01 / 0</strong>
                    <small>Prediction output</small>
                </div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# PROJECT PROBLEM
# ---------------------------------------------------------
st.markdown(
    """
    <section class="section">
        <div class="section-label">01 / Why this exists</div>

        <h2 class="section-title">
            Water can look clean.<br>
            <span>Its quality still needs evidence.</span>
        </h2>

        <p class="problem-copy">
            Water potability cannot be judged reliably from appearance alone.
            This project turns a set of measurable chemical and physical
            characteristics into a machine-learning classification.
            Instead of manually interpreting every parameter in isolation,
            the trained SVM model evaluates the complete input profile and
            returns a binary prediction.
        </p>

        <div class="problem-grid">
            <div class="problem-card">
                <div class="problem-number">09</div>
                <h4>Input parameters</h4>
                <p>pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes and turbidity.</p>
            </div>

            <div class="problem-card">
                <div class="problem-number">01</div>
                <h4>Model</h4>
                <p>A trained Support Vector Machine is loaded from the project's serialized model file.</p>
            </div>

            <div class="problem-card">
                <div class="problem-number">02</div>
                <h4>Classes</h4>
                <p>The application maps the model output into Safe to Drink or Not Safe to Drink.</p>
            </div>

            <div class="problem-card">
                <div class="problem-number">∞</div>
                <h4>Screening value</h4>
                <p>A fast project-level screening interface for exploring how the trained model responds to water profiles.</p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# ANALYSIS CONSOLE
# ---------------------------------------------------------
st.markdown(
    """
    <section class="section" style="padding-top:70px;">
        <div class="section-label">02 / Analysis console</div>

        <h2 class="section-title">
            Build the <span>water profile.</span>
        </h2>

        <p class="problem-copy">
            Enter the nine parameters used by the current prediction pipeline.
            The values below are starting points only and can be replaced with
            measurements from your sample.
        </p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="console">
        <div class="console-top">
            <div class="console-title">Sample composition</div>
            <div class="console-status">Model ready</div>
        </div>
        <div class="console-body">
            <div class="field-note">Measurement inputs</div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# INPUTS — SAME PARAMETERS AS ORIGINAL CODE
# ---------------------------------------------------------
c1, c2, c3 = st.columns(3)

with c1:
    ph = st.number_input(
        "pH Level",
        min_value=0.0,
        max_value=14.0,
        value=7.0,
        step=0.1,
    )

    Hardness = st.number_input(
        "Hardness",
        min_value=0.0,
        value=100.0,
        step=1.0,
    )

    Solids = st.number_input(
        "Solids (ppm)",
        min_value=0.0,
        value=20000.0,
        step=100.0,
    )

with c2:
    Chloramines = st.number_input(
        "Chloramines",
        min_value=0.0,
        value=5.0,
        step=0.1,
    )

    Sulfate = st.number_input(
        "Sulfate",
        min_value=0.0,
        value=300.0,
        step=1.0,
    )

    Conductivity = st.number_input(
        "Conductivity",
        min_value=0.0,
        value=500.0,
        step=1.0,
    )

with c3:
    Organic_carbon = st.number_input(
        "Organic Carbon",
        min_value=0.0,
        value=10.0,
        step=0.1,
    )

    Trihalomethanes = st.number_input(
        "Trihalomethanes",
        min_value=0.0,
        value=80.0,
        step=1.0,
    )

    Turbidity = st.number_input(
        "Turbidity",
        min_value=0.0,
        value=4.0,
        step=0.1,
    )

st.markdown("</div></div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# MODEL PREDICTION
# ---------------------------------------------------------
if st.button("Run Water Quality Analysis", use_container_width=True):

    input_data = np.array([[
        ph,
        Hardness,
        Solids,
        Chloramines,
        Sulfate,
        Conductivity,
        Organic_carbon,
        Trihalomethanes,
        Turbidity,
    ]])

    prediction = model.predict(input_data)

    is_safe = prediction[0] == 1

    if is_safe:
        result = "Safe to Drink"
        result_class = "safe"
        description = (
            "The trained SVM model classified the supplied parameter profile "
            "as the positive class used by this application."
        )
    else:
        result = "Not Safe to Drink"
        result_class = "unsafe"
        description = (
            "The trained SVM model classified the supplied parameter profile "
            "as the negative class used by this application."
        )

    st.markdown(
        f"""
        <section class="result-wrap">
            <div class="section-label">03 / Model prediction</div>

            <div class="result-card {result_class}">
                <div class="result-kicker">SVM classification result</div>
                <div class="result-value">{result}</div>
                <div class="result-description">
                    {description}
                    This is a machine-learning prediction and should not be
                    treated as a substitute for laboratory water-quality testing
                    or regulatory certification.
                </div>
                <div class="drop-icon"></div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    # Compact input snapshot
    st.markdown(
        """
        <div style="margin-top:32px;">
            <div class="section-label">Input snapshot</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    snapshot_cols = st.columns(5)

    snapshot = [
        ("pH", ph),
        ("Hardness", Hardness),
        ("Solids", Solids),
        ("Chloramines", Chloramines),
        ("Sulfate", Sulfate),
        ("Conductivity", Conductivity),
        ("Organic carbon", Organic_carbon),
        ("Trihalomethanes", Trihalomethanes),
        ("Turbidity", Turbidity),
    ]

    for i, (label, value) in enumerate(snapshot):
        with snapshot_cols[i % 5]:
            st.metric(label, f"{value:g}")

# ---------------------------------------------------------
# MODEL FLOW
# ---------------------------------------------------------
st.markdown(
    """
    <section class="section">
        <div class="section-label">04 / How the system works</div>

        <h2 class="section-title">
            From measurement<br>
            <span>to classification.</span>
        </h2>

        <div class="flow">
            <div class="flow-card">
                <div class="flow-index">01 / INPUT</div>
                <h4>Water profile</h4>
                <p>Nine numerical parameters describe the supplied water sample.</p>
            </div>

            <div class="arrow">→</div>

            <div class="flow-card">
                <div class="flow-index">02 / MODEL</div>
                <h4>SVM classifier</h4>
                <p>The serialized Support Vector Machine receives the complete feature vector.</p>
            </div>

            <div class="arrow">→</div>

            <div class="flow-card">
                <div class="flow-index">03 / OUTPUT</div>
                <h4>Binary decision</h4>
                <p>The prediction is mapped to Safe to Drink or Not Safe to Drink.</p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        <span>AQUA / WATER QUALITY INTELLIGENCE</span>
        <span>Machine learning project · SVM classification</span>
    </div>
    """,
    unsafe_allow_html=True,
)
