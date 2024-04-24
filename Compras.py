import pandas as pd
import streamlit as st

#Define o Layout da Pagina para WideScreen
st.set_page_config(layout='wide')

try:
    #Realiza o upload do arquivo e realiza os devidos tratamentos
    arquivo = st.file_uploader('Faça o Upload do Arquivo de Sugestão de Compra')
    df = pd.read_excel(arquivo)

    # Faz a leitura do arquivo que contem Origem e Pack
    intelbras = st.file_uploader('Faça o Upload do Arquivo de Pack')
    pack = pd.read_excel(intelbras)
    
    df = df.drop(index=[0,1,2])
    df = df.rename(columns={
        'Período da Consulta 90 dias':'Codigo',
        'Unnamed: 1':'Produto',
        'Unnamed: 2':'Marca',
        'Unnamed: 3':'Curva',
        'Unnamed: 4':'Em Estoque',
        'Unnamed: 5':'excluir0',
        'Unnamed: 6':'Vendas',
        'Unnamed: 7':'Remessa',
        'Unnamed: 8':'excluir1',
        'Unnamed: 9':'Vendas+Remessa',
        'Unnamed: 10':'excluir2',
        'Unnamed: 11':'Media Mensal',
        'Unnamed: 12':'excluir3',
        'Unnamed: 13':'Cobertura em Dias',
        'Unnamed: 14':'excluir4',
        'Unnamed: 15':'Status',
        'Unnamed: 16':'excluir5',
        'Unnamed: 17':'Sugestao 40 dias',
        'Unnamed: 18':'excluir6',
        'Unnamed: 19':'Comprado',
        'Unnamed: 20':'Compras Programadas',
    })

    # Excluir as colunas em branco
    df = df.drop(columns=['excluir0', 'excluir1','excluir2','excluir3','excluir4','excluir5','excluir6' ])

    # Define o tipo de variavel em cada coluna
    df['Sugestao 40 dias'] = df['Sugestao 40 dias'].astype(float)
    df['Comprado'] = df['Comprado'].astype(float)
    df['Compras Programadas'] = df['Compras Programadas'].astype(float)

    # Substitui todos os valores faltantes para o numero 0
    df['Comprado'] = df['Comprado'].fillna(0)
    df['Compras Programadas'] = df['Compras Programadas'].fillna(0)

    # Cria a Coluna com o devido calculo de compras
    df['Comprar'] = (df['Sugestao 40 dias'] - df['Comprado'])

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
    df = df[df['Comprar'] > 0]
    st.write('Planilha de Compras')
    st.dataframe(df , use_container_width=True)

    a = len(df)
    st.write('Produtos para comprar: ',str(a))
except:
    st.write('Por favor faça o upload do arquivo em excel com extensão xlsx, obrigado')
