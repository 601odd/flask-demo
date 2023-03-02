from src import create_app

app = create_app()

if __name__ == '__main__':
    # session会话存储
    app.secret_key = '121839eyiusdhkjasdnfkasndfkasd'
    app.run()
