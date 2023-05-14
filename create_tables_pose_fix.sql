CREATE TABLE Users (
	user_id INT NOT NULL UNIQUE,
	username VARCHAR(60) NOT NULL UNIQUE,
	pass VARCHAR(60),
	created_at DATE,
	updated_at DATE
);

CREATE TABLE User_Admin (
	user_admin_id INT NOT NULL UNIQUE,
	user_id INT NOT NULL UNIQUE,
	admin_id INT NOT NULL UNIQUE
);

CREATE TABLE Admin (
	admin_id INT NOT NULL UNIQUE,
	admin_name ENUM ('Admin',
		'User') NOT NULL
);