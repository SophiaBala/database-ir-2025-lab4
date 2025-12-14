from flask import Blueprint, request, jsonify
from my_project.auth.service.staff_service import StaffService
from my_project.auth.domain.staff import Staff
from my_project import db
from sqlalchemy import text


staff_bp = Blueprint('staff_bp', __name__)

@staff_bp.route('/staff', methods=['GET'])
def get_staff():
    staff_members = StaffService.get_all_staff()
    return jsonify([
        {
            "idstaff": s.idstaff,
            "name": s.name,
            "shop_idshop": s.shop_idshop,
            "position": s.position
        } for s in staff_members
    ])


@staff_bp.route('/staff', methods=['POST'])
def create_staff():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400
    
    try:
        new_staff = StaffService.create_staff(data)
        return jsonify(new_staff.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@staff_bp.route('/staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    data = request.get_json()
    staff = StaffService.update_staff(staff_id, data)
    if staff:
        return jsonify({
            "idstaff": staff.idstaff,
            "name": staff.name,
            "shop_idshop": staff.shop_idshop,
            "position": staff.position
        })
    return jsonify({"error": "Staff not found"}), 404


@staff_bp.route('/staff/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    staff = StaffService.delete_staff(staff_id)
    if staff:
        return jsonify({"message": "Staff deleted"})
    return jsonify({"error": "Staff not found"}), 404


@staff_bp.route('/staff/add', methods=['POST'])
def add_staff():
    try:
        data = request.json
        name = data.get('name')
        position = data.get('position')
        shop_id = data.get('shop_id')

        if not name or not position or not shop_id:
            return jsonify({"error": "Missing required fields"}), 400

        new_staff = Staff(name=name, position=position, shop_idshop=shop_id)
        db.session.add(new_staff)
        db.session.commit()

        return jsonify({
            "message": "Staff added successfully",
            "idstaff": new_staff.idstaff,
            "name": new_staff.name,
            "position": new_staff.position,
            "shop_idshop": new_staff.shop_idshop
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    


@staff_bp.route('/10inserts', methods=['POST'])
def insert_10_noname_staff():
    try:
        db.session.execute(text("CALL insert_10_noname_staff()"))
        db.session.commit()
        return jsonify({"message": "10 staff inserted successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500