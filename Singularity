Bootstrap: docker
From: python:3.7

# sudo singularity build trumpbot.sif Singularity

%setup
    echo "Adding code to container."
    mkdir -p "${SINGULARITY_ROOTFS}/code"
    cp -R . "${SINGULARITY_ROOTFS}/code"

%post
apt-get update && \
    apt-get install -y python-numpy && \
    mkdir -p /code

cd /code
pip install -r requirements.txt

%runscript
    exec python /code/trumpbot.py "$@"
