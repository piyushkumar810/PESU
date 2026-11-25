
# ============================================================
#          TOP 15 DOCKER INTERVIEW QUESTIONS & ANSWERS
#               Data Engineer - Internship / Fresher
# ============================================================


# Q1. What is Docker?

'''
Docker is an open-source platform used to build, package, and run
applications inside isolated environments called containers.

It packages application code, libraries, dependencies, and runtime
into a container so that the application works consistently
across different environments.

Advantages:
1. Environment consistency.
2. Application portability.
3. Dependency management.
4. Faster deployment.
5. Application isolation.

Example:
A Python application developed on my laptop can run on another
computer using Docker without manually installing all dependencies.
'''


# Q2. What is Containerisation?

'''
Containerisation is the process of packaging an application
and its dependencies into an isolated unit called a container.

Containers share the host operating system kernel but maintain
isolated process environments.

Advantages:
1. Lightweight.
2. Fast startup.
3. Portability.
4. Efficient resource utilisation.
5. Consistent execution environment.

Example:
I can package a Python application with its required libraries
and run it consistently on different systems.
'''


# Q3. What is the difference between Docker and Virtual Machine?

'''
DOCKER CONTAINER:

1. Shares the host operating system kernel.
2. Lightweight.
3. Starts quickly.
4. Uses comparatively fewer resources.
5. Isolates application processes and dependencies.

VIRTUAL MACHINE:

1. Runs a complete guest operating system.
2. Requires a hypervisor.
3. Is comparatively heavier.
4. Takes more time to start.
5. Usually consumes more resources.

Conclusion:
Containers virtualise the operating system environment,
whereas Virtual Machines virtualise hardware through a hypervisor.
'''


# Q4. What is a Docker Image?

'''
A Docker Image is a read-only template used to create Docker containers.

It contains:
1. Application code.
2. Runtime environment.
3. Required libraries.
4. Dependencies.
5. Configuration.

A Docker Image is generally built using a Dockerfile.

Important points:
- Images are made up of layers.
- Images are generally immutable.
- Multiple containers can be created from one image.

Example:
A Python image can be used to create multiple Python containers.
'''


# Q5. What is a Docker Container?

'''
A Docker Container is an isolated, runnable instance of a Docker Image.

It provides an environment in which an application executes.

A container has:
1. Its own process environment.
2. An isolated filesystem view.
3. Networking configuration.
4. A writable container layer.

A container can be:
- Created.
- Started.
- Stopped.
- Restarted.
- Deleted.

Example:
If a Python image is used to run a Python application,
the resulting running instance is called a container.
'''


# Q6. What is the difference between Docker Image and Docker Container?

'''
DOCKER IMAGE:

1. It is a template used to create containers.
2. It is generally read-only.
3. Contains application code and dependencies.
4. Created using a Dockerfile.
5. Multiple containers can be created from one image.

DOCKER CONTAINER:

1. It is an instance of an image.
2. Provides an isolated runtime environment.
3. Executes the application.
4. Has a writable container layer.
5. Can be started, stopped, and deleted.

Example:

Image = Blueprint or template.
Container = Instance created from that template.

One Docker Image can create multiple containers.
'''


# Q7. What is a Dockerfile?

'''
A Dockerfile is a text file containing instructions used
to build a Docker Image.

Important Dockerfile instructions:

FROM:
Specifies the base image.

WORKDIR:
Sets the working directory inside the container.

COPY:
Copies files into the image.

RUN:
Executes commands during image building.

ENV:
Sets environment variables.

EXPOSE:
Documents the intended container port.

CMD:
Specifies the default command when the container starts.

Example:

FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
'''


# Q8. What is Docker Compose?

'''
Docker Compose is a tool used to define and manage
multi-container Docker applications.

It uses a YAML configuration file, usually named
compose.yaml or docker-compose.yml.

It allows us to manage multiple services together.

Example:

A Data Engineering application may require:
1. Python application.
2. PostgreSQL database.
3. Apache Airflow.
4. Redis.

Docker Compose allows us to define these services,
their networking, volumes, and configurations in one file.

Important commands:

docker compose up -d
Starts services in detached mode.

docker compose down
Stops and removes Compose-managed containers and networks.

docker compose ps
Displays service status.
'''


# Q9. What is the difference between Dockerfile and Docker Compose?

'''
DOCKERFILE:

1. Contains instructions to build a Docker Image.
2. Defines the application environment.
3. Specifies base image and dependencies.
4. Uses instructions like FROM, RUN, COPY and CMD.
5. Used with docker build.

DOCKER COMPOSE:

1. Manages multi-container applications.
2. Uses a YAML configuration file.
3. Defines multiple services.
4. Manages networking, volumes, and dependencies.
5. Used with docker compose up.

Example:

Dockerfile:
Defines how to build a Python application image.

Docker Compose:
Defines how to run the Python application
along with PostgreSQL and other services.

Conclusion:

Dockerfile = Builds the image.
Docker Compose = Defines and manages services.
'''


# Q10. What are Docker Volumes?

'''
Docker Volumes are used to persist data generated or used
by containers.

Normally, when a container is deleted, its writable layer
is deleted as well.

Docker Volumes store data separately from the container's
writable layer.

Advantages:
1. Data persistence.
2. Data sharing between containers.
3. Backup and recovery.
4. Separation of application and data.

Example:

If PostgreSQL runs inside a Docker container,
I can use a Docker Volume to preserve database records
even if the container is deleted.

Commands:

docker volume create mydata
docker volume ls
docker volume inspect mydata
'''


# Q11. What is the difference between Docker Volume and Bind Mount?

'''
DOCKER VOLUME:

1. Managed by Docker.
2. Stored in Docker-managed storage.
3. Useful for persistent application data.
4. Can exist independently of containers.

BIND MOUNT:

1. Connects a specific host path to a container path.
2. The host directory or file is specified explicitly.
3. Useful during development.
4. Changes can be shared between host and container.

Example:

Volume:
docker run -v mydata:/app/data myimage

Bind Mount:
docker run -v "C:/project:/app" myimage

Conclusion:

Volume = Docker-managed storage.
Bind Mount = Direct connection to a host filesystem path.
'''


# Q12. What is Docker Registry and Docker Hub?

'''
A Docker Registry is a storage and distribution system
for Docker Images.

Docker Hub is a popular cloud-based Docker Registry.

Developers can:
1. Download existing images.
2. Upload their own images.
3. Share images.
4. Maintain different image versions.

Important commands:

docker pull python:3.12-slim
Downloads an image.

docker login
Authenticates with a registry.

docker push username/myapp:v1
Uploads an image after authentication and tagging.

docker images
Lists locally available images.
'''


# Q13. What is Docker Networking?

'''
Docker Networking allows containers to communicate with
other containers, the host machine, and external networks.

Important network drivers:

1. Bridge:
   Common network type for standalone containers.
   Containers on the same user-defined bridge can communicate.

2. Host:
   Shares the host network namespace on supported systems.

3. None:
   Disables normal external container networking.

4. Overlay:
   Supports communication across multiple Docker hosts
   in supported multi-host environments.

Example:

Suppose I have:
Container 1 = Python application.
Container 2 = PostgreSQL database.

If both containers are connected to the same user-defined network,
the Python application can connect to PostgreSQL
using its container or service name.
'''


# Q14. What is Port Mapping in Docker?

'''
Port Mapping connects a port on the host machine
to a port inside a Docker container.

Syntax:

docker run -p HOST_PORT:CONTAINER_PORT image_name

Example:

docker run -p 8080:5000 myapp

Here:

8080 = Port on the host machine.
5000 = Port inside the container.

If my Flask application runs on port 5000 inside the container,
I can access it using:

http://localhost:8080

Important:

EXPOSE in Dockerfile documents the intended container port.

-p publishes the container port to the host.
'''


# Q15. What is the difference between Docker and Kubernetes?

'''
DOCKER:

Docker is a platform used to build, package, and run containers.

It helps with:
1. Building Docker Images.
2. Running containers.
3. Managing container networking.
4. Managing volumes.
5. Packaging applications.

KUBERNETES:

Kubernetes is a container orchestration platform.

It helps with:
1. Container deployment.
2. Scaling applications.
3. Scheduling workloads.
4. Self-healing.
5. Service discovery.
6. Load balancing.

Example:

Docker can package a Python data processing application.

Kubernetes can manage multiple instances of that
containerised application across a cluster.

Conclusion:

Docker focuses on building and running containers.
Kubernetes focuses on orchestrating containerised applications.
'''

# ============================================================
#                    END OF INTERVIEW NOTES
# ============================================================
