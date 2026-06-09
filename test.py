import streamlit as st

st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖")

st.title("🤖 AI Code Reviewer")
st.subheader("🚀 Advanced Code Analysis")

code = st.text_area("Paste your code here")

if st.button("Review Code"):

    if code == "":
        st.warning("Please paste some code!")

    else:
        st.success("✅ Code Review Completed!")

        score = 100

        if "#" not in code:
            score -= 20

        if "try:" not in code:
            score -= 20

        st.info(f"📊 Code Quality Score: {score}/100")

        lines = len(code.split("\n"))
        st.write(f"📄 Total Lines: {lines}")

        if "print(" in code:
            st.success("✅ Output statements found")

        if "#" not in code:
            st.warning("⚠️ Add comments to improve readability")

        if "try:" not in code:
            st.warning("⚠️ Consider error handling")

        if lines > 50:
            st.warning("⚠️ Large code block detected")

        if "TODO" in code:
            st.warning("📝 TODO items found")

        # Security Checks
        if "import *" in code:
            st.error("❌ Avoid using import *")

        if "password" in code.lower():
            st.error("🔒 Possible hardcoded password detected")

        if len(code) > 500:
            st.warning("⚠️ Large code detected. Consider splitting into modules.")

        report = f"""
AI CODE REVIEW REPORT

Code Quality Score: {score}/100
Total Lines: {lines}

Review Results:
- Output Statement Check Completed
- Comment Check Completed
- Error Handling Check Completed
- Security Check Completed

Review Completed Successfully
"""

        st.download_button(
            "📥 Download Report",
            report,
            file_name="review_report.txt"
        )