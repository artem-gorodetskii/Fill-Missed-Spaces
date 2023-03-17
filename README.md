# Fill-Missed-Spaces
HTTP-service that receives text with missed spaces and returns a corrected sentence and a list of missed spaces positions. 

The [algorithm](https://github.com/artem-gorodetskii/Fill-Missed-Spaces/blob/main/model/space_predictor.py#L6) reconstructs the string using its tokenized representation. The [tokenization algorithm](https://github.com/artem-gorodetskii/Fill-Missed-Spaces/blob/main/model/tokenizer.py#L7) is based on dynamic programming and probabilistic modeling of unigrams with a predefined vocabulary.

### Installation
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
$ docker run -it -p 5100:5100 -d fill-missed-spaces
```

### Usage
**Request example**
``` python
import requests

request = {'text': 'Theladysoon appeared,presentinga mostcharmingspectacleofperfectbeauty,set off bythemost appropriateadornments.'}

result = requests.post('http://127.0.0.1:5100/predict_spaces', json=request).json()

print(result)
```
``` bash
{
  'missed_spaces': [3, 8, 23, 34, 41, 50, 60, 63, 71, 79, 90, 94, 111],
  'text': 'The lady soon appeared, presenting a most charming spectacle of perfect beauty, set off by the most appropriate adornments.'
 }
```

**Health checking**
```
$ !curl http://127.0.0.1:5100/healthcheck
```

**Application interface**

To access the application visit the following URL:
```
http://127.0.0.1:5100/
```
You will see the following interface with text fields and submit button.

<p align="center">
  <img alt="img-name" src="assets/homepage_screen_recording.gif" width="800">
  <br>
    <em>Fig. 1. Application home page.</em>
</p>
