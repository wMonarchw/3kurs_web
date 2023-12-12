CREATE USER admin_knowledge_base_orm WITH PASSWORD '123';
CREATE DATABASE knowledge_base_orm WITH OWNER admin_knowledge_base_orm;





INSERT INTO users (username, password) VALUES ('alex', 123);
INSERT INTO users (username, password) VALUES ('alex2', 12354);
INSERT INTO users (username, password) VALUES ('alex3', 12333);
INSERT INTO users (username, password) VALUES ('alex4', 12321);
INSERT INTO users (username, password) VALUES ('alex5', 12312);
select * from articles;
select * from users;
INSERT INTO articles (user_id, title, article_text) VALUES (1, 'Книги 33', 'это 32 книги как сделать что-то');
INSERT INTO articles (user_id, title, article_text) VALUES (2, 'Программирование', 'как кодить на питоне? научите');
INSERT INTO articles (user_id, title, article_text) VALUES (2, 'Не знаю?', 'ну серьезно не знаю');
