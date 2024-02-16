import streamlit as st

def registration_form():
    st.title("Registration Form")

    name = st.text_input("Name:")
    employee_id = st.text_input("Employee ID:")
    designation = st.text_input("Designation:")
    department = st.text_input("Department:")
    password = st.text_input("Password:", type="password")
    confirm_password = st.text_input("Re-enter Password:", type="password")
    timetable_file = st.file_uploader("Upload Timetable (Excel):", type=["xls", "xlsx"])

    if st.button("Submit"):
        if not (name and employee_id and designation and department and password and confirm_password):
            st.error("Please fill in all the required fields.")
        elif password != confirm_password:
            st.error("Passwords do not match. Please re-enter your password.")
        elif not timetable_file:
            st.error("Please upload the timetable file.")
        else:
            st.success(
                f"Registration successful!\nName: {name}\nEmployee ID: {employee_id}\nDesignation: {designation}"
                f"\nDepartment: {department}\nTimetable File: {timetable_file.name}"
            )

if __name__ == "__main__":
    registration_form()
