CREATE TABLE IF NOT EXISTS sales_schema.sales (
    doc_id TEXT,
    item TEXT,
    category TEXT,
    amount BIGINT,
    price FLOAT(53),
    discount FLOAT(53),
    shop_num TEXT,
    cash_num TEXT
);
