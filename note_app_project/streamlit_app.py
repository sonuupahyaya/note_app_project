import streamlit as st
import requests

# Django backend URL (running on port 8000)
BASE_URL = "http://127.0.0.1:8000/api/notes/"

st.set_page_config(page_title="Notes App", layout="centered")

st.title("📝 Notes App ")

# Fetch notes from Django API
def fetch_notes():
    try:
        response = requests.get(BASE_URL, cookies=st.session_state.get("cookies", {}))
        if response.status_code == 200:
            return response.json()
        else:
            
            st.error("Failed to fetch notes. Please log in via Django first.")
            return []
    except Exception as e:
        st.error(f"Error: {e}")
        return []

# Add a new note
def add_note(title, content):
    data = {"title": title, "content": content}
    response = requests.post(BASE_URL, data=data, cookies=st.session_state.get("cookies", {}))
    if response.status_code in [200, 201]:
        st.success("Note added successfully!")
    else:
        st.error("Failed to add note.")

# Show existing notes
notes = fetch_notes()

if notes:
    st.subheader("📚 Your Notes")
    for note in notes:
        with st.expander(note["title"]):
            st.write(note["content"])
            st.caption(f"Created at: {note['created_at']}")
else:
    st.info("No notes found.")

# Create new note
st.subheader("➕ Add a New Note")
with st.form("new_note"):
    title = st.text_input("Title")
    content = st.text_area("Content")
    submitted = st.form_submit_button("Save Note")
    if submitted:
        add_note(title, content)
        st.experimental_rerun()
