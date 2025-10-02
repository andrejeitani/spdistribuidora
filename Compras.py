import pandas as pd
import streamlit as st
import numpy as np

#Define o Layout da Pagina para WideScreen
st.set_page_config(layout='wide', 
                   page_title='SP Distribuidora - Compras')

try:
    #Realiza o upload do arquivo e realiza os devidos tratamentos
    arquivo = st.file_uploader('Faça o Upload do Arquivo Ponto de Compra')
    df = pd.read_excel(arquivo, engine='openpyxl')
    #pack = st.file_uploader('Faça o Upload da tabela da Intelbras')
    pack = pd.read_excel('Pack.xlsx' , engine='openpyxl') # ATUALIZAR SEMPRE A TABELA DA INTELBRAS *****************************
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
    df = df[df['Marca'] != 'INATIVO/FL'] # FORA DE LINHA
    df = df[df['Marca'] != 'INTELBRAS PRJ'] # PROJETOS
    df = df[df['Marca'] != 'INTELBRAS SDP'] # DISPLAY PROFISSIONAL
    df = df[df['Marca'] != 'INTELBRAS SDRON'] # DRONES
    df = df[df['Marca'] != 'INTELBRAS SOFT'] # SOFTWARE
    df = df[df['Marca'] != 'INTELBRAS SOF'] # SOLAR OFF GRID
    df = df[df['Marca'] != 'CONTROL ID']
    df = df[df['Marca'] != 'GAREN/FL']
    df = df[df['Marca'] != 'LINEAR']
    df = df[df['Codigo'] != '4560026'] # VHD 1220 D G7
    df = df[df['Codigo'] != '4560027'] # VHD 3220 D G7
    df = df[df['Codigo'] != '4560028'] # VHD 1220 D BLACK G2
    df = df[df['Codigo'] != '4560039'] # VHD 1230 B BLACK G7
    df = df[df['Codigo'] != '4560040'] # VHD 1230 B G7
    df = df[df['Codigo'] != '4560045'] # VHD 1220 B FULL COLOR G7  
    df = df[df['Codigo'] != '4560046'] # VHD 1220 D FULL COLOR G7
    df = df[df['Codigo'] != '4565298'] # VHL 1120 D
    df = df[df['Codigo'] != '4565299'] # VHL 1120 B
    df = df[df['Codigo'] != '4565321'] # VHL 1220 B G2
    df = df[df['Codigo'] != '4565320'] # VHL 1220 D G2
    df = df[df['Codigo'] != '4565357'] # VHD 1530 B 
    df = df[df['Codigo'] != '4565358'] # VHD 1520 D 
    df = df[df['Codigo'] != '4564068'] # VIP 3230 B SL G3
    df = df[df['Codigo'] != '4564069'] # VIP 3230 D SL G3 
    df = df[df['Codigo'] != '4570001'] # VIP 1220 D FULL COLOR 
    df = df[df['Codigo'] != '4570002'] # VIP 1220 B FULL COLOR 
    df = df[df['Codigo'] != '4570012'] # VIP 3220 B FULL COLOR 
    df = df[df['Codigo'] != '4570013'] # VIP 3220 D FULL COLOR 
    df = df[df['Codigo'] != '4570030'] # VIP 1220 D FULL COLOR+
    df = df[df['Codigo'] != '4570031'] # VIP 1220 B FULL COLOR+
    df = df[df['Codigo'] != '4543509'] # AMT 1016 NET
    df = df[df['Codigo'] != '4543516'] # AMT 8000
    df = df[df['Codigo'] != '4581155'] # MHDX 1108-C C/ SSD
    df = df[df['Codigo'] != '4581156'] # MHDX 1104-C C/ SSD
    df = df[df['Codigo'] != '4680256'] # SS 5531 MF W 
    df = df[df['Codigo'] != '4680261'] # SS 5532 MF W
    df = df[df['Codigo'] != '4680257'] # SS 5541 MF W
    df = df[df['Codigo'] != '4680260'] # SS 5542 MF W
    df = df[df['Codigo'] != '4680052'] # SS 1530 MF W
    df = df[df['Codigo'] != '4680058'] # SS 1540 MF W
    df = df[df['Codigo'] != '4580772'] # MHDX 1116 - HD 4TB
    df = df[df['Codigo'] != '4580773'] # MHDX 1116 - HD 1TB
    df = df[df['Codigo'] != '4581048'] # MHDX 1108 - HD 1TB
    df = df[df['Codigo'] != '4581082'] # MHDX 1304 - HD 1TB
    df = df[df['Codigo'] != '4581093'] # MHDX 1308 - HD 1TB
    df = df[df['Codigo'] != '4581100'] # MHDX 1116 - HD 2TB  
    df = df[df['Codigo'] != '4682073'] # SS 3430 MF
    df = df[df['Codigo'] != '4663150'] # CAP 3000 VAZIA
    df = df[df['Codigo'] != '4390176'] # AMT 2018 EG
    df = df[df['Codigo'] != '4390179'] # AMT 2018 E
    df = df[df['Codigo'] != '4400338'] # LICENÇA RAMAL UNNITI
    df = df[df['Codigo'] != '4679011'] # FX 2000 PRETA
    df = df[df['Codigo'] != '4679015'] # FX 2000 INOX
    df = df[df['Codigo'] != '4679010'] # FX 2000 CINZA
    df = df[df['Codigo'] != '4679000'] # FX 2000 
    df = df[df['Codigo'] != '4679001'] # FX 2000 
    df = df[df['Codigo'] != '4679021'] # FX 2000 AJUSTAVEL
    df = df[df['Codigo'] != '4760089'] # S1010F-P
    df = df[df['Codigo'] != '4564045'] # VIP 5500 FISH EYE
    df = df[df['Codigo'] != '4681027'] # LE 170
    df = df[df['Codigo'] != '4760040'] # SF 900 HI POE
    df = df[df['Codigo'] != '4780039'] # VEX 3004
    df = df[df['Codigo'] != '4780072'] # VEX 3120
    df = df[df['Codigo'] != '4780073'] # VEX 3120
    df = df[df['Codigo'] != '4810040'] # VB 503
    df = df[df['Codigo'] != '4810043'] # VB 1104 WP  
    df = df[df['Codigo'] != '4682070'] # CT 3000 2PB
    df = df[df['Codigo'] != '4580787'] # NVD 1416 # SUBSTITUIDO PELO 1516
    df = df[df['Codigo'] != '4580934'] # NVD 3316 P # SUBSTITUIDO PELO iNVD 3016 P
    df = df[df['Codigo'] != '4830135'] # CABO DE REDE CAT5
    df = df[df['Codigo'] != '4830134'] # CABO DE REDE CAT5
    df = df[df['Codigo'] != '4830007'] # CABO DE REDE CAT6
    df = df[df['Codigo'] != '4830008'] # CABO DE REDE CAT6
    df = df[df['Codigo'] != '4830030'] # CABO DE REDE CAT5
    df = df[df['Codigo'] != '4830050'] # CABO MULTICAMERAS
    df = df[df['Codigo'] != '4830051'] # CABO MULTICAMERAS
    df = df[df['Codigo'] != '4830052'] # CABO MULTICAMERAS
    df = df[df['Codigo'] != '4080085'] # TC 50 PREMIUM
    df = df[df['Codigo'] != '4140034'] # RECEPTOR RDS 830
    df = df[df['Codigo'] != '4141007'] # ANTENA DIGITAL AI 2031  
    df = df[df['Codigo'] != '4631200'] # BLA 1200
    df = df[df['Codigo'] != '4632200'] # BLA 1200
    df = df[df['Codigo'] != '4670007'] # IFR 7000
    df = df[df['Codigo'] != '4670008'] # IFR 7000 +
    df = df[df['Codigo'] != '4671085'] # FS 150 KIT ELITE
    df = df[df['Codigo'] != '4580934'] # NVD 3316 P , substituido pelo iNVD 3016P
    df = df[df['Codigo'] != '4560025'] # VHD 3230 B
    df = df[df['Codigo'] != '4560027'] # VHD 3230 D
    df = df[df['Codigo'] != '4830053'] # CABO COAXIAL CFTV 4mm 67% COBRE
    
    # Substitui o codigo e a descrição dos produtos em pashout, para os seus substitutos diretos
    df = df.replace(to_replace='4565151' , value='4565150')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 5820 D 4K - IR 20M, LENTE 2,8mm, RESOL 2160P, HDCVI, IP66, CASE PLAST, INST INT/EXT, ABERT110',
        value='SUBSTITUIDO - DE VHD 5820 D4K PARA VHD 5830 B 4K'
        ) # DESCRIÇÃO  
    
    df = df.replace(to_replace='4581038' , value='4581252')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR MHDX 1104-C C/HD 1TB - 4 CANAIS (HDCVI/AHD/HDTVI/IP), RES 1080P LITE, GAB COMPACTO, ANAL VIDEO, MODO NVR',
        value='SUBSTITUIDO - DE MHDX 1104-C c/HD 1TB PARA MHDX 1204-C c/HD 1TB'
        ) # DESCRIÇÃO  
       
    df = df.replace(to_replace='4581039' , value='4581250')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR MHDX 1104-C - 4 CANAIS (HDCVI/AHD/HDTVI/IP), RES 1080P LITE, GAB COMPACTO,ANAL VIDEO,MODO NVR, SUP 1HD SATA/SSD',
        value='SUBSTITUIDO - DE MHDX 1104-C PARA MHDX 1204-C'
        ) # DESCRIÇÃO       
    
    df = df.replace(to_replace='4681020' , value='4680303')   # CODIGO
    df = df.replace(
        to_replace='LEITOR DE CARTAO RFID PROX LE 130 MF',
        value='SUBSTITUIDO - DE LE 130 MF PARA LE 1110 MF'
        ) # DESCRIÇÃO  
     
    df = df.replace(to_replace='4681021' , value='4680302')   # CODIGO
    df = df.replace(
        to_replace='LEITOR DE CARTAO RFID PROX LE 130',
        value='SUBSTITUIDO - DE LE 130 PARA LE 1110'
        ) # DESCRIÇÃO   
    
    df = df.replace(to_replace='4710018' , value='4710016')   # CODIGO
    df = df.replace(
        to_replace='ADAPTADOR USB WIRELESS DUAL BAND ACTION A1200',
        value='SUBSTITUIDO - DE A1200 PARA IWA 3001'
        ) # DESCRIÇÃO    

    df = df.replace(to_replace='4682071' , value='4680332')   # CODIGO
    df = df.replace(
        to_replace='CONTROLADOR DE ACESSO CT 3000 4PB - CAP 100 MIL USUARIOS, 3MIL BIOMET, ATE 4 PORTAS',
        value='SUBSTITUIDO - DE CT 3000 4PB PARA CT 5000 4PB'
        ) # DESCRIÇÃO 
  
    df = df.replace(to_replace='4580964' , value='4581206')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR EM REDE NVD 3308 P - 8 CANAIS IP, RESOL 4K, H265/H265+, POE, PADR LGPD, SUP 1 HD SATA',
        value='SUBSTITUIDO - DE NVD 3308 P PARA iNVD 3008 P'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4581051' , value='4580645')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR MHDX 1304 - 4 CANAIS (HDCVI/AHD/HDTVI/ANAL/IP), RES 1080P LITE/1080P, ANAL VIDEO,MODO NVR,SUP 1 HD SATA10TB/SSD',
        value='SUBSTITUIDO - DE MHDX 1304 PARA MHDX 3104-C'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4581092' , value='4580771')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR MHDX 1308 - 8 CANAIS (HDCVI/AHD/HDTVI/ANAL/IP), RES 1080P LITE/1080P, ANAL VIDEO,MODO NVR,SUP 1 HD SATA 10TB/SS',
        value='SUBSTITUIDO - DE MHDX 1308 PARA MHDX 3108-C'
        ) # DESCRIÇÃO 
  
    df = df.replace(to_replace='4581097' , value='4580130')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR MHDX 1316 - 16 CANAIS (HDCVI/AHD/HDTVI/ANAL/IP), RES 1080P LITE/1080P,ANAL VIDEO,MODO NVR,SUP 1 HD SATA10TB/SSD',
        value='SUBSTITUIDO - DE MHDX 1316 PARA MHDX 3116-C'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4560029' , value='4560152')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 3240 D VF G7 - IR 40M, LENTE 2,7 A 12mm, RESOL 1080P/ 800TVL, MULTI HD4X1,IP67/IK10, CASE METAL, INST INT/EXT',
        value='SUBSTITUIDO - DE VHD 3240 D VF G7 PARA VHD 3240 D VF G8'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4560085' , value='4560175')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 1220 D MIC G8 - IR 20M, LENTE 2,8mm, RESOL 1080P, MULTI HD 4X1, CASE PLAST, INST INT, MICROFONE 40M, ABERT108',
        value='SUBSTITUIDO - DE VHD 1220 D MIC G8 PARA VHD 1220 D MIC G9'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4290721' , value='4290059')   # CODIGO
    df = df.replace(
        to_replace='WEBCAM CAM HD 720P',
        value='SUBSTITUIDO - DE HD 720P PARA HDWCI 720p'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4291080' , value='4290060')   # CODIGO
    df = df.replace(
        to_replace='VIDEO CONFERENCIA USB CAM-1080P',
        value='SUBSTITUIDO - DE CAM-1080P PARA Webcam 1080p 60FPS'
        ) # DESCRIÇÃO 
  
    df = df.replace(to_replace='4291220' , value='4290008')   # CODIGO
    df = df.replace(
        to_replace='MOUSE MSI100 SEM FIO PRETO',
        value='SUBSTITUIDO - DE MOUSE MSI100 PARA MSI100 BLISTER'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4560042' , value='4560054')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 3220 D A G6- IR 20M, LENTE 2,8mm, RESOL1080P, MULTI HD4X1,IP67, CASE METAL, INST INT/EXT, ENTR AUDIO, ABER106',
        value='SUBSTITUIDO - DE VHD 3220 D A PARA VHD 3220 DFC+'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4690011' , value='4540080')   # CODIGO
    df = df.replace(
        to_replace='SENSOR DE MOVIMENTO SMART ISM 1001',
        value='SUBSTITUIDO - DE ISM 1001 PARA MSM 1001'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4690012' , value='4540081')   # CODIGO
    df = df.replace(
        to_replace='SENSOR DE ABERTURA SMART ISA 1001',
        value='SUBSTITUIDO - DE ISA 1001 PARA MSA 1001'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4690016' , value='4610027')   # CODIGO
    df = df.replace(
        to_replace='SENSOR DE TEMPERATURA E UMIDADE SMART IST 1001',
        value='SUBSTITUIDO - DE IST 1001 PARA MTU 1001'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4690017' , value='4500036')   # CODIGO
    df = df.replace(
        to_replace='MINI BOTAO SEM FIO ISW 1001',
        value='SUBSTITUIDO - DE IST 1001 PARA MSW 1001'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4750061' , value='4750058')   # CODIGO
    df = df.replace(
        to_replace='ROTEADOR WOM 5A MIMO FAST WIRELESS (CPE) 5GHZ 16DBI',
        value='SUBSTITUIDO - DE WOM 5A MIMO PARA WOM AC'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4822037' , value='4300739')   # CODIGO
    df = df.replace(
        to_replace='PLACA SNMP PARA GERENCIAMENTO REMOTO PGR 801L',
        value='SUBSTITUIDO - DE PGR 801L PARA PGR 801S'
        ) # DESCRIÇÃO 
  
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
    df['Comprar'] = np.floor(df['Sugestao 40 Dias'] / df['Qtd. Multipla']) * df['Qtd. Multipla']

    # Define a coluna Total, sendo a quantidade ajustada do COMPRAR multiplicando o PV
    df['Total'] = (df['PV'] * df['Comprar']).round(2)

    # Função de filtro 
    def filtro():
    # Campo de texto para inserir o critério de filtro
        col_marca , col_produto = st.columns(2)
        with col_marca:
            filtro_marca = st.text_input('Digite uma marca para filtrar:')
        with col_produto:
            filtro_produto = st.text_input('Digite um produto para filtrar:')

        # Aplicar o filtro e mostrar o resultado
        global filtered_df
        filtered_df = df[df['Marca'].str.contains(filtro_marca, case=False) & df['Produto'].str.contains(filtro_produto , case=False)]
        st.title('Planilha de Compras')
        st.text('Tabela de Referencia : Outubro-2025') # ATUALIZAR SEMPRE A TABELA DA INTELBRAS *****************************
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
