import streamlit as st
import pandas as pd

df = pd.read_json('scrapy_crawler/scrapy_crawler/books.json')

st.markdown("""
    <style>
        div.st-emotion-cache-1wivap2 {
            font-size: 28px;
            font-weight: bold; 
        }
        div.st-emotion-cache-14553y9 {
            font-size:18px;
            font-weight: bold; 
        }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Projeto Inspira - Web Crawler (Interface)")

df["price"] = df["price"].astype(str).str.replace("£", "").astype(float)

df.dropna(subset=['genre'], inplace=True)

st.subheader("Tabela Baseada em Todos os Livros")
st.dataframe(df)

average_price_per_category = df.groupby("genre")["price"].mean().reset_index()
average_price_per_category.columns = ["Gênero", "Preço Médio"]

st.subheader("Selecione um Gênero")
selected_genre = st.selectbox("Escolha o gênero:", average_price_per_category['Gênero'].unique())
average_price = average_price_per_category[average_price_per_category['Gênero'] == selected_genre]['Preço Médio'].values[0]

st.write(f"Preço Médio do gênero '{selected_genre}': £{average_price:.2f}")

st.subheader("Preço Médio Geral")
st.metric(label="Preço Médio Geral", value=f"£{df['price'].mean():.2f}")

st.subheader("Distribuição de Avaliações")
ratings = df['rating'].value_counts().sort_index() 
for rating, count in ratings.items():
    st.write(f"{rating}: {count}")
    st.progress(count / ratings.sum())

st.subheader("Filtrar Produtos")
optionsfilter = {
    "Preço": "price",
    "Disponibilidade": "availability",
    "Avaliação": "rating",
    "Gênero": "genre"
}
selected_label = st.selectbox("Escolha o filtro:", list(optionsfilter.keys()))
selected_filter = optionsfilter[selected_label]

if df[selected_filter].dtype == "object":
    selected_value = st.selectbox("Escolha um valor:", df[selected_filter].unique())
    filtered_df = df[df[selected_filter] == selected_value]
else:
    min_value, max_value = st.slider("Selecione um intervalo:", 
                                     float(df[selected_filter].min()),
                                     float(df[selected_filter].max()),
                                     (float(df[selected_filter].min()),
                                     float(df[selected_filter].max())))
    filtered_df = df[(df[selected_filter] >= min_value) & (df[selected_filter] <= max_value)]

st.dataframe(filtered_df, use_container_width=True)
