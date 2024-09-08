import streamlit as st
from datetime import datetime
import yfinance as yf
import plotly.graph_objects as go


symbol = st.sidebar.text_input('Hisse Senedi Sembolü', value='ASELS')

st.title(symbol + ' Hisse Senedi Grafiği')

start_date = st.sidebar.date_input('Başlangıç Tarihi', value=datetime(2020, 1, 1))
end_date = st.sidebar.date_input('Bitiş Tarihi', value=datetime.now())


df = yf.download(symbol + '.IS', start=start_date, end=end_date)


df = df.rename(columns={
    'Open': 'Açılış',
    'High': 'Yüksek',
    'Low': 'Düşük',
    'Close': 'Kapanış',
    'Adj Close': 'Düzeltilmiş Kapanış',
    'Volume': 'Hacim'
})


fig = go.Figure()


fig.add_trace(go.Scatter(x=df.index, y=df['Kapanış'], mode='lines', name='Kapanış'))


fig.update_layout(
    xaxis_title='Tarih',
    yaxis_title='Kapanış Fiyatı (TL)',
    template='plotly_dark'
)


st.plotly_chart(fig)


st.subheader(symbol + ' Hisse Senedi Verileri')
st.write(df.style.format({
    'Açılış': '{:,.2f} TL',
    'Yüksek': '{:,.2f} TL',
    'Düşük': '{:,.2f} TL',
    'Kapanış': '{:,.2f} TL',
    'Düzeltilmiş Kapanış': '{:,.2f} TL',
    'Hacim': '{:,}'
}))
