# Install conda & co
## Install packages
source: https://www.anaconda.com/rpm-and-debian-repositories-for-miniconda/

Install our public gpg key to trusted store:

curl https://repo.anaconda.com/pkgs/misc/gpgkeys/anaconda.asc | gpg --dearmor > conda.gpg
install -o root -g root -m 644 conda.gpg /etc/apt/trusted.gpg.d/

Add our debian repo:

echo "deb [arch=amd64] https://repo.anaconda.com/pkgs/misc/debrepo/conda stable main" >
 /etc/apt/sources.list.d/conda.list

add this line @ end of .bashrc:

source /opt/conda/etc/profile.d/conda.sh

(close terminal & open new one in order to read modified .bashrc)

install spyder (gui):

sudo apt install spyder3 -y

## Setup Conda env

### creat it


    $ conda create --name quants python=3

output:
  ##Package Plan ##

    environment location: /home/gmiravalles/.conda/envs/quants

    added / updated specs:
      - python=3


  To activate this environment, use:

      $ conda activate quants

  To deactivate an active environment, use:

       $ conda deactivate

### activate it & add python libs
  $ conda activate quants
  $ pip install yfinance
  $ pip install pyfolio
