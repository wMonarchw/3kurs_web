CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(102) NOT NULL
);

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(50),
    article_text TEXT,
    is_favorite BOOLEAN,
    is_public BOOLEAN,
    likes INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

GRANT ALL ON TABLE public.users TO zavgorodniy_knowledge_base;;
GRANT ALL ON TABLE public.articles TO zavgorodniy_knowledge_base;;
GRANT usage ON SEQUENCE users_id_seq TO zavgorodniy_knowledge_base;;
GRANT usage ON SEQUENCE articles_id_seq TO zavgorodniy_knowledge_base;;


INSERT INTO users(username, password) VALUES ('alex1', 'supersecretassword');
INSERT INTO users(username, password) VALUES ('alex2', 'supersecretassword2');
INSERT INTO users(username, password) VALUES ('alex3', 'supersecretassword3');
INSERT INTO users(username, password) VALUES ('alex4', 'supersecretassword4');

SELECT FROM users *;

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    title VARCHAR(255),
    article_text TEXT
);
