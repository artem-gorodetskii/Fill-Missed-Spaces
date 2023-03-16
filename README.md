# Fill-Missed-Spaces
HTTP-service that receives text with missed spaces and returns a corrected sentence and a list of missed spaces positions.

## Installation
Clone the repository:
```
$ git clone https://github.com/artem-gorodetskii/Fill-Missed-Spaces.git
```

To run in a base or virtual environment:
```
$ cd Fill-Missed-Spaces
$ pip install -r requirements.txt
$ python app.py
```

To run as a docker container:
```
$ cd Fill-Missed-Spaces
$ docker build ./ -t fill-missed-spaces
$ docker run -it -p 5100:5100 fill-missed-spaces
```
