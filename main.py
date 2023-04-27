from website import create_app

app = create_app()

if __name__ == '__main__': #webserver is running only if you run this file
    app.run(debug=True) 
    