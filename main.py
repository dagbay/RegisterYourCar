from website_car import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Debug is true for development purposes.