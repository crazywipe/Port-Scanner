"""
Script per il port_scanning TCP
"""
import socket
from datetime import datetime

def scelta_porte(porte_da_esaminare):
    """Chiediamo all'utente le porte da esaminare e le immaganizzeremo in un lista """
    while True:

        try:
            porta = int(input('Inserisci una porta per la scansione '))
            porte_da_esaminare.append(porta)
            altra_porta = input('Vuoi inserire un altra porta? S/N ')
            if altra_porta.lower()[0] != 's':
                break
        except:
            print('Errore, inserire una porta corretta.')


    if len(porte_da_esaminare) < 20:
        print('\nEsamineremo le seguenti porte:')
        for porta in porte_da_esaminare:
            print(porta)

    return porte_da_esaminare

def continua_programma():
    """ Chiede se si vuole continuare ad utilizzare il programma """ 
    continua = input('Vuoi effettuare un altro scan? S/N ')
    if continua.lower()[0] != 's':
        print('\nProgramma Terminato.\nGrazie per aver usato PortScanner.')
        return False
    return True

def tipo_di_scan():
    """ Funzione di scelta del tipo di portscanning"""
    while True:
        try:
            prompt = '\nPer favore scegliere la modalità di esecuzione del port scanning:\n'
            prompt += '\nCUSTOM SCAN: premi tasto 1. Consigliato, più veloce.'
            prompt += '\nFULL SCAN: premi tasto 2. Molto Lento, scan su tutte le porte.\n'
            scelta = int(input(prompt))
            if (scelta == 1) or (scelta == 2):
                return scelta
            print('\nErrore, perfavore effettuare una scelta corretta.')
        except:
            print('\nErrore, perfavore effettuare una scelta corretta.')


def sito_bersaglio():
    """ Chiediamo l'inserimento di un indirizzo e risolviamo il suo IP """
    while True:
        try:
            obiettivo = input('Inserire un indirizzo web per lo scan ')
            ip = socket.gethostbyname(obiettivo)
            print(f'\nIl port scanning verrà eseguito su seguente indirizzo IP: {ip}')
            return ip
        except:
            print('\nErrore, controllare che i dati inseriti siano corretti')


def scan(porte_da_esaminare):
    """ La funzione riceve una lista di porte da esaminare e ritorna il risultato """   
    try:
        print('\nSCANNING INIZIATO, attendere prego...\n')
        ora_inizio = datetime.now()
        for port in porte_da_esaminare:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0)
            risultato = sock.connect_ex((ip, port))
            if risultato == 0:
                print(f'Porta {port} Aperta')
                sock.close()
            else:
                print(f'Porta {port} Chiusa')
    except:
        print('Errore')

    ora_fine = datetime.now()
    tempo_trascorso = ora_fine - ora_inizio
    print(f'\nSCANNING TERMINATO\nTempo totale scansione: {tempo_trascorso}')

def crea_porte(porte_da_esaminare):
    """ crea una lista con 1099 porte per full scan """
    for porta in range(1, 1100):
        porte_da_esaminare.append(porta)

#MAIN
if __name__ == "__main__":
    print("\n"*100)
    print('\n ***Benvenuto a PortScanner by Fabio Rocco***\nProgramma per solo scopo educativo\n')
    print('Il programma effettuerà lo scanning TCP delle porte selezionate.')

    while True:

        porte_da_esaminare = []

        scansione = tipo_di_scan()

        ip = sito_bersaglio()
        
        if scansione == 1:
            scelta_porte(porte_da_esaminare)
            
        if scansione == 2:
            crea_porte(porte_da_esaminare)

        scan(porte_da_esaminare)

        if continua_programma() == False:
            break
