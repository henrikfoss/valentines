import streamlit as st
import subprocess
import json

# Check snd version
snd_version = subprocess.getoutput('snd version').split("\n")[1]

if snd_version < 'snd-cli version v1.1.3 ':
    st.error('This app requires snd version v1.1.1 or higher. Please update snd to use this app.')

# Define the environment options and command options
env_options = ['test', 'production']
spark_command_options = ['request-status', 'runtime-info', 'logs', 'submit', 'configuration']
algorithm_command_options = ['run', 'get', 'payload'] #'cancel']
payload_file = './crystal-payload.json'

# Create user input fields
mode = st.selectbox('Select Mode', ['spark', 'algorithm'])
env = st.selectbox('Select Environment', env_options)

if mode == 'spark':
    command = st.selectbox('Select Command', spark_command_options)

    if command in ['request-status', 'runtime-info', 'logs']:
        job_id = st.text_input('Enter Job ID')
        if st.button('Execute Spark Command'):
            command_output = subprocess.getoutput(f'snd spark {command} --id {job_id} --env {env}')
            if command == 'logs':
                logs = command_output.split('\n')
                python_errors = [line for line in logs if 'Traceback (most recent call last):' in line]
                other_logs = [line for line in logs if line not in python_errors]
                st.text_area('Python Errors', '\n'.join(python_errors), height=200)
                st.text_area('Other Logs', '\n'.join(other_logs + python_errors), height=500)
            else:
                st.write(command_output)

    if command == 'submit':
        job_name = st.text_input('Enter Job name')

        extra_agrs = None
        project_inputs = None
        project_outputs = None
        expected_parallelism = None
        if st.checkbox('Add custom configuration'):
            custom_configuration = True
            if st.checkbox('Add extraArguments'):
                extra_args = st.text_area('Enter Extra Arguments in JSON format')
            if st.checkbox('Add projectInputs'):
                project_inputs = st.text_area('Enter Project Inputs in JSON format')
            if st.checkbox('Add projectOutputs'):
                project_outputs = st.text_area('Enter Project Outputs in JSON format')
            if st.checkbox('Add expectedParallelism'):
                expected_parallelism = st.text_input('Enter Expected Parallelism')
        else:
            custom_configuration = False
            # Create a dictionary to store the data
        data = {}

        if st.button('Execute Spark Command'):

            if custom_configuration:
                if extra_args:
                    data['extra_arguments'] = json.loads(extra_args)
                if project_inputs:
                    data['project_inputs'] = json.loads(project_inputs)
                if project_outputs:
                    data['project_outputs'] = json.loads(project_outputs)
                if expected_parallelism:
                    data['expected_parallelism'] = expected_parallelism

                    # Write data to overrides.json
                with open('./overrides.json', 'w') as f:
                    json.dump(data, f)
                st.text('Submitting job with the following configuration:')
                st.write(data)

                command_output = subprocess.getoutput(
                    f'snd spark {command} --job-name {job_name} --overrides ./overrides.json --env {env}')
                st.write(command_output)

            else:
                command_output = subprocess.getoutput(f'snd spark {command} --job-name {job_name} --env {env}')
                st.write(command_output)

    if command == 'configuration':
        job_name = st.text_input('Job Name')
        if st.button('Execute Spark Command'):
            configuration_output = subprocess.getoutput(f'snd spark configuration --name {job_name} --env {env}')
            st.write(configuration_output)

if mode == 'algorithm':
    algorithm = st.text_input('Enter Algorithm Name')
    command = st.selectbox('Select Command', algorithm_command_options)
    if command == 'run':
        parameters = None
        inputs = None
        outputs = None
        if st.checkbox('Add parameters'):
            parameters = st.text_area('Enter parameters in JSON format')
        if st.checkbox('Add inputs'):
            inputs = st.text_area('Enter inputs in JSON format')
        if st.checkbox('Add outputs'):
            outputs = st.text_input('Enter outputs in JSON format')
        data = {}
            # Create a dictionary to store the data
        if st.button('Send request to Crystal'):
            data["algorithmName"] = algorithm
            if parameters:
                data['AlgorithmParameters'] = json.loads(parameters)
            if inputs:
                data['inputs'] = json.loads(inputs)
            if outputs:
                data['outputs'] = json.loads(outputs)

                # Write data to overrides.json
            with open('./payload.json', 'w') as f:
                json.dump(data, f)
            st.text('Submitting job with the following configuration:')
            st.write(data)

            command_output = subprocess.getoutput(
                f'snd algorithm run --algorithm {algorithm} --payload ./payload.json --env {env}')
            st.write(command_output)
    if command == "get":
        job_id = st.text_input('Enter Job ID')
        if st.button('Get Algorithm Job'):
            command_output = subprocess.getoutput(f'snd algorithm get --id {job_id} --algorithm {algorithm} --env {env}')
            st.write(command_output)

    if command == "payload":
        job_id = st.text_input('Enter Job ID')
        if st.button('Get Algorithm Job'):
            command_output = subprocess.getoutput(f'snd algorithm payload --id {job_id} --algorithm {algorithm}')
            st.write(command_output)
