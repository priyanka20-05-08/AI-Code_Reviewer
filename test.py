import streamlit as st

st.title("🤖 AI Code Reviewer")

code = st.text_area("Paste your code here")

if st.button("Review Code"):

    if code == "":
        st.warning("Please paste some code!")

    else:
        st.success("Code Review Completed!")

        score = 100

        if "#" not in code:
            score -= 20

        if "try:" not in code:
            score -= 20

        st.info(f"📊 Code Quality Score: {score}/100")

        lines = len(code.split("\n"))
        st.write(f"📄 Total Lines: {lines}")

        if "print(" in code:
            st.write("✅ Output statements found")

        if "#" not in code:
            st.write("⚠️ Add comments to improve readability")

        if "try:" not in code:
            st.write("⚠️ Consider error handling")

        if lines > 50:
            st.warning("⚠️ Large code block detected")

        if "TODO" in code:
            st.warning("📝 TODO items found")

        report = f"""
AI Code Review Report

Code Quality Score: {score}/100
Total Lines: {lines}

Review Completed Successfully
"""

        st.download_button(
            "📥 Download Report",
            report,
            file_name="review_report.txt"
        )