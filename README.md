# Lab 3

## Pre-requisites

* Install _Pipenv_

```
pip install pipenv
```

* Install _[Flask](https://palletsprojects.com/p/flask/)_

```
pipenv install flask==1.1.1
```
* Install _[Ariadne](https://ariadnegraphql.org/docs/flask-integration.html)_ for handling GraphQL schema and binding.

```
pipenv install ariadne==0.10.0
```

* Create a schema.py and add this code:

```
type Query {
  get_student(student_id: ID): student
  get_class(class_id: Int): classes
}

type Mutation {
  create_student(student_id: ID!, name: String, course_name: String): [student]

  create_class(class_id: Int!, course_name: String): [classes]

  update_student_class(class_id: Int!, student_id: ID!): classes

  update_class(class_id: Int!, course_name: String!): classes
}

type student {
  student_id: ID!
  name: String
  course_name: String
}

type classes {
  class_id: Int!
  course_name: String
  students: [student]
}

```

* Create a file called _app.py_ and add this code snippet.

```python
from flask import Flask, escape, request

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```

* Run your Hello World Flask application from a shell/terminal.

```sh
pipenv shell
$ env FLASK_APP=app.py flask run
```

* Open [this URL](http://127.0.0.1:5000/) in a web browser or run this CLI to see the output.

```
curl -i http://127.0.0.1:5000/
```

## Requirements

You will be building a RESTful class registration API in this lab.

### Domain Model

```
|-------|               |---------|
| Class |* ---------- * | Student |
|-------|               |---------|
```

### GraphQL operations to be implemented.

* Mutate a new student

```
 mutation{create_student(student_id: 3,
    name: "Sindhu")
    {
	name
    }
  }
```

* Quety an existing student

_Request_

```
{
  students(id:1238125) {
    name
  }
}
```

_Response_

```
{
    "name" : "Bob Smith"
}
```

* Mutate a class

```
mutation{
    create_class(course_name: "CMPE309")
    {
			course_name
      class_id
    }
  }
```

* Query a class

```
{
  classess(id:1238125) {
    name
    students
  }
}
```

* Add students to a class

```
mutation{update_student_class(class_id: 290, student_id: 3384 )
    {
        class_id
      	course_name
      	students{
          student_id
          name
        }
    }
  }
```



