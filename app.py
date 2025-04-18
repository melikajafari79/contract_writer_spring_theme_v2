
import streamlit as st
import openai

st.set_page_config(page_title="قراردادساز هوشمند", page_icon="📝", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #f5fbe7;
            color: #2e2e2e;
            font-family: "Vazirmatn", sans-serif;
        }
        .stButton>button {
            background-color: #9be7ff;
            color: #1a1a1a;
            border-radius: 10px;
            padding: 0.5em 1em;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📝 قراردادساز هوشمند")

with st.form("contract_form"):
    contract_type = st.selectbox("نوع قرارداد", ["قرارداد همکاری", "قرارداد اجاره", "قرارداد فروش"])
    party_a = st.text_input("نام طرف اول")
    party_b = st.text_input("نام طرف دوم")
    subject = st.text_area("موضوع قرارداد")
    submitted = st.form_submit_button("تولید قرارداد")

if submitted:
    with st.spinner("در حال تولید قرارداد..."):
        prompt = f"قراردادی به زبان فارسی بنویس با اطلاعات زیر:\nنوع قرارداد: {contract_type}\nطرف اول: {party_a}\nطرف دوم: {party_b}\nموضوع: {subject}"
        try:
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
            )
            st.success("✅ قرارداد تولید شد")
            st.text_area("متن قرارداد", response.choices[0].message.content, height=400)
        except Exception as e:
            st.error("❌ خطا در تولید قرارداد: " + str(e))
