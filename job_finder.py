
import os
from jobspy import scrape_jobs
import requests
import time
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

locais = ["Belém, PA", "Remote"]
termos = [
    "Estágio Desenvolvimento",
    "Estágio TI",
    "Desenvolvedor Junior"
]

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    data = {"chat_id": CHAT_ID, "text": mensagem}
    
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"❌ Erro do Telegram: {response.text}")
        else:
            print("✅ Mensagem enviada para o Telegram!")
    except Exception as e:
        print(f"Erro de conexão: {e}")

def buscar_vagas():
    print("--- Iniciando Varredura ---")
    
    for local in locais:
        for termo in termos:
            print(f"🔎 Buscando: '{termo}' em '{local}'...")
            
            try:
                jobs = scrape_jobs(
                    site_name=["linkedin", "indeed", "glassdoor"],
                    search_term=termo,
                    location=local,
                    results_wanted=3, 
                    hours_old=24,
                    country_indeed='Brazil'
                )
                
                if not jobs.empty:
                    print(f"Encontradas {len(jobs)} vagas.")
                    for index, row in jobs.iterrows():
                        msg = f"NOVA VAGA ENCONTRADA!\n\n" \
                              f"Cargo: {row['title']}\n" \
                              f"Empresa: {row['company']}\n" \
                              f"Local: {row['location']}\n" \
                              f"Link: {row['job_url']}"
                        
                        enviar_telegram(msg)
                        time.sleep(1)
                else:
                    print(f"Zero vagas para {termo}.")
                
                time.sleep(5) 

            except Exception as e:
                print(f"Erro na busca: {e}")

if __name__ == "__main__":
    buscar_vagas()