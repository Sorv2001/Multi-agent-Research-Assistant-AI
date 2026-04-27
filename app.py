import streamlit as st
from pipeline import run_research_pipeline

# ---------- CONFIG ----------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🌿",
    layout="wide"
)

# ---------- STYLING ----------
st.markdown("""
<style>
body {
    background-color: #f7fdf9;
}
.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #2e7d32;
}

.stButton button {
    background: linear-gradient(90deg, #66bb6a, #43a047);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-weight: 600;
}

.stTextInput input {
    border-radius: 12px;
    border: 1px solid #c8e6c9;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<h1>🌿 AI Research Assistant</h1>
<p style='color:#555;'>Turn any topic into a structured research report in seconds</p>
""", unsafe_allow_html=True)

# ---------- INPUT ----------
col1, col2 = st.columns([3,1])

with col1:
    topic = st.text_input("🔍 What would you like to research?")

with col2:
    run_btn = st.button("✨ Generate")

# ---------- MAIN ----------
if run_btn:

    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("🌿 AI is researching for you..."):
            result = run_research_pipeline(topic)

        st.success("✨ Your research is ready!")

        # ---------- CARDS ----------
        
        

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📄 Extracted Knowledge")
        st.write(result.get("scraped_content", ""))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📝 Final Report")
        st.write(result.get("report", ""))
        
        
        
        
        


        st.download_button(
            "📥 Download Report",
            result.get("report", ""),
            file_name="research.txt"
        )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📊 Expert Feedback")
        st.write(result.get("feedback", ""))
        st.markdown("</div>", unsafe_allow_html=True)
        
        

# ---------- FOOTER ----------
st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>
Built with 💚 using LangChain + Mistral AI
</p>
""", unsafe_allow_html=True)