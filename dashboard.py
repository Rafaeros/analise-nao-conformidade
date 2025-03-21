"""
Streamlit DashBoard of Nonconformities
"""

from typing import Tuple
from datetime import datetime as dt
from datetime import timedelta as td

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

today = dt.today()
pd.set_option('future.no_silent_downcasting', True)

def generate_graphics(
    df_nc: pd.DataFrame, init_date: str, final_date: str
) -> Tuple[go.Figure, go.Figure, go.Figure]:
    """
    Generate two graphics from a dataframe of nonconformities (df_nc)
    Parameters
    ----------
    df_nc : pd.DataFrame
        Dataframe of nonconformities
    init_date : str
        Initial date of the period
    final_date : str
        Final date of the period

    Returns
    -------
    Tuple[go.Figure, go.Figure]
        Two graphics, the first one is a bar chart of the nonconformities by type, and the
        second one is a bar chart of the nonconformities by client
    """

    all_nc = df_nc.groupby(by="NÃO CONFORMIDADE", as_index=False)[
        "QTD NÃO CONFORME"
    ].sum()
    all_nc_count = all_nc["QTD NÃO CONFORME"].sum()
    all_nc = all_nc.sort_values(by="QTD NÃO CONFORME", ascending=False)
    all_nc = all_nc.loc[all_nc["QTD NÃO CONFORME"] > 10]
    f1 = px.bar(
        all_nc,
        x="NÃO CONFORMIDADE",
        y="QTD NÃO CONFORME",
        title=f"RELATÓRIO DE NÃO CONFORMIDADES {init_date} ATE {final_date}",
        labels={"count": "QUANTIDADE NÃO CONFORME"},
        color="NÃO CONFORMIDADE",
        text_auto=True
    )
    f1.add_annotation(
        x=3,
        y=all_nc_count + 5,
        text=f"TOTAL DE NÃO CONFORMIDADES:{all_nc_count:.0f}",
        showarrow=False,
        font=dict(size=14, color="red"),
        align="center"
    )
    f1.update_layout(
        width=1000,
        height=600,
    )

    all_nc_by_client = df_nc.groupby(by="CLIENTE", as_index=False)[
        "QTD NÃO CONFORME"
    ].sum()
    all_nc_by_client = all_nc_by_client.sort_values(
        by="QTD NÃO CONFORME", ascending=False
    )

    f2 = px.bar(
        all_nc_by_client,
        x="CLIENTE",
        y="QTD NÃO CONFORME",
        title=f"RELATÓRIO DE NÃO CONFORMIDADES POR CLIENTE {init_date} ATE {final_date}",
        labels={"count": "QUANTIDADE NÃO CONFORME", "CLIENTE": "CLIENTES"},
        color="CLIENTE",
        text_auto=True
    )
    f2.update_layout(width=1000, height=600)

    all_nc_by_sector = df_nc.groupby(by="OPERAÇÃO", as_index=False)["QTD NÃO CONFORME"].sum()
    all_nc_by_sector = all_nc_by_sector.sort_values(
        by="QTD NÃO CONFORME", ascending=False
    )

    f3 = px.bar(
        all_nc_by_sector,
        x="OPERAÇÃO",
        y="QTD NÃO CONFORME",
        title=f"RELATÓRIO DE NÃO CONFORMIDADES POR LINHA DE PRODUÇÃO {init_date} ATE {final_date}",
        labels={"count": "QUANTIDADE NÃO CONFORME", "OPERAÇÃO": "LINHA DE PRODUÇÃO"},
        color="OPERAÇÃO",
        text_auto=True
    )
    f3.update_layout(width=1000, height=600)

    return f1, f2, f3


st.title("ANALISE DE NÃO CONFORMIDADES")
file = st.file_uploader("ADICIONE O ARQUIVO EXCEL:", accept_multiple_files=False)
st.write("DATA DO RELATORIO")
days_before = today - td(days=30)
start_date = st.date_input("DE:", value=days_before.date())
end_date = st.date_input("ATÉ:", value=today)
generate_graphics_bt = st.button("Gerar Gráficos")

if file:
    df = pd.read_excel(file)
    df["DATA NÃO CONFORMIDADE"] = pd.to_datetime(
        df["DATA NÃO CONFORMIDADE"], errors="coerce"
    )
    df = df.iloc[:, 0:10]
    operation_map = {
        "AMPOLA": 3,
        "PROTOTIPO": 4,
        "UPC": 5,
    }
    df["OPERAÇÃO"] = df["OPERAÇÃO"].replace(operation_map)
    df = df.dropna()

if generate_graphics_bt:
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    date_filter = (df["DATA NÃO CONFORMIDADE"] >= start_date) & (
        df["DATA NÃO CONFORMIDADE"] <= end_date
    )
    df = df.loc[date_filter]

    nc, nc2, nc3 = generate_graphics(
        df, start_date.strftime("%d/%m/%Y"), end_date.strftime("%d/%m/%Y")
    )
    st.plotly_chart(nc)
    st.plotly_chart(nc2)
    st.plotly_chart(nc3)
