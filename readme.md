## About The Project

As Flask project that exposes a REST API endpoint. When called via the GET method,
this endpoint should retrieve a list of all starships from the Star Wars movies (provided by
SWAPI), sorted by the hyperdrive rating.

### Built With

- Python 3.6
- Flask 1.1.1
- Heroku

<!-- GETTING STARTED -->

## Getting Started Locally

- Clone the repo

```sh
git clone
cd starships-test
```

- instal VirtualEnv

```sh
pip install virtualenv
```

- Create a virtualenv folder and ectivate it

```sh
python3 -m venv venv/
source venv/bin/activate
```

- Install the requirements.txt

```sh
pip -r requirements.txt
```

- Run the project

```sh
python app.py
```

### Deployment

- Heroku
  You need Heroku CLI you can install iy by:

```sh
sudo snap install --classic heroku
```

Then:

```sh
heroku login -i
heroku git:remote -a your-project-name
git push heroku master
```

<!-- CONTACT -->

## Contact

Abdelghani ANNANI - abdelghani.annani@gmail.com

Project Link: [https://github.com/AbdelghaniAnnani/](https://github.com/AbdelghaniAnnani/)

[linkedin-url]: https://www.linkedin.com/in/abdelghani-annani/
[product-screenshot]: images/screenshot.png
