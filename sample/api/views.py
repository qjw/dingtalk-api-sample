from flask import jsonify, request

from dingding_api.base import DingBase
from dingding_api.department import DingDepartment
from dingding_api.media import DingMedia
from dingding_api.message import DingMessage
from sample.api import api
from .. import swagger

@api.route('/departments')
@swagger.doc('doc.yml#/departments')
def departments():
    _a = DingDepartment()
    v = _a.get_department_list()
    return jsonify(code=0, message='ok', data=v)


@api.route('/department/<id>')
@swagger.doc('doc.yml#/department_detail')
def department_detail(id):
    _a = DingDepartment()
    v = _a.get_department_detail(id)
    return jsonify(code=0, message='ok', data=v)


@api.route('/department/<id>/subids')
@swagger.doc('doc.yml#/department_subids')
def department_subids(id):
    _a = DingDepartment()
    v = _a.get_department_subids(id)
    return jsonify(code=0, message='ok', data=v)


@api.route('/department/<id>/parent')
@swagger.doc('doc.yml#/department_parent')
def department_parent(id):
    _a = DingDepartment()
    v = _a.get_department_parent(id)
    return jsonify(code=0, message='ok', data=v)

@api.route('/department/<id>/userids')
@swagger.doc('doc.yml#/department_userids')
def department_userids(id):
    _a = DingDepartment()
    v = _a.get_department_userids(id)
    return jsonify(code=0, message='ok', data=v)

@api.route('/department/<id>/users')
@swagger.doc('doc.yml#/department_users')
def department_users(id):
    _a = DingDepartment()
    v = _a.get_department_users(id)
    return jsonify(code=0, message='ok', data=v)

@api.route('/department/<id>/user_details')
@swagger.doc('doc.yml#/department_user_details')
def department_user_details(id):
    _a = DingDepartment()
    v = _a.get_department_users_detail(id)
    return jsonify(code=0, message='ok', data=v)

@api.route('/department', methods=["POST"])
@swagger.doc('doc.yml#/create_department')
def create_department():
    _a = DingDepartment()
    v = _a.create_department(request.json_dict)
    return jsonify(code=0, message='ok', data=v)

@api.route('/department/<id>', methods=["DELETE"])
@swagger.doc('doc.yml#/delete_department')
def delete_department(id):
    _a = DingDepartment()
    v = _a.delete_department(id)
    return jsonify(code=0, message='ok', data=v)

@api.route('/user/get_org_user_count')
@swagger.doc('doc.yml#/get_org_user_count')
def get_org_user_count():
    _a = DingDepartment()
    v = _a.get_org_user_count(request.query_dict['active'])
    return jsonify(code=0, message='ok', data=v)


@api.route('/user/<id>')
@swagger.doc('doc.yml#/user_detail')
def user_detail(id):
    _a = DingDepartment()
    v = _a.get_user_detail(id)
    return jsonify(code=0, message='ok', data=v)

@api.route('/user', methods=["POST"])
@swagger.doc('doc.yml#/create_user')
def create_user():
    _a = DingDepartment()
    v = _a.create_user(request.json_dict)
    return jsonify(code=0, message='ok', data=v)

@api.route('/user/<id>', methods=["DELETE"])
@swagger.doc('doc.yml#/delete_user')
def delete_user(id):
    _a = DingDepartment()
    v = _a.delete_user(id)
    return jsonify(code=0, message='ok', data=v)

@api.route('/admin_users')
@swagger.doc('doc.yml#/admin_users')
def admin_users():
    _a = DingDepartment()
    v = _a.get_admin_users()
    return jsonify(code=0, message='ok', data=v)


@api.route('/admin_user/<id>/scopes')
@swagger.doc('doc.yml#/admin_scopes')
def admin_scopes(id):
    _a = DingDepartment()
    v = _a.get_admin_user_scopes(id)
    return jsonify(code=0, message='ok', data=v)


@api.route('/corpconversation/text', methods=["POST"])
@swagger.doc('notify.yml#/send_corpconversation_text')
def send_corpconversation_text():
    _d = DingMessage()
    p = request.json_dict
    r = _d.send(p["msg"], p.get('userid_list'), p.get('dept_id_list'))
    return jsonify(code=0, message='ok', data=r)


@api.route('/corpconversation/link', methods=["POST"])
@swagger.doc('notify.yml#/send_corpconversation_link')
def send_corpconversation_link():
    _d = DingMessage()
    p = request.json_dict
    r = _d.send(p["msg"], p.get('userid_list'), p.get('dept_id_list'))
    return jsonify(code=0, message='ok', data=r)

@api.route('/corpconversation/markdown', methods=["POST"])
@swagger.doc('notify.yml#/send_corpconversation_markdown')
def send_corpconversation_markdown():
    _d = DingMessage()
    p = request.json_dict
    r = _d.send(p["msg"], p.get('userid_list'), p.get('dept_id_list'))
    return jsonify(code=0, message='ok', data=r)


@api.route('/corpconversation/action_card', methods=["POST"])
@swagger.doc('notify.yml#/send_corpconversation_action_card')
def send_corpconversation_action_card():
    _d = DingMessage()
    p = request.json_dict
    r = _d.send(p["msg"], p.get('userid_list'), p.get('dept_id_list'))
    return jsonify(code=0, message='ok', data=r)


@api.route('/corpconversation/image', methods=["POST"])
@swagger.doc('notify.yml#/send_corpconversation_image')
def send_corpconversation_image():
    _d = DingMessage()
    p = request.json_dict
    r = _d.send(p["msg"], p.get('userid_list'), p.get('dept_id_list'))
    return jsonify(code=0, message='ok', data=r)

@api.route('/corpconversation/file', methods=["POST"])
@swagger.doc('notify.yml#/send_corpconversation_file')
def send_corpconversation_file():
    _d = DingMessage()
    p = request.json_dict
    r = _d.send(p["msg"], p.get('userid_list'), p.get('dept_id_list'))
    return jsonify(code=0, message='ok', data=r)


@api.route('/media/upload', methods=["POST"])
@swagger.doc('media.yml#/media_upload')
def media_upload():
    _m = DingMedia()
    name = None
    for fn in request.files:
        name = fn
        break

    if not name:
        return jsonify(code=404, message='name不存在')

    storage = request.files[name]
    filename = storage.filename
    v = _m.upload(storage, filename, request.query_dict["tp"])
    return jsonify(code=0, message='ok', data=v)

@api.route('/jsapi')
def jsapi_config():
    url = request.args["url"]
    _b = DingBase()
    v = _b.jsapi_config(url)
    return jsonify(code=0, message='ok', data=v)

