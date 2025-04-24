import numpy as np
import pandas as pd

dict_produtos = {
    0: 'Arroz, trigo e outros cereais',
    1: 'Milho em grão',
    2: 'Algodão herbáceo, outras fibras da lavoura temporária',
    3: 'Cana-de-açúcar',
    4: 'Soja em grão',
    5: 'Outros produtos e serviços da lavoura temporária',
    6: 'Laranja',
    7: 'Café em grão',
    8: 'Outros produtos da lavoura permanente',
    9: 'Bovinos e outros animais vivos, produtos animal, caça e serviços',
    10: 'Leite de vaca e de outros animais',
    11: 'Suínos',
    12: 'Aves e ovos',
    13: 'Produtos da exploração florestal e da silvicultura',
    14: 'Pesca e aquicultura (peixe, crustáceos e moluscos)',
    15: 'Carvão mineral',
    16: 'Minerais não metálicos',
    17: 'Petróleo, gás natural e serviços de apoio',
    18: 'Minério de ferro',
    19: 'Minerais metálicos não ferrosos',
    20: 'Carne de bovinos e outros produtos de carne',
    21: 'Carne de suíno',
    22: 'Carne de aves',
    23: 'Pescado industrializado',
    24: 'Leite resfriado, esterilizado e pasteurizado',
    25: 'Outros produtos do laticínio',
    26: 'Açúcar',
    27: 'Conservas de frutas, legumes, outros vegetais e sucos de frutas',
    28: 'Óleos e gorduras vegetais e animais',
    29: 'Café beneficiado',
    30: 'Arroz beneficiado e produtos derivados do arroz',
    31: 'Produtos derivados do trigo, mandioca ou milho',
    32: 'Rações balanceadas para animais',
    33: 'Outros produtos alimentares',
    34: 'Bebidas',
    35: 'Produtos do fumo',
    36: 'Fios e fibras têxteis beneficiadas',
    37: 'Tecidos',
    38: 'Artigos têxteis de uso doméstico e outros têxteis',
    39: 'Artigos do vestuário e acessórios',
    40: 'Calçados e artefatos de couro',
    41: 'Produtos de madeira, exclusive móveis',
    42: 'Celulose',
    43: 'Papel, papelão, embalagens e artefatos de papel',
    44: 'Serviços de impressão e reprodução',
    45: 'Combustíveis para aviação',
    46: 'Gasoálcool',
    47: 'Naftas para petroquímica',
    48: 'Óleo combustível',
    49: 'Diesel - biodiesel',
    50: 'Outros produtos do refino do petróleo',
    51: 'Etanol e outros biocombustíveis',
    52: 'Produtos químicos inorgânicos',
    53: 'Adubos e fertilizantes',
    54: 'Produtos químicos orgânicos',
    55: 'Resinas, elastômeros e fibras artificiais e sintéticas',
    56: 'Defensivos agrícolas e desinfestantes domissanitários',
    57: 'Produtos químicos diversos',
    58: 'Tintas, vernizes, esmaltes e lacas',
    59: 'Perfumaria, sabões e artigos de limpeza',
    60: 'Produtos farmacêuticos',
    61: 'Artigos de borracha',
    62: 'Artigos de plástico',
    63: 'Cimento',
    64: 'Artefatos de cimento, gesso e semelhantes',
    65: 'Vidros, cerâmicos e outros produtos de minerais não metálicos',
    66: 'Ferro gusa e ferroligas',
    67: 'Semi acabados, laminados planos, longos e tubos de aço',
    68: 'Produtos da metalurgia de metais não ferrosos',
    69: 'Peças fundidas de aço e de metais não ferrosos',
    70: 'Produtos de metal, exclusive máquinas e equipamentos',
    71: 'Componentes eletrônicos',
    72: 'Máquinas para escritório e equipamentos de informática',
    73: 'Material eletrônico e equipamentos de comunicações',
    74: 'Equipamentos de medida, teste e controle, ópticos e eletromédicos',
    75: 'Máquinas, aparelhos e materiais elétricos',
    76: 'Eletrodomésticos',
    77: 'Tratores e outras máquinas agrícolas',
    78: 'Máquinas para a extração mineral e a construção',
    79: 'Outras máquinas e equipamentos mecânicos',
    80: 'Automóveis, camionetas e utilitários',
    81: 'Caminhões e ônibus, inclusive cabines, carrocerias e reboques',
    82: 'Peças e acessórios para veículos automotores',
    83: 'Aeronaves, embarcações e outros equipamentos de transporte',
    84: 'Móveis',
    85: 'Produtos de industrias diversas',
    86: 'Manutenção, reparação e instalação de máquinas e equipamentos',
    87: 'Eletricidade, gás e outras utilidades',
    88: 'Água, esgoto, reciclagem e gestão de resíduos',
    89: 'Edificações',
    90: 'Obras de infraestrutura',
    91: 'Serviços especializados para construção',
    92: 'Comércio por atacado e varejo',
    93: 'Transporte de carga (terrestre e aquaviário)',
    94: 'Transporte terrestre de passageiros',
    95: 'Transporte aéreo',
    96: 'Armazenamento e serviços auxiliares aos transportes',
    97: 'Correio e outros serviços de entrega',
    98: 'Serviços de alojamento em hotéis e similares',
    99: 'Serviços de alimentação',
    100: 'Livros, jornais e revistas',
    101: 'Serviços cinematográficos, música, rádio e televisão',
    102: 'Telecomunicações, TV por assinatura e outros serviços relacionados',
    103: 'Desenvolvimento de sistemas e outros serviços de informação',
    104: 'Intermediação financeira, seguros e previdência complementar',
    105: 'Aluguel efetivo e serviços imobiliários',
    106: 'Aluguel imputado',
    107: 'Serviços jurídicos, contabilidade e consultoria',
    108: 'Pesquisa e desenvolvimento',
    109: 'Serviços de arquitetura e engenharia',
    110: 'Publicidade e outros serviços técnicos',
    111: 'Aluguéis não imobiliários e gestão de ativos de propriedade intelectual',
    112: 'Condomínios e serviços para edifícios',
    113: 'Outros serviços administrativos',
    114: 'Serviços de vigilância, segurança e investigação',
    115: 'Serviços coletivos da administração pública',
    116: 'Serviços de previdência e assistência social',
    117: 'Educação pública',
    118: 'Educação privada',
    119: 'Saúde pública',
    120: 'Saúde privada',
    121: 'Serviços de artes, cultura, esporte e recreação',
    122: 'Organizações patronais, sindicais e outros serviços associativos',
    123: 'Manutenção de computadores, telefones e objetos domésticos',
    124: 'Serviços pessoais',
    125: 'Serviços domésticos'
}

dict_setores = {
    0: 'Agricultura, inclusive o apoio à agricultura e a pós-colheita',
    1: 'Pecuária, inclusive o apoio à pecuária',
    2: 'Produção florestal; pesca e aquicultura',
    3: 'Extração de carvão mineral e de minerais não metálicos',
    4: 'Extração de petróleo e gás, inclusive as atividades de apoio',
    5: 'Extração de minério de ferro, inclusive beneficiamentos e a aglomeração',
    6: 'Extração de minerais metálicos não ferrosos, inclusive beneficiamentos',
    7: 'Abate e produtos de carne, inclusive os produtos do laticínio e da pesca',
    8: 'Fabricação e refino de açúcar',
    9: 'Outros produtos alimentares',
    10: 'Fabricação de bebidas',
    11: 'Fabricação de produtos do fumo',
    12: 'Fabricação de produtos têxteis',
    13: 'Confecção de artefatos do vestuário e acessórios',
    14: 'Fabricação de calçados e de artefatos de couro',
    15: 'Fabricação de produtos da madeira',
    16: 'Fabricação de celulose, papel e produtos de papel',
    17: 'Impressão e reprodução de gravações',
    18: 'Refino de petróleo e coquerias',
    19: 'Fabricação de biocombustíveis',
    20: 'Fabricação de químicos orgânicos e inorgânicos, resinas e elastômeros',
    21: 'Fabricação de defensivos, desinfestantes, tintas e químicos diversos',
    22: 'Fabricação de produtos de limpeza, cosméticos/perfumaria e higiene pessoal',
    23: 'Fabricação de produtos farmoquímicos e farmacêuticos',
    24: 'Fabricação de produtos de borracha e de material plástico',
    25: 'Fabricação de produtos de minerais não metálicos',
    26: 'Produção de ferro gusa/ferroligas, siderurgia e tubos de aço sem costura',
    27: 'Metalurgia de metais não ferosos e a fundição de metais',
    28: 'Fabricação de produtos de metal, exceto máquinas e equipamentos',
    29: 'Fabricação de equipamentos de informática, produtos eletrônicos e ópticos',
    30: 'Fabricação de máquinas e equipamentos elétricos',
    31: 'Fabricação de máquinas e equipamentos mecânicos',
    32: 'Fabricação de automóveis, caminhões e ônibus, exceto peças',
    33: 'Fabricação de peças e acessórios para veículos automotores',
    34: 'Fabricação de outros equipamentos de transporte, exceto veículos automotores',
    35: 'Fabricação de móveis e de produtos de indústrias diversas',
    36: 'Manutenção, reparação e instalação de máquinas e equipamentos',
    37: 'Energia elétrica, gás natural e outras utilidades',
    38: 'Água, esgoto e gestão de resíduos',
    39: 'Construção',
    40: 'Comércio por atacado e varejo',
    41: 'Transporte terrestre',
    42: 'Transporte aquaviário',
    43: 'Transporte aéreo',
    44: 'Armazenamento, atividades auxiliares dos transportes e correio',
    45: 'Alojamento',
    46: 'Alimentação',
    47: 'Edição e edição integrada à impressão',
    48: 'Atividades de televisão, rádio, cinema e gravação/edição de som e imagem',
    49: 'Telecomunicações',
    50: 'Desenvolvimento de sistemas e outros serviços de informação',
    51: 'Intermediação financeira, seguros e previdência complementar',
    52: 'Atividades imobiliárias',
    53: 'Atividades jurídicas, contábeis, consultoria e sedes de empresas',
    54: 'Serviços de arquitetura, engenharia, testes/análises técnicas e P & D',
    55: 'Outras atividades profissionais, científicas e técnicas',
    56: 'Aluguéis não imobiliários e gestão de ativos de propriedade intelectual',
    57: 'Outras atividades administrativas e serviços complementares',
    58: 'Atividades de vigilância, segurança e investigação',
    59: 'Administração pública, defesa e seguridade social',
    60: 'Educação pública',
    61: 'Educação privada',
    62: 'Saúde pública',
    63: 'Saúde privada',
    64: 'Atividades artísticas, criativas e de espetáculos',
    65: 'Organizações associativas e outros serviços pessoais',
    66: 'Serviços domésticos'
}

class MIPCalculator:
    def __init__(self, mip_file, tru_file):
        self.mip_file = mip_file
        self.tru_file = tru_file
        self.V = None
        self.D = None
        self.L = None
        self.L_plus = None
        self.share_impostos = None
        self.precos_mercado = None
        self.W = None
        self.RMB = None
        self.Imp_ou_sub = None
        self.total_importacao = None
        self.detalhes_importacao = None
        self.impostos_detalhados = None

        self.precos_basicos = None
        self.load_data()

    def load_data(self):
        # Carregar dados da MIP
        self.V = pd.read_excel(self.mip_file, sheet_name='Recursos', skiprows=5, skipfooter=4, usecols=range(11, 78), header=None).transpose().to_numpy()
        Imp = pd.read_excel(self.mip_file, sheet_name='Recursos', skiprows=5, skipfooter=4, usecols=[8], header=None).to_numpy()
        Un = pd.read_excel(self.mip_file, sheet_name='Usos Nacional', skiprows=5, skipfooter=4, usecols=range(2, 69), header=None).to_numpy()
        Fn = pd.read_excel(self.mip_file, sheet_name='Usos Nacional', skiprows=5, skipfooter=4, usecols=range(70, 76), header=None).to_numpy()
        Um = pd.read_excel(self.mip_file, sheet_name='Usos Importado', skiprows=5, skipfooter=4, usecols=range(2, 69), header=None).to_numpy()
        Fm = pd.read_excel(self.mip_file, sheet_name='Usos Importado', skiprows=5, skipfooter=4, usecols=range(70, 76), header=None).to_numpy()
        Impostos_Detalhados = pd.read_excel(self.mip_file, sheet_name='Recursos', skiprows=5, skipfooter=4, usecols=range(5, 9), header=None).to_numpy()

        # Carregar dados da TRU
        planilha = pd.read_excel(self.tru_file, sheet_name='VA', skiprows=5, skipfooter=4, usecols=range(1, 69), header=None)
        self.W = planilha.loc[1, :].to_numpy()
        self.RMB = planilha.loc[8, :].to_numpy()
        Out_Imp = planilha.loc[10, :].to_numpy()
        Sub = planilha.loc[11, :].to_numpy()
        self.Imp_ou_sub = Out_Imp + Sub

        # Agregar dados
        agg_68_67 = np.concatenate((np.eye(67, 41), np.concatenate((np.zeros((40, 27)), np.eye(27, 27)))), axis=1)
        self.W = np.matmul(agg_68_67, self.W.transpose())
        self.RMB = np.matmul(agg_68_67, self.RMB.transpose())
        self.Imp_ou_sub = np.matmul(agg_68_67, self.Imp_ou_sub.transpose())

        # Calcular market share
        g = np.matmul(self.V, np.ones(self.V.shape[1]))
        q = np.matmul(np.ones(self.V.shape[0]), self.V)
        self.D = np.matmul(self.V, np.linalg.inv(np.diag(q)))

        # Calcular coeficientes técnicos
        Bn = np.matmul(Un, np.linalg.inv(np.diag(g)))
        A = np.matmul(self.D, Bn)
        self.L = np.linalg.inv(np.eye(A.shape[0]) - A)

        Bm = np.matmul(Um, np.linalg.inv(np.diag(g)))
        A_plus = np.matmul(self.D, Bn + Bm)
        self.L_plus = np.linalg.inv(np.eye(A_plus.shape[0]) - A_plus)

        # Calcular impostos
        self.impostos_detalhados = Impostos_Detalhados
        self.share_impostos = np.matmul(self.D, Impostos_Detalhados)

        self.precos_mercado = pd.read_excel(self.mip_file,sheet_name='Recursos',skiprows=5,skipfooter=4,usecols=[2],header=None)
        self.precos_mercado = self.precos_mercado[2]
        self.precos_mercado = np.matmul(self.D,self.precos_mercado)

        self.precos_basicos = pd.read_excel(self.mip_file,sheet_name='Recursos',skiprows=5,skipfooter=4,usecols=[78],header=None)    
        self.precos_basicos = self.precos_basicos[78]
        self.precos_basicos = np.matmul(self.D,self.precos_basicos)

        self.detalhes_importacao = pd.read_excel(self.mip_file,sheet_name='Recursos',skiprows=5,skipfooter=4,usecols=[78,79],header=None)
        self.detalhes_importacao['Participação Importação'] =self.detalhes_importacao[79]/(self.detalhes_importacao[78]+self.detalhes_importacao[79])
        self.detalhes_importacao['Participação Importação']=self.detalhes_importacao['Participação Importação']*100

        self.total_importacao = np.matmul(self.D,self.detalhes_importacao[79])



    def calcular_precos(self,indice_produto, aumento_imposto=0.1, participacao_produto=0.3,precos_basicos=False):
        # Alterar impostos
        Impostos_Detalhados_alterados = self.impostos_detalhados.copy()
        
        Impostos_Detalhados_alterados[indice_produto, 0] *= (1.0 + aumento_imposto * participacao_produto)
        Impostos_Detalhados_alterados = np.matmul(self.D, Impostos_Detalhados_alterados)
        preco_referencia = self.precos_basicos if precos_basicos else self.precos_mercado
        # Calcular custos antes e depois do aumento de impostos
        custo = self.W + self.share_impostos.sum(axis=1) + self.RMB + self.Imp_ou_sub + self.total_importacao
        custo = np.divide(custo, preco_referencia)
        preco_antes = np.matmul(self.L_plus, custo)

        custo_alterado = self.W + Impostos_Detalhados_alterados.sum(axis=1) + self.RMB + self.Imp_ou_sub + self.total_importacao
        custo_alterado = np.divide(custo_alterado, preco_referencia)
        preco_depois = np.matmul(self.L_plus, custo_alterado)

        return preco_antes, preco_depois

    def calculate_differences(self, preco_antes, preco_depois):
        # Calcular diferenças absolutas
        difference = 100*(preco_depois - preco_antes)/ preco_antes
        return difference

    def show_top_differences(self, difference, top_n=5):
        # Identificar setores com maiores diferenças
        max_diff_positions = np.argsort(difference.ravel())[::-1]
        print("Setores com as maiores diferenças:")
        for i in range(top_n):
            setor = max_diff_positions[i]
            print(setor)
            valor_diferenca = difference[setor]
            print(f"Setor {dict_setores[setor]}: Diferença = {valor_diferenca:.2f}")