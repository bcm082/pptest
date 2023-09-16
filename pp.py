import streamlit as st
import pandas as pd

st.title('Public Policy Data Portal')

st.sidebar.header('List of Congresses')

congresses = list(range(105, 119))  # This will create a list [105, 106, ..., 118]

selected_congress = st.sidebar.selectbox('Select a Congress', congresses)

file_path = f'./{selected_congress}.csv'
try:
    df = pd.read_csv(file_path)

    columns_to_search = st.multiselect("Choose columns to search:", df.columns.tolist(), default=df.columns.tolist())

    search_query = st.text_input("Enter your search query:")

    if search_query:
        mask = df[columns_to_search].apply(lambda x: x.str.contains(search_query, case=False, na=False)).any(axis=1)
        df = df[mask]
    
    st.dataframe(df)

    st.markdown(f"Total number of bills: {len(df)}")

except FileNotFoundError:
    st.error(f"Data for Congress {selected_congress} not found.")

