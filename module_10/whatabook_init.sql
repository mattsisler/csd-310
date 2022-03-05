#Sisler - Module 10.3 Assignment
#whatabook_init.sql


-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1234 Main St, Augusta, GA 30907');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('A Time To Kill','John Grisham','A white lawyer defends a black man who killed two men who raped his daughter');

INSERT INTO book(book_name, author, details)
    VALUES('Of Mice and Men','John Steinbeck','Classic novel about the living during the Great Depression');

INSERT INTO book(book_name, author, details) 
    VALUES('Old Man and The Sea','Ernest Hemingway','Tells story of Santiago, a cuban fisherman, trying to catch a marlin');

INSERT INTO book(book_name, author,details) 
    VALUES("Charlotte's Web", 'E.B. White','Tells story of friendship between spider and pig');

INSERT INTO book(book_name, author, details) 
    VALUES('Huckleberry Finn','Mark Twain','Sequel to Tom Sawyer');

INSERT INTO book(book_name, author, details) 
    VALUES('Moby Dick','Herman Melville','Classic novel about a whale');

INSERT INTO book(book_name, author, details) 
    VALUES('Little Women','Louisa May Alcott','The story of four sisters');

INSERT INTO book(book_name, author, details)
     VALUES('Call of the Wild','Jack Landon','Sled dogs in Canada during the gold rush');

INSERT INTO book(book_name, author, details) 
    VALUES('Frankenstein','Mary Shelley','A young scientist creates a creature');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('James', 'Brown');

INSERT INTO user(first_name, last_name)
    VALUES('Lee', 'Smith');

INSERT INTO user(first_name, last_name)
    VALUES('Mark', 'Smith');

/*
    insert wishlist records 
*/

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'James'),
    (SELECT book_id FROM book WHERE book_name = 'Call of the Wild')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Lee'),
        (SELECT book_id FROM book WHERE book_name = 'Moby Dick')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Mark'),
        (SELECT book_id FROM book WHERE book_name = 'A Time To Kill')
    );
