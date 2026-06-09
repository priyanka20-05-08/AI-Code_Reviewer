import streamlit as st

st.title("🤖 AI Code Reviewer")


code = st.text_area("Paste your code here")

if st.button("Review Code"):

    if code == "":
        st.warning("Please paste some code!")

    else:
        st.success("Code Review Completed!")
        if "print(" in code:
            st.write("✅ Output statements found")
        if "#" not in code:
            st.write("⚠ Add comments to improve readability")
        if "try:" not in code:

            st.write("⚠ Consider error handling")