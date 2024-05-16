sudo apt install python3.8-venv
# Creating virtual envn called Gunicorn
python3 -m venv Gunicorn

source Gunicorn/bin/activate
pip install flask
sudo lsof -i :5000
sudo kill pid

ls /etc/nginx
