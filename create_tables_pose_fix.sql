CREATE TABLE user_login (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_videos (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES user_login(id),
  title VARCHAR(100) NOT NULL,
  description TEXT,
  video_path VARCHAR(255) NOT NULL,
  created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);