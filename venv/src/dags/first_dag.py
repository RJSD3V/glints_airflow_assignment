try:
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from airflow.operators.dummy_operator import DummyOperator
    from datetime import datetime
    import psycopg2
    from config import config
    print("All Dag modules are ok .....")
except Exception as e:
    print("Error {}".format(e))


def get_data(**context):
    conn = psycopg2.connect(database="glints",
        user="postgres",
        password="tiger",
        host="localhost",
        port=5432)
    curr=conn.cursor()
    cur.execute('select * from Employee')
    df = DataFrame(cur.fetchall(),columns=['ID','Name','Email'])
    context['ti'].xcom_push(key='pass_emp_table', value = df)
    if conn:
        conn.commit()
        curr.close()
        conn.close()


def push_data(**context):
    conn = psycopg2.connect(database="glints",
                            user="postgres",
                            password="tiger",
                            host="localhost",
                            port=5431)
    curr=conn.cursor()
    table = context.get("ti").xcom_pull(key='pass_emp_table')
    print("Table Recieved from First Container")
    for i in table.index:
        query = """
        INSERT INTO Employee(ID,NAME,EMAIL) VALUES ( '%s' , '%s' , '%s')
        """.format(table['ID'],table['NAME'],table['EMAIL'])
        curr.execute(query)
    conn.commit()
    if conn:
        conn.commit()
        curr.close()
        conn.close()

def first_function_execute(**context):
    print("First part of the dag has started executing.")




def last_function_execute(**context):
    print("This is the last portion of the dag to be executed.")
    print("If this part is executed, Your dag has successfully been run.")




# */2 * * * * Execute Every Two Minutes
with DAG(
    dag_id="first_dag",
    schedule_interval="@daily",
    default_args={
        "owner":"airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        "start_date": datetime(2022,8,21)



    },
    catchup=False) as f:


    first_function_execute = PythonOperator(
        task_id="first_function_execute",
        python_callable=first_function_execute,
        provide_context=True,
        op_kwargs={"name":"Raajas Sode"},


    ),

    last_function_execute = PythonOperator(
        task_id="last_function_execute",
        python_callable=last_function_execute,
        provide_context=True


    ),
    write_table_x = PythonOperator(
        task_id="write_table_x",
        python_callable=write_table_x,
        provide_context=True

    ),

    push_data = PythonOperator(
        task_id= "push_data",
        python_callable=push_data,
        provide_context=True
    )



    first_function_execute >> get_data >> push_data >> last_function_execute