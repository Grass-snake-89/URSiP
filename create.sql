DROP TABLE data;

CREATE TABLE IF NOT EXISTS data(
	row_id INTEGER,
   	row_date DATE,
	company VARCHAR(10),
	status VARCHAR(10),
	record_type VARCHAR(10),
	data_type VARCHAR(10),
	data_value INTEGER
);
