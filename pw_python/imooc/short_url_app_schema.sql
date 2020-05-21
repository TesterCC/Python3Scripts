-- for generate short_url_app.py mysql database, testdb -> short_url table
CREATE TABLE short_url(
  id bigint unsigned NOT NULL AUTO_INCREMENT,
  token varchar(10),
  url varchar(2048),
  create_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_token` (`token`)
);