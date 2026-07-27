create index idx_student_enrollment_year 
on students(enrollment_year);

create unique index idx_unique_student_course
on enrollments(student_id,course_id);

create index idx_course_code
on courses(course_code);

explain format=json
select s.first_name,s.lanst_name,c.course_name
from enrollments e join students s 
on s.student_id = e.student_id
join courses c
on c.course_id=e.course_id
where s.enrollment_year=2022;

/*
{
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "6.84"
    },
    "nested_loop": [
      {
        "table": {
          "table_name": "s",
          "access_type": "ref",
          "possible_keys": [
            "PRIMARY",
            "idx_students_enrollment_year",
            "idx_student_enrollment_year"
          ],
          "key": "idx_students_enrollment_year",
          "used_key_parts": [
            "enrollment_year"
          ],
          "key_length": "5",
          "ref": [
            "const"
          ],
          "rows_examined_per_scan": 6,
          "rows_produced_per_join": 6,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "0.50",
            "eval_cost": "0.60",
            "prefix_cost": "1.10",
            "data_read_per_join": "4K"
          },
          "used_columns": [
            "student_id",
            "first_name",
            "last_name",
            "enrollment_year"
          ]
        }
      },
      {
        "table": {
          "table_name": "e",
          "access_type": "ref",
          "possible_keys": [
            "idx_enrollments_student_course",
            "course_id"
          ],
          "key": "idx_enrollments_student_course",
          "used_key_parts": [
            "student_id"
          ],
          "key_length": "5",
          "ref": [
            "college_db.s.student_id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 9,
          "filtered": "100.00",
          "using_index": true,
          "cost_info": {
            "read_cost": "1.50",
            "eval_cost": "0.94",
            "prefix_cost": "3.54",
            "data_read_per_join": "301"
          },
          "used_columns": [
            "student_id",
            "course_id"
          ],
          "attached_condition": "(`college_db`.`e`.`course_id` is not null)"
        }
      },
      {
        "table": {
          "table_name": "c",
          "access_type": "eq_ref",
          "possible_keys": [
            "PRIMARY"
          ],
          "key": "PRIMARY",
          "used_key_parts": [
            "course_id"
          ],
          "key_length": "4",
          "ref": [
            "college_db.e.course_id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 9,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "2.36",
            "eval_cost": "0.94",
            "prefix_cost": "6.84",
            "data_read_per_join": "6K"
          },
          "used_columns": [
            "course_id",
            "course_name"
          ]
        }
      }
    ]
  }
}
*/