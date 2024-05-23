# BKK Project

## Pre-requisites 
- GTFS Static Data needs to be downloaded and added to backend/gtfs_data
    - This can be downloaded from [BKK OpenData Portal](https://go.bkk.hu/api/static/v1/public-gtfs/budapest_gtfs.zip).
- In backend/ folder, a `.env` file needs to be created with the following variables:
    - BKK_KEY
        - This can be obtained from [BKK OpenData Portal](https://opendata.bkk.hu/data-sources)


## To run the backend:
Clone this repo and go into the backend/ folder
```
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
cd backend
```

To run this project, virtualenv was used, but this is optional.
```
pip install virtualenv
python -m virtualenv --python python venv
```

Installing the requirements.
```
pip install -r requirements.txt
```

Starting the main file.
```
python main.py
```
Starting the downloader. 
```
python downloader.py
```
Starting the WebSocket server.
```
python ws_server.py
```

## To run the frontend
The frontend dashboard can be used locally by simply opening the index.html file in a browser or hosted on a webserver.

One thing that needs to be changed for the frontend is to update the address for the WebSocket server, which is used for the const named `ws`. This can be found on line 57 in index.html.

```
57| const ws = new WebSocket("ws://localhost:61354/ws?");
```