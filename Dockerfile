# Step 1: Use an official Python runtime as a base image
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED=1

# Step 3: Set the working directory
WORKDIR /app

# Step 4: Copy the current directory contents into the container
COPY . /app

# Step 5: Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Expose port 5000 to the outside world
EXPOSE 5000

# Step 7: Run the Flask app
CMD ["python3", "app.py"]
