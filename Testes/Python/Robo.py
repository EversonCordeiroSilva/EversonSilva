import xlsxwriter
from selenium import webdriver
import os

class teste_BPA:
    def __init__(self):
        self.__pesquisado = ''
        self.__chrome_options = webdriver.ChromeOptions()
        self.__chrome_options.add_argument("--start-maximized")
        self.__caminho_webdriver = r'C:\chromedriver\chromedriver.exe'
        self.__link_pesquisa = 'https://www.amazon.com.br/'
        self.__lista = []
        self.__nome = []
        self.__preco = []
        self.__descricao = []
        self.__CAIXA_DE_BUSCA = 'twotabsearchtextbox'
        self.__XPATH_ALL_HREF = "//a[@class='a-link-normal a-text-normal'][@href]"
        self.__XPATH_NOME_ITEM = "//span[@id='productTitle']"
        self.__XPATH_PRECO_ITEM = "//span[@id='priceblock_ourprice']"
        self.__XPATH_DESCRI_ITEM = "//*[@dir='ltr']/body/div/div/div/div"
        self.__XPATH_IFRAME = "//*[@id='product-description-iframe']"
        self.__PASTA = r'C:\dados'


    def pesquisaBonita(self, pesquisado):
        try:
            # Buscando o ChromeDriver no meu diretório do Chrome.
            self.__pesquisado = pesquisado
            driver = webdriver.Chrome(
                self.__caminho_webdriver, chrome_options=self.__chrome_options)
            # Acessar
            driver.get(self.__link_pesquisa)
            # Buscar
            search_box = driver.find_element_by_id(self.__CAIXA_DE_BUSCA)
            search_box.send_keys(self.__pesquisado)
            search_box.submit()
            # Salvando Lista De Itens na pagina
            for link in driver.find_elements_by_xpath(self.__XPATH_ALL_HREF):
                self.__lista.append(link.get_attribute('href'))
            # Salvando todas as informações em uma variavel
            for cont in range(len(self.__lista)):
                # Acessar
                driver.get(self.__lista[cont])
                # Nome
                nome = driver.find_element_by_xpath(self.__XPATH_NOME_ITEM)
                self.__nome.append(nome.text)
                # Preço
                try:
                    preco = driver.find_element_by_xpath(self.__XPATH_PRECO_ITEM)
                    self.__preco.append(preco.text)
                except Exception:
                    self.__preco.append('Indisponivel/Não Encontrado')
                # Descricao
                try:
                    iframe = driver.find_element_by_xpath(self.__XPATH_IFRAME)
                    driver.switch_to.frame(iframe)
                    descri = driver.find_element_by_xpath(self.__XPATH_DESCRI_ITEM)
                    self.__descricao.append(descri.text)
                    driver.switch_to.default_content()
                except Exception:
                    self.__descricao.append('Indisponivel/Não Encontrado')
                # FIM DO LAÇO
            # E Fechar
            driver.quit()
            # Chamar excel
            self.excel()
            return 'Pesquisa realizada com sucesso!'
        except Exception:
            # E Fechar
            driver.quit()
            # Chamar excel
            self.excel()
            return 'Um ou mais produtos não encontrado ou Com característica inválidas'

    def excel(self):
        if not os.path.exists(self.__PASTA):
            os.mkdir(self.__PASTA)
        workbook = xlsxwriter.Workbook(r'C:\dados\{0}.xlsx'.format(self.__pesquisado))
        sheet = workbook.add_worksheet()
        for linha in range(len(self.__nome)):
            sheet.write(linha, 0, self.__nome[linha])
            sheet.write(linha, 1, self.__preco[linha])
            sheet.write(linha, 2, self.__descricao[linha])
        workbook.close()


print('OBS: \n Os dados em excel será criado no caminho "C:\dados"' )
print('OBS: \n Certifique-se de que o caminho do chromedriver esteja como a seguir:\n"C:\chromedriver\chromedrive.exe"' )
busca = input('Buscar:\n')
classe = teste_BPA()
print(classe.pesquisaBonita(busca))
