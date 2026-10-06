import streamlit as st
import numpy as np
import pickle

# =========================================================
# AQUA // WATER QUALITY INTELLIGENCE
# New visual concept:
# Editorial water experience + scientific analysis console
# Original model logic is preserved.
# =========================================================

st.set_page_config(
    page_title="AQUA // Water Quality Intelligence",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# MODEL — KEEPING YOUR ORIGINAL PREDICTION PIPELINE
# ---------------------------------------------------------
with open("svm_water_quality_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


# ---------------------------------------------------------
# DESIGN SYSTEM
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    * {
        box-sizing: border-box;
    }

    .stApp {
        background: #071b20;
        color: #f3fbfa;
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    .block-container {
        max-width: 1440px;
        padding: 0 0 80px 0;
    }

    /* =====================================================
       HERO
       ===================================================== */

    .hero {
        position: relative;
        min-height: 720px;
        overflow: hidden;
        padding: 34px 6vw 60px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;

        background:
            radial-gradient(circle at 72% 30%, rgba(79,220,214,.20), transparent 17%),
            radial-gradient(circle at 35% 70%, rgba(23,112,125,.22), transparent 26%),
            linear-gradient(180deg, #07191e 0%, #0a3038 57%, #071b20 100%);
    }

    /* water surface lines */
    .hero::before {
        content: "";
        position: absolute;
        inset: 0;
        opacity: .30;
        background:
            repeating-radial-gradient(
                ellipse at 50% 110%,
                transparent 0 24px,
                rgba(175,255,248,.10) 25px 26px,
                transparent 27px 48px
            );
        transform: perspective(500px) rotateX(55deg) scale(1.6);
        transform-origin: center bottom;
        pointer-events: none;
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 620px;
        height: 620px;
        right: -150px;
        top: 70px;
        border-radius: 50%;
        background:
            radial-gradient(
                circle at 36% 27%,
                rgba(255,255,255,.55) 0 1.5%,
                transparent 2%
            ),
            radial-gradient(
                circle at 42% 34%,
                rgba(255,255,255,.15),
                transparent 24%
            ),
            radial-gradient(
                circle,
                rgba(92,229,220,.20),
                rgba(92,229,220,.03) 44%,
                transparent 69%
            );
        border: 1px solid rgba(169,255,249,.13);
        box-shadow:
            inset -45px -50px 80px rgba(0,0,0,.25),
            0 0 100px rgba(73,224,215,.08);
        pointer-events: none;
    }

    .topbar {
        position: relative;
        z-index: 5;
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-size: 10px;
        letter-spacing: .20em;
        text-transform: uppercase;
    }

    .logo {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        letter-spacing: .22em;
    }

    .logo-dot {
        width: 28px;
        height: 28px;
        border: 1px solid rgba(147,255,247,.65);
        border-radius: 50%;
        display: grid;
        place-items: center;
        color: #8ef4ec;
        font-size: 12px;
    }

    .top-status {
        color: #7e9b9f;
    }

    .hero-content {
        position: relative;
        z-index: 4;
        max-width: 900px;
        margin-top: 90px;
    }

    .hero-kicker {
        color: #79e8df;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: .30em;
        text-transform: uppercase;
        margin-bottom: 24px;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(64px, 10vw, 142px);
        line-height: .82;
        letter-spacing: -.075em;
        font-weight: 700;
        margin: 0;
    }

    .hero-title .outline {
        color: transparent;
        -webkit-text-stroke: 1px rgba(234,255,253,.55);
    }

    .hero-title .aqua {
        color: #75e9e1;
    }

    .hero-description {
        max-width: 610px;
        margin-top: 34px;
        color: #9ab4b7;
        font-size: 14px;
        line-height: 1.85;
    }

    .hero-bottom {
        position: relative;
        z-index: 5;
        display: flex;
        align-items: end;
        justify-content: space-between;
        gap: 30px;
        margin-top: 80px;
    }

    .scroll-note {
        color: #668489;
        font-size: 10px;
        letter-spacing: .20em;
        text-transform: uppercase;
    }

    .hero-index {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 12px;
        color: #6f898d;
        letter-spacing: .15em;
    }

    .hero-index strong {
        color: #eefcfb;
        font-size: 28px;
    }

    /* floating data chips */
    .data-chip {
        position: absolute;
        z-index: 6;
        border: 1px solid rgba(187,255,250,.16);
        background: rgba(5,25,30,.48);
        backdrop-filter: blur(14px);
        border-radius: 13px;
        padding: 12px 15px;
        min-width: 118px;
        box-shadow: 0 20px 50px rgba(0,0,0,.18);
    }

    .chip-a {
        right: 12%;
        bottom: 145px;
    }

    .chip-b {
        right: 30%;
        top: 250px;
    }

    .chip-label {
        color: #628086;
        font-size: 8px;
        letter-spacing: .16em;
        text-transform: uppercase;
    }

    .chip-value {
        margin-top: 4px;
        color: #dffdfa;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 18px;
        font-weight: 600;
    }

    /* =====================================================
       SECTION STRUCTURE
       ===================================================== */

    .section {
        padding: 105px 6vw 10px;
    }

    .eyebrow {
        color: #6fe2da;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: .25em;
        text-transform: uppercase;
        margin-bottom: 18px;
    }

    .section-heading {
        max-width: 920px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(38px, 5vw, 68px);
        line-height: .98;
        letter-spacing: -.055em;
        margin: 0;
    }

    .section-heading span {
        color: #718d91;
    }

    .body-copy {
        max-width: 720px;
        color: #829da0;
        font-size: 14px;
        line-height: 1.85;
        margin-top: 24px;
    }

    /* =====================================================
       PROBLEM STATEMENT
       ===================================================== */

    .problem-layout {
        display: grid;
        grid-template-columns: 1.4fr .6fr;
        gap: 22px;
        margin-top: 50px;
    }

    .problem-main,
    .problem-side {
        border: 1px solid rgba(255,255,255,.09);
        border-radius: 25px;
        background: rgba(9,42,49,.55);
    }

    .problem-main {
        min-height: 330px;
        padding: 42px;
        position: relative;
        overflow: hidden;
    }

    .problem-main::after {
        content: "H₂O";
        position: absolute;
        right: 30px;
        bottom: -40px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 180px;
        line-height: 1;
        color: rgba(116,232,224,.035);
        font-weight: 700;
    }

    .problem-quote {
        position: relative;
        z-index: 2;
        max-width: 690px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(28px, 4vw, 51px);
        line-height: 1.03;
        letter-spacing: -.045em;
    }

    .problem-quote span {
        color: #73e7df;
    }

    .problem-side {
        padding: 32px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .side-label {
        color: #658186;
        font-size: 9px;
        letter-spacing: .18em;
        text-transform: uppercase;
    }

    .side-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 80px;
        line-height: .9;
        color: #e9fdfb;
    }

    .side-text {
        color: #789296;
        font-size: 11px;
        line-height: 1.7;
    }

    /* =====================================================
       PARAMETERS
       ===================================================== */

    .parameter-strip {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1px;
        margin-top: 52px;
        background: rgba(255,255,255,.09);
        border: 1px solid rgba(255,255,255,.09);
        border-radius: 20px;
        overflow: hidden;
    }

    .parameter {
        min-height: 130px;
        padding: 25px;
        background: #08252c;
    }

    .parameter-number {
        color: #64dcd5;
        font-size: 9px;
        letter-spacing: .16em;
    }

    .parameter-name {
        margin-top: 14px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 17px;
        color: #e6f8f6;
    }

    .parameter-desc {
        margin-top: 6px;
        color: #668388;
        font-size: 10px;
    }

    /* =====================================================
       ANALYSIS AREA
       ===================================================== */

    .analysis-shell {
        margin-top: 55px;
        border: 1px solid rgba(113,230,223,.15);
        border-radius: 30px;
        background:
            radial-gradient(circle at 95% 10%, rgba(87,226,216,.08), transparent 25%),
            #071f25;
        padding: 34px;
        box-shadow: 0 35px 90px rgba(0,0,0,.22);
    }

    .analysis-head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 25px;
        border-bottom: 1px solid rgba(255,255,255,.08);
        margin-bottom: 30px;
    }

    .analysis-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 22px;
        font-weight: 600;
    }

    .ready {
        border: 1px solid rgba(101,225,181,.25);
        color: #78dfb8;
        border-radius: 999px;
        padding: 7px 12px;
        font-size: 8px;
        letter-spacing: .16em;
        text-transform: uppercase;
    }

    [data-testid="stNumberInput"] label {
        color: #8da8ab !important;
        font-size: 10px !important;
        letter-spacing: .04em;
    }

    [data-testid="stNumberInput"] input {
        color: #eafffc !important;
        background: #0b3037 !important;
        border: 1px solid rgba(255,255,255,.09) !important;
        border-radius: 10px !important;
    }

    [data-testid="stNumberInput"] input:focus {
        border-color: rgba(110,231,223,.6) !important;
        box-shadow: 0 0 0 1px rgba(110,231,223,.16) !important;
    }

    .stButton > button {
        min-height: 58px;
        border-radius: 12px !important;
        border: 1px solid rgba(124,239,231,.45) !important;
        background: #7ce9e0 !important;
        color: #052127 !important;
        font-weight: 800 !important;
        letter-spacing: .12em;
        text-transform: uppercase;
        transition: all .2s ease;
        box-shadow: 0 16px 45px rgba(76,222,213,.12);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 22px 55px rgba(76,222,213,.20);
    }

    /* =====================================================
       RESULT
       ===================================================== */

    .result-section {
        margin-top: 58px;
    }

    .result-card {
        position: relative;
        overflow: hidden;
        min-height: 310px;
        border-radius: 30px;
        padding: 45px;
        border: 1px solid rgba(105,229,220,.22);
        background:
            radial-gradient(circle at 85% 35%, rgba(89,230,218,.16), transparent 25%),
            linear-gradient(135deg, #0b3a42, #072229);
    }

    .result-card.bad {
        border-color: rgba(255,124,119,.25);
        background:
            radial-gradient(circle at 85% 35%, rgba(255,124,119,.13), transparent 25%),
            linear-gradient(135deg, #3a2228, #1e171c);
    }

    .result-label {
        color: #6c8d91;
        font-size: 9px;
        letter-spacing: .22em;
        text-transform: uppercase;
    }

    .result-title {
        margin-top: 18px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(43px, 6vw, 78px);
        line-height: .92;
        letter-spacing: -.065em;
        max-width: 750px;
    }

    .result-copy {
        max-width: 650px;
        margin-top: 22px;
        color: #9ab5b8;
        font-size: 13px;
        line-height: 1.8;
    }

    .result-orb {
        position: absolute;
        width: 180px;
        height: 180px;
        right: 8%;
        top: 65px;
        border-radius: 50%;
        border: 1px solid rgba(168,255,249,.18);
        background: radial-gradient(
            circle at 33% 28%,
            rgba(255,255,255,.45),
            rgba(91,226,218,.20) 18%,
            rgba(11,74,83,.05) 62%,
            transparent 70%
        );
        box-shadow:
            inset -25px -25px 50px rgba(0,0,0,.28),
            0 0 65px rgba(89,229,219,.10);
    }

    .bad .result-orb {
        background: radial-gradient(
            circle at 33% 28%,
            rgba(255,255,255,.25),
            rgba(255,122,117,.22) 18%,
            rgba(88,32,40,.06) 62%,
            transparent 70%
        );
        box-shadow: 0 0 65px rgba(255,100,100,.08);
    }

    .snapshot-title {
        margin: 35px 0 14px;
        color: #678388;
        font-size: 9px;
        letter-spacing: .20em;
        text-transform: uppercase;
    }

    [data-testid="stMetric"] {
        background: #09262d;
        border: 1px solid rgba(255,255,255,.07);
        border-radius: 12px;
        padding: 12px !important;
    }

    [data-testid="stMetricLabel"] {
        color: #6c898d !important;
        font-size: 9px !important;
    }

    [data-testid="stMetricValue"] {
        color: #e7fbf9 !important;
        font-size: 19px !important;
    }

    /* =====================================================
       PROCESS
       ===================================================== */

    .process {
        display: grid;
        grid-template-columns: 1fr 50px 1fr 50px 1fr;
        align-items: center;
        margin-top: 48px;
    }

    .process-card {
        border: 1px solid rgba(255,255,255,.08);
        border-radius: 19px;
        background: #09252c;
        padding: 26px;
        min-height: 170px;
    }

    .process-num {
        color: #69ded6;
        font-size: 9px;
        letter-spacing: .18em;
    }

    .process-card h3 {
        font-family: 'Space Grotesk', sans-serif;
        margin: 16px 0 8px;
        font-size: 21px;
    }

    .process-card p {
        color: #708b8f;
        font-size: 11px;
        line-height: 1.7;
        margin: 0;
    }

    .process-arrow {
        color: #47767b;
        text-align: center;
        font-size: 22px;
    }

    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {
        margin: 105px 6vw 0;
        padding-top: 22px;
        border-top: 1px solid rgba(255,255,255,.08);
        display: flex;
        justify-content: space-between;
        gap: 20px;
        color: #506d71;
        font-size: 9px;
        letter-spacing: .16em;
        text-transform: uppercase;
    }

    /* =====================================================
       RESPONSIVE
       ===================================================== */

    @media (max-width: 950px) {
        .hero {
            min-height: 650px;
        }

        .hero::after {
            width: 390px;
            height: 390px;
            right: -130px;
        }

        .problem-layout {
            grid-template-columns: 1fr;
        }

        .parameter-strip {
            grid-template-columns: repeat(2, 1fr);
        }

        .process {
            grid-template-columns: 1fr;
            gap: 12px;
        }

        .process-arrow {
            display: none;
        }

        .result-orb {
            opacity: .3;
        }
    }

    @media (max-width: 620px) {
        .hero {
            min-height: 650px;
            padding: 24px 22px 38px;
        }

        .top-status {
            display: none;
        }

        .hero-title {
            font-size: 59px;
        }

        .hero-content {
            margin-top: 65px;
        }

        .chip-b {
            display: none;
        }

        .chip-a {
            right: 7%;
            bottom: 105px;
        }

        .section {
            padding-left: 22px;
            padding-right: 22px;
        }

        .parameter-strip {
            grid-template-columns: 1fr;
        }

        .problem-main,
        .problem-side,
        .analysis-shell,
        .result-card {
            padding: 25px;
        }

        .result-orb {
            display: none;
        }

        .footer {
            margin-left: 22px;
            margin-right: 22px;
            flex-direction: column;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown(
    """
    <section class="hero">

        <div class="topbar">
            <div class="logo">
                <div class="logo-dot">≈</div>
                AQUA
            </div>

            <div class="top-status">
                Water Quality Intelligence / SVM System
            </div>
        </div>

        <div class="hero-content">
            <div class="hero-kicker">
                Machine learning · water analysis · classification
            </div>

            <h1 class="hero-title">
                WATER<br>
                <span class="outline">IS</span>
                <span class="aqua">DATA.</span>
            </h1>

            <p class="hero-description">
                Water can appear clear and still contain a complex combination
                of measurable properties. AQUA transforms nine water-quality
                measurements into a machine-learning classification using the
                trained Support Vector Machine model behind this project.
            </p>
        </div>

        <div class="data-chip chip-b">
            <div class="chip-label">Input vector</div>
            <div class="chip-value">09 features</div>
        </div>

        <div class="data-chip chip-a">
            <div class="chip-label">Model engine</div>
            <div class="chip-value">SVM / ML</div>
        </div>

        <div class="hero-bottom">
            <div class="scroll-note">↓ Enter a water profile below</div>

            <div class="hero-index">
                PROJECT <strong>01</strong> / POTABILITY
            </div>
        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# PROBLEM STATEMENT
# ---------------------------------------------------------
st.markdown(
    """
    <section class="section">

        <div class="eyebrow">01 / The problem</div>

        <h2 class="section-heading">
            Clear water does not automatically mean
            <span>safe water.</span>
        </h2>

        <p class="body-copy">
            Water quality is influenced by multiple measurable characteristics.
            Looking at one value alone does not describe the complete sample.
            This project uses a trained Support Vector Machine to evaluate the
            combined input profile and classify the sample into the two output
            classes used by the application.
        </p>

        <div class="problem-layout">

            <div class="problem-main">
                <div class="problem-quote">
                    Instead of asking
                    <span>"Does the water look clean?"</span>
                    the system asks:
                    <span>"What does the data say?"</span>
                </div>
            </div>

            <div class="problem-side">
                <div class="side-label">Parameters observed</div>

                <div class="side-number">09</div>

                <div class="side-text">
                    pH · Hardness · Solids · Chloramines · Sulfate ·
                    Conductivity · Organic Carbon · Trihalomethanes ·
                    Turbidity
                </div>
            </div>

        </div>

    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# FEATURE MAP
# ---------------------------------------------------------
st.markdown(
    """
    <section class="section" style="padding-top:55px;">

        <div class="eyebrow">02 / What the model sees</div>

        <h2 class="section-heading">
            Nine measurements.<br>
            <span>One water profile.</span>
        </h2>

        <div class="parameter-strip">

            <div class="parameter">
                <div class="parameter-number">01 / CHEMISTRY</div>
                <div class="parameter-name">pH Level</div>
                <div class="parameter-desc">Acidity / alkalinity input</div>
            </div>

            <div class="parameter">
                <div class="parameter-number">02 / COMPOSITION</div>
                <div class="parameter-name">Hardness</div>
                <div class="parameter-desc">Dissolved mineral characteristic</div>
            </div>

            <div class="parameter">
                <div class="parameter-number">03 / SOLIDS</div>
                <div class="parameter-name">Solids</div>
                <div class="parameter-desc">Total dissolved solids input</div>
            </div>

            <div class="parameter">
                <div class="parameter-number">04 / TREATMENT</div>
                <div class="parameter-name">Chloramines</div>
                <div class="parameter-desc">Disinfection-related measurement</div>
            </div>

            <div class="parameter">
                <div class="parameter-number">05 / MINERALS</div>
                <div class="parameter-name">Sulfate</div>
                <div class="parameter-desc">Chemical composition input</div>
            </div>

            <div class="parameter">
                <div class="parameter-number">06 / ELECTRICAL</div>
                <div class="parameter-name">Conductivity</div>
                <div class="parameter-desc">Electrical conductivity input</div>
            </div>

            <div class="parameter">
                <div class="parameter-number">07 / ORGANIC</div>
                <div class="parameter-name">Organic Carbon</div>
                <div class="parameter-desc">Organic-content measurement</div>
            </div>

            <div class="parameter">
                <div class="parameter-number">08 / DISINFECTION</div>
                <div class="parameter-name">Trihalomethanes</div>
                <div class="parameter-desc">THM measurement</div>
            </div>

            <div class="parameter">
                <div class="parameter-number">09 / PHYSICAL</div>
                <div class="parameter-name">Turbidity</div>
                <div class="parameter-desc">Water clarity measurement</div>
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
    <section class="section" style="padding-top:95px;">

        <div class="eyebrow">03 / Live analysis</div>

        <h2 class="section-heading">
            Give the model<br>
            <span>a sample to read.</span>
        </h2>

        <p class="body-copy">
            Enter the same nine numerical parameters used by your original
            application. The model receives them in the original feature order.
        </p>

        <div class="analysis-shell">

            <div class="analysis-head">
                <div class="analysis-title">Water profile / input console</div>
                <div class="ready">● Model loaded</div>
            </div>

        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# ORIGINAL INPUTS — SAME FEATURES, NEW PRESENTATION
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
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

with col2:
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

with col3:
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


# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------
if st.button("Analyze Water Quality", use_container_width=True):

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

    if prediction[0] == 1:
        result = "Safe to Drink"
        result_class = "good"
        description = (
            "The trained SVM classified this parameter profile as the "
            "positive class used by the current application."
        )
    else:
        result = "Not Safe to Drink"
        result_class = "bad"
        description = (
            "The trained SVM classified this parameter profile as the "
            "negative class used by the current application."
        )

    st.markdown(
        f"""
        <section class="section result-section">

            <div class="eyebrow">04 / Model output</div>

            <div class="result-card {"" if result_class == "good" else "bad"}">

                <div class="result-label">
                    SVM classification / current sample
                </div>

                <div class="result-title">
                    {result}
                </div>

                <div class="result-copy">
                    {description}
                    <br><br>
                    This result is a machine-learning prediction from the
                    trained project model. It is not a laboratory test,
                    medical recommendation, or regulatory certification.
                </div>

                <div class="result-orb"></div>

            </div>

            <div class="snapshot-title">Input snapshot / values sent to model</div>

        </section>
        """,
        unsafe_allow_html=True,
    )

    # Snapshot of exactly what was sent to the model
    snapshot = [
        ("pH", ph),
        ("Hardness", Hardness),
        ("Solids", Solids),
        ("Chloramines", Chloramines),
        ("Sulfate", Sulfate),
        ("Conductivity", Conductivity),
        ("Organic Carbon", Organic_carbon),
        ("THM", Trihalomethanes),
        ("Turbidity", Turbidity),
    ]

    snap_cols = st.columns(5)

    for i, (label, value) in enumerate(snapshot):
        with snap_cols[i % 5]:
            st.metric(label, f"{value:g}")


# ---------------------------------------------------------
# MODEL FLOW
# ---------------------------------------------------------
st.markdown(
    """
    <section class="section">

        <div class="eyebrow">05 / The intelligence layer</div>

        <h2 class="section-heading">
            From raw measurements<br>
            <span>to a model decision.</span>
        </h2>

        <div class="process">

            <div class="process-card">
                <div class="process-num">01 / INPUT</div>
                <h3>Water profile</h3>
                <p>
                    Nine numerical measurements are collected from the
                    supplied water sample.
                </p>
            </div>

            <div class="process-arrow">→</div>

            <div class="process-card">
                <div class="process-num">02 / CLASSIFIER</div>
                <h3>SVM model</h3>
                <p>
                    The serialized Support Vector Machine evaluates the
                    complete feature vector.
                </p>
            </div>

            <div class="process-arrow">→</div>

            <div class="process-card">
                <div class="process-num">03 / DECISION</div>
                <h3>Classification</h3>
                <p>
                    The prediction is mapped to the two output labels used
                    by the original application.
                </p>
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
        <span>AQUA // WATER QUALITY INTELLIGENCE</span>
        <span>09 parameters · SVM classification · ML project</span>
    </div>
    """,
    unsafe_allow_html=True,
)
