import streamlit as st

def calculate_area(length_ft, length_inch, breadth_ft, breadth_inch, height_ft, height_inch, num_doors, num_windows, door_data, window_data):
    # Convert feet and inches to total feet for room dimensions
    length = length_ft + length_inch / 12
    breadth = breadth_ft + breadth_inch / 12
    height = height_ft + height_inch / 12

    # Calculate the wall area
    wall_area = 2 * height * (length + breadth)  # Total wall area in sqft
    roof_area = length * breadth  # Roof area in sqft

    # Calculate door areas
    total_door_area = 0
    if num_doors > 0:
        for i in range(num_doors):
            door_length = door_data[i][0] + door_data[i][1] / 12  # Door length in feet
            door_height = door_data[i][2]  # Door height in feet
            total_door_area += door_length * door_height  # Add door area

    # Calculate window areas
    total_window_area = 0
    if num_windows > 0:
        for i in range(num_windows):
            window_length = window_data[i][0] + window_data[i][1] / 12  # Window length in feet
            total_window_area += window_length * height  # Window area in sqft

    # Adjust wall area by subtracting door and window areas
    adjusted_wall_area = wall_area - total_door_area - total_window_area

    # Total area including walls and roof
    total_area = adjusted_wall_area + roof_area

    return adjusted_wall_area, roof_area, total_area


def main():
    st.title("Room Area Calculator")

    # Input for Room Dimensions
    st.header("Room Dimensions")
    length_ft = st.number_input("Length (Feet)", min_value=0, step=1)
    length_inch = st.number_input("Length (Inches)", min_value=0, max_value=11, step=1)
    breadth_ft = st.number_input("Breadth (Feet)", min_value=0, step=1)
    breadth_inch = st.number_input("Breadth (Inches)", min_value=0, max_value=11, step=1)
    height_ft = st.number_input("Height (Feet)", min_value=0, step=1)
    height_inch = st.number_input("Height (Inches)", min_value=0, max_value=11, step=1)

    # Optional input for Doors
    st.header("Doors")
    num_doors = st.number_input("Number of Doors", min_value=0, step=1)
    door_data = []
    for i in range(num_doors):
        st.subheader(f"Door {i + 1}")
        door_length_ft = st.number_input(f"  Door {i + 1} Length (Feet)", min_value=0, step=1, key=f"door_length_ft_{i}")
        door_length_inch = st.number_input(f"  Door {i + 1} Length (Inches)", min_value=0, max_value=11, step=1, key=f"door_length_inch_{i}")
        door_height = st.number_input(f"  Door {i + 1} Height (Feet)", min_value=0, step=1, key=f"door_height_{i}")
        door_data.append((door_length_ft, door_length_inch, door_height))

    # Optional input for Windows
    st.header("Windows")
    num_windows = st.number_input("Number of Windows", min_value=0, step=1)
    window_data = []
    for i in range(num_windows):
        st.subheader(f"Window {i + 1}")
        window_length_ft = st.number_input(f"  Window {i + 1} Length (Feet)", min_value=0, step=1, key=f"window_length_ft_{i}")
        window_length_inch = st.number_input(f"  Window {i + 1} Length (Inches)", min_value=0, max_value=11, step=1, key=f"window_length_inch_{i}")
        window_data.append((window_length_ft, window_length_inch))

    # Automatically calculate the areas as the user interacts with inputs
    adjusted_wall_area, roof_area, total_area = calculate_area(
        length_ft, length_inch, breadth_ft, breadth_inch,
        height_ft, height_inch, num_doors, num_windows,
        door_data, window_data
    )

    # Display results automatically
    st.header("Results")
    st.write(f"Adjusted Wall Area: {adjusted_wall_area:.2f} sqft")
    st.write(f"Roof Area: {roof_area:.2f} sqft")
    st.write(f"Total Area (Wall + Roof): {total_area:.2f} sqft")

if __name__ == "__main__":
    main()
