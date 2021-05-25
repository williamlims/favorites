sudo apt-get update -y
clear
echo "### SYSTEM UPDATED ###"
sudo apt-get upgrade -y
clear
echo "### SYSTEM UPGRADED ###"
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt-get install python3-venv -y
sudo apt install python3-django -y
clear
echo "### ECOSYSTEM PYTHON INSTALLED ###"
python3 -m venv env
clear
echo "### VIRTUAL ENVIRONMENT CREATED ###"
source env/bin/activate
sudo apt-get install libpq-dev
pip install -r requirements.txt
clear
echo "### REQUIREMENTS DONE! ###"