import streamlit as st
import pandas as pd

#Define o Layout da Pagina para WideScreen
st.set_page_config(layout='wide', 
                   page_title='SP Distribuidora - ROTHEVA')

arquivo = st.file_uploader('Faça o Upload do Arquivo ROTHEVA')
try:
    df = pd.read_excel(arquivo, engine='openpyxl')

    df = df.drop(columns={'Código de Barras','Situação tributária de ICMS - Entrada',
                        'Cd. Grupo Produto','Código da Situação Tributária do ICMS - Entrada',
                        'Grupo de Produto','Situação tributária de COFINS - Saída',
                        'Unid.Venda','Código de Situação Tributária da COFINS - Saída',
                        'Unid. Compra','Situação tributária de PIS - Saída',
                        'Aceita Desconto Padrão','Valor Custo','Código da Situação Tributária do IPI - Entrada',
                        'Qtd. Item','% Desvio Inferior - Diretor','Situação tributária de IPI - Entrada',
                        'Qtd. Volumes','% Desvio Superior - Diretor','Descrição de Compra',
                        'Unidade Volume','% Desvio Inferior - Supervisor/Gerente',
                        'Peso Líquido','% Desvio Superior - Supervisor/Gerente',
                        'Período','% Desvio Inferior - Representante/Vendedor',
                        'dias vencidos','% Desvio Superior - Representante/Vendedor',
                        'Setor','Alq. ICMS','Alq. ICMS de compra','Estoque Máximo',
                        'Estante','Alq. Importação','Estoque Mínimo',
                        'Nível','Código da Situação Tributária do PIS - Saída',
                        'Box','Situação tributária de IPI - Saída',
                        'Origem','Código da Situação Tributária do IPI - Saída',
                        'Valor de Mercado', 'Situação tributária de ICMS - Saída',
                        'Cd.Empresa', 'Código da Situação Tributária do ICMS - Saída',
                        'Cd.Filial','Origem da Mercadoria','Consumo Médio',
                        'Descrição para Faturamento','St. Vendas','Código NCM',
                        'Peso bruto','Vl. Índice Custo Standard','Situação tributária de COFINS - Entrada',
                        'Unidade de Peso','Índice Custo Standard','CEST',
                        'Data Cadastro','Vl.Custo Standard','Unidade de Consumo',
                        'Data Desativado','Vl. Indexado Custo','Dt.Última Compra',
                        'St. Demais operações','Vl. Índice Custo','NBM/Classif.Fiscal',
                        'St. Compras','Índice Custo','Dt.Última Venda','Razão Social do Fornecedor',
                        'Dt. Ult. Inventário','IPI Venda','IPI Compra','Código de Situação Tributária da COFINS - Entrada',
                        'Dados Técnicos','Descrição NCM','Descrição CEST',
                        'Custo Médio (Reais)','Fornecedor Preferencial','Situação tributária de PIS - Entrada',
                        'Vl. Indexado Custo Standard','Código da Situação Tributária do PIS - Entrada'
                        })
    df = df.drop(index=0)
    df['Qtde em Estoque'] = (df['Qtde em Estoque'] / 2).round(0)
    df = df.dropna()
    df = df[df['Marca'].str.contains('INTELBRAS', case=False)]
    df = df[df['Qtde em Estoque'] != 0]
    st.dataframe(df , hide_index=True ,use_container_width=True)
except:
    st.text('SP Distribuidora - Envie o Arquivo  Rotheva para receber 50% do Estoque intelbras')
