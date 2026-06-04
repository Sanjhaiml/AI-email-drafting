import streamlit as st
import google.generativeai as genai

# Paste your Gemini API Key
GEMINI_API_KEY = "AQ.Ab8RN6Ic72VaOJhxbCP-ZkGyC7uzGG7IIVkIQkiEjabhycERtg"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Email Drafting Assistant",
    page_icon="📧",
    layout="wide"
)

st.title("📧 AI Email Drafting Assistant")

email_type = st.selectbox(
    "Select Email Type",
    [
        "Professional",
        "Leave Request",
        "Complaint",
        "Job Application",
        "Meeting Request",
        "Customer Support",
        "Custom"
    ]
)

recipient = st.text_input("Recipient Name")

purpose = st.text_area(
    "Describe the purpose of the email"
)

tone = st.selectbox(
    "Email Tone",
    [
        "Formal",
        "Professional",
        "Friendly",
        "Polite"
    ]
)

if st.button("Generate Email"):

    if purpose == "":
        st.warning("Please enter email details.")
    else:

        prompt = f"""
        Generate a professional email.

        Email Type: {email_type}
        Recipient: {recipient}
        Purpose: {purpose}
        Tone: {tone}

        Include:
        Subject Line
        Email Body
        Proper Greeting
        Professional Closing
        """

        try:
            with st.spinner("Generating Email..."):
                response = model.generate_content(prompt)

            st.success("Email Generated Successfully")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.caption("AI Email Drafting Assistant using Streamlit & Gemini AI")
