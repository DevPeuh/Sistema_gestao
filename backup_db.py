import os
import subprocess
from datetime import datetime

def backup_postgresql():
    db_name = os.environ.get('DATABASE_URL').split('/')[-1]
    backup_filename = f"backup_{db_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    
    print(f"Iniciando backup de {db_name}...")
    
    try:
        # Comando pg_dump
        # Nota: DATABASE_URL deve estar configurada no ambiente
        command = f"pg_dump {os.environ.get('DATABASE_URL')} > {backup_filename}"
        subprocess.run(command, shell=True, check=True)
        print(f"Backup concluído: {backup_filename}")
        
        # TODO: Implementar upload para Google Drive via API
        # Requer google-api-python-client e credenciais
        print("Upload para Google Drive (Simulado)")
        
        # Limpeza local
        # os.remove(backup_filename)
        
    except Exception as e:
        print(f"Erro no backup: {e}")

if __name__ == "__main__":
    backup_postgresql()
