# Use a base image
FROM ubuntu:latest

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    libasound2 \
    libatk1.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxtst6 \
    tigervnc-standalone-server \
    x11vnc \
    xvfb \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Download and install the browser (example: Brave)
RUN curl -sSL https://brave-browser-apt-release.s3.brave.com/brave-core.asc | apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
RUN echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | tee /etc/apt/sources.list.d/brave-browser-release.list
RUN apt-get update && apt-get install -y brave-browser

# Set up the VNC server
ENV DISPLAY=:1
ENV VNC_RESOLUTION=1280x720
RUN Xvfb $DISPLAY -screen 0 $VNC_RESOLUTION -ac +extension RANDR && \
    x11vnc -display $DISPLAY -rfbport 5900 -rfbauth /root/.vnc/passwd -noxdamage -wait 5 -shared -forever && \
    mkdir -p /root/.vnc && \
    x11vnc -storepasswd secret /root/.vnc/passwd

# Set up a user to run the browser (optional but recommended for security reasons)
RUN useradd -m browser-user
USER browser-user

# Set the entry point to start the browser and VNC server
ENTRYPOINT ["brave-browser-stable"]
