import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="تولید قرارداد", page_icon="📄", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #e0f7e9;
    }
    .stApp {
        background-color: #e0f7e9;
        color: #333333;
    }
    .stTextInput > div > div > input {
        background-color: white;
        color: #333333;
    }
    .stButton > button {
        background-color: #ffb6b9;
        color: #333;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📄 تولید هوشمند قرارداد")
st.markdown("لطفاً اطلاعات زیر را برای تولید قرارداد وارد کنید:")

party_a = st.text_input("نام طرف اول")
party_b = st.text_input("نام طرف دوم")
subject = st.text_input("موضوع قرارداد")
duration = st.text_input("مدت زمان قرارداد")
amount = st.text_input("مبلغ قرارداد (تومان)")
conditions = st.text_area("شرایط خاص")

if st.button("تولید قرارداد"):
    if not all([party_a, party_b, subject, duration, amount]):
        st.warning("لطفاً همه فیلدها را پر کنید.")
    else:
        with st.spinner("در حال تولید قرارداد..."):
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            prompt = f'''
            یک قرارداد حقوقی به زبان فارسی بنویس بین "{party_a}" و "{party_b}" با موضوع "{subject}"، مدت "{duration}" و مبلغ "{amount}" تومان.
            شرایط خاص: {conditions if conditions else "ندارد"}.
            قرارداد را به صورت رسمی و حقوقی بنویس.
            '''
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "شما یک وکیل حرفه‌ای هستید که قرارداد رسمی می‌نویسد."},
                    {"role": "user", "content": prompt}
                ]
            )
            contract = response.choices[0].message.content
            st.success("✅ قرارداد تولید شد:")
            st.text_area("متن قرارداد", contract, height=400)