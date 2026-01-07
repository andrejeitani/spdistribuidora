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
    df = df[df['Codigo'] != '4560039'] # VHD 1230 B BLACK G7
    df = df[df['Codigo'] != '4560045'] # VHD 1220 B FULL COLOR G7  
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
    df = df[df['Codigo'] != '4680261'] # SS 5532 MF W
    df = df[df['Codigo'] != '4680260'] # SS 5542 MF W
    df = df[df['Codigo'] != '4680052'] # SS 1530 MF W
    df = df[df['Codigo'] != '4680058'] # SS 1540 MF W
    df = df[df['Codigo'] != '4660167'] # CATRACA C/RECONHECIMENTO FACIAL CAP 3000
    df = df[df['Codigo'] != '4663150'] # Catraca Pedestal CAP 3000
    df = df[df['Codigo'] != '4663160'] # Catraca Pedestal CAP 3000 UC 
    df = df[df['Codigo'] != '4580772'] # MHDX 1116 - HD 4TB
    df = df[df['Codigo'] != '4580773'] # MHDX 1116 - HD 1TB
    df = df[df['Codigo'] != '4581048'] # MHDX 1108 - HD 1TB
    df = df[df['Codigo'] != '4581082'] # MHDX 1304 - HD 1TB
    df = df[df['Codigo'] != '4581093'] # MHDX 1308 - HD 1TB
    df = df[df['Codigo'] != '4581100'] # MHDX 1116 - HD 2TB  
    df = df[df['Codigo'] != '4682073'] # SS 3430 MF
    df = df[df['Codigo'] != '4390176'] # AMT 2018 EG
    df = df[df['Codigo'] != '4390179'] # AMT 2018 E
    df = df[df['Codigo'] != '4400338'] # LICENÇA RAMAL UNNITI
    df = df[df['Codigo'] != '4679011'] # FX 2000 PRETA
    df = df[df['Codigo'] != '4679015'] # FX 2000 INOX
    df = df[df['Codigo'] != '4679010'] # FX 2000 CINZA
    df = df[df['Codigo'] != '4679021'] # FX 2000 AJUSTAVEL
    df = df[df['Codigo'] != '4670051'] # MFD 2020 CHAMPANHE 
    df = df[df['Codigo'] != '4670058'] # MFD 2020 PRETA
    df = df[df['Codigo'] != '4760089'] # S1010F-P
    df = df[df['Codigo'] != '4564045'] # VIP 5500 FISH EYE
    df = df[df['Codigo'] != '4760040'] # SF 900 HI POE
    df = df[df['Codigo'] != '4780039'] # VEX 3004
    df = df[df['Codigo'] != '4780072'] # VEX 3120
    df = df[df['Codigo'] != '4780073'] # VEX 3120
    df = df[df['Codigo'] != '4810040'] # VB 503
    df = df[df['Codigo'] != '4810043'] # VB 1104 WP  
    df = df[df['Codigo'] != '4682070'] # CT 3000 2PB
    df = df[df['Codigo'] != '4580787'] # NVD 1416 # SUBSTITUIDO PELO 1516
    df = df[df['Codigo'] != '4580785'] # NVD 1432 # AINDA SEM SUBSTITUTO
    df = df[df['Codigo'] != '4580934'] # NVD 3316 P # SUBSTITUIDO PELO iNVD 3016 P
    df = df[df['Codigo'] != '4830135'] # CABO DE REDE CAT5
    df = df[df['Codigo'] != '4830134'] # CABO DE REDE CAT5
    df = df[df['Codigo'] != '4830007'] # CABO DE REDE CAT6
    df = df[df['Codigo'] != '4830008'] # CABO DE REDE CAT6
    df = df[df['Codigo'] != '4830030'] # CABO DE REDE CAT5
    df = df[df['Codigo'] != '4830050'] # CABO MULTICAMERAS
    df = df[df['Codigo'] != '4830051'] # CABO MULTICAMERAS
    df = df[df['Codigo'] != '4830052'] # CABO MULTICAMERAS
    df = df[df['Codigo'] != '4140034'] # RECEPTOR RDS 830
    df = df[df['Codigo'] != '4141007'] # ANTENA DIGITAL AI 2031  
    df = df[df['Codigo'] != '4631200'] # BLA 1200
    df = df[df['Codigo'] != '4632200'] # BLA 1200
    df = df[df['Codigo'] != '4670008'] # IFR 7000 +
    df = df[df['Codigo'] != '4671085'] # FS 150 KIT ELITE
    df = df[df['Codigo'] != '4580934'] # NVD 3316 P , substituido pelo iNVD 3016P
    df = df[df['Codigo'] != '4560025'] # VHD 3230 B
    df = df[df['Codigo'] != '4830053'] # CABO COAXIAL CFTV 4mm 67% COBRE
    df = df[df['Codigo'] != '4690014'] # IZY Sirene Smart ISI 1001
    df = df[df['Codigo'] != '4690015'] # IZY Sistema de Segurança Smart ISS 1001 
    df = df[df['Codigo'] != '4011025'] # IZY Sistema de Segurança Smart ISS 102 
    df = df[df['Codigo'] != '4830132'] # CABO DROP
    df = df[df['Codigo'] != '4990147'] # IMPACTAS 16/40/68
    df = df[df['Codigo'] != '4990148'] # IMPACTAS 16/40/68
    df = df[df['Codigo'] != '4400080'] # IMPACTAS 16/40/68
    df = df[df['Codigo'] != '4400302'] # CONECTA E MODULARE +
    df = df[df['Codigo'] != '4990515'] # IMPACTAS 94/140/220/300
    df = df[df['Codigo'] != '4995861'] # IMPACTAS 94/140/220/300
    df = df[df['Codigo'] != '4080015'] # PLENO
    df = df[df['Codigo'] != '4080057'] # PLENO C/ CHAVE
    df = df[df['Codigo'] != '4080058'] # PLENO C/ CHAVE
    df = df[df['Codigo'] != '4080015'] # PLENO 100 MS
    df = df[df['Codigo'] != '4080085'] # TC 50 BRANCO
    df = df[df['Codigo'] != '4080086'] # TC 50 PRETO
    df = df[df['Codigo'] != '4080091'] # TC 50 PREMIUM
    df = df[df['Codigo'] != '4100015'] # QDI 15 R9
    df = df[df['Codigo'] != '4119041'] # TEL. RURAL CFW 9041
    df = df[df['Codigo'] != '4122513'] # TS 2513
    df = df[df['Codigo'] != '4123103'] # TS 3113
    df = df[df['Codigo'] != '4125122'] # TS 5122
    df = df[df['Codigo'] != '4125123'] # TS 5123
    df = df[df['Codigo'] != '4125150'] # TS 5150
    df = df[df['Codigo'] != '4590009'] # IMX1
    df = df[df['Codigo'] != '4590011'] # IMX1 C/ CARTÃO
    df = df[df['Codigo'] != '4760016'] # IFR 7000
    df = df[df['Codigo'] != '4670210'] # FR 210 
    df = df[df['Codigo'] != '4100014'] # QDP 15
    df = df[df['Codigo'] != '4100025'] # QDO 20
    df = df[df['Codigo'] != '4568013'] # VBOX 5100
    df = df[df['Codigo'] != '4690014'] # ISI 1001
    df = df[df['Codigo'] != '4690015'] # ISS 1001
    df = df[df['Codigo'] != '4690016'] # IST 1001
    df = df[df['Codigo'] != '4690017'] # ISW 1001
    df = df[df['Codigo'] != '4990147'] # PLACA RAMAL IMPACTA
    df = df[df['Codigo'] != '4990148'] # PLACA RAMAL IMPACTA
    df = df[df['Codigo'] != '4990515'] # PLACA RAMAL IMPACTA 
    df = df[df['Codigo'] != '4750090'] # WOM 5A MIMO FAST
    df = df[df['Codigo'] != '4100005'] # PLACA RAMAL DECT 5RM
    df = df[df['Codigo'] != '4110000'] # CIP 850
    df = df[df['Codigo'] != '4400304'] # PLACA RAMAL DESBALANCEADA
    df = df[df['Codigo'] != '4990253'] # PLACA FONTE IMPACTA 16/68
    df = df[df['Codigo'] != '4990260'] # PLACA FXS CIP 850
    df = df[df['Codigo'] != '4990261'] # PLACA FXO CIP 850
    df = df[df['Codigo'] != '4993018'] # PLACA TRONCO IMPACTA
    df = df[df['Codigo'] != '4321708'] # UNNITI 2000
    df = df[df['Codigo'] != '4321709'] # UNNITI 3000
    df = df[df['Codigo'] != '4201201'] # TIP 120I
    df = df[df['Codigo'] != '4320208'] # UNNITI 2000 IP
    df = df[df['Codigo'] != '4400094'] # PLACA GRAVAÇÃO IMPACTA 68I
    df = df[df['Codigo'] != '4841059'] # ECM 6048
    df = df[df['Codigo'] != '4400404'] # UNNITI 1000
    df = df[df['Codigo'] != '4320216'] # UNNITI 2000
    df = df[df['Codigo'] != '4822000'] # XNB 720 110V
    df = df[df['Codigo'] != '4822001'] # XNB 720 220V
    df = df[df['Codigo'] != '4822002'] # XNB 1440 110V
    df = df[df['Codigo'] != '4822003'] # XNB 1440 220V
    df = df[df['Codigo'] != '4822004'] # XNB 600 110V
    df = df[df['Codigo'] != '4822005'] # XNB 600 220V
    df = df[df['Codigo'] != '4822006'] # XNB 1200 110V
    df = df[df['Codigo'] != '4822007'] # XNB 1200 220V
    df = df[df['Codigo'] != '4822008'] # XNB 1800 110V
    df = df[df['Codigo'] != '4822009'] # XNB 1800 220V
    df = df[df['Codigo'] != '4822010'] # XNB 720 BI
    df = df[df['Codigo'] != '4822011'] # XNB 1440 BI
    df = df[df['Codigo'] != '4822016'] # XNB 1440 BI +
    df = df[df['Codigo'] != '4822017'] # XNB 1800 BI +
    df = df[df['Codigo'] != '4527003'] # FR 330
    df = df[df['Codigo'] != '4670028'] # MFR 1001
    df = df[df['Codigo'] != '4670036'] # MFD 7001
    df = df[df['Codigo'] != '4670037'] # MFD 7000
    df = df[df['Codigo'] != '4670100'] # FD 1000
    df = df[df['Codigo'] != '4670200'] # FD 2000
    df = df[df['Codigo'] != '4670210'] # FR 210
    df = df[df['Codigo'] != '4670300'] # FD 3000
    df = df[df['Codigo'] != '4670331'] # FR 331
    df = df[df['Codigo'] != '4670500'] # FR 500 D
    df = df[df['Codigo'] != '4670620'] # FR 620
    df = df[df['Codigo'] != '4670630'] # FR 630
    df = df[df['Codigo'] != '4674005'] # FR 400
    df = df[df['Codigo'] != '4820017'] # EF 1201+ 
    df = df[df['Codigo'] != '4400080'] # IMPACTAS 16/40/68
    df = df[df['Codigo'] != '4750206'] # ROTEADOR 5G BRANCO GX 1001C BR
    df = df[df['Codigo'] != '4540011'] # IVP 4000 SMART
    df = df[df['Codigo'] != '4820017'] # EF 1201+
    df = df[df['Codigo'] != '4750206'] # ROTEADOR 5G BRANCO GX 1001C BR 
  
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

    df = df.replace(to_replace='4580760' , value='4900022')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR MHDX 1232 - 32 CANAIS (HDCVI/AHD/HDTVI/ANAL/IP), RES 1080P LITE, ANAL VIDEO, MODO HIB,PADR LGPD, SUP 2 HDs SATA',
        value='SUBSTITUIDO - DE MHDX 1232 PARA MHDX 1332'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='1950464' , value='4300696')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VIP 7430 B A FT -IR 30M, LENTE 2,8mm, RESOL4MP,STARLIGHT,IP67, CASE METAL/PLAST, INST INT/EXT, MICROF,ANAL VIDEO',
        value='SUBSTITUIDO - DE VIP 7430 PARA I 5430'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4123001' , value='4123102')   # CODIGO
    df = df.replace(
        to_replace='TELEFONE SEM FIO TS 3111 RAMAL BRANCO',
        value='SUBSTITUIDO - DE TS 3111 BRANCO PARA TS 3111 PRETO'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4123002' , value='4123102')   # CODIGO
    df = df.replace(
        to_replace='TELEFONE SEM FIO TS 3112 BRANCO',
        value='SUBSTITUIDO - DE TS 3112 BRANCO PARA TS 3111 PRETO'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4123010' , value='4123110')   # CODIGO
    df = df.replace(
        to_replace='TELEFONE SEM FIO TS 3110 BRANCO',
        value='SUBSTITUIDO - DE TS 3112 BRANCO PARA TS 3111 PRETO'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4123101' , value='4123110')   # CODIGO
    df = df.replace(
        to_replace='TELEFONE SEM FIO TS 3110 VERMELHO',
        value='SUBSTITUIDO - DE TS 3112 VERMELHO PARA TS 3111 PRETO'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4123153' , value='4123110')   # CODIGO
    df = df.replace(
        to_replace='TELEFONE SEM FIO TS 3110 BRANCO E PRETO',
        value='SUBSTITUIDO - DE TS 3112 VERMELHO PARA TS 3111 PRETO'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4140032' , value='4140033')   # CODIGO
    df = df.replace(
        to_replace='SMART BOX ANDROID TV IZY PLAY STICK',
        value='SUBSTITUIDO - DE IZY HD PARA IZY FULL HD'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4504401' , value='4504400')   # CODIGO
    df = df.replace(
        to_replace='TRANSMISSOR XTR 1000 BRANCO/ROSA',
        value='SUBSTITUIDO - DE XTR BRANCO/ROSA PARA PRETO/BRANCO'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4504500' , value='4684018')   # CODIGO
    df = df.replace(
        to_replace='CHAVEIRO DE PROXIMIDADE XID1000 RDIF MIFARE 13,56MHZ',
        value='SUBSTITUIDO - DE XID1000 PARA TH 1000 DT'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4560033' , value='4560164')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 1130 B G7 - IR 30M, LENTE 2,8mm, RESOL 720P, MULTI HD 4X1, IP67, CASE PLAST, INST INT/EXT, ABERT 109',
        value='SUBSTITUIDO - DE VHD 1130 B G7 PARA VHD 1230 B G9'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4560035' , value='4560163')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 1120 D G7 - IR 20M, LENTE 2,8mm, RESOL HD 720P/ ANAL600TVL, MULTI HD4X1, CASE PLAST, INST INT ABERT 97',
        value='SUBSTITUIDO - DE VHD 1120 D G7 PARA VHD 1220 D G9'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4560090' , value='4560164')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 1230 B G8 - IR 30M, LENTE 3,6mm, RESOL 1080P, MULTI HD 4X1, IP67, CASE PLAST, INST INT/EXT, ABERT98',
        value='SUBSTITUIDO - DE G8 PARA G9'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4565355' , value='4560164')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 3530 B - IR 30M, LENTE 3,6mm, RESOL 5MP, HDCVI, IP67, CASE METAL, INST INT/EXT, ABERT92',
        value='SUBSTITUIDO - DE VHD 3530 B PARA VHD 3530 B FC+'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4565356' , value='4560108')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 3520 D - IR 20M, LENTE 2,8mm, RESOL 5MP, HDCVI, IP67, CASE MET, INST INT/EXT, ABERT110',
        value='SUBSTITUIDO - DE VHD 3520 D PARA VHD 3520 D FC+'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4581117' , value='4581104')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR EM REDE INVD 5232-16P - 32 CANAIS IP, RESOL 16MP, 16 POE, ANALIT DE VIDEO, SUP 4 HDs SATA 18TB',
        value='SUBSTITUIDO - DE 5232-16P D PARA 5232'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4770006' , value='4770025')   # CODIGO
    df = df.replace(
        to_replace='FRENTE FALSA P/ RACK FF1U',
        value='SUBSTITUIDO - DE FRENTE FALSA D PARA CONJUNTO FRENTE FALSA'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4830092' , value='4830249')   # CODIGO
    df = df.replace(
        to_replace='PATCH CORD IMPACT LAN UTP CAT5E 4P PRETO 3,0M',
        value='SUBSTITUIDO - APENAS TROCA DE CODIGO'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4950304' , value='4950305')   # CODIGO
    df = df.replace(
        to_replace='SPEED DOME VIP 7210 SD TM FT - IR 50M, RESOL 2MP, IP67, TERMICO, DET TEMP/INCENDIO, ENT/SAI ALARME, ALIM 12V',
        value='SUBSTITUIDO - DE VIP 7210 PARA VIP 7207'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4750060' , value='4750058')   # CODIGO
    df = df.replace(
        to_replace='ROTEADOR WOM 5A FAST WIRELESS (CPE) 5GHZ 16DBI',
        value='SUBSTITUIDO - DE WOM 5A FAST PARA WOM AC GIGA'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4760116' , value='4760129')   # CODIGO
    df = df.replace(
        to_replace='SWITCH NAO GERENCIAVEL POE 26P FAST ETHERNET (4P UPLINK, SENDO 2P SFP) S1126F-PA 4760116',
        value='SUBSTITUIDO - DE S1126F PARA S1126F-HPA'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4760118' , value='4760130')   # CODIGO
    df = df.replace(
        to_replace='SWITCH NAO GERENCIAVEL POE 5P FAST ETHERNET 100Mbps (SENDO 4P FUNCAO POE E 1 UNIK) S1105F-P  4760118',
        value='SUBSTITUIDO - DE S1105F PARA S1105G-P'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4950048' , value='4950780')   # CODIGO
    df = df.replace(
        to_replace='SPEED DOME VIP 5432 SD IA FT - IR 150M, ZOOM OPT 32X/DIG 16X, L 4,8 A 154mm, RES 4MP,IP67/IK10, ALIM 24V/2,5A, AUTO TRAC',
        value='SUBSTITUIDO - APENAS TROCA DE CODIGO'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4581040' , value='4581253')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR MHDX 1108-C - 8 CANAIS (HDCVI/AHD/HDTVI/IP), RES 1080P LITE, GAB COMPACTO,ANAL VIDEO,MODO NVR, SUP 1HD SATA/SSD',
        value='SUBSTITUIDO - DE 1108C PARA 1208C'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4541051' , value='4540088')   # CODIGO
    df = df.replace(
        to_replace='SENSOR INFRA VERMELHO PASSIVO IVP 7001 MW PET',
        value='SUBSTITUIDO - DE IVP 7001 PARA IVP 5000 MW LD'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4613533' , value='4610049')   # CODIGO
    df = df.replace(
        to_replace='DETECTOR DE TEMPERATURA DTE 521 - ENDERECAVEL, TERMOVELOCIMETRICO, 20/30V',
        value='SUBSTITUIDO - DE DTE 521 PARA DTE 523'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4613532' , value='4610050')   # CODIGO
    df = df.replace(
        to_replace='DETECTOR DE FUMACA DFE 521 - ENDERECAVEL, OPTICO INFRAVERMELHO, 20 a 30Vdc, AMB INTERNO, CASE ABS PROT UV',
        value='SUBSTITUIDO - DE DFE 521 PARA DFE 523'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4565352' , value='4560048')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 3240 B FULL COLOR G6, IR 40M, LENTE 3,6mm, RSOL 1080P, MULTI HD 4X1, IP67, CASE PLAST, INST INT/EXT, ABERT91',
        value='SUBSTITUIDO - DE VHD 3240 FC PARA VHD 3240 FC +'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4560036' , value='4560053')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 3130 B G7 - IR 30M, LENTE 3,6mm, RESOL 720P/ 600TVL, MULTI HD 4X1, IP67, CASE METAL, INST INT/EXT, ABERT98',
        value='SUBSTITUIDO - DE VHD 3130 B G7 PARA VHD 3220 B FC +'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4560024' , value='4560054')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 3130 D G7 - IR 30M, LENTE 3,6mm, RESOL 720P/ 600TVL, MULTI HD 4X1, IP67, CASE METAL, INST INT/EXT, ABERT98',
        value='SUBSTITUIDO - DE VHD 3130 D G7 PARA VHD 3220 D FC +'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4560080' , value='4560054')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 3230 D G8 - IR 30M, LENTE 2,8mm, RESOL 1080P, MULTI HD 4X1, IP67, CASE METAL, INST INT/EXT, ABERT98',
        value='SUBSTITUIDO - DE VHD 3230 D G8 PARA VHD 3220 D FC +'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4570046' , value='4900014')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VIP 1230 D G5- IR 30M, LENTE 2,8mm, RESOL 1080P, POE, IP67, CASE AL/PLAST, INST INT/EXT, MICROFONE, DET MOVIMENTO',
        value='SUBSTITUIDO - DE VIP 1230 D G5 PARA VIP 1230 D FC +'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4560081' , value='4560053')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHD 3230 B G8 - IR 30M, LENTE 3,6mm, RESOL 1080P/ 600TVL, MULTI HD 4X1, IP67, CASE METAL, INST INT/EXT, ABERT98',
        value='SUBSTITUIDO - DE VHD 3230 B G8 PARA VHD 3220 B FC +'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4560086' , value='4900046')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHL 1220 D G8 - IR 20M, LENTE 2,8mm, RESOL 1080P, HDCVI, CASE PLAST, INST INT, ABERT108',
        value='SUBSTITUIDO - DE VHL 1120 D G8 PARA VHL 1120 B G9'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4560075' , value='4900045')   # CODIGO
    df = df.replace(
        to_replace='CAMERA VHL 1220 B G8 - IR 20M, LENTE 2,8mm, RESOL1080P, HDCVI,IP66, CASE PLAST, INST INT/EXT, ABERT 108, LINHA FULLHD',
        value='SUBSTITUIDO - DE VHL 1220 B G8 PARA VHL 1220 B G9'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4780033' , value='4760107')   # CODIGO
    df = df.replace(
        to_replace='SWITCH SG2404 POE L2+ GIGA 24 PORTAS POE GERENCIAVEL + 4 PORTAS GBIC SFP',
        value='SUBSTITUIDO - DE SG 2404 POE L2 PARA S2328 G-PA'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4760041' , value='4760104')   # CODIGO
    df = df.replace(
        to_replace='SWITCH SG 1002MR L2+ GIGA 8 PORTAS GERENCIAVEL 2 PORTAS MINI-GBIC SFP',
        value='SUBSTITUIDO - DE SG 1002 MR L2 PARA S2310G-A'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4760039' , value='4760128')   # CODIGO
    df = df.replace(
        to_replace='SWITCH SF 1821 POE FAST 16 PORTAS POE 2 PORTAS GIGABIT E 1 PORTA SFP UPLINK',
        value='SUBSTITUIDO - DE SF 1821 PARA S1118F-PA'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4760046' , value='4760110')   # CODIGO
    df = df.replace(
        to_replace='SWITCH GERENCIAVEL 48 PORTAS GIGA + 4PGBIC SG 5204MR L2+',
        value='SUBSTITUIDO - DE S5204 MR L2 PARA S2352G-A'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4760075' , value='4760129')   # CODIGO
    df = df.replace(
        to_replace='SWITCH SF 2421 FAST 24 PORTAS POE 2 PORTAS GIGA 1 PORTA MINI-GBIC SFP',
        value='SUBSTITUIDO - DE SF 2421 PARA S1126F-HPA'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4760089' , value='4760125')   # CODIGO
    df = df.replace(
        to_replace='SWITCH S1010F-P FAST 8 PORTAS POE 2 PORTAS UPLINK',
        value='SUBSTITUIDO - DE S1010F-P PARA S1110F'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4760080' , value='4760125')   # CODIGO
    df = df.replace(
        to_replace='SWITCH S3028G-B GIGA 24 PORTAS GERENCIAVEL L3 4 PORTAS MINI-GBIC SFP',
        value='SUBSTITUIDO - DE S3028G-B PARA S3328G-B'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4760081' , value='4760119')   # CODIGO
    df = df.replace(
        to_replace='SWITCH S1005G GIGA 5 PORTAS',
        value='SUBSTITUIDO - DE S1005G PARA S1105G'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4760020' , value='4760117')   # CODIGO
    df = df.replace(
        to_replace='SWITCH SF 800 Q+ FAST 8 PORTAS QOS 12-24V',
        value='SUBSTITUIDO - DE SF 800 PARA S1108F'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4682071' , value='4680332')   # CODIGO
    df = df.replace(
        to_replace='CONTROLADOR DE ACESSO CT 3000 4PB - CAP 100 MIL USUARIOS, 3MIL BIOMET, ATE 4 PORTAS',
        value='SUBSTITUIDO - DE CT 3000 PARA CT 5000'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4822014' , value='4820158')   # CODIGO
    df = df.replace(
        to_replace='NOBREAK SNB 1500VA SENOIDAL BIVOLT BATERIA EXTERNA OPCIONAL 2 X 45A',
        value='SUBSTITUIDO - DE SNB 1500 PARA ATTIV SENO 1800'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4850001' , value='4300400')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR CONTROLADOR DE CARGAS WIFI EWS 201 E',
        value='SUBSTITUIDO - DE EWS 201 E PARA ECW 1000'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4850006' , value='4300403')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR CONTROLADOR DE CARGAS WIFI 2/2 EWS 222',
        value='SUBSTITUIDO - DE EWS 222 E PARA ECW 1002'
        ) # DESCRIÇÃO  
  
    df = df.replace(to_replace='4850005' , value='4300402')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR CONTROLADOR DE CARGAS WIFI 1/1 EWS 211',
        value='SUBSTITUIDO - DE EWS 211 E PARA ECW 1001'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4850013' , value='4300404')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR SMART WI-FI TOUCH 1 EWS 1001 BR',
        value='SUBSTITUIDO - DE EWS 1001 BR E PARA EIW 1001 BR'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4850014' , value='4300405')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR SMART WI-FI TOUCH 1 EWS 1001 PT',
        value='SUBSTITUIDO - DE EWS 1001 PT E PARA EIW 1001 PT'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4850015' , value='4300412')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR SMART WI-FI TOUCH 2 EWS 1002 BR',
        value='SUBSTITUIDO - DE EWS 1002 BR E PARA EIW 1002 BR'
        ) # DESCRIÇÃO    

    df = df.replace(to_replace='4850016' , value='4300406')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR SMART WI-FI TOUCH 2 EWS 1002 PT',
        value='SUBSTITUIDO - DE EWS 1002 PT E PARA EIW 1002 PT'
        ) # DESCRIÇÃO    

    df = df.replace(to_replace='4850017' , value='4300407')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR SMART WI-FI TOUCH 3 EWS 1003 BR',
        value='SUBSTITUIDO - DE EWS 1003 BR E PARA EIW 1003 BR'
        ) # DESCRIÇÃO    

    df = df.replace(to_replace='4850018' , value='4300408')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR SMART WI-FI TOUCH 3 EWS 1003 PT',
        value='SUBSTITUIDO - DE EWS 1003 PT E PARA EIW 1003 PT'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4522000' , value='4520064')   # CODIGO
    df = df.replace(
        to_replace='CAMPAINHA CIB 101 PRETA S/ FIO C/ BATERIA',
        value='SUBSTITUIDO - DE CIB 101 PT E PARA CIB 101 S PT'
        ) # DESCRIÇÃO     

    df = df.replace(to_replace='4522001' , value='4520063')   # CODIGO
    df = df.replace(
        to_replace='CAMPAINHA CIB 101 BRANCA S/ FIO C/ BATERIA',
        value='SUBSTITUIDO - DE CIB 101 BR E PARA CIB 101 S BR'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4850028' , value='4300397')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR ELETRICOSMART WIFI TOUCH PRETO EWS 1004',
        value='SUBSTITUIDO - DE EWS 1004 PT PARA EIW 1004 PT'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4850029' , value='4300396')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR ELETRICOSMART WIFI TOUCH BRANCO EWS 1004',
        value='SUBSTITUIDO - DE EWS 1004 BR PARA EIW 1004 BR'
        ) # DESCRIÇÃO     

    df = df.replace(to_replace='4850027' , value='4300399')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR ELETRICO SMART WIF TOUCH PRETO EWS 1006',
        value='SUBSTITUIDO - DE EWS 1006 PT PARA EIW 1006 PT'
        ) # DESCRIÇÃO    

    df = df.replace(to_replace='4850030' , value='4300398')   # CODIGO
    df = df.replace(
        to_replace='INTERRUPTOR ELETRICO SMART WIFI TOUCH BRANCO EWS 1006',
        value='SUBSTITUIDO - DE EWS 1006 BR PARA EIW 1006 BR'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4850062' , value='4300390')   # CODIGO
    df = df.replace(
        to_replace='TOMADA ETS 1001 - SIMPLES INTELIGENTE WI-FI, IZY, 10A, BRANCO, MED CONSUMO, COMP APP VOZ ALEXA/GOOGLE',
        value='SUBSTITUIDO - DE ETS 1001 PARA ETW 1001 BR'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4850063' , value='4300391')   # CODIGO
    df = df.replace(
        to_replace='TOMADA ETS 1001 - SIMPLES INTELIGENTE WI-FI, IZY, 10A, PRETO, MED CONSUMO, COMP APP VOZ ALEXA/GOOGLE',
        value='SUBSTITUIDO - DE ETS 1001 PARA ETW 1001 PT'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4850064' , value='4300392')   # CODIGO
    df = df.replace(
        to_replace='TOMADA ETS 1002 - DUPLA INTELIG, SMART WI-FI, 10A, BRANCO, MED CONSUMO, COMP APP VOZ ALEXA/GOOGLE',
        value='SUBSTITUIDO - DE ETS 1002 PARA ETW 1002 BR'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4850065' , value='4300393')   # CODIGO
    df = df.replace(
        to_replace='TOMADA ETS 1002 - DUPLA INTELIG, SMART WI-FI, 10A, PRETO, MED CONSUMO, COMP APP VOZ ALEXA/GOOGLE',
        value='SUBSTITUIDO - DE ETS 1002 PARA ETW 1021 PT'
        ) # DESCRIÇÃO 

    df = df.replace(to_replace='4850068' , value='4300410')   # CODIGO
    df = df.replace(
        to_replace='TOMADA ETS 2002 - SIMPLES C/ INTERRUP INTELIG WI-FI, 2 TECLA TOUCH, 10A, BRANCO, MED CONSUMO, COMP APP VOZ ALEXA/GOOGLE',
        value='SUBSTITUIDO - DE ETS 2002 PARA ETW 1021 BR'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4850066' , value='4300394')   # CODIGO
    df = df.replace(
        to_replace='TOMADA ETS 2001 - SIMPLES C/ INTERRUP INTELIG WI-FI, 1 TECLA TOUCH, 10A, BRANCO, MED CONSUMO, COMP APP VOZ ALEXA/GOOGLE',
        value='SUBSTITUIDO - DE ETS 2002 PARA ETW 1011 BR'
        ) # DESCRIÇÃO

    df = df.replace(to_replace='4850067' , value='4300395')   # CODIGO
    df = df.replace(
        to_replace='TOMADA ETS 2001 - SIMPLES C/ INTERRUP INTELIG WI-FI, 1 TECLA TOUCH, 10A, PRETO, MED CONSUMO, COMP APP VOZ ALEXA/GOOGLE',
        value='SUBSTITUIDO - DE ETS 2001 PARA ETW 1011 PT'
        ) # DESCRIÇÃO  

    df = df.replace(to_replace='4850069' , value='4300395')   # CODIGO
    df = df.replace(
        to_replace='TOMADA ETS 2002 - SIMPLES C/ INTERRUP INTELIG WI-FI, 2 TECLA TOUCH, 10A, PRETO, MED CONSUMO, COMP APP VOZ ALEXA/GOOGLE',
        value='SUBSTITUIDO - DE ETS 2002 PARA ETW 1021 PT'
        ) # DESCRIÇÃO   

    df = df.replace(to_replace='4581052' , value='4580641')   # CODIGO
    df = df.replace(
        to_replace='GRAVADOR EM REDE NVD 1404 P - 4 CANAIS IP, RESOL 4K, H265/H265+, POE, PADR LGPD, SUP 1 HD SATA',
        value='SUBSTITUIDO - DE NVD 1404 P PARA NVD 1404 P AM'
        ) # DESCRIÇÃO   
  
    ##############################################################################################
    # Itens em promoção
    promocao1 = ['4540055','4541073','4543544','4543590','4541041','4541032','4540089','4540088','4541076','4541014','4550018','4541019']
    descricao1 = '***COMPRAR SEPARADO - BU SEGURANÇA - 28-02-26***'
    df['Produto'] = np.where(df['Codigo'].isin(promocao1) , descricao1 , df['Produto'])

    promocao2 = ['4294200' , '4294100' , '4293200' , '4293100' , '4290060' , '4290059' , '4290024' , '4290009' , '4290008' , '4061001' , '4290048' , '4900027' , '4900014']
    descricao2 = '***COMPRAR SEPARADO - CAMPANHA COMERCIAL JAN - 31-01-26***'
    df['Produto'] = np.where(df['Codigo'].isin(promocao2) , descricao2 , df['Produto'])

    promocao3 = ['4760132' , '4760105' , '4760104' , '4760102' , '4760101' , '4830105' , '4830092' , '4830056' , '4830039' , '4830246' , '4830232' , '4830213' , '4830229' , '4710031' , '4710029' , '4993018' , '4991013' , '4990690' , '4990260' , '4990195' , '4990152' , '4990144' , '4990003' , '4990002' , '4401042' , '4400405' , '4400403' , '4400402' , '4400348' , '4400305' , '4400073' , '4400072' , '4340204' , '4340013' , '4340011' , '4340003' , '4320215' , '4115100' , '4830191' , '4830166' , '4830165' , '4830164' , '4830163' , '4830160' , '4830132' , '4160025' , '4140034' , '4140020' , '4780194' , '4780193' , '4710034' , '4710033' , '4710021' , '4770076' , '4770076' , '4770075' , '4770073' , '4770070' , '4770065' , '4770055' , '4770042' , '4570028' , '4570034' , '4560058' , '4560077' , '4560047' , '4540109' , '4541061' , '4540015' , '4540041' , '4540054' , '4550004' , '4543582' , '4540050' , '4820097' , '4820121' , '4820181' , '4822046' , '4822300' , '4822034' , '4822026' , '4820131' , '4820142' , '4830145' , '4830149' , '4830151' , '4830152' , '4830146' , '4670051' , '4670036' , '4670037' , '4140027' , '4142105']
    descricao3 = '***COMPRAR SEPARADO - SELL IN/OUT - 31-01-26***'
    df['Produto'] = np.where(df['Codigo'].isin(promocao3) , descricao3 , df['Produto'])

    ##############################################################################################

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
    df['Comprar'] = np.floor(df['Sugestao 40 Dias'] / df['Qtd. Multipla']) * df['Qtd. Multipla'] # Arredonda para baixo
    #df['Comprar'] = np.ceil(df['Sugestao 40 Dias'] / df['Qtd. Multipla']) * df['Qtd. Multipla'] # Arredonda para cima
    #df['Comprar'] = (df['Sugestao 40 Dias'] / df['Qtd. Multipla']) * df['Qtd. Multipla'] # Arredonda conforme a casa decimal

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
        st.text('Tabela de Referencia : Janeiro-2026') # ATUALIZAR SEMPRE A TABELA DA INTELBRAS *****************************
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
