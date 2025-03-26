import streamlit as st 
st.title("Counter App With Streamlit")
# session state
if 'count' not in st.session_state:
    st.session_state.count = 0

st.header("st.session_state.count 🔄")
count = st.session_state.count
col1, col2 = st.columns(2)

# Increment with col1:
with col1:
    if st.button("Increment"):
        st.session_state.count +=1  # Fix increment logic

# Decrement with col2:
with col2:
    if st.button("Decrement"):
        st.session_state.count -=1 # Fix decrement logic
st.write(f"Current count: {st.session_state.count}")

