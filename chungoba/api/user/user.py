# -*- coding:utf8 -*-
#pylint: disable=E1101,C0103
from flask import g, current_app
from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger

from chungoba import db
from chungoba.swagger import ResponseModel

class User(Resource):
    @swagger.doc({
        'tags': ['user'],
        'description': '사용자 로그인',
        'parameters': [
            
        ],
        'responses': {
            '200': {
                'description': '사용자 로그인 성공',
                'schema': ResponseModel,
                'examples': {
                    'application/json': {
                        'code': 200,
                        'message': '사용자 로그인 성공'
                    }
                }
            },
            '400': {
                'description': '파라미터 값 이상',
                'schema': ResponseModel,
                'examples': {
                    'application/json': {
                        'code': 400,
                        'message': '올바르지 않는 정보',
                        'data': {

                        }
                    }
                }
            }
        }
    })
    def get(self):
        """로그인"""

        return {
            'code': 200,
            'message': '사용자 로그인 성공',
            'data': {
                
            }
        }, 200