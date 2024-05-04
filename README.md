# Desafio - Modelando o Sistema Bancário em POO com Python v3.2.0
Em nossa aplicação financeira, identificamos a necessidade de rastrear e auditar as ações dos usuários para garantir segurança e integridade das operações. O console tem sido útil até agora a atividade crescente ultimamente torna difícil acompanhar todas as operações em tempo real. Portanto, decidimos que é vital registrar essas informações em um arquivo para análise posterior de backup contínuo.
## Objetivo do desafio
Modificar o atual decorador de log, que imprime informações no console, para que ele salve essas informações em um arquivo de log, possivelmente uma revisão mais fácil é uma análise mais detalhada das operações dos usuários.
## Funcionalidades do Sistema
### Requisitos 
Decorador deve às seguintes para cada chamada para função.
-	Data e hora atuais 
-	Nome da função 
-	Argumentos das função
-	O valor retornado pelas função 
```
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.utcnow().strftime("%d/%m/%Y - %H:%M:%S")

        with open(ROOT_PATH / 'data-log' /'log.txt', 'a' , encoding='utf-8') as arquivo:
             arquivo.write( 
                f"[{data_hora} Função: '{func.__name__}' executadas com argumentos {args} e {kwargs}." 
                f"Retornou {resultado}\n]"
             )
        print(f'{data_hora}: {func.__name__.upper()}')

        return resultado

    return envelope
```

