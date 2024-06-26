import streamlit as st
import pandas as pd

#Define o layout da pagina como expandido
st.set_page_config(layout='wide', 
                   page_title='SP Distribuidora - Orçamentos')

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

    #Define os Input's de entrada 
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
    def main():
        col_cliente , col_produto = st.columns(2)
        with col_cliente:
            filtro_cliente = st.text_input('Digite o Nome do Cliente:')
        with col_produto:
            filtro_produto = st.text_input('Digite o Nome do Produto:')
        df_filtro = df[df['Cliente'].str.contains(filtro_cliente, case=False) & df['Produto'].str.contains(filtro_produto, case=False)]
        st.dataframe(df_filtro, use_container_width=True)

        total_real = df_filtro['Valor Total'].sum()
        total_qtd = df_filtro['Quantidade'].sum()

    st.dataframe(df , use_container_width=True)
    
    #Conta a quantidade de clientes atendidos
    clientes = df['Cliente'].unique() 

    #Define variaveis
    total_real = df['Valor Total'].sum()
    total_qtd = df['Quantidade'].sum()

    #Informe de Quantitativos
    st.write(f'Total Orçado R$ {total_real.round(2)}')
    st.write("Clientes atendidos:",str(len(clientes)))
    st.divider()

    #Define colunas de filtro
    col3 , col4 = st.columns(2)
    with col3:
        st.write('Agrupado por Marca')
        df2 = df.groupby(df['Marca']).sum('Valor Total').sort_values(by='Valor Total', ascending=False)
        st.dataframe(df2 , use_container_width=True)
    with col4:
        st.write('Agrupado por Produto')
        df3 = df.groupby(df['Produto']).sum('Valor Total').sort_values(by='Valor Total', ascending=False)
        st.dataframe(df3 , use_container_width=True)
    st.divider()

    # Dados agrupados por cliente
    st.write('Agrupado por Cliente')
    df3 = df.groupby('Cliente').sum('Valor Total').sort_values(by='Valor Total', ascending=False)
    st.dataframe(df3 , use_container_width=True)
    st.divider()

    # Grafico de Quantitativo de Marcas
    st.write('Demanda por Marcas')
    chart_marcas = df2.sort_values(by='Valor Total', ascending=False)
    st.bar_chart(data=chart_marcas , y='Valor Total' , use_container_width=True , color='#368900')
    st.divider()

    col5 , col6 = st.columns(2)
    with col5:
        # Grafico de Orçamentos por Vendedor
        df4 = df.groupby(df['Vendedor']).sum('Valor Total').sort_values(by='Valor Total', ascending=False)
        st.write('Total de Orçamentos por Vendedor')
        chart_vendedores = df4.sort_values(by='Valor Total', ascending=False)
        st.bar_chart(data=chart_vendedores , y='Valor Total' , use_container_width=True , color='#368900')
    with col6:
        #Grafico de Taxa de Conversão
        st.write('Gráfico de Conversão')
        tx_conversao = df.groupby(df['Status']).sum('Valor Total')
        chart_conversao = tx_conversao.sort_values(by='Valor Total', ascending=False)
        st.bar_chart(data=chart_conversao , y='Valor Total' , use_container_width=True , color='#368900')  
        
        # calculo de taxa de conversão
        pendente = tx_conversao['Valor Total'].reset_index()
        Filtro_fechados = pendente['Status'] == 'Fechado'
        Filtro_pendentes = pendente['Status'] == 'Pendente'
        Fe = pendente.loc[Filtro_fechados, 'Valor Total'].sum()
        Pe = pendente.loc[Filtro_pendentes, 'Valor Total'].sum()
        taxa = ((Fe / (Fe + Pe))*100).round(2)
        st.write(f'Taxa de conversão de: {taxa} %')
    st.divider()

    # Vendas Por semana
    st.write('Orçamentos por dia da semana')
    df['Data'] = pd.to_datetime(df['Data']).dt.dayofweek
    df['Data'] = df['Data'].replace({0:'Segunda' , 1:'Terça' , 2:'Quarta' , 3:'Quinta' , 4:'Sexta' , 5:'Sabado' , 6:'Domingo'})
    vendas_semanal = df.groupby(df['Data']).sum('Valor Total')
    vendas_semanal = vendas_semanal.sort_values(by=['Valor Total'], ascending=True)
    st.bar_chart(vendas_semanal , y='Valor Total' , use_container_width=True , color='#368900')
    st.divider()
except:
    st.write('SP Distribuidora')
