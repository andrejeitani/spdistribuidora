import pandas as pd
import streamlit as st
import plotly.express as px

#Define o Layout da Pagina para WideScreen
st.set_page_config(layout='wide', 
                   page_title='SP Distribuidora - Compras')

try:
    #Realiza o upload do arquivo e realiza os devidos tratamentos
    arquivo = st.file_uploader('Faça o Upload do Arquivo Ponto de Compra')
    df = pd.read_excel(arquivo, engine='openpyxl')
    pack = st.file_uploader('Faça o Upload da tabela da Intelbras')
    pack = pd.read_excel(pack)
    df = df.drop(index=[0,1])
    df = df.rename(columns={
        'Período da Consulta 90 dias':'Codigo',
        'Unnamed: 1':'Produto',
        'Unnamed: 2':'Marca',
        'Unnamed: 3':'Curva',
        'Unnamed: 4':'Vendas',
        'Unnamed: 5':'Excluir 1',
        'Unnamed: 6':'Remessa',
        'Unnamed: 7':'Vendas&Remessas',
        'Unnamed: 8':'Excluir 2',
        'Unnamed: 9':'Media Mensal',
        'Unnamed: 10':'Estoque',
        'Unnamed: 11':'Cobertura em Dias',
        'Unnamed: 12':'Excluir 3',
        'Unnamed: 13':'Comprado',
        'Unnamed: 14':'Excluir 4',
        'Unnamed: 15':'Programado',
        'Unnamed: 16':'Status',
        'Unnamed: 17':'Sugestao 40 Dias',
        'Unnamed: 18':'Excluir 5',
        'Unnamed: 19':'Pack',
    })

    # Excluir as colunas em branco e retira a marca Intelbras FL e PRJ
    df = df.drop(columns=['Excluir 1','Excluir 2','Excluir 3','Excluir 4','Excluir 5'])
    df = df[df['Marca'] != 'INTELBRAS FL'] 
    df = df[df['Marca'] != 'INTELBRAS PRJ']

    # Define o tipo de variavel em cada coluna
    df['Sugestao 40 Dias'] = df['Sugestao 40 Dias'].astype(float)
    df['Comprado'] = df['Comprado'].astype(float)
    df['Programado'] = df['Programado'].astype(float)

    # Substitui todos os valores faltantes para o numero 0
    df['Vendas'] = df['Vendas'].fillna(0)
    df['Remessa'] = df['Remessa'].fillna(0)
    df['Vendas&Remessas'] = df['Vendas&Remessas'].fillna(0)
    df['Comprado'] = df['Comprado'].fillna(0)
    df['Programado'] = df['Programado'].fillna(0)

    # Classica as colunas pela sua ordem alfabetica
    df = df.sort_values(by='Marca' , ascending=True)

    # Define o tipo de variavel da coluna, para que a chave seja do mesmo tipo em ambos os dataframes
    pack['Codigo'] = pack['Codigo'].astype(str)

    # Exclui todos os valores faltantes do arquivo que contem o Pack e a Origem
    pack = pack.dropna()

    # Realiza a junção entre os 2 dataframes e Exclui os codigos em duplicidade
    df = df.merge(pack , left_on='Codigo' , right_on='Codigo' , how='outer')
    df = df.drop_duplicates() 

    # Realiza o filtro do arquivo , para produtos com definição de compra maior que 1
    df = df[df['Sugestao 40 Dias'] > 0]

    # Cria a Coluna comprar, ja com o ajuste da multiplicidade dos pack's
    df['Comprar'] = ((df['Sugestao 40 Dias'] / df['Qtd. Multipla']).round(0) * df['Qtd. Multipla'])

    # Define a coluna Total, sendo a quantidade ajustada do COMPRAR multiplicando o PV
    df['Total'] = (df['PV'] * df['Comprar']).round(2)

    # Função de filtro 
    def filtro():
    # Campo de texto para inserir o critério de filtro
        filtro = st.text_input('Digite uma marca para filtrar:')

        # Aplicar o filtro e mostrar o resultado
        global filtered_df
        filtered_df = df[df['Marca'].str.contains(filtro, case=False)]
        st.write('Planilha de Compras')
        st.dataframe(filtered_df , use_container_width=True , hide_index=True)

        a = len(filtered_df['Produto'])
        b = filtered_df['Total'].sum().round(2) 
        st.write('Produtos para comprar: ',str(a) ,
            ' - ' ,
            f'Total de intelbras a comprar: R$ {b:,}'
                )
    filtro() 

    # Define os dataframes por agregação
    origem = df.groupby('Origem').sum('Total')
    origem['%'] = ((origem['Total'] / origem['Total'].sum()) * 100).round(2)
    origem = origem.sort_values('%' , ascending=False)
    origem = origem.reset_index()
    marca = df.groupby('Marca').sum('Total')
    marca['%'] = ((marca['Total'] / marca['Total'].sum()) * 100).round(2)
    marca = marca.sort_values('%' , ascending=False)
    marca = marca.reset_index()
    curva = df.groupby('Curva').sum('Total')
    curva['%'] = ((curva['Total'] / curva['Total'].sum()) * 100).round(2)
    curva = curva.sort_values('%' , ascending=False)
    curva = curva.reset_index()
    
    # Imprimi os dataframes por agregação
    st.write('Agrupado por Origem/Fabrica')
    st.dataframe(origem , use_container_width=True , hide_index=True)
    st.write('Agrupado por Curva')
    st.dataframe(curva , use_container_width=True , hide_index=True)
    st.write('Agrupado por Marca')
    st.dataframe(marca , use_container_width=True , hide_index=True)

except:
    st.write('SP Distribuidora')
