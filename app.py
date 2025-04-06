import streamlit as st
import json

st.set_page_config(page_title="GPT Prompt Generator", layout="wide")
st.title("🧠 GPT Prompt Generator")

mode = st.radio("เลือกโหมด", ["My GPTs", "Customize ChatGPT"], horizontal=True)

# Common inputs
role = st.text_input("🧑‍💼 บทบาท (Role)", "")
task = st.text_input("🎯 งานหรือภารกิจ (Task)", "")
language = st.text_input("🌐 ภาษา", "Thai")

# Generate content
if mode == "My GPTs":
    gpt_name = st.text_input("🤖 ชื่อ GPT", "")
    file_name = st.text_input("📎 ไฟล์ (optional)", "")
    tool_name = st.text_input("🔧 เครื่องมือ (optional)", "")
    welcome_message = st.text_area("👋 ข้อความต้อนรับ", "")
    user_example = st.text_area("👤 ตัวอย่างคำถาม", "")
    assistant_example = st.text_area("🤖 ตัวอย่างคำตอบ", "")

    if st.button("🚀 Generate Prompt"):
        config = {
            "instructions": f"You are a {role} who helps users with {task}. Always respond formally, concisely, and in {language}.",
            "files": [file_name] if file_name else [],
            "tools": [tool_name] if tool_name else [],
            "name": gpt_name,
            "description": f"An assistant that helps users with {task} in {language}",
            "welcome_message": welcome_message,
            "sample_dialogue": [
                {
                    "user": user_example,
                    "assistant": assistant_example
                }
            ]
        }
        st.download_button("📥 Download JSON", data=json.dumps(config, indent=2), file_name="my_gpt_config.json", mime="application/json")
        st.code(json.dumps(config, indent=2), language="json")

else:
    tone = st.text_input("✒️ น้ำเสียง (Tone)", "formal and precise")
    output_style = st.text_input("🧱 โครงสร้างคำตอบ (Style)", "bullet points")
    rules = st.text_area("📏 Behavior Rules (1 บรรทัดต่อ 1 กฎ)")
    sample_question = st.text_area("🧪 คำถามตัวอย่าง", "")
    expected_answer = st.text_area("✅ คำตอบที่คาดหวัง", "")

    if st.button("🚀 Generate Prompt"):
        rules_list = "\n".join([f"- {r.strip()}" for r in rules.splitlines() if r.strip()])
        system_prompt = f"""You are a {role} who always responds in a {tone} tone using {output_style}.
Respond in {language}.
Rules:
{rules_list}
"""

        prompt_block = {
            "system_prompt": system_prompt,
            "sample_interaction": {
                "user": sample_question,
                "assistant": expected_answer
            }
        }
        st.download_button("📥 Download JSON", data=json.dumps(prompt_block, indent=2), file_name="custom_chatgpt_prompt.json", mime="application/json")
        st.code(json.dumps(prompt_block, indent=2), language="json")