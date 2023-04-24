/*Creating Suppliers table*/
CREATE TABLE suppliers (
    supplier_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    contact VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(50) NOT NULL
);

INSERT INTO suppliers (name, contact, phone, email)
VALUES ('ABC Supplier', 'John Smith', '1234567890', 'john@abcsupplier.com'),
       ('XYZ Supplier', 'Jane Doe', '0987654321', 'jane@xyzsupplier.com'),
       ('123 Supplier', 'Jack Black', '5551234567', 'jack@123supplier.com');
       

/*Creating Customers table */
CREATE TABLE customers (
    customer_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL, 
    lastname VARCHAR(50) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(50) NOT NULL
);

INSERT INTO customers (firstname, lastname, phone, email)
VALUES  ('Andrew', 'Smith', '123456789', 'andrew@smith.com'),
	('Pamela', 'Banks', '098563816', 'pamela@banks.com'),
        ('Erika', 'Larsson', '1356738291', 'erika@larsson.com');
 
/*Creating Products table*/
CREATE TABLE products (
    product_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10,2) NOT NULL,
    warranty INT NOT NULL,
    supplier_id INT UNSIGNED,
    category VARCHAR(50) NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

INSERT INTO products (name, description, price, warranty, supplier_id, category)
VALUES ('Laptop', '15-inch laptop with Intel Core i5 processor', 899.99, 2, 1, 'Laptops and notebooks'),
       ('Desktop PC', 'Powerful desktop PC with AMD Ryzen 7 processor', 1299.99, 3, 2, 'Computers'),
       ('Windows 10', 'Operating system for PCs', 139.99, 1, 3, 'OS and Software');

/*Creating Orders table*/
CREATE TABLE orders (
    order_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(50) NOT NULL,
    customer_id INT UNSIGNED, 
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders (status, customer_id)
VALUES ('ENTERED', 123),
       ('IN PROCESSING', 124),
       ('DELIVERED', 125);
       
/*Creating Ordered products table*/
CREATE TABLE ordered_products (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    order_id INT UNSIGNED,
    product_id INT UNSIGNED, 
    amount INT UNSIGNED,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO ordered_products (order_id, product_id, amount)
VALUES (1,2,1),
       (2,3,2),
       (3,1,2);

/* Updating a record */
SELECT * FROM products; 
UPDATE products SET price = 799.99 WHERE product_id = 1;

/*Deleting a record*/
SELECT * FROM ordered_products; 
DELETE FROM ordered_products WHERE id = 1;


/*Simple SQL Statement*/
SELECT order_id FROM orders
WHERE status = 'IN PROCESSING'; 

/*Advanced SQL Statement*/
SELECT p.name AS product_name, p.price, op.amount
FROM ordered_products op
JOIN products p ON op.product_id = p.product_id
JOIN orders o ON op.order_id = o.order_id
WHERE o.customer_id = 125;


