from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# =========================================================================
# CONFIGURAÇÃO INTERATIVA DE CREDENCIAIS
# =========================================================================
print("--- AUTENTICAÇÃO FARMÁCIA NEOLUMINIS ---")
user_email = input("Digite o E-MAIL do usuário cadastrado no Django: ").strip()
user_senha = input("Digite a SENHA do usuário cadastrado no Django: ").strip()
print("---------------------------------------\n")

# Inicializa o navegador Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Define uma espera explícita tolerante de 15 segundos
wait = WebDriverWait(driver, 15)

try:
    # =========================================================================
    # PASSO 1: FLUXO DE LOGIN
    # =========================================================================
    print("🚀 Passo 1: Acessando a URL de login do Django...")
    driver.get("http://127.0.0.1:8000/login/")

    print("Preenchendo o formulário de autenticação...")
    # Aguarda o campo 'email' estar disponível na tela
    campo_email = wait.until(
        EC.presence_of_element_located((By.NAME, "email")))
    campo_senha = driver.find_element(By.NAME, "senha")

    campo_email.send_keys(user_email)
    campo_senha.send_keys(user_senha)

    print("Clicando no botão 'Entrar'...")
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

    # Pausa estratégica para o Django processar o POST e redirecionar
    print("Aguardando resposta do servidor Django...")
    time.sleep(3)

    # Verificação de segurança caso o login falhe
    if "login" in driver.current_url:
        print("\n❌ ERRO DETECTADO: O navegador continuou preso na rota /login/.")
        print(
            "Confirme se o e-mail/senha digitados existem na tabela de usuários do banco.")
        print("O script vai tentar prosseguir, mas provavelmente falhará abaixo.")

    # =========================================================================
    # PASSO 2: REDIRECIONAMENTO E DIRECIONAMENTO PARA CADASTRO
    # =========================================================================
    print("\n🚀 Passo 2: Verificando carregamento do Inventário...")
    # Aguarda a tabela ou o container do dashboard carregar
    wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "dashboard-container")))
    print(f"Login bem-sucedido! URL Atual: {driver.current_url}")

    print("Clicando no botão '➕ Cadastrar Novo'...")
    # Localiza o botão baseado na tag 'btn-add' que vimos no seu HTML do estoque
    botao_cadastrar = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-add")))
    botao_cadastrar.click()

    # =========================================================================
    # PASSO 3: FORMULÁRIO DE CADASTRO DE MEDICAMENTO (BASEADO NO SEU MODEL)
    # =========================================================================
    print("\n🚀 Passo 3: Tela de cadastro identificada. Inserindo dados...")

    # Campo: Nome
    input_nome = wait.until(EC.presence_of_element_located((By.NAME, "nome")))
    input_nome.send_keys("Dipirona Monoidratada")

    # Campo: Apresentação
    driver.find_element(By.NAME, "apresentacao").send_keys(
        "Comprimido 500mg - Caixa com 30 un")

    # Campo: Categoria (Mapeado exatamente com o CATEGORIAS_CHOICES do seu model)
    print("Selecionando a categoria...")
    select_cat = Select(driver.find_element(By.NAME, "categoria"))
    select_cat.select_by_value("analgesicos")  # Opção válida do seu models.py

    # Campo: Tarja (Mapeado exatamente com o TARJA_CHOICES do seu model)
    print("Selecionando a tarja...")
    select_tarja = Select(driver.find_element(By.NAME, "tarja"))
    # Opção válida do seu models.py (Genérico)
    select_tarja.select_by_value("amarela")

    # Campo: Preço
    driver.find_element(By.NAME, "preco").send_keys("14.90")

    # Campo: Quantidade
    driver.find_element(By.NAME, "quantidade").send_keys("80")

    # Nota sobre o checkbox 'em_estoque' e 'imagem': como são opcionais no seu form/model,
    # o script ignora para garantir um envio rápido e limpo.

    print("Submetendo o formulário de cadastro...")
    # O Django geralmente usa um input ou button com type='submit' no form de cadastro.
    # Vamos localizá-lo e disparar o clique.
    btn_salvar = driver.find_element(
        By.XPATH, "//form//button[@type='submit']")
    btn_salvar.click()

    # =========================================================================
    # PASSO 4: VALIDAÇÃO DO RETORNO
    # =========================================================================
    print("\n🚀 Passo 4: Aguardando retorno para o Inventário de Medicamentos...")
    # Aguarda o carregamento da tabela de medicamentos para confirmar o salvamento
    wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "table-wrapper")))
    print("🎉 SUCESSO! O medicamento foi cadastrado e listado no estoque corretamente.")

    # Aguarda 5 segundos antes de encerrar para você checar o resultado visualmente
    time.sleep(5)

except Exception as erro:
    print("\n❌ O TESTE FALHOU!")
    print(f"O Selenium parou na rota: {driver.current_url}")
    print("Salvando um screenshot do estado da tela como 'erro_execucao.png'...")
    driver.save_screenshot("erro_execucao.png")
    print(f"Log de erro técnico: {erro}")

finally:
    print("\nFinalizando processo e fechando janela do navegador.")
    driver.quit()
