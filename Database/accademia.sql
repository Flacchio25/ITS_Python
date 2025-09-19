create type Strutturato as
    enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as
    enum ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');

create type LavoroNonProgettuale as
    enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro
Accademico', 'Altro');

create type CausaAssenza as
    enum ('Chiusura Universitaria', 'Maternita', 'Malattia');

create domain PosInteger as Integer 
    check (value >0);

create domain StringaM as varchar(100);

create domain NumeroOre as Integer
    check ( value between 0 and 8);

create domain Denaro as Real
    check (value >= 0);


create table Persona (
    id PosIntegernome PRIMARY KEY
    nome StringaM
    cognome StringaM
    posizione Strutturato
    stipendio Denaro
);

create table Progetto (
    id PosInteger PRIMARY KEY,
    nome StringaM UNIQUE, -- [VincoloDB.1] altra chiave: (nome)
    inizio DATE,
    fine DATE,
    budget Denaro,
    CHECK (inizio < fine) -- [VincoloDB.2] ennupla: inizio < fine
);

create table WP (
    progetto PosInteger,
    id PosInteger,
    nome StringaM,
    inizio DATE,
    fine DATE,
    PRIMARY KEY (progetto, id),
    UNIQUE (progetto, nome), --[VincoloDB.4] altra chiave: (progetto, nome)
    FOREIGN KEY (progetto) REFERENCES Progetto(id), -- [VincoloDB.5] foreign key: progetto references Progetto(id)
    CHECK (inizio < fine) -- [VincoloDB.3] ennupla: inizio < fine
);

CREATE TABLE AttivitaProgetto (
    id PosInteger PRIMARY KEY,
    persona PosInteger,
    progetto PosInteger,
    wp PosInteger,
    giorno DATE,
    tipo LavoroProgetto,
    oreDurata NumeroOre,
    FOREIGN KEY (persona) REFERENCES Persona(id), -- [VincoloDB.6] foreign key: persona references Persona(id) [cite: 82]
    FOREIGN KEY (progetto, wp) REFERENCES WP(progetto, id) -- [VincoloDB.7] foreign key: (progetto, wp) references WP(progetto, id) [cite: 83]
);

-- Tabella AttivitaNonProgettuale [cite: 84]
CREATE TABLE AttivitaNonProgettuale (
    id PosInteger PRIMARY KEY,
    persona PosInteger,
    tipo LavoroNonProgettuale,
    giorno DATE,
    oreDurata NumeroOre,
    FOREIGN KEY (persona) REFERENCES Persona(id) -- [VincoloDB.8] foreign key: persona references Persona(id) [cite: 85]
);

-- Tabella Assenza [cite: 86]
CREATE TABLE Assenza (
    id PosInteger PRIMARY KEY,
    persona PosInteger,
    tipo CausaAssenza,
    giorno DATE,
    UNIQUE (persona, giorno), -- [VincoloDB.9] altra chiave: persona, giorno 
    FOREIGN KEY (persona) REFERENCES Persona(id) -- [VincoloDB.10] foreign key: persona references Persona(id) [cite: 88]
);