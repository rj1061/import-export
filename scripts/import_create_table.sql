create table imports(
  import_id INT(16) AUTO_INCREMENT PRIMARY KEY,
  unit_quantity_code VARCHAR(100),
  location_state VARCHAR(20),
  customs_tariff_heading INT(16),
  value_of_goods_in_rupees DOUBLE,
  quantity_desc VARCHAR(100),
  description_of_goods VARCHAR(250),
  location_code VARCHAR(25),
  quantity_type VARCHAR(10),
  date DATE,
  location_name VARCHAR(25),
  type VARCHAR(25),
  port_or_country_of_origin VARCHAR(50),
  quantity INT(16),
  serialid INT(16)
)
