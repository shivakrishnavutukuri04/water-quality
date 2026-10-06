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
