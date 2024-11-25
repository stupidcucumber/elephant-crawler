CREATE TABLE IF NOT EXISTS scrapped_texts (
    id serial primary key,
    link text,
    source text,
    lang text,
    author text,
    header text,
    scrapped_text text,
    date_added timestamp
);
