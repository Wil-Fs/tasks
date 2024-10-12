# Controle de Tarefas

Web app, registra tarefas, e o tempo gasto em cada uma.

## Pré-requisitos

```
    Python 3.12.3
    Docker && Docker Compose
```

## QuickStart - Docker

1. Clonar o repositório
    
   ```shell
        git clone https://github.com/Wil-Fs/tasks.git
   ```

2. Configurar dependências 

   ```shell
        cd tasks
   ```
   2.1 Criar um .env file na raiz do projeto com as seguintes variaveis
   ```
   # No passo 2.2 estão os dados de conexão com o banco de dados
        
        #Super user   
        ADMIN_USER=          #Username do Admin no sistema
        ADMIN_PASSWORD=      #Senha para o Admin   
        ADMIN_EMAIL=         #Email para o Admin
        
        #App settings
        ALLOWED_HOSTS=       #Hosts permitidos Ex: * --permite todos
        DEBUG=               #Ativar ou não o DEBUG
            
        #Database  
        DATABASE_NAME=       #Nome do banco de dados
        DATABASE_HOST=       #Host de conexão com o banco
        DATABASE_USER=       #Usuário do banco
        DATABASE_PASSWORD=   #Senha para o banco
        DATABASE_PORT=       #Porta Ex: 5432
        TIME_ZONE=           #Define o horário local e formato das datas
   
   #Exemplo .env preenchido
      
         #Super user
         ADMIN_USER=admin
         ADMIN_PASSWORD=admin
         ADMIN_EMAIL=admin@email.com
         
         #App settings
         ALLOWED_HOSTS=*
         DEBUG=False
         
         #Database
         DATABASE_NAME=tasks_db
         DATABASE_HOST=postgres
         DATABASE_USER=postgres
         DATABASE_PASSWORD=8744821jk99ww@13
         DATABASE_PORT=5432
         TIME_ZONE=America/Sao_Paulo
   ```
   2.2 Observações sobre o compose.yaml
    ```
         services:
           postgres:                                 #Host de conexão com o banco
             image: postgres:13
             container_name: postgres
             restart: always
             environment:
               - POSTGRES_DB=tasks_db                #Nome do banco de dados
               - POSTGRES_PASSWORD=8744jk99ww@13     #Senha para o banco de dados
               - POSTGRES_USER=postgres              #Usuário do banco de dados
             ports:
               - "5432:5432"                         #Porta
             networks:
               - tasks_network                       #Network
    ```
3. Executar o app
    ```shell
        docker compose up --build
    ```
4. Após o app subir a página pode ser acessada
   ```
        https://localhost:8000/  ou  https://<ip_da_maquina>:8000/
   ```