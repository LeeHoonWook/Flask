from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'

    if app.config['DEBUG'] == True:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    """ === CSRF Init === """
    csrf.init_app(app)

    @app.route("/")
    def index():
        return render_template('index.html')

    """ === User Route === """
    from gogglekaap.forms.auth_form import LoginForm, RegisterForm

    @app.route('/auth/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            # TODO
            # 1) 유저조회
            # 2) 존재하는 유저 인지 체크
            # 3) 패스워드 정합확인
            # 3) 로그인 유지(세션)
            user_id = form.data.get('user_id')
            password = form.data.get('password')
            return f'{user_id}, {password}'
        else:
            # TODO: 에러컨트롤
            pass
        return render_template('user/login.html', form=form)

    @app.route('/auth/logout')
    def logout():
        # TODO: 로그아웃 제거(세션)
        return 'logout'

    @app.route('/auth/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            # TODO
            # 1) 유저조회
            # 2) 유저 이미 존재하는지 체크
            # 3) 없으면 유저 생성
            # 4) 로그인 유지(세션)
            user_id = form.data.get('user_id')
            password = form.data.get('password')
            repassword = form.data.get('repassword')
            user_name = form.data.get('user_name')
            return f'{user_id}, {password}, {repassword}, {user_name}'
        else:
            # TODO: 에러컨트롤
            pass
        return render_template('user/register.html', form=form)

    """ === Error Route === """
    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404

    return app
