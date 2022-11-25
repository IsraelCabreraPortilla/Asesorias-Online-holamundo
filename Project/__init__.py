from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.app_context().push()

    app.config['SECRET_KEY'] = "b'\xf4<\xb9c3\xde\xe9\xeeQ\xa1\xec+'"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from Project.models import User
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from Project.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprints for non-auth parts of app
    from Project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from Project.telegramBot.telegramBot import telegramBot as telegram_bot_blueprint
    app.register_blueprint(telegram_bot_blueprint, url_prefix='/subirDocumento/')

    from Project.User_PnL.user_pnl import userPnL as user_pnl_blueprint
    app.register_blueprint(user_pnl_blueprint, url_prefix='/buscarAsesorias/')

    from Project.autoBook.autobook import autoBook as autobook_blueprint
    app.register_blueprint(autobook_blueprint, url_prefix='/buscarDocumentos/')

    from Project.Booking.booking import Booking as booking_blueprint
    app.register_blueprint(booking_blueprint, url_prefix='/quieroSerAsesor/')

    return app

