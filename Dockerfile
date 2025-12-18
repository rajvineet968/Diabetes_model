# 1️⃣ Base image (Python)
FROM python:3.10-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy requirements file
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy entire project
COPY . .

# 6️⃣ Default command
CMD ["bash"]
