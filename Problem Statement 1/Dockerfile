# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install required packages
RUN apt-get update && \
    apt-get install -y fortune cowsay && \
    apt-get clean

# Copy the script into the container
COPY wisecow.sh /app/wisecow.sh

# Make the script executable
RUN chmod +x /app/wisecow.sh

# Expose the application port
EXPOSE 4499

# Run the script
CMD ["/app/wisecow.sh"]

