import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import datetime, timedelta

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Initialize sample data
patients_df = pd.DataFrame({
    'patient_id': range(1001, 1004),
    'name': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'age': [45, 32, 58],
    'contact': ['555-0101', '555-0102', '555-0103'],
    'blood_group': ['A+', 'B-', 'O+']
})

doctors_df = pd.DataFrame({
    'doctor_id': range(2001, 2004),
    'name': ['Dr. Sarah Wilson', 'Dr. Mike Brown', 'Dr. Emily Davis'],
    'specialization': ['Cardiology', 'Pediatrics', 'Orthopedics'],
    'contact': ['555-0201', '555-0202', '555-0203']
})

appointments_df = pd.DataFrame({
    'appointment_id': range(3001, 3004),
    'patient_id': [1001, 1002, 1003],
    'doctor_id': [2001, 2002, 2003],
    'date': ['2024-10-23', '2024-10-24', '2024-10-25'],
    'time': ['10:00 AM', '2:30 PM', '11:15 AM'],
    'status': ['Scheduled', 'Completed', 'Scheduled']
})

# Layout components
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Patients", href="#")),
        dbc.NavItem(dbc.NavLink("Doctors", href="#")),
        dbc.NavItem(dbc.NavLink("Appointments", href="#")),
    ],
    brand="Hospital Management System",
    brand_href="#",
    color="primary",
    dark=True,
)

# Patient management tab
patient_tab = dbc.Card(
    dbc.CardBody([
        html.H4("Patient Management"),
        dbc.Row([
            dbc.Col([
                dbc.Input(id="patient-name", placeholder="Patient Name"),
                dbc.Input(id="patient-age", placeholder="Age", type="number"),
                dbc.Input(id="patient-contact", placeholder="Contact"),
                dbc.Select(
                    id="patient-blood-group",
                    options=[
                        {"label": bg, "value": bg}
                        for bg in ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
                    ],
                    placeholder="Blood Group"
                ),
                dbc.Button("Add Patient", id="add-patient-button", color="success", className="mt-3"),
            ], width=4),
            dbc.Col([
                html.H5("Patients List"),
                html.Div(id="patients-table")
            ], width=8)
        ])
    ])
)

# Doctor management tab
doctor_tab = dbc.Card(
    dbc.CardBody([
        html.H4("Doctor Management"),
        dbc.Row([
            dbc.Col([
                dbc.Input(id="doctor-name", placeholder="Doctor Name"),
                dbc.Input(id="doctor-specialization", placeholder="Specialization"),
                dbc.Input(id="doctor-contact", placeholder="Contact"),
                dbc.Button("Add Doctor", id="add-doctor-button", color="success", className="mt-3"),
            ], width=4),
            dbc.Col([
                html.H5("Doctors List"),
                html.Div(id="doctors-table")
            ], width=8)
        ])
    ])
)

# Appointment management tab
appointment_tab = dbc.Card(
    dbc.CardBody([
        html.H4("Appointment Management"),
        dbc.Row([
            dbc.Col([
                dbc.Select(
                    id="appointment-patient",
                    options=[
                        {"label": row['name'], "value": row['patient_id']}
                        for _, row in patients_df.iterrows()
                    ],
                    placeholder="Select Patient"
                ),
                dbc.Select(
                    id="appointment-doctor",
                    options=[
                        {"label": row['name'], "value": row['doctor_id']}
                        for _, row in doctors_df.iterrows()
                    ],
                    placeholder="Select Doctor"
                ),
                dcc.DatePickerSingle(
                    id="appointment-date",
                    min_date_allowed=datetime.now().date(),
                    max_date_allowed=datetime.now().date() + timedelta(days=30),
                    initial_visible_month=datetime.now().date(),
                    placeholder="Select Date"
                ),
                dbc.Select(
                    id="appointment-time",
                    options=[
                        {"label": f"{h:02d}:00", "value": f"{h:02d}:00"}
                        for h in range(9, 18)
                    ],
                    placeholder="Select Time"
                ),
                dbc.Button("Schedule Appointment", id="add-appointment-button", color="success", className="mt-3"),
            ], width=4),
            dbc.Col([
                html.H5("Appointments List"),
                html.Div(id="appointments-table")
            ], width=8)
        ])
    ])
)

# Main layout
app.layout = html.Div([
    navbar,
    dbc.Container([
        dbc.Tabs([
            dbc.Tab(patient_tab, label="Patients"),
            dbc.Tab(doctor_tab, label="Doctors"),
            dbc.Tab(appointment_tab, label="Appointments"),
        ], className="mt-4")
    ], fluid=True)
])

# Callbacks for updating tables
@app.callback(
    Output("patients-table", "children"),
    Input("add-patient-button", "n_clicks")
)
def update_patients_table(n_clicks):
    return dbc.Table.from_dataframe(
        patients_df,
        striped=True,
        bordered=True,
        hover=True
    )

@app.callback(
    Output("doctors-table", "children"),
    Input("add-doctor-button", "n_clicks")
)
def update_doctors_table(n_clicks):
    return dbc.Table.from_dataframe(
        doctors_df,
        striped=True,
        bordered=True,
        hover=True
    )

@app.callback(
    Output("appointments-table", "children"),
    Input("add-appointment-button", "n_clicks")
)
def update_appointments_table(n_clicks):
    # Join with patient and doctor names for display
    display_df = appointments_df.merge(
        patients_df[['patient_id', 'name']],
        on='patient_id',
        suffixes=('', '_patient')
    ).merge(
        doctors_df[['doctor_id', 'name']],
        on='doctor_id',
        suffixes=('_patient', '_doctor')
    )
    display_df = display_df.rename(columns={
        'name_patient': 'Patient Name',
        'name_doctor': 'Doctor Name',
        'date': 'Date',
        'time': 'Time',
        'status': 'Status'
    })
    return dbc.Table.from_dataframe(
        display_df[['Patient Name', 'Doctor Name', 'Date', 'Time', 'Status']],
        striped=True,
        bordered=True,
        hover=True
    )

if __name__ == '__main__':
    app.run_server(debug=True)
