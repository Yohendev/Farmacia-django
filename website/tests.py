from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("http://127.0.0.1:8000/login/")
time.sleep(2)

btn_criar_conta = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Criar agora")))
btn_criar_conta.click()
time.sleep(2)

input_nome = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Nome Completo']")))
input_nome.send_keys("Novo Operador 10")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@placeholder='E-mail']").send_keys("operador10@neoluminis.com")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@placeholder='Telefone']").send_keys("81999999999")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@placeholder='Senha']").send_keys("SenhaSegura2026!")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@placeholder='Confirmar Senha']").send_keys("SenhaSegura2026!")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(4)

btn_novo = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Cadastrar Novo")))
btn_novo.click()
time.sleep(2)

input_remedio = wait.until(EC.presence_of_element_located((By.NAME, "nome")))
input_remedio.send_keys("Dipirona Monoidratada 500mg")
time.sleep(1)

wait.until(EC.presence_of_element_located((By.NAME, "apresentacao"))).send_keys("Indicado para dor e febre.")
time.sleep(1)

select_categoria = Select(wait.until(EC.presence_of_element_located((By.NAME, "categoria"))))
select_categoria.select_by_index(1) 
time.sleep(1)

select_tarja = Select(wait.until(EC.presence_of_element_located((By.NAME, "tarja"))))
select_tarja.select_by_index(1)
time.sleep(1)

wait.until(EC.presence_of_element_located((By.NAME, "preco"))).send_keys("12.50")
time.sleep(1)

wait.until(EC.presence_of_element_located((By.NAME, "quantidade"))).send_keys("150")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)
driver.quit()