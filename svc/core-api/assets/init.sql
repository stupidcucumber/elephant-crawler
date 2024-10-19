CREATE TABLE IF NOT EXISTS scrapped_texts (
    id serial primary key,
    scrapped_text text,
    date_added timestamp
);
