from flask_sqlalchemy import SQLAlchemy


db_connection = "mysql://avnadmin:AVNS_oXmc4rbaAybAi7fOIBt@mysql-3d3eacf2-kouroshcareer.b.aivencloud.com:21821/defaultdb?charset=utf8mb4"

engine = SQLAlchemy.create_engine(
    db_connection,
    connect_args={
        'ssl': {
            'sslmode': 'REQUIRED',
            'ca': 'C:/Users/m.aghazadeh/Downloads/ca.pem'
        }
    })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(SQLAlchemy.text('select * from jobs')).fetchall()
        jobs = []
        for i in range(len(result)):
            row_dict = result[i]._mapping
            jobs.append(row_dict)
        return jobs