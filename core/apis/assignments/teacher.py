from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from .schema import AssignmentSchema

teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)


@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.auth_principal
def list_assignments_of_teacher(t):
    """List all assignments of a particular teacher"""
    teachers_assignments = Assignment.get_assignments_by_teacher(t.teacher_id)

    # print(teachers_assignments)

    teachers_assignments_dump = AssignmentSchema().dump(teachers_assignments, many=True)

    return APIResponse.respond(data=teachers_assignments_dump)


@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.auth_principal
def grade_assignment(p, incoming_payload):
    """Grade assignment by teacher"""

    graded_assignment = Assignment.gradeAssignment(
        _id = incoming_payload['id'],
        _grade = incoming_payload['grade'],
        principal=p
    )

    db.session.commit()

    graded_assignment_dump = AssignmentSchema().dump(graded_assignment, many=False)

    return APIResponse.respond(data=graded_assignment_dump)
    
    # teacher_assignments = Assignment.get_assignments_by_teacher(t.teacher_id)

    # print(incoming_payload)


    # id = incoming_payload['id']

    # grade = incoming_payload['grade']

    # print('h')

    # print(t)

    # # Principal p = t

    # # print(p)
    
    # print(grade)

    # assertions.assert_valid(GradeEnum.A == grade or GradeEnum.B == grade or GradeEnum.C == grade or GradeEnum.D == grade, 'FyleError')

    # assignment = Assignment().get_by_id(id)

    # # assertions.assert_valid(assignment.teacher_id == t.teacher_id, 'FyleError')

    # assertions.assert_found(assignment, 'FyleError')

    # assertions.assert_valid(assignment.state == AssignmentStateEnum.SUBMITTED, 'FyleError')

    # # assertions.assert_valid(GradeEnum.A == grade or GradeEnum.B == grade or GradeEnum.C == grade or GradeEnum.D == grade, 'ValidationError')
    # # assertions.assert_valid(assignment.teacher_id == t.teacher_id, 'FyleError')


    # try:

    #     assignment.grade = grade

    #     assignment.state = AssignmentStateEnum.GRADED

    #     # print(assignment)

    #     assignment_dump = AssignmentSchema().dump(assignment, many=False)

    #     db.session.commit()

    #     return APIResponse.respond(data=assignment_dump)
    # except:
    #     assertions.assert_valid(grade != 'AB', 'ValidationError')



