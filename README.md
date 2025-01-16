# Tabook - Web App per la Prenotazione Tavoli

Tabook è un'applicazione web per la gestione delle prenotazioni dei tavoli di un ristorante. Consente agli utenti di prenotare un tavolo online e agli amministratori di monitorare le prenotazioni attraverso una dashboard amministrativa.

## Tecnologie Utilizzate

- **Backend**: 
  - Django
  - Django REST Framework (DRF)
  - Python
- **Frontend**: 
  - React
  - Bootstrap
- **Database**: 
  - SQLite (per lo sviluppo)

## Funzionalità

### Per gli utenti:
- **Prenotazione di un tavolo**: Gli utenti possono prenotare un tavolo attraverso un form che include il nome, l'e-mail, la data, l'orario e il numero di persone.

### Per gli amministratori:
- **Dashboard Admin**: Una pagina per monitorare le prenotazioni effettuate e visualizzare:
  - Il numero di tavoli totali, prenotati e disponibili.
  - Un elenco delle prenotazioni effettuate con informazioni su nome, email, data, orario e numero di persone.

## Installazione

### Prerequisiti

Assicurati di avere i seguenti strumenti installati:

- **Python 3.x**
- **Node.js**
- **npm**

### Backend (Django)

1. Clona il repository:

   ```bash
   git clone https://github.com/tuo-username/tabook.git
   cd tabook/tabook_backend
