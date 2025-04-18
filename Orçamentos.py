import streamlit as st
import pandas as pd
import plotly.express as px

#Define o layout da pagina como expandido
st.set_page_config(layout='wide', 
                   page_title='SP Distribuidora - Orçamentos' )

try:
    #Faz a leitura do arquivo e carrega na memoria
    file_uploader = st.file_uploader('Faça upload do arquivo XLSX')
    df = pd.read_excel(file_uploader)


    #Seleciona as colunas desejadas e altera os seus nomes
    df = df[['Razão','Data do Orçamento','Situação','Apelido Vendedor','Descrição do Produto','Marca','Quantidade','Valor Total']]
    df = df.rename(columns={'Razão':'Cliente',
                            'Data do Orçamento':'Data',
                            'Situação':'Status',
                            'Apelido Vendedor':'Vendedor',
                            'Descrição do Produto':'Produto',
                            'Marca':'Marca',
                            'Quantidade':'Quantidade',
                            'Valor Total':'Valor Total'})


    #Converte o tipo de campo para o padrão Data Ano_Mes_dia 
    df['Data'] = pd.to_datetime(df['Data']).dt.date

    #Exclui as linhas em branco
    df = df.dropna()

    #Cria Lista de Vendedores
    vendedores = df['Vendedor'].unique()

    #Segmenta em Pendente e Fechado
    status_ = df['Status'].unique()

    #Define os Filtros de entrada (Data , Vendedor e Status)
    col1 , col2 , col3 = st.columns(3)

    with col1:
        Data_Inicial , Data_Final = st.date_input('Data Inicial') , st.date_input('Data Final')
    with col2:    
        vendedor = st.multiselect('Vendedor' , vendedores , default=vendedores )
    with col3:
        status = st.multiselect('Status Do Pedido' , status_, default=status_)
    st.divider()

    #Trata o Dataframe com os input's selecionados
    df = df[
        (df['Data'] >= Data_Inicial) & 
        (df['Data'] <= Data_Final) & 
        (df['Vendedor'].isin(vendedor)) & 
        (df['Status'].isin(status)) #&
        ]
    
    # Define a Função de filtro do dataframe por cliente e produto
    def filtro_produto_cliente():
        col_cliente , col_produto = st.columns(2)
        with col_cliente:
            filtro_cliente = st.text_input('Digite o Nome do Cliente:')
        with col_produto:
            filtro_produto = st.text_input('Digite o Nome do Produto:')
        global df_filtro , total_real
        df_filtro = df[df['Cliente'].str.contains(filtro_cliente, case=False) & df['Produto'].str.contains(filtro_produto, case=False)]
        st.dataframe(df_filtro, use_container_width=True , hide_index=True)
        total_real = df_filtro['Valor Total'].sum()
    filtro_produto_cliente()
    
    #Conta a quantidade de clientes atendidos
    clientes = df_filtro['Cliente'].unique() 

    #Informe de Quantitativos
    st.write(f'Total Orçado R$ {total_real.round(2):,}')
    st.write("Clientes atendidos:",str(len(clientes)))
    st.divider()

    #Imprimi os grid's Agrupados por Marca e Agrupados por Produto
    col3 , col4 = st.columns(2)
    with col3:
        st.write('Agrupado por Marca')
        df2 = df_filtro.groupby('Marca').sum('Valor Total').sort_values(by='Valor Total', ascending=False)
        df2['%'] = (( df2['Valor Total'] / df2['Valor Total'].sum() ) * 100 ).round(2)
        df2 = df2.reset_index()
        st.dataframe(df2 , use_container_width=True , hide_index=True)
    with col4:
        st.write('Agrupado por Produto')
        df3 = df_filtro.groupby('Produto').sum('Valor Total').sort_values(by='Valor Total', ascending=False)
        df3['%'] = ( df3['Valor Total'] / df3['Valor Total'].sum() *100 ).round(2)
        df3 = df3.reset_index()
        st.dataframe(df3 , use_container_width=True , hide_index=True)
    st.divider()

    # Imprimi o grid com dados agrupados por cliente
    st.write('Agrupado por Cliente')
    df3 = df_filtro.groupby('Cliente').sum('Valor Total').sort_values(by='Valor Total', ascending=False)
    df3['%'] = ((df3['Valor Total'] / df3['Valor Total'].sum()) * 100 ).round(2)  
    df3 = df3.reset_index()
    st.dataframe(df3 , use_container_width=True , hide_index=True)
    st.divider()

    # Grafico de Quantitativo de Marcas
    def grafico_marca(tabela):
        tabela = tabela.groupby(['Marca','Status']).sum('Valor Total')
        tabela = tabela.reset_index()
        tabela = tabela.sort_values('Valor Total' , ascending=False)
        fig = px.histogram(tabela , x = 'Marca' , y = 'Valor Total' , color = 'Status' , title='Demanda Por Marcas')
        st.plotly_chart(fig)
    grafico_marca(df_filtro)
    st.divider()

    # Grafico de orçamentos por Vendedor
    col5 , col6 = st.columns(2)
    with col5:
        def grafico_vendedor(tabela):
            tabela = tabela.groupby(['Vendedor' , 'Status']).sum('Valor Total')
            tabela = tabela.sort_values('Valor Total' , ascending=False)
            tabela = tabela.reset_index()
            fig = px.histogram(tabela , x = 'Vendedor' , y = 'Valor Total' , color = 'Status' , title='Orçamentos Por Vendedor')
            st.plotly_chart(fig)
        grafico_vendedor(df_filtro)
    with col6:
    # Grafico de orçamentos por Situação Fechado / Pendente    
        tx_conversao = df_filtro.groupby(df['Status']).sum('Valor Total')
        def grafico_conversao(tabela):
            tabela = tabela.groupby(['Status']).sum('Valor Total')
            tabela = tabela.reset_index()
            tabela = tabela.sort_values('Valor Total' , ascending=False)
            fig = px.histogram(tabela , x = 'Status' , y = 'Valor Total' , color = 'Status' , title='Taxa de Conversão' , text_auto='.2f')
            st.plotly_chart(fig)
        grafico_conversao(df_filtro)  
        
        # calculo de taxa de conversão
        pendente = tx_conversao['Valor Total'].reset_index()
        Filtro_fechados = pendente['Status'] == 'Fechado'
        Filtro_pendentes = pendente['Status'] == 'Pendente'
        Fe = pendente.loc[Filtro_fechados, 'Valor Total'].sum()
        Pe = pendente.loc[Filtro_pendentes, 'Valor Total'].sum()
        taxa = ((Fe / (Fe + Pe))*100).round(2)
        st.write(f'Taxa de conversão de: {taxa} %')
    st.divider()

    # Grafico de orçamentos por dia do mês
    def grafico_data(tabela):
        tabela = tabela.groupby(['Data','Status']).sum('Valor Total')
        tabela = tabela.reset_index()
        fig = px.bar(tabela , x = 'Data' , y = 'Valor Total' , color = 'Status' , title='Orçamentos por dia')
        st.plotly_chart(fig)
    grafico_data(df_filtro)
    st.divider()

except:
    st.write('SP Distribuidora')
