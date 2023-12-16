from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8080) #listen at port 8080, enabling debug causes reload following changes
