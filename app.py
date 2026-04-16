import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Startup Funding Analysis")

# load data
df = pd.read_csv("startup_funding.csv")

# clean
df.columns = df.columns.str.strip()
df['AmountInUSD'] = df['AmountInUSD'].replace(',', '', regex=True)
df['AmountInUSD'] = pd.to_numeric(df['AmountInUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Year'] = df['Date'].dt.year
df = df.dropna(subset=['AmountInUSD', 'IndustryVertical'])

# show data
st.subheader("Dataset Preview")
st.dataframe(df.head())

# top sectors
st.subheader("Top Funded Sectors")
top_sectors = df.groupby('IndustryVertical')['AmountInUSD'].sum().sort_values(ascending=False).head(10)

fig1, ax1 = plt.subplots()
sns.barplot(x=top_sectors.values, y=top_sectors.index, ax=ax1)
st.pyplot(fig1)

# investor trends
st.subheader("Top Investors")
top_investors = df['InvestorsName'].value_counts().head(10)

fig2, ax2 = plt.subplots()
sns.barplot(x=top_investors.values, y=top_investors.index, ax=ax2)
st.pyplot(fig2)

# yearly growth
st.subheader("Year-wise Funding Growth")
yearly = df.groupby('Year')['AmountInUSD'].sum()

fig3, ax3 = plt.subplots()
yearly.plot(kind='line', marker='o', ax=ax3)
st.pyplot(fig3)