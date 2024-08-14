version=3.10
echo "***************************************"
echo "Installing Python Environment $version (.venv)"
echo "***************************************"

echo `python$version -V`
python$version -m venv `pwd`/.venv
source `pwd`/.venv/bin/activate
pip install --upgrade pip
pip install -U -r requirements.txt

