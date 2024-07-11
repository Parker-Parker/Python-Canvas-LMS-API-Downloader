
from cached_requests import request_cached
import tokens

token_set = tokens.get_tokens()
# print(token_set.keys())
auth = {'Authorization': f'Bearer {token_set["canvas.instructure.com"]}'} #canvas

# data = request_cached(f'https://canvas.instructure.com/api/v1/courses', header=auth)
# data = request_cached(f'https://canvas.instructure.com/api/v1/courses/{data[1]["id"]}', header=auth)
domain = "canvas.instructure.com"
def course(id:str)->dict:
    course_dict = {"metadata":request_cached(f'https://{domain}/api/v1/courses/{id}', header=auth)}
    course_resources = [ "bulk_user_progress",
                      "permissions",
                      "effective_due_dates",
                      "settings",
                      "todo",
                      "activity_stream",
                      "activity_stream/summary",
                      "content_share_users",
                      "recent_students",
                      "search_users",
                      "users",
                      "users/self/progress",
                      
                      "media_objects",
                      "media_attachments",

                      "discussion_topics",
                      "tabs",
                     
                      "assignments",
                      "sections",
                      "modules",
                      "modules",
                      "modules",
                      "quizzes",
                      "folders",
                      "files"
                     ]# TODO: finish this list.
                        #search  GET /api/v1/courses/:course_id on https://canvas.instructure.com/doc/api/sections.html
    for resource in course_resources:
        course_dict[resource] = request_cached(f'https://{domain}/api/v1/courses/{id}/{resource}', header=auth)

    return course_dict
