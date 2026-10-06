import streamlit as st
import numpy as np
import pickle
import base64
from pathlib import Path

# ============================================================
# AQUA / WATER QUALITY ANALYSIS
# Visual direction:
# Editorial environmental website + scientific analysis tool
#
# Original ML pipeline is intentionally preserved.
# ============================================================

st.set_page_config(
    page_title="HYDROPREDICT — Water Quality Prediction",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"

HERO_IMAGE = ASSET_DIR / "water_testing_hero.jpg"
PROBLEM_IMAGE = ASSET_DIR / "water_access_problem.jpg"

def image_data_uri(path: Path) -> str:
    """Embed local image assets directly into the Streamlit HTML."""
    mime = "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"

# ------------------------------------------------------------
# MODEL — ORIGINAL LOGIC PRESERVED
# ------------------------------------------------------------
with open(BASE_DIR / "svm_water_quality_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


# ------------------------------------------------------------
# GLOBAL DESIGN
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    :root {
        --ink: #0a1719;
        --deep: #082b32;
        --water: #0e5661;
        --aqua: #70e1d7;
        --foam: #eefaf7;
        --sand: #d8c9aa;
        --muted: #71888a;
        --line: rgba(10, 23, 25, .12);
        --white: #ffffff;
        --danger: #c75b51;
        --safe: #247d68;
    }

    * { box-sizing: border-box; }

    .stApp {
        background: #f4f0e7;
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    .block-container {
        max-width: 1480px;
        padding: 0 0 80px;
    }

    /* Hide Streamlit's empty top spacing */
    .main .block-container {
        padding-top: 0;
    }

    /* ========================================================
       TOP NAV
       ======================================================== */

    .nav-wrap {
        height: 72px;
        padding: 0 5vw;
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: rgba(244,240,231,.94);
        border-bottom: 1px solid rgba(10,23,25,.08);
        position: relative;
        z-index: 10;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: .18em;
    }

    .brand-mark {
        width: 27px;
        height: 27px;
        border: 1.5px solid #0c777a;
        border-radius: 50%;
        display: grid;
        place-items: center;
        color: #0c777a;
        font-size: 12px;
    }

    .nav-right {
        display: flex;
        gap: 30px;
        color: #617476;
        font-size: 9px;
        letter-spacing: .18em;
        text-transform: uppercase;
    }

    /* ========================================================
       HERO — REAL WATER TESTING IMAGE
       ======================================================== */

    .hero {
        position: relative;
        min-height: 720px;
        overflow: hidden;
        background: #0a292f;
    }

    .hero-photo {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
        filter: saturate(.82) contrast(1.03);
    }

    .hero-overlay {
        position: absolute;
        inset: 0;
        background:
            linear-gradient(90deg, rgba(5,28,32,.93) 0%, rgba(5,28,32,.76) 43%, rgba(5,28,32,.16) 78%),
            linear-gradient(180deg, rgba(4,24,28,.48), rgba(4,24,28,.16) 45%, rgba(4,24,28,.68));
    }

    .hero-content {
        position: relative;
        z-index: 2;
        padding: 105px 7vw 70px;
        max-width: 950px;
    }

    .hero-eyebrow {
        color: #b7eee7;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: .28em;
        text-transform: uppercase;
        margin-bottom: 25px;
    }

    .hero-title {
        margin: 0;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(62px, 8vw, 126px);
        line-height: .82;
        letter-spacing: -.075em;
        color: white;
        font-weight: 700;
    }

    .hero-title .thin {
        color: rgba(255,255,255,.68);
        font-weight: 400;
    }

    .hero-title .accent {
        color: #76e4da;
    }

    .hero-copy {
        max-width: 590px;
        color: rgba(238,250,247,.75);
        font-size: 14px;
        line-height: 1.85;
        margin-top: 32px;
    }

    .hero-rule {
        width: 70px;
        height: 1px;
        background: #76e4da;
        margin-top: 38px;
    }

    .hero-meta {
        display: flex;
        gap: 38px;
        margin-top: 24px;
        flex-wrap: wrap;
    }

    .hero-meta-item {
        color: rgba(238,250,247,.62);
        font-size: 9px;
        letter-spacing: .15em;
        text-transform: uppercase;
    }

    .hero-meta-item strong {
        display: block;
        color: white;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 20px;
        letter-spacing: -.02em;
        margin-bottom: 4px;
    }

    .hero-side {
        position: absolute;
        z-index: 3;
        right: 5vw;
        bottom: 46px;
        color: rgba(255,255,255,.66);
        font-size: 9px;
        letter-spacing: .20em;
        text-transform: uppercase;
        writing-mode: vertical-rl;
        transform: rotate(180deg);
    }

    /* ========================================================
       INTRO / PROBLEM
       ======================================================== */

    .section {
        padding: 105px 6vw 20px;
    }

    .section-tag {
        color: #237b7a;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: .22em;
        text-transform: uppercase;
        margin-bottom: 18px;
    }

    .section-title {
        max-width: 980px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(38px, 5vw, 70px);
        line-height: .98;
        letter-spacing: -.055em;
        margin: 0;
    }

    .section-title em {
        color: #718184;
        font-style: normal;
    }

    .intro-copy {
        max-width: 730px;
        color: #617477;
        font-size: 14px;
        line-height: 1.85;
        margin-top: 25px;
    }

    /* ========================================================
       IMAGE + PROBLEM STORY
       ======================================================== */

    .story {
        margin-top: 54px;
        display: grid;
        grid-template-columns: 1.1fr .9fr;
        min-height: 530px;
        border-radius: 25px;
        overflow: hidden;
        background: #0a282e;
    }

    .story-photo {
        width: 100%;
        height: 100%;
        min-height: 530px;
        object-fit: cover;
    }

    .story-copy {
        padding: 54px;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        background:
            radial-gradient(circle at 90% 15%, rgba(110,225,214,.15), transparent 30%),
            #0a282e;
    }

    .story-kicker {
        color: #70dfd5;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: .23em;
        text-transform: uppercase;
    }

    .story-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(31px, 4vw, 52px);
        line-height: 1;
        letter-spacing: -.045em;
        margin: 20px 0;
    }

    .story-title span {
        color: #70dfd5;
    }

    .story-text {
        max-width: 520px;
        color: #9bb4b6;
        font-size: 13px;
        line-height: 1.8;
    }

    .story-foot {
        margin-top: 35px;
        padding-top: 18px;
        border-top: 1px solid rgba(255,255,255,.11);
        display: flex;
        gap: 30px;
    }

    .story-stat strong {
        display: block;
        font-family: 'Space Grotesk', sans-serif;
        color: white;
        font-size: 26px;
    }

    .story-stat span {
        color: #668185;
        font-size: 9px;
        letter-spacing: .12em;
        text-transform: uppercase;
    }

    /* ========================================================
       FEATURE CARDS
       ======================================================== */

    .feature-grid {
        margin-top: 50px;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
    }

    .feature-card {
        min-height: 215px;
        padding: 28px;
        border: 1px solid rgba(10,23,25,.10);
        background: #faf8f2;
        border-radius: 18px;
        position: relative;
        overflow: hidden;
    }

    .feature-card::after {
        content: "";
        position: absolute;
        width: 120px;
        height: 120px;
        right: -50px;
        bottom: -50px;
        border-radius: 50%;
        background: rgba(72,178,172,.09);
    }

    .feature-number {
        color: #23827f;
        font-size: 9px;
        letter-spacing: .17em;
        font-weight: 700;
    }

    .feature-name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 22px;
        margin-top: 20px;
    }

    .feature-text {
        color: #718083;
        font-size: 11px;
        line-height: 1.7;
        margin-top: 9px;
        max-width: 300px;
    }

    /* ========================================================
       ANALYSIS CONSOLE
       ======================================================== */

    .console-section {
        background: #0a242a;
        margin-top: 110px;
        padding: 100px 6vw 110px;
        color: white;
    }

    .console-section .section-tag {
        color: #75e0d7;
    }

    .console-title {
        max-width: 900px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(40px, 5vw, 70px);
        line-height: .98;
        letter-spacing: -.055em;
        margin: 0;
    }

    .console-title span {
        color: #6e8e92;
    }

    .console-description {
        max-width: 680px;
        color: #8ea8ab;
        font-size: 13px;
        line-height: 1.8;
        margin-top: 22px;
    }

    .console {
        margin-top: 48px;
        border: 1px solid rgba(255,255,255,.10);
        border-radius: 25px;
        background: #0d3037;
        padding: 31px;
    }

    .console-head {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 23px;
        margin-bottom: 28px;
        border-bottom: 1px solid rgba(255,255,255,.09);
    }

    .console-head-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 20px;
    }

    .console-status {
        color: #74dfb8;
        border: 1px solid rgba(116,223,184,.25);
        border-radius: 999px;
        padding: 7px 12px;
        font-size: 8px;
        letter-spacing: .14em;
        text-transform: uppercase;
    }

    [data-testid="stNumberInput"] label {
        color: #9ab5b7 !important;
        font-size: 10px !important;
    }

    [data-testid="stNumberInput"] input {
        background: #09262c !important;
        color: #f0fffd !important;
        border: 1px solid rgba(255,255,255,.09) !important;
        border-radius: 10px !important;
    }

    [data-testid="stNumberInput"] input:focus {
        border-color: rgba(112,225,215,.65) !important;
        box-shadow: 0 0 0 1px rgba(112,225,215,.15) !important;
    }

    .stButton > button {
        min-height: 58px;
        margin-top: 18px;
        border-radius: 11px !important;
        border: 1px solid rgba(112,225,215,.55) !important;
        background: #72dfd5 !important;
        color: #062127 !important;
        font-weight: 800 !important;
        letter-spacing: .11em;
        text-transform: uppercase;
        transition: .2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 16px 45px rgba(91,218,208,.15);
    }

    /* ========================================================
       RESULT
       ======================================================== */

    .result {
        margin-top: 48px;
        padding: 42px;
        border-radius: 25px;
        border: 1px solid rgba(112,225,215,.20);
        background:
            radial-gradient(circle at 90% 30%, rgba(112,225,215,.16), transparent 24%),
            #0d333a;
        position: relative;
        overflow: hidden;
    }

    .result.bad {
        border-color: rgba(231,122,112,.25);
        background:
            radial-gradient(circle at 90% 30%, rgba(231,122,112,.13), transparent 24%),
            #342328;
    }

    .result-label {
        color: #79979b;
        font-size: 9px;
        letter-spacing: .20em;
        text-transform: uppercase;
    }

    .result-title {
        margin-top: 16px;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(43px, 6vw, 78px);
        line-height: .92;
        letter-spacing: -.065em;
        color: white;
    }

    .result-copy {
        max-width: 690px;
        margin-top: 20px;
        color: #9eb8ba;
        font-size: 13px;
        line-height: 1.8;
    }

    .result-ring {
        position: absolute;
        right: 8%;
        top: 48px;
        width: 185px;
        height: 185px;
        border: 1px solid rgba(115,229,220,.22);
        border-radius: 50%;
        box-shadow:
            inset 0 0 0 18px rgba(112,225,215,.025),
            0 0 0 28px rgba(112,225,215,.025);
    }

    .bad .result-ring {
        border-color: rgba(231,122,112,.25);
        box-shadow:
            inset 0 0 0 18px rgba(231,122,112,.025),
            0 0 0 28px rgba(231,122,112,.025);
    }

    /* ========================================================
       SNAPSHOT + PROCESS
       ======================================================== */

    .snapshot-label {
        margin: 32px 0 14px;
        color: #789396;
        font-size: 9px;
        letter-spacing: .17em;
        text-transform: uppercase;
    }

    [data-testid="stMetric"] {
        background: #09262c;
        border: 1px solid rgba(255,255,255,.07);
        border-radius: 11px;
        padding: 11px !important;
    }

    [data-testid="stMetricLabel"] {
        color: #6f898d !important;
        font-size: 8px !important;
    }

    [data-testid="stMetricValue"] {
        color: #e7fbf8 !important;
        font-size: 18px !important;
    }

    .process-grid {
        margin-top: 48px;
        display: grid;
        grid-template-columns: 1fr 40px 1fr 40px 1fr;
        gap: 10px;
        align-items: center;
    }

    .process-card {
        padding: 28px;
        min-height: 180px;
        background: #faf8f2;
        border: 1px solid rgba(10,23,25,.09);
        border-radius: 18px;
    }

    .process-num {
        color: #2a8581;
        font-size: 9px;
        letter-spacing: .17em;
        font-weight: 700;
    }

    .process-card h3 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 21px;
        margin: 15px 0 8px;
    }

    .process-card p {
        color: #718083;
        font-size: 11px;
        line-height: 1.7;
        margin: 0;
    }

    .process-arrow {
        text-align: center;
        color: #2c8884;
        font-size: 22px;
    }

    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        margin: 90px 6vw 0;
        padding-top: 20px;
        border-top: 1px solid rgba(10,23,25,.12);
        display: flex;
        justify-content: space-between;
        color: #718083;
        font-size: 9px;
        letter-spacing: .16em;
        text-transform: uppercase;
    }

    @media (max-width: 900px) {
        .hero { min-height: 650px; }
        .story { grid-template-columns: 1fr; }
        .story-photo { min-height: 380px; }
        .feature-grid { grid-template-columns: 1fr; }
        .process-grid { grid-template-columns: 1fr; }
        .process-arrow { display: none; }
        .result-ring { opacity: .25; }
    }

    @media (max-width: 600px) {
        .nav-wrap { padding: 0 20px; }
        .nav-right { display: none; }
        .hero-content { padding: 75px 22px 55px; }
        .hero-title { font-size: 59px; }
        .hero-side { display: none; }
        .section { padding-left: 22px; padding-right: 22px; }
        .story-copy { padding: 30px; }
        .console-section { padding-left: 22px; padding-right: 22px; }
        .console { padding: 22px; }
        .result { padding: 27px; }
        .result-ring { display: none; }
        .footer {
            margin-left: 22px;
            margin-right: 22px;
            flex-direction: column;
            gap: 8px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# NAV
# ------------------------------------------------------------
st.html(
    """
    <div class="nav-wrap">
        <div class="brand">
            <div class="brand-mark">≈</div>
            HYDROPREDICT
        </div>


        <div class="nav-right">
            <span>Water quality</span>
            <span>Machine learning</span>
            <span>SVM analysis</span>
        </div>
    </div>
    """
)


# ------------------------------------------------------------
# HERO IMAGE
# ------------------------------------------------------------
if HERO_IMAGE.exists():
    hero_uri = image_data_uri(HERO_IMAGE)
    st.html(
        f"""
        <section class="hero">
            <img class="hero-photo" src="{hero_uri}" alt="Water quality testing">
            <div class="hero-overlay"></div>

            <div class="hero-content">
                <div class="hero-eyebrow">
                    Water quality analysis / machine learning
                </div>

                <h1 class="hero-title">
                    KNOW THE<br>
                    <span class="thin">WATER.</span><br>
                    <span class="accent">BEYOND</span><br>
                    APPEARANCE.
                </h1>

                <p class="hero-copy">
                    A project that uses nine measurable water-quality
                    parameters and a trained Support Vector Machine to
                    classify the supplied sample into the two classes used
                    by the prediction system.
                </p>

                <div class="hero-rule"></div>

                <div class="hero-meta">
                    <div class="hero-meta-item">
                        <strong>09</strong>
                        parameters
                    </div>

                    <div class="hero-meta-item">
                        <strong>SVM</strong>
                        classifier
                    </div>

                    <div class="hero-meta-item">
                        <strong>01 → 0</strong>
                        output classes
                    </div>
                </div>
            </div>

            <div class="hero-side">
                Measure · Analyse · Classify
            </div>
        </section>
        """
    )
else:
    st.error("Hero image missing. Keep assets/water_testing_hero.jpg beside app.py.")


# ------------------------------------------------------------
# INTRO
# ------------------------------------------------------------
st.html(
    """
    <section class="section">

        <div class="section-tag">01 / The reason</div>

        <h2 class="section-title">
            Water is essential.<br>
            <em>Its quality is a data problem.</em>
        </h2>

        <p class="intro-copy">
            A sample can look clear without telling the complete story.
            Water quality is influenced by several measurable chemical and
            physical properties. This project brings those measurements
            together and uses machine learning to produce a consistent
            classification from the complete input profile.
        </p>

    </section>
    """
)


# ------------------------------------------------------------
# STORY IMAGE + PROBLEM
# ------------------------------------------------------------
if PROBLEM_IMAGE.exists():
    problem_uri = image_data_uri(PROBLEM_IMAGE)

    st.html(
        f"""
        <section class="section" style="padding-top:35px;">

            <div class="story">

                <img
                    class="story-photo"
                    src="{problem_uri}"
                    alt="Person drinking water"
                >

                <div class="story-copy">

                    <div class="story-kicker">
                        The real-world question
                    </div>

                    <div class="story-title">
                        Can we make the
                        <span>invisible</span>
                        measurable?
                    </div>

                    <div class="story-text">
                        Water quality cannot be understood from appearance
                        alone. A machine-learning system can combine several
                        measured properties and learn a classification pattern
                        from historical water-quality data.
                        <br><br>
                        That is the idea behind this project:
                        turn a water sample into a structured feature vector,
                        pass it through the trained SVM model, and return the
                        corresponding class.
                    </div>

                    <div class="story-foot">
                        <div class="story-stat">
                            <strong>09</strong>
                            <span>measured features</span>
                        </div>

                        <div class="story-stat">
                            <strong>SVM</strong>
                            <span>learning model</span>
                        </div>
                    </div>

                </div>
            </div>

        </section>
        """
    )


# ------------------------------------------------------------
# FEATURE MAP
# ------------------------------------------------------------
st.html(
    """
    <section class="section" style="padding-top:90px;">

        <div class="section-tag">02 / The water profile</div>

        <h2 class="section-title">
            One sample.<br>
            <em>Nine signals.</em>
        </h2>

        <div class="feature-grid">

            <div class="feature-card">
                <div class="feature-number">01 / CHEMISTRY</div>
                <div class="feature-name">pH Level</div>
                <div class="feature-text">
                    Acidity / alkalinity measurement supplied to the model.
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-number">02 / COMPOSITION</div>
                <div class="feature-name">Hardness</div>
                <div class="feature-text">
                    Dissolved mineral characteristic of the sample.
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-number">03 / SOLIDS</div>
                <div class="feature-name">Solids</div>
                <div class="feature-text">
                    Total dissolved-solids measurement.
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-number">04 / TREATMENT</div>
                <div class="feature-name">Chloramines</div>
                <div class="feature-text">
                    Disinfection-related input used by the model.
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-number">05 / MINERALS</div>
                <div class="feature-name">Sulfate</div>
                <div class="feature-text">
                    Chemical composition measurement.
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-number">06 / ELECTRICAL</div>
                <div class="feature-name">Conductivity</div>
                <div class="feature-text">
                    Electrical conductivity of the water profile.
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-number">07 / ORGANIC</div>
                <div class="feature-name">Organic Carbon</div>
                <div class="feature-text">
                    Organic-content measurement.
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-number">08 / DISINFECTION</div>
                <div class="feature-name">Trihalomethanes</div>
                <div class="feature-text">
                    THM measurement supplied to the classifier.
                </div>
            </div>

            <div class="feature-card">
                <div class="feature-number">09 / PHYSICAL</div>
                <div class="feature-name">Turbidity</div>
                <div class="feature-text">
                    Water clarity measurement.
                </div>
            </div>

        </div>
    </section>
    """
)


# ------------------------------------------------------------
# ANALYSIS CONSOLE
# ------------------------------------------------------------
st.html(
    """
    <section class="console-section">

        <div class="section-tag">03 / Live analysis</div>

        <h2 class="console-title">
            Give the model<br>
            <span>a water profile.</span>
        </h2>

        <p class="console-description">
            Enter the nine numerical measurements used by the original
            application. The values are passed to the trained SVM in the
            same feature order as the existing project.
        </p>

        <div class="console">

            <div class="console-head">
                <div class="console-head-title">
                    Sample analysis console
                </div>

                <div class="console-status">
                    ● Model loaded
                </div>
            </div>

        </div>

    </section>
    """
)


# ------------------------------------------------------------
# ORIGINAL INPUTS — SAME VALUES / SAME ORDER
# ------------------------------------------------------------
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


# ------------------------------------------------------------
# PREDICTION
# ------------------------------------------------------------
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

    is_safe = prediction[0] == 1

    if is_safe:
        result = "Safe to Drink"
        result_class = ""
        description = (
            "The trained SVM classified this supplied parameter profile "
            "as the positive class used by the current application."
        )
    else:
        result = "Not Safe to Drink"
        result_class = "bad"
        description = (
            "The trained SVM classified this supplied parameter profile "
            "as the negative class used by the current application."
        )

    st.html(
        f"""
        <section class="console-section" style="padding-top:25px;">

            <div class="section-tag">04 / Model output</div>

            <div class="result {result_class}">

                <div class="result-label">
                    SVM classification / current sample
                </div>

                <div class="result-title">
                    {result}
                </div>

                <div class="result-copy">
                    {description}
                    <br><br>
                    This is a machine-learning prediction from the trained
                    project model. It is not a laboratory test or regulatory
                    certification.
                </div>

                <div class="result-ring"></div>

            </div>

            <div class="snapshot-label">
                Input snapshot / values sent to the model
            </div>

        </section>
        """
    )

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


# ------------------------------------------------------------
# MODEL PIPELINE
# ------------------------------------------------------------
st.html(
    """
    <section class="section">

        <div class="section-tag">05 / The intelligence</div>

        <h2 class="section-title">
            Measure.<br>
            <em>Classify.</em>
        </h2>

        <div class="process-grid">

            <div class="process-card">
                <div class="process-num">01 / INPUT</div>
                <h3>Water profile</h3>
                <p>
                    Nine numerical measurements describe the supplied sample.
                </p>
            </div>

            <div class="process-arrow">→</div>

            <div class="process-card">
                <div class="process-num">02 / MODEL</div>
                <h3>SVM classifier</h3>
                <p>
                    The serialized Support Vector Machine receives the complete
                    feature vector and predicts its learned class.
                </p>
            </div>

            <div class="process-arrow">→</div>

            <div class="process-card">
                <div class="process-num">03 / OUTPUT</div>
                <h3>Decision</h3>
                <p>
                    The numeric prediction is mapped to the application's
                    Safe to Drink or Not Safe to Drink result.
                </p>
            </div>

        </div>

    </section>
    """
)


# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.html(
    """
    <div class="footer">
        <span>HYDROPREDICT / Water Quality Prediction</span>
        <span>09 parameters · SVM classification · Machine learning project</span>
    </div>
    """
)

