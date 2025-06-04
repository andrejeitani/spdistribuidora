import pandas as pd
import streamlit as st

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

    # Excluir as colunas em branco e retira a marcas em desuso.
    df = df.drop(columns=['Excluir 1','Excluir 2','Excluir 3','Excluir 4','Excluir 5'])
    df = df[df['Marca'] != 'INTELBRAS FL'] # FORA DE LINHA
    df = df[df['Marca'] != 'INTELBRAS PRJ'] # PROJETOS
    df = df[df['Marca'] != 'INTELBRAS SDP'] # DISPLAY PROFISSIONAL
    df = df[df['Marca'] != 'INTELBRAS SDRON'] # DRONES
    df = df[df['Marca'] != 'INTELBRAS SOFT'] # SOFTWARE
    df = df[df['Marca'] != 'CONTROL ID']
    df = df[df['Marca'] != 'GAREN/FL']
    df = df[df['Marca'] != 'LINEAR']
    df = df[df['Codigo'] != '4560026'] # VHD 1220 D G7
    df = df[df['Codigo'] != '4560027'] # VHD 3220 D G7
    df = df[df['Codigo'] != '4560028'] # VHD 1220 D BLACK G2
    df = df[df['Codigo'] != '4560040'] # VHD 1230 B G7
    df = df[df['Codigo'] != '4560045'] # VHD 1220 B FULL COLOR G7  
    df = df[df['Codigo'] != '4560046'] # VHD 1220 D FULL COLOR G7
    df = df[df['Codigo'] != '4565298'] # VHL 1120 D
    df = df[df['Codigo'] != '4565299'] # VHL 1120 B
    df = df[df['Codigo'] != '4565329'] # VHC 1120 D
    df = df[df['Codigo'] != '4565330'] # VHC 1120 B
    df = df[df['Codigo'] != '4543509'] # AMT 1016 NET
    df = df[df['Codigo'] != '4543516'] # AMT 8000
    df = df[df['Codigo'] != '4581155'] # MHDX 1108-C C/ SSD
    df = df[df['Codigo'] != '4581156'] # MHDX 1104-C C/ SSD
    df = df[df['Codigo'] != '4780051'] # ONU 110 B
    df = df[df['Codigo'] != '4320007'] # IMPACTA 220
    df = df[df['Codigo'] != '4351000'] # CONECTA MAIS
    df = df[df['Codigo'] != '4680256'] # SS 5531 MF W 
    df = df[df['Codigo'] != '4680261'] # SS 5532 MF W
    df = df[df['Codigo'] != '4680257'] # SS 5541 MF W
    df = df[df['Codigo'] != '4680260'] # SS 5542 MF W
    df = df[df['Codigo'] != '4680052'] # SS 1530 MF W
    df = df[df['Codigo'] != '4680058'] # SS 1540 MF W
    df = df[df['Codigo'] != '4390176'] # AMT 2018 EG
    df = df[df['Codigo'] != '4390179'] # AMT 2018 E
    df = df[df['Codigo'] != '4400338'] # LICENÇA RAMAL UNNITI
    df = df[df['Codigo'] != '4679011'] # FX 2000 PRETA
    df = df[df['Codigo'] != '4679015'] # FX 2000 INOX
    df = df[df['Codigo'] != '4679010'] # FX 2000 CINZA
    df = df[df['Codigo'] != '4679021'] # FX 2000 AJUSTAVEL
    df = df[df['Codigo'] != '4760089'] # S1010F-P
    df = df[df['Codigo'] != '4750103'] # APC 5A-20
    df = df[df['Codigo'] != '4750146'] # AP 3000 AX
    df = df[df['Codigo'] != '4564045'] # VIP 5500 FISH EYE
    df = df[df['Codigo'] != '4681027'] # LE 170
    df = df[df['Codigo'] != '4580787'] # NVD 1416 # SUBSTITUIDO PELO 1516
    df = df[df['Codigo'] != '4842905'] # MODULO FOTOVOLTAICO EMS 170
    df = df[df['Codigo'] != '4830135'] # CABO DE REDE CAT5
    df = df[df['Codigo'] != '4830134'] # CABO DE REDE CAT5
    df = df[df['Codigo'] != '4830007'] # CABO DE REDE CAT6
    df = df[df['Codigo'] != '4830030'] # CABO DE REDE CAT5
    df = df[df['Codigo'] != '4830050'] # CABO MULTICAMERAS
    df = df[df['Codigo'] != '4830051'] # CABO MULTICAMERAS
    df = df[df['Codigo'] != '4830052'] # CABO MULTICAMERAS
    df = df[df['Codigo'] != '4080085'] # TC 50 PREMIUM
    df = df[df['Codigo'] != '4080085'] # TC 50 PREMIUM
    df = df[df['Codigo'] != '4140034'] # RECEPTOR RDS 830
    df = df[df['Codigo'] != '4141007'] # ANTENA DIGITAL AI 2031  
  
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
        st.title('Planilha de Compras')
        st.dataframe(filtered_df , use_container_width=True , hide_index=True)

        a = len(filtered_df['Produto'])
        b = filtered_df['Total'].sum().round(2) 
        st.write('Produtos para comprar: ',str(a) ,
            ' - ' ,
            f'Total de intelbras a comprar: R$ {b:,}'
                )
    filtro() 
    
    st.divider()

    # Define os dataframes por agregação
    origem = df.groupby('Origem').sum('Total')
    origem['%'] = ((origem['Total'] / origem['Total'].sum()) * 100).round(2)
    origem = origem.sort_values('%' , ascending=False)
    origem = origem.drop(columns=['Comprado','Programado','Sugestao 40 Dias','PV','Qtd. Multipla','Comprar'])
    origem = origem.reset_index()
    marca = df.groupby('Marca').sum('Total')
    marca['%'] = ((marca['Total'] / marca['Total'].sum()) * 100).round(2)
    marca = marca.sort_values('%' , ascending=False)
    marca = marca.drop(columns=['Comprado','Programado','Sugestao 40 Dias','PV','Qtd. Multipla','Comprar'])
    marca = marca.reset_index()
    curva = df.groupby('Curva').sum('Total')
    curva['%'] = ((curva['Total'] / curva['Total'].sum()) * 100).round(2)
    curva = curva.sort_values('%' , ascending=False)
    curva = curva.drop(columns=['Comprado','Programado','Sugestao 40 Dias','PV','Qtd. Multipla','Comprar'])
    curva = curva.reset_index()
    
    # Imprimi os dataframes por agregação
    st.subheader('Agrupado por Origem/Fabrica')
    st.dataframe(origem , use_container_width=True , hide_index=True)
    st.subheader('Agrupado por Curva')
    st.dataframe(curva , use_container_width=True , hide_index=True)
    st.subheader('Agrupado por Marca')
    st.dataframe(marca , use_container_width=True , hide_index=True)

except:
    st.write('SP Distribuidora')
