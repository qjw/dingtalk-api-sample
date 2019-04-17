from flask import request, render_template, jsonify, url_for
from werkzeug.exceptions import abort

from dingding_api.department import DingDepartment
from dingding_api.scan import get_scan_login_url, getuserinfo_bycode
from sample.main import main

@main.route('/scan')
def scan_index():
    callback = url_for(
        ".scan_calback",
        _external=True,
    )
    return render_template('scan_index.html', url=get_scan_login_url(callback))


@main.route('/scan_callback')
def scan_calback():
    code = request.args.get("code")
    if code is None:
        abort(400)

    user = getuserinfo_bycode(code)
    return jsonify(code=0, message='ok', data=user)


@main.route('/x')
def index():
    return render_template('jsapi_demo.html')


@main.route('/login_callback')
def login_callback():
    code = request.args.get("code")
    if code is None:
        abort(400)

    _a = DingDepartment()
    user = _a.get_user_by_code(code)
    return jsonify(code=0, message='ok', data=user)