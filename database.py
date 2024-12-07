from sqlalchemy import create_engine, text
import os


db_connection = os.environ['DB_CONNECTION']

engine = create_engine(
    db_connection,
    connect_args={
        'ssl': {
            'ca': '/etc/secrets/ca.pem'
        }
    })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs')).fetchall()
        jobs = []
        for i in range(len(result)):
            row_dict = result[i]._mapping
            jobs.append(row_dict)
        return jobs

def add_application_to_db(application):
    with engine.connect() as conn:
        query = text("Insert into applications (full_name, email) values (:full_name, :email)")
        conn.execute(query, full_name=application['full_name'], email=application['email'])